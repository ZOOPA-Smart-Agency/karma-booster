#!/usr/bin/env python3
"""
Digital Karma Index (DKI) Calculator

Toma un YAML del cliente (output de profile assessment) y calcula:
- DKI baseline (0-1000)
- Breakdown por las 5 capas (Earned, Discoverability, LLM, Trust, Owned)
- Tier identification (Invisible → Emerging → Established → Recognized → Leading → Top)
- Gaps priorizados para plan personalizado

Usage:
    python3 calculate_dki.py path/to/{client}-profile-data.yaml
    python3 calculate_dki.py path/to/{client}-profile-data.yaml --output report.md

Spec completa: ~/.claude/skills/karma-booster/references/digital-karma-formula.md
"""
import sys, math, json, argparse
from pathlib import Path


# ============================================================
# CONSTANTS · pesos y normalizaciones
# ============================================================

LAYER_WEIGHTS = {
    "earned": 0.40,
    "discoverability": 0.20,
    "llm_visibility": 0.15,
    "trust_signals": 0.15,
    "owned_anchor": 0.10,
}

# Discoverability components (suma directa, max 1000)
DISCOVERABILITY_COMPONENTS = {
    "wikipedia_article": 200,
    "wikidata_entity": 100,
    "google_knowledge_panel": 150,
    "schema_org_person": 80,
    "orcid": 70,
    "custom_domain": 50,
    "llms_txt": 50,
    "google_scholar": 50,
    "crunchbase": 50,
    "angellist": 40,
    "imdb": 80,
    "bar_association": 50,
    "doximity_verified": 50,
    "wikipedia_commons_photo": 30,
}

DKI_TIERS = [
    (0, 100, "Invisible"),
    (100, 300, "Emerging"),
    (300, 500, "Established en niche"),
    (500, 700, "Recognized regional/sectorial"),
    (700, 900, "Leading authority"),
    (900, 1001, "Top of field globally"),
]


# ============================================================
# Platform normalization formulas
# ============================================================

def safe_log10(x, default=0):
    """log10 que devuelve default si x <= 0."""
    if x is None or x <= 0:
        return default
    return math.log10(x)


def normalize_linkedin(p):
    followers = p.get("followers", 0)
    ssi = p.get("ssi_score") or 35  # default if not measured
    return min(100, safe_log10(followers / 100) * 30 + ssi * 0.4)


def normalize_twitter(p):
    followers = p.get("followers", 0)
    imp = p.get("monthly_impressions_est", 0)
    return min(100, safe_log10(followers / 100) * 25 + safe_log10(imp / 1000) * 15)


def normalize_bluesky(p):
    followers = p.get("followers", 0)
    return min(100, safe_log10(followers / 10) * 30)


def normalize_threads(p):
    followers = p.get("followers", 0)
    return min(100, safe_log10(followers / 100) * 30)


def normalize_mastodon(p):
    followers = p.get("followers", 0)
    return min(100, safe_log10(followers / 10) * 30)


def normalize_hackernews(p):
    karma = p.get("karma", 0)
    return min(100, safe_log10(karma) * 30)


def normalize_reddit(p):
    karma = p.get("total_karma", 0)
    return min(100, safe_log10(karma) * 20)


def normalize_quora(p):
    followers = p.get("followers", 0)
    answers = p.get("answers", 0)
    return min(100, safe_log10(followers) * 25 + answers * 0.5)


def normalize_medium(p):
    followers = p.get("followers", 0)
    claps = p.get("total_claps", 0)
    return min(100, safe_log10(followers) * 30 + safe_log10(claps / 100) * 15)


def normalize_substack(p):
    subs = p.get("subscribers", 0)
    open_rate = p.get("open_rate", 0)
    return min(100, safe_log10(subs) * 30 + open_rate * 50)


def normalize_youtube(p):
    subs = p.get("subscribers", 0)
    monthly_views = p.get("monthly_views", 0)
    return min(100, safe_log10(subs / 10) * 25 + safe_log10(monthly_views / 100) * 20)


