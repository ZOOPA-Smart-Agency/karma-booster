#!/usr/bin/env python3
"""
Authority Score Compute · karma-booster skill
==============================================

Computes per-client priority scores for platforms in `platform-authority-db.yaml`
based on client objective + sector + bandwidth.

Usage:
    python authority_score.py --profile path/to/profile.yaml
    python authority_score.py --objective google --sector tech
    python authority_score.py --top 15 --objective llm

Outputs ranked list of platforms with composed scores + rationale.

Version: 1.0 · 2026-05-25
"""

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("Missing dependency: pip install pyyaml\n")
    sys.exit(1)


# ─────────────────────────────────────────────────────────────────────────
# WEIGHT PROFILES (per objective)
# ─────────────────────────────────────────────────────────────────────────

WEIGHT_PROFILES = {
    "google":     {"google": 0.55, "llm": 0.20, "trust": 0.25},
    "llm":        {"google": 0.20, "llm": 0.55, "trust": 0.25},
    "trust":      {"google": 0.25, "llm": 0.20, "trust": 0.55},
    "balanced":   {"google": 0.40, "llm": 0.30, "trust": 0.30},
}

# Bandwidth penalty multipliers (penalty applied to effort score)
BANDWIDTH_PENALTY = {
    "low":    0.4,   # heavy penalty for high-effort platforms
    "medium": 0.2,
    "high":   0.05,  # almost no penalty (client has time)
}

# Status multipliers
STATUS_MULTIPLIER = {
    "live":      1.00,
    "emerging":  1.05,   # slight bonus: early-mover advantage
    "declining": 0.85,   # discount: probably not worth deep investment
    "dead":      0.00,
}


# ─────────────────────────────────────────────────────────────────────────
# CORE SCORING
# ─────────────────────────────────────────────────────────────────────────

def compose_score(platform: dict, weights: dict) -> float:
    """Weighted composition of the 3 authority dims."""
    a = platform.get("authority", {})
    return (
        a.get("google", 0) * weights["google"]
        + a.get("llm", 0) * weights["llm"]
        + a.get("trust", 0) * weights["trust"]
    )


def apply_sector_bonus(score: float, platform: dict, sector: str) -> float:
    """Apply 1.3x bonus if client sector is in platform's sectors_bonus."""
    if not sector:
        return score
    sector_l = sector.lower().replace(" ", "_").replace("-", "_")
    bonuses = [s.lower() for s in platform.get("sectors_bonus", [])]
    if sector_l in bonuses:
        return score * 1.3
    return score


def apply_bandwidth_penalty(score: float, platform: dict, bandwidth: str) -> float:
    """Subtract penalty proportional to effort if client has low bandwidth."""
    if bandwidth not in BANDWIDTH_PENALTY:
        return score
    effort = platform.get("effort", 50)
    penalty = effort * BANDWIDTH_PENALTY[bandwidth]
    return max(0, score - penalty)


def apply_status_multiplier(score: float, platform: dict) -> float:
    """Multiplier based on platform health."""
    status = platform.get("status", "live")
    return score * STATUS_MULTIPLIER.get(status, 1.0)


def score_platform(
    platform: dict,
    objective: str = "balanced",
    sector: str = None,
    bandwidth: str = "medium",
) -> dict:
    """Compute final priority score for a platform given client context."""
    weights = WEIGHT_PROFILES.get(objective, WEIGHT_PROFILES["balanced"])

    raw = compose_score(platform, weights)
    after_sector = apply_sector_bonus(raw, platform, sector)
    after_bandwidth = apply_bandwidth_penalty(after_sector, platform, bandwidth)
    final = apply_status_multiplier(after_bandwidth, platform)

    return {
        "slug": platform["slug"],
        "name": platform["name"],
        "category": platform["category"],
        "final_score": round(min(100, final), 1),
        "raw_composite": round(raw, 1),
        "authority": platform.get("authority", {}),
        "effort": platform.get("effort", 50),
        "status": platform.get("status", "live"),
        "brings": platform.get("brings", ""),
        "llms_citing": platform.get("llms_citing", []),
        "sector_bonus_applied": (
            sector
            and sector.lower().replace(" ", "_") in [s.lower() for s in platform.get("sectors_bonus", [])]
        ),
    }


