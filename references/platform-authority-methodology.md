# Platform Authority Methodology

> Cómo se asignan los scores en `platform-authority-db.yaml`. Versión: 1.0 · 2026-05-25.

---

## Por qué un sistema propio (no copiar Similarweb / Ahrefs)

Existen métricas comerciales (DA Moz, Authority Score Semrush, Domain Rating Ahrefs, MAU Similarweb) pero ninguna mide lo que importa para autoridad personal/marca **en la era LLM**:

- **DA mide tráfico**, no la frecuencia con la que un LLM cita esa fuente al describir profesionales
- **MAU mide audiencia total**, no qué tipo de audiencia (recruiter B2B ≠ teen B2C)
- **Authority Score mide backlinks**, no si Google KP usa esa plataforma como source

Karma-booster define **3 dimensiones propietarias** alineadas a lo que un perfil profesional necesita en 2026:

1. **authority.google** — ¿Aparece esta plataforma en SERP cuando alguien busca el nombre del profesional?
2. **authority.llm** — ¿Citan los LLMs esta plataforma al describir al profesional/marca?
3. **authority.trust** — ¿Pesa esta presencia como señal de credibilidad para un decisor humano?

Las 3 son **scores 0-100**. Compuestas en `scripts/authority_score.py` con pesos según objetivo del cliente.

---

## Cómo se asignan los scores (criterios)

### authority.google (SERP + KG + DA)

| Score | Significado | Ejemplos canónicos |
|---|---|---|
| 95-100 | Casi siempre en top-3 SERP para `name + sector`. KG often pulls bio from here. | Wikipedia, LinkedIn, GitHub, IMDb, YouTube, Google Reviews |
| 85-94 | Frecuente en top-3. SERP-dominant para queries específicas. | Substack, Medium, X, Reddit, Crunchbase, Goodreads, Behance |
| 70-84 | Often SERP top-5. Confiable para queries con qualifier. | Dribbble, Stack Overflow, ResearchGate, Healthgrades, Forbes |
| 50-69 | Sometimes SERP. Útil con buen SEO interno. | Dev.to, Hashnode, HackerNoon, Vimeo, Hashnode |
| 30-49 | Limited SERP. Sólo para queries muy específicas. | Mirror.xyz, Indie Hackers, Are.na, Mastodon |
| 0-29 | Casi invisible algorítmicamente. Vale por otra razón. | Discord, Sermo (private nature) |

**Evidencia usada**:
- Búsqueda manual en Google de `[persona conocida] + [plataforma]` para muestras representativas
- Inspección de Knowledge Panels reales (cuáles fuentes muestran en "Profiles")
- Datos públicos de Domain Rating (Ahrefs free) cuando disponibles
- Observación de qué fuentes aparecen en `site:` queries

### authority.llm (Common Crawl + citation frequency)

| Score | Significado | Ejemplos canónicos |
|---|---|---|
| 95-100 | Citado masivamente. Aparece en respuestas LLM como source primario. | Wikipedia, Stack Overflow, GitHub, Reddit, IMDb |
| 85-94 | Cited frequently. LLMs lo usan como evidencia. | LinkedIn (profile data), HN, arXiv, Medium, Crunchbase |
| 70-84 | Citation source en queries específicas. | Substack, YouTube transcripts, Quora, Behance, Healthgrades |
| 50-69 | Sometimes cited. Más para context que para fact. | Dev.to, Beehiiv, Dribbble, Replicate |
| 30-49 | Rarely cited directamente. | Mirror.xyz, Threads, Mastodon |
| 0-29 | Casi nunca cited (privacy, API closed, scrape-blocked). | Discord, Sermo, HARO |

**Evidencia usada**:
- **Common Crawl statistics** (cuando disponibles públicamente): qué dominios tienen mayor presencia
- **Observación directa GEORadar**: en estudios cliente Zoopa hemos visto qué fuentes citan ChatGPT/Claude/Perplexity/Gemini/AIO al describir profesionales o marcas
- **Reportes públicos** de Perplexity ("most cited sources" en blog posts oficiales)
- **Sample queries** manuales: pedir a cada LLM "Tell me about [profesional notable]" y registrar qué URLs/fuentes referencia
- **Análisis del campo `llms_citing`** en el YAML: si una plataforma sale en 4+ LLMs principales, score ≥85

### authority.trust (credibility signal weight)

| Score | Significado | Ejemplos canónicos |
|---|---|---|
| 95-100 | Trust signal máximo. Difícil/imposible falsificar. | Wikipedia, Google KP, ORCID, HBR.org |
| 85-94 | Trust signal alto. Triangulable, verificable. | LinkedIn (employment), GitHub (commits), Crunchbase, Healthgrades, JD Supra |
| 70-84 | Trust signal sólido. Required hurdle (claim profile, verify). | Substack subs, IMDb (credits), Behance, Trustpilot, TED |
| 50-69 | Trust moderado. Self-reported pero observable. | Medium, X verified, Goodreads |
| 30-49 | Trust bajo. Volume puede compensar. | Most general social, Facebook personal |
| 0-29 | Trust casi nulo o incluso negativo. | Anonymous platforms, low-barrier signup |