def normalize_instagram(p):
    followers = p.get("followers", 0)
    er = p.get("engagement_rate", 0)
    return min(100, safe_log10(followers / 10) * 25 + er * 100)


def normalize_tiktok(p):
    followers = p.get("followers", 0)
    likes = p.get("total_likes", 0)
    return min(100, safe_log10(followers / 10) * 25 + safe_log10(likes / 100) * 15)


def normalize_github(p):
    followers = p.get("followers", 0)
    stars = p.get("total_stars", 0)
    return min(100, safe_log10(followers) * 30 + safe_log10(stars) * 15)


def normalize_stackoverflow(p):
    rep = p.get("reputation", 0)
    return min(100, safe_log10(rep) * 20)


def normalize_dev_to(p):
    return min(100, safe_log10(p.get("followers", 0) / 10) * 30)


def normalize_hashnode(p):
    return min(100, safe_log10(p.get("followers", 0) / 10) * 30)


def normalize_google_scholar(p):
    h_index = p.get("h_index", 0)
    citations = p.get("total_citations", 0)
    return min(100, h_index * 4 + safe_log10(citations / 100) * 10)


def normalize_orcid(p):
    works = p.get("works", 0)
    return min(100, works * 2)


def normalize_researchgate(p):
    rg = p.get("rg_score", 0)
    return min(100, rg * 2)


def normalize_dribbble(p):
    followers = p.get("followers", 0)
    appr = p.get("appreciations", 0)
    return min(100, safe_log10(followers) * 25 + safe_log10(appr) * 15)


def normalize_behance(p):
    followers = p.get("followers", 0)
    views = p.get("total_project_views", 0)
    return min(100, safe_log10(followers) * 25 + safe_log10(views) * 15)


def normalize_imdb(p):
    rank = p.get("starmeter_rank", 50000)
    credits = p.get("credits", 0)
    return min(100, max(0, (50000 - rank) / 500) + credits * 0.5)


def normalize_spotify(p):
    ml = p.get("monthly_listeners", 0)
    return min(100, safe_log10(ml / 10) * 20)


# Map de plataformas a sus normalizers
PLATFORM_NORMALIZERS = {
    "linkedin": normalize_linkedin,
    "twitter_x": normalize_twitter,
    "twitter": normalize_twitter,
    "x": normalize_twitter,
    "bluesky": normalize_bluesky,
    "threads": normalize_threads,
    "mastodon": normalize_mastodon,
    "hackernews": normalize_hackernews,
    "reddit": normalize_reddit,
    "quora": normalize_quora,
    "medium": normalize_medium,
    "substack": normalize_substack,
    "youtube": normalize_youtube,
    "instagram": normalize_instagram,
    "tiktok": normalize_tiktok,
    "github": normalize_github,
    "stackoverflow": normalize_stackoverflow,
    "dev_to": normalize_dev_to,
    "dev.to": normalize_dev_to,
    "hashnode": normalize_hashnode,
    "google_scholar": normalize_google_scholar,
    "orcid": normalize_orcid,
    "researchgate": normalize_researchgate,
    "dribbble": normalize_dribbble,
    "behance": normalize_behance,
    "imdb": normalize_imdb,
    "spotify": normalize_spotify,
}


# ============================================================
# Quality multiplier
# ============================================================

def calculate_quality_multiplier(platform_data):
    """Q ∈ [0.5, 1.5]"""
    engagement_rate = platform_data.get("engagement_rate", 0)
    last_post = platform_data.get("last_post", None)

    # Recency factor (approx — sin parsear dates por simplicidad)
    posts_3m = platform_data.get("posts_last_3m", 0)
    if posts_3m >= 8:
        recency = 1.0
    elif posts_3m >= 3:
        recency = 0.7
    elif posts_3m >= 1:
        recency = 0.3
    else:
        recency = 0.0

    q = 0.5 + (engagement_rate * 1.0) + (recency * 0.5)
    return max(0.5, min(1.5, q))