# ─────────────────────────────────────────────────────────────────────────
# IO
# ─────────────────────────────────────────────────────────────────────────

def load_db(path: Path = None) -> list:
    """Load platforms from YAML db. Default path: ../references/platform-authority-db.yaml"""
    if path is None:
        path = Path(__file__).parent.parent / "references" / "platform-authority-db.yaml"
    if not path.exists():
        sys.stderr.write(f"Database not found at {path}\n")
        sys.exit(1)
    with open(path) as f:
        data = yaml.safe_load(f)
    return data.get("platforms", [])


def load_profile(path: Path) -> dict:
    """Load client profile from YAML."""
    if not path.exists():
        sys.stderr.write(f"Profile not found at {path}\n")
        sys.exit(1)
    with open(path) as f:
        return yaml.safe_load(f)


# ─────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Compute priority scores for platforms in karma-booster authority DB."
    )
    parser.add_argument("--profile", type=Path, help="Path to client profile YAML")
    parser.add_argument(
        "--objective",
        choices=list(WEIGHT_PROFILES.keys()),
        default="balanced",
        help="Client objective (drives weight profile)",
    )
    parser.add_argument("--sector", default=None, help="Client sector (for bonus)")
    parser.add_argument(
        "--bandwidth",
        choices=list(BANDWIDTH_PENALTY.keys()),
        default="medium",
        help="Client bandwidth for content production",
    )
    parser.add_argument("--top", type=int, default=20, help="How many top platforms to show")
    parser.add_argument(
        "--category",
        default=None,
        help="Filter results to single category (e.g. tech_dev, owned_anchor)",
    )
    parser.add_argument("--db", type=Path, default=None, help="Path to authority DB YAML")

    args = parser.parse_args()

    # If profile provided, override individual flags
    if args.profile:
        profile = load_profile(args.profile)
        objective = profile.get("objective", args.objective)
        sector = profile.get("sector", args.sector)
        bandwidth = profile.get("bandwidth", args.bandwidth)
        print(f"Client: {profile.get('name', '?')}")
        print(f"Sector: {sector} · Objective: {objective} · Bandwidth: {bandwidth}")
        print("─" * 80)
    else:
        objective = args.objective
        sector = args.sector
        bandwidth = args.bandwidth

    platforms = load_db(args.db)

    if args.category:
        platforms = [p for p in platforms if p.get("category") == args.category]

    scored = [score_platform(p, objective, sector, bandwidth) for p in platforms]
    scored.sort(key=lambda r: r["final_score"], reverse=True)

    # Print top N
    print(f"\nTop {min(args.top, len(scored))} platforms"
          f" (objective={objective}, sector={sector or 'none'}, bandwidth={bandwidth}):\n")

    print(f"{'#':<3} {'PLATFORM':<35} {'SCORE':>6}  {'CAT':<22} {'STATUS':<10} BRINGS")
    print("─" * 145)

    for i, r in enumerate(scored[: args.top], start=1):
        bonus_mark = " ★" if r["sector_bonus_applied"] else "  "
        print(
            f"{i:<3} {r['name'][:33]:<33}{bonus_mark} "
            f"{r['final_score']:>6.1f}  "
            f"{r['category'][:20]:<22} "
            f"{r['status']:<10} "
            f"{r['brings'][:80]}"
        )

    print()
    print("★ = sector bonus applied (+30%)")
    print(f"Weights used: g={WEIGHT_PROFILES[objective]['google']:.2f} "
          f"l={WEIGHT_PROFILES[objective]['llm']:.2f} "
          f"t={WEIGHT_PROFILES[objective]['trust']:.2f}")


if __name__ == "__main__":
    main()