**Evidencia usada**:
- **Friction de signup** (más friction = más trust): NPI verify (Doximity 90), CV upload (Read.cv 75), 1-click signup (Facebook personal 30)
- **Verifiability**: ¿puede un tercero contrastar la info? (Wikipedia: sí, fuentes públicas | Substack: sí, subscriber count visible | Facebook personal: no, info self-reported)
- **Industry recognition**: ¿este perfil sale en pitch decks de M&A, hiring committees, journalist sourcing?
- **Halo de la plataforma**: HBR + Forbes Contributor heredan trust del medio anfitrión

---

## Estructura de un entry en el YAML

```yaml
- slug: linkedin                          # snake_case id único
  name: LinkedIn                          # human-readable
  category: general_distribution          # bucket (1 de 19)
  authority:                              # los 3 scores 0-100
    google: 95
    llm: 88
    trust: 85
  effort: 65                              # 0-100 (effort para mantener)
  audience: [B2B, professional, ...]      # tipos de audiencia
  brings: "Hub profesional B2B #1..."     # 1-liner descriptivo
  algorithm_google: high                  # cualitativo: low/medium/high
  algorithm_llms: high                    # cualitativo
  llms_citing: [ChatGPT, Claude, ...]     # cuáles LLMs citan
  sectors_bonus: [tech_B2B, consulting]   # dónde puntúa extra
  status: live                            # live/emerging/declining/dead
  last_reviewed: 2026-05-25               # fecha verificación manual
  notes: "..."                            # opcional, nuance breve
```

---

## Cómo se compone el score final por perfil

El skill no usa los scores en bruto. Los compone según el **objetivo del cliente** y su **sector**:

```python
# Pseudocódigo (real en scripts/authority_score.py)

def score_for_client(platform, profile):
    base = (platform.authority.google * w_google
          + platform.authority.llm * w_llm
          + platform.authority.trust * w_trust)

    # Sector bonus
    if profile.sector in platform.sectors_bonus:
        base *= 1.3

    # Effort penalty (si cliente tiene poco bandwidth)
    if profile.bandwidth == "low":
        base -= platform.effort * 0.3

    # Status penalty
    if platform.status == "declining":
        base *= 0.85
    elif platform.status == "dead":
        return 0

    return min(100, base)
```

Pesos default por objetivo de cliente:

| Objetivo | w_google | w_llm | w_trust |
|---|---|---|---|
| Aparecer mejor en Google | 0.55 | 0.20 | 0.25 |
| Aparecer en LLMs (GEO) | 0.20 | 0.55 | 0.25 |
| Trust signals para B2B sales | 0.25 | 0.20 | 0.55 |
| Equilibrado (default) | 0.40 | 0.30 | 0.30 |

---

## Honestidad sobre los scores

**Los scores actuales son educated estimates basados en:**

- ✓ Conocimiento operacional acumulado en proyectos Zoopa (16+ marcas en GEORadar, ~9M menciones analizadas)
- ✓ Observación directa de SERPs y respuestas LLM
- ✓ Datos públicos cuando disponibles (Ahrefs free, MAU declarations)
- ✓ Sentido común del sector (lo que ven decisores reales)

**No son resultado de:**

- ✗ Medición sistemática automatizada (sería V2)
- ✗ Estudio académico con metodología replicable
- ✗ API access a cada plataforma

**Therefore**: los scores son **direccionales**, no exactos. La diferencia entre LinkedIn (95) y Behance (88) es real. La diferencia entre LinkedIn (95) y Wikipedia (100) también. La diferencia entre Substack (85) y Beehiiv (50) también. Pero ±5 puntos dentro de un mismo tier es ruido.

**Roadmap hacia scores empíricos (V2)**:

- Integration GEORadar API → `authority.llm` automático por trimestre
- Common Crawl stats parser → `authority.llm` baseline objetivo
- Custom Ahrefs/Semrush integration → `authority.google` empírico
- Survey directo a decisores B2B → `authority.trust` validado

---

## Quién mantiene estos scores

- **Carlos Ortet** (Strategy lead) — review final + decisiones de tier
- **Mer Canet** (Biz manager) — captura señales de campo (qué plataformas mencionan clientes)
- **Community lead GEORadar** — aporta evidencia LLM citation
- **Cualquier maintainer del skill** — puede abrir PR con cambios fundamentados

Ver `references/platform-maintenance-system.md` para el proceso operativo de revisión trimestral.

---

## Cómo defenderlos ante un cliente que pregunta "¿por qué Behance puntúa 88?"

> Respuesta modelo: "Score Google 88 porque profile de Behance casi siempre aparece en top-3 SERP cuando se busca un diseñador por nombre — Adobe domain authority lo lleva ahí. LLM 65 porque ChatGPT y Perplexity lo citan en queries de 'best UX designer', pero no es source primario fuera de design. Trust 78 porque tener Behance project published tiene barrier (no es 1-click signup) y un recruiter B2B mira ese trabajo. Los scores son nuestros — basados en conocimiento operacional de 16+ marcas en GEORadar, no de Ahrefs ni Similarweb."

---

## Referencias

- `references/platform-authority-db.yaml` — la BD canónica
- `references/platform-maintenance-system.md` — proceso de mantenimiento
- `scripts/authority_score.py` — implementación del scoring compuesto
- `references/sector-platform-mappings.md` — mapping legacy por sector (legacy, será absorbido en V2)