# ============================================================
# Layer calculators
# ============================================================

def calculate_earned(profile, sector_weights):
    """E ∈ [0, 1000]"""
    total = 0
    breakdown = []
    platforms = profile.get("platforms", {})

    for plat_name, plat_data in platforms.items():
        if plat_data is None or not plat_data:
            continue

        # Get normalizer
        norm = PLATFORM_NORMALIZERS.get(plat_name)
        if not norm:
            continue

        # Normalized score
        p_norm = norm(plat_data)

        # Sector weight
        w = sector_weights.get(plat_name, 0)
        if w == 0:
            continue  # platform irrelevant for sector

        # Quality multiplier
        q = calculate_quality_multiplier(plat_data)

        contribution = p_norm * w * q
        total += contribution
        breakdown.append({
            "platform": plat_name,
            "normalized": round(p_norm, 1),
            "weight": w,
            "quality": round(q, 2),
            "contribution": round(contribution, 1),
        })

    return min(1000, total), sorted(breakdown, key=lambda x: -x["contribution"])


def calculate_discoverability(profile):
    """D ∈ [0, 1000]"""
    d = profile.get("discoverability", {})
    score = 0
    breakdown = []

    for key, value in DISCOVERABILITY_COMPONENTS.items():
        # Check both presence (boolean) and explicit value
        if d.get(key):
            score += value
            breakdown.append({"component": key, "score": value})

    # Sector-specific directories (up to 5 × 30)
    sector_dirs = d.get("sector_directories", 0)
    score += min(150, sector_dirs * 30)
    if sector_dirs:
        breakdown.append({"component": f"sector_directories ({sector_dirs})",
                         "score": min(150, sector_dirs * 30)})

    return min(1000, score), breakdown


def calculate_llm_visibility(profile):
    """L ∈ [0, 1000] — depende de GEORadar measurement."""
    g = profile.get("georadar", {})
    if not g.get("measured", False):
        return 0, [{"component": "georadar_not_measured", "score": 0,
                   "note": "Baseline measurement needed in Foundation phase"}]

    sov = g.get("sov", 0)
    pos = g.get("position_score", 0)
    sent = g.get("sentiment_score", 0)
    cob = g.get("cobranding_score", 0)

    # All on 0-100 scale, weighted, then multiplied to 0-1000
    composite = (sov * 0.40) + (pos * 0.30) + (sent * 0.20) + (cob * 0.10)
    score = composite * 10

    return score, [
        {"component": "share_of_voice", "score": round(sov * 0.40 * 10, 1)},
        {"component": "position_score", "score": round(pos * 0.30 * 10, 1)},
        {"component": "sentiment_score", "score": round(sent * 0.20 * 10, 1)},
        {"component": "cobranding_score", "score": round(cob * 0.10 * 10, 1)},
    ]


def calculate_trust_signals(profile):
    """T ∈ [0, 1000]"""
    t = profile.get("trust_signals", {})
    score = 0
    breakdown = []

    components = [
        ("linkedin_recommendations", 20, 20),
        ("google_reviews_business", 2, 100),
        ("trustpilot_reviews", 2, 100),
        ("g2_reviews", 3, 100),
        ("press_tier1", 30, 10),
        ("press_tier2", 10, 20),
        ("verified_badges", 30, 5),
        ("years_active_public", 20, 10),
        ("conference_keynote_tier1", 30, 10),
        ("ted_talk", 200, 1),
        ("tedx_talk", 100, 1),
        ("bar_association", 50, 1),
        ("medical_license_verified", 50, 1),
        ("patents", 10, 20),
        ("imdb_credited_projects", 5, 100),
        ("goodreads_ratings", 1, 200),
        ("amazon_author_reviews", 1, 200),
    ]

    for key, multiplier, cap in components:
        count = t.get(key, 0)
        if isinstance(count, bool):
            count = 1 if count else 0
        capped = min(count, cap)
        contribution = capped * multiplier
        if contribution > 0:
            score += contribution
            breakdown.append({"component": key, "count": count,
                            "contribution": contribution})

    return min(1000, score), breakdown


def calculate_owned_anchor(profile):
    """O ∈ [0, 1000]"""
    o = profile.get("owned_anchor", {})
    score = 0
    breakdown = []

    # Website DA (0-100 Moz) × 5
    da = o.get("website_da", 0)
    if da > 0:
        contrib = da * 5
        score += contrib
        breakdown.append({"component": "website_da", "value": da, "contribution": contrib})

    # Newsletter subs (log scale, max 300)
    subs = o.get("newsletter_subscribers", 0)
    if subs > 0:
        contrib = min(300, safe_log10(subs / 10) * 100)
        score += contrib
        breakdown.append({"component": "newsletter_subscribers", "value": subs,
                         "contribution": round(contrib, 1)})

    # Long-form content count (5 × N, max 200)
    lfc = o.get("long_form_content_count", 0)
    if lfc > 0:
        contrib = min(200, 5 * lfc)
        score += contrib
        breakdown.append({"component": "long_form_content", "value": lfc,
                         "contribution": contrib})

    # Podcast own
    if o.get("podcast_own"):
        score += 100
        breakdown.append({"component": "podcast_own", "contribution": 100})

    # Online course/cohort
    if o.get("online_course_owned"):
        score += 150
        breakdown.append({"component": "online_course", "contribution": 150})

    # Self-hosted blog/portfolio
    if o.get("self_hosted_blog"):
        score += 80
        breakdown.append({"component": "self_hosted_blog", "contribution": 80})

    # Books published (200 per book)
    books = o.get("book_published", 0)
    if books > 0:
        contrib = 200 * books
        score += contrib
        breakdown.append({"component": "book_published", "value": books, "contribution": contrib})

    # Open source projects (50 per, max 200)
    oss = o.get("open_source_projects", 0)
    if oss > 0:
        contrib = min(200, 50 * oss)
        score += contrib
        breakdown.append({"component": "open_source_projects", "value": oss,
                         "contribution": contrib})

    return min(1000, score), breakdown


# ============================================================
# Main DKI calculator
# ============================================================

def get_dki_tier(dki):
    for low, high, name in DKI_TIERS:
        if low <= dki < high:
            return name
    return "Unknown"


def calculate_dki(profile, sector_weights):
    """Returns dict with score + breakdown by layer."""
    e_score, e_breakdown = calculate_earned(profile, sector_weights)
    d_score, d_breakdown = calculate_discoverability(profile)
    l_score, l_breakdown = calculate_llm_visibility(profile)
    t_score, t_breakdown = calculate_trust_signals(profile)
    o_score, o_breakdown = calculate_owned_anchor(profile)

    dki = (
        e_score * LAYER_WEIGHTS["earned"]
        + d_score * LAYER_WEIGHTS["discoverability"]
        + l_score * LAYER_WEIGHTS["llm_visibility"]
        + t_score * LAYER_WEIGHTS["trust_signals"]
        + o_score * LAYER_WEIGHTS["owned_anchor"]
    )

    return {
        "dki": round(dki, 1),
        "tier": get_dki_tier(dki),
        "layers": {
            "earned_authority": {
                "score": round(e_score, 1),
                "weighted": round(e_score * LAYER_WEIGHTS["earned"], 1),
                "max_weighted": LAYER_WEIGHTS["earned"] * 1000,
                "breakdown": e_breakdown,
            },
            "discoverability": {
                "score": round(d_score, 1),
                "weighted": round(d_score * LAYER_WEIGHTS["discoverability"], 1),
                "max_weighted": LAYER_WEIGHTS["discoverability"] * 1000,
                "breakdown": d_breakdown,
            },
            "llm_visibility": {
                "score": round(l_score, 1),
                "weighted": round(l_score * LAYER_WEIGHTS["llm_visibility"], 1),
                "max_weighted": LAYER_WEIGHTS["llm_visibility"] * 1000,
                "breakdown": l_breakdown,
            },
            "trust_signals": {
                "score": round(t_score, 1),
                "weighted": round(t_score * LAYER_WEIGHTS["trust_signals"], 1),
                "max_weighted": LAYER_WEIGHTS["trust_signals"] * 1000,
                "breakdown": t_breakdown,
            },
            "owned_anchor": {
                "score": round(o_score, 1),
                "weighted": round(o_score * LAYER_WEIGHTS["owned_anchor"], 1),
                "max_weighted": LAYER_WEIGHTS["owned_anchor"] * 1000,
                "breakdown": o_breakdown,
            },
        },
    }


def identify_gaps(dki_result):
    """Identifica las 3 capas con mayor gap proporcional para priorización del plan."""
    gaps = []
    for layer_name, layer_data in dki_result["layers"].items():
        score = layer_data["weighted"]
        max_s = layer_data["max_weighted"]
        if max_s > 0:
            pct = score / max_s
            gap_pct = 1 - pct
            gaps.append({
                "layer": layer_name,
                "current": score,
                "max": max_s,
                "pct_achieved": round(pct * 100, 1),
                "gap_pct": round(gap_pct * 100, 1),
            })
    gaps.sort(key=lambda x: -x["gap_pct"])
    return gaps


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("yaml_file", help="Path to client profile YAML")
    parser.add_argument("--sector-weights", help="Path to sector weights JSON",
                       default=None)
    parser.add_argument("--output", help="Path to output markdown report")
    parser.add_argument("--json", action="store_true", help="Output JSON instead")
    args = parser.parse_args()

    # Load profile
    try:
        import yaml
    except ImportError:
        print("ERROR: PyYAML not installed. pip install pyyaml")
        sys.exit(1)

    with open(args.yaml_file) as f:
        profile = yaml.safe_load(f)

    # Load sector weights (default if not specified, use embedded)
    if args.sector_weights:
        with open(args.sector_weights) as f:
            sector_weights = json.load(f)
    else:
        # Default tech/founder weights as fallback
        sector_weights = {
            "linkedin": 3.0, "github": 3.0, "hackernews": 2.5,
            "twitter_x": 2.0, "bluesky": 1.5, "mastodon": 1.5,
            "substack": 2.0, "medium": 1.5, "quora": 1.0,
            "threads": 1.0, "stackoverflow": 2.5, "dev_to": 2.0,
            "instagram": 0.5, "tiktok": 0.5, "youtube": 1.0,
        }

    result = calculate_dki(profile, sector_weights)
    gaps = identify_gaps(result)

    if args.json:
        out = {"dki": result, "gaps": gaps}
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return

    # Markdown report
    lines = []
    lines.append(f"# DKI Report · {profile.get('client', {}).get('name', 'Unknown')}")
    lines.append(f"\nAssessment date: {profile.get('client', {}).get('assessment_date', 'N/A')}")
    lines.append(f"\n## DKI: **{result['dki']} / 1000**")
    lines.append(f"\nTier: **{result['tier']}**")
    lines.append("\n## Breakdown by layer\n")
    lines.append("| Layer | Weighted score | Max | % achieved |")
    lines.append("|---|---|---|---|")
    for name, data in result["layers"].items():
        pct = (data["weighted"] / data["max_weighted"] * 100) if data["max_weighted"] else 0
        lines.append(f"| {name} | {data['weighted']} | {data['max_weighted']} | {pct:.0f}% |")

    lines.append("\n## Priority gaps (where to focus)\n")
    for g in gaps:
        lines.append(f"- **{g['layer']}**: {g['current']}/{g['max']} ({g['pct_achieved']}% achieved · {g['gap_pct']}% gap)")

    if args.output:
        Path(args.output).write_text("\n".join(lines))
        print(f"Report saved to {args.output}")
    else:
        print("\n".join(lines))


if __name__ == "__main__":
    main()
