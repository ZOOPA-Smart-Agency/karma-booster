# karma-booster

> Skill de Claude Code para evaluar y impulsar la autoridad digital de cualquier profesional. Toma un perfil de entrada, calcula el **Digital Karma Index (DKI)** sobre las 5 capas que importan, identifica las plataformas relevantes según sector, y genera un plan personalizado por fases (Foundation · Build · Scale).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![ZOOPA](https://img.shields.io/badge/by-ZOOPA--Smart--Agency-blue.svg)](https://zoopa.es)

## Qué hace este skill

1. Recibe perfil del profesional (LinkedIn URL, CV PDF, sitio web, o cuestionario)
2. Identifica sector + sub-sector + audiencia objetivo
3. Calcula **DKI baseline** (0-1000) con breakdown en 5 capas
4. Compara con benchmarks del sector
5. Identifica gaps priorizados
6. Genera plan personalizado 90 días (Foundation/Build/Scale)
7. Recomienda plataformas core para el sector específico
8. Integra con Authority Boost 90 service de Zoopa

## El Digital Karma Index (DKI)

Score composite 0-1000 que mide autoridad digital cross-platform de un profesional. Compuesta de 5 capas con pesos según impacto real en visibilidad:

```
DKI = (E × 0.40) + (D × 0.20) + (L × 0.15) + (T × 0.15) + (O × 0.10)

E = Earned Authority    (followers + karma nativos, ponderados por sector)
D = Discoverability     (Wikipedia + Wikidata + Schema.org + Google KP + directorios)
L = LLM Visibility      (vía GEORadar: SoV + Position + Sentiment + Co-branding)
T = Trust Signals       (Recommendations + Reviews + Press + Verified + TEDx)
O = Owned Anchor        (sitio personal DA + newsletter + long-form + libros)
```

Scale interpretation:
- 0-100 · **Invisible**
- 100-300 · **Emerging**
- 300-500 · **Established en niche**
- 500-700 · **Recognized regional/sectorial**
- 700-900 · **Leading authority**
- 900-1000 · **Top of field globally**

Detalle completo: [`references/digital-karma-formula.md`](references/digital-karma-formula.md)

## Sectores cubiertos (20)

1. Tech / Software / Engineer
2. Legal
3. Medical / Healthcare
4. Actor / Performing Arts
5. Designer / Creative
6. Academic / Researcher
7. CEO B2B SaaS / Founder
8. Chef / Restaurant
9. Writer / Author
10. Musician
11. Architect
12. Athlete
13. Politician
14. Consultant / Coach
15. Journalist / Analyst
16. Influencer / Creator
17. Investor / VC
18. Real Estate Pro
19. Financial Pro
20. Catch-all dinámico (otros) — busca plataformas vía WebSearch

Cada sector tiene su mapping de plataformas con pesos `W_sector` 0-3.

## Platform Authority Database (86 plataformas scored · sistema vivo)

> **A partir de V1.2** el catálogo legacy se sustituye por una **base de datos viva con scores propietarios** en 3 dimensiones (Google authority, LLM authority, Trust signal) + mantenimiento trimestral disciplinado. Ver [`references/platform-authority-db.yaml`](references/platform-authority-db.yaml).

### El qué

86 plataformas catalogadas en 19 categorías. Cada entrada tiene:

- **3 scores de autoridad** (0-100): `google`, `llm`, `trust`
- **Status**: `live` · `emerging` · `declining` · `dead`
- **Effort**: cuánto cuesta mantener presencia activa
- **LLMs citing**: qué LLMs específicamente la usan como fuente
- **Sectors bonus**: sectores donde puntúa extra
- **Brings**: 1-liner de qué aporta al perfil

### Cómo se usa

Script `scripts/authority_score.py` compone scores según objetivo + sector + bandwidth del cliente:

```bash
# Top 12 plataformas para un perfil tech buscando visibilidad LLM
python scripts/authority_score.py --objective llm --sector tech --bandwidth medium --top 12

# Top 10 para un abogado buscando trust signals
python scripts/authority_score.py --objective trust --sector lawyer --top 10

# Top 10 sólo de la categoría tech_dev
python scripts/authority_score.py --category tech_dev --top 10

# Desde un profile YAML
python scripts/authority_score.py --profile clients/{slug}/profile.yaml
```

Objectives disponibles: `google` · `llm` · `trust` · `balanced` (default).
Bandwidth: `low` · `medium` · `high` (penaliza plataformas high-effort si low).

### Pesos por objetivo

| Objetivo | w_google | w_llm | w_trust |
|---|---|---|---|
| Aparecer mejor en Google | 0.55 | 0.20 | 0.25 |
| Aparecer en LLMs (GEO) | 0.20 | 0.55 | 0.25 |
| Trust signals B2B | 0.25 | 0.20 | 0.55 |
| Balanced (default) | 0.40 | 0.30 | 0.30 |

### Mantenimiento

Review trimestral disciplinada (25 ene · 25 abr · 25 jul · 25 oct) con checklist en [`references/platform-maintenance-system.md`](references/platform-maintenance-system.md):

1. Health check de las 86 plataformas (DNS + status + scores estimados siguen siendo correctos)
2. Scan de candidatas nuevas (Product Hunt, HN, TechCrunch, GEORadar runs)
3. Demotion de plataformas declining/dead
4. Re-scoring evidence pass para 5-10 platforms (rotativo)

PRs al repo requieren **evidencia citable** (SERP screenshot, respuesta LLM, datos públicos).

### Metodología de scoring

Cómo se asignan los scores (criterios + evidencia + honestidad sobre límites V1) en [`references/platform-authority-methodology.md`](references/platform-authority-methodology.md). Resumen:

- Scores **direccionales** basados en conocimiento operacional Zoopa (16+ marcas en GEORadar, ~9M menciones analizadas)
- ±5pt dentro de mismo tier es ruido; diferencias de tier son reales
- Roadmap V2: integration GEORadar API + Common Crawl stats + Ahrefs/Semrush para scores empíricos automatizados

### Vista resumen del universo (para conversación cliente)

> Resumen visible **en el sitio público AB90**: https://zoopa-smart-agency.github.io/authority-boost-90/ (página 03 "Universo de medios"). Útil cuando un prospect quiere ver el alcance sin profundizar en YAML.

Lista compacta original (sigue válida como vista rápida humano-readable):

### Bloque 01 · Owned anchor (tu casa) — 4

`Web personal` · `Newsletter` · `Blog canonical` · `Podcast host`

### Bloque 02 · Generales de distribución — 10

`LinkedIn` · `X / Twitter` · `Bluesky` · `Threads` · `Mastodon` · `Facebook` · `Instagram` · `TikTok` · `YouTube` · `Quora`

### Bloque 03 · Comunidad / Q&A — 4

`Hacker News` · `Reddit` · `Stack Overflow` · `Discord`

### Bloque 04 · Editorial / Newsletter — 4

`Substack` · `Medium` · `LinkedIn Newsletter` · `Beehiiv`

### Bloque 05 · Discoverability / Knowledge graphs — 4

`Wikipedia` · `Wikidata` · `Google Knowledge Panel` · `Schema.org Person`

### Bloque 06 · Reviews / Trust signals — 6

`Google Reviews / Local Guide` · `Trustpilot` · `G2` · `Glassdoor` · `Goodreads` · `Amazon Author`

### Bloque 07 · Tech-specific (devs, founders, makers) — 6

`GitHub` · `Dev.to` · `Hashnode` · `Lobste.rs` · `HackerNoon` · `DZone`

### Bloque 08 · Academic / Research — 5

`Google Scholar` · `ORCID` · `ResearchGate` · `Semantic Scholar` · `arXiv`

### Bloque 09 · Sector-specialized — 14+

`IMDb` · `Spotify for Artists` · `Doximity` · `Sermo` · `JD Supra` · `Avvo` · `Dribbble` · `Behance` · `ArchDaily` · `Dezeen` · `Crunchbase` · `AngelList` · `Indie Hackers` · `Product Hunt`

Mapping ejemplo por sector:
- **Actor**: IMDb · Spotify · Instagram · TikTok
- **Médico**: Doximity · Sermo · Google Reviews
- **Abogado**: JD Supra · Avvo · LinkedIn
- **Diseñador**: Dribbble · Behance · Are.na
- **Arquitecto**: ArchDaily · Dezeen · Instagram
- **Founder**: Crunchbase · AngelList · Product Hunt

### Bloque 10 · Comunidad activa · Events · LLM surfaces — 8

`TED / TEDx` · `Conference circuit` · `Podcast guesting` · `HARO / Qwoted` · `ChatGPT` · `Claude` · `Perplexity` · `Google AI Overviews`

> Las 4 superficies LLM (capa 5 del framework) se miden con **GEORadar** (SoV · Position · Sentiment · Co-branding). Ningún competidor de personal branding las cubre.

### Regla operativa

En el kickoff calculamos DKI baseline y elegimos contigo las **5-8 plataformas core** donde concentrar Foundation / Build / Scale. El resto queda en mantenimiento de identidad. No prometemos cubrir 45 canales en 90 días: prometemos elegir bien y ejecutar a fondo.

Catálogo técnico completo (con métricas + normalizaciones): [`references/platform-catalog-master.md`](references/platform-catalog-master.md)
Mapping sectorial con pesos: [`references/sector-platform-mappings.md`](references/sector-platform-mappings.md)

## Cómo usar el skill

### Invocación

En Claude Code, escribir:
```
karma booster
```

O el trigger natural:
```
calcula mi digital karma
evalúa mi perfil online
qué plataformas debería trabajar
```

### Inputs aceptados

| Input | Cómo proveerlo |
|---|---|
| LinkedIn URL pública | Pega URL `linkedin.com/in/{slug}` |
| CV / Resume PDF | Adjunta el PDF |
| Sitio web personal | Pega URL del dominio |
| Cuestionario interactivo | El skill te hace 6 turnos de preguntas |

### Output

3 documentos:

1. `{client-slug}-profile-assessment.md` — perfil estructurado
2. `{client-slug}-dki-baseline-report.md` — DKI calculado + gaps
3. `{client-slug}-personalized-plan.md` — plan 90 días

Outputs van a `~/Documents/claudecode-proj/karma-booster-clients/{slug}/` (LOCAL, NUNCA al repo).

## Privacidad y GDPR

- **NUNCA scrapear** LinkedIn sin consentimiento explícito del cliente
- Datos del cliente guardados LOCAL, no en este repo
- Retención datos: 30 días post-cierre cliente
- Atender solicitudes GDPR (acceso/borrado/portabilidad) en 72h
- CVs procesados en memoria, no se guarda el PDF original

## Integración con ecosistema Zoopa / 498A

Este skill es la herramienta de evaluación inicial del servicio comercial **Authority Boost 90** (3 meses, €5-30K según tier).

| Skill / Producto | Función |
|---|---|
| **karma-booster** (este skill) | Evaluación + plan inicial |
| **content-factory** | Genera contenido para los canales recomendados |
| **GEORadar** (producto Zoopa) | Mide L (LLM Visibility) en el DKI |
| **DOC** (producto Zoopa) | Optimiza AX del sitio personal del cliente |
| **S.A.M.** (producto Zoopa) | Valida contenido contra prompts target |
| **Authority Boost 90** (servicio comercial) | Ejecución del plan completo 90 días |

## Estructura del skill

```
karma-booster/
├── SKILL.md                                # Orchestrator principal
├── README.md                               # Este archivo
├── references/
│   ├── digital-karma-formula.md           # DKI formula completa
│   ├── platform-catalog-master.md         # 45 plataformas
│   ├── sector-platform-mappings.md        # 20 sectores → plataformas
│   ├── profile-assessment-process.md      # Cómo procesar inputs
│   ├── phase-system.md                    # Foundation/Build/Scale
│   └── content-styles-imports/            # Style guides imported
│       ├── linkedin-voice.md
│       ├── linkedin-optimization-deep-dive.md
│       ├── x-twitter-voice-style.md
│       ├── substack-style.md
│       ├── quora-best-practices.md
│       ├── orthography-rules.md
│       ├── platform-mechanics.md
│       └── editorial-patterns.md
├── scripts/
│   └── calculate_dki.py                   # DKI calculator
├── templates/                              # Output templates (próximo)
└── examples/
    ├── carlos-ortet-case-study.md         # Case study V1 (senior)
    └── guillermo-cardiel-case-study.md    # Case study V1.1 (junior, contraste)
```

## Servicio comercial · Authority Boost 90

El skill karma-booster es el **calculador DKI + planificador** que alimenta el servicio comercial **Authority Boost 90** de Zoopa Smart Agency.

- **Sitio público compartible**: https://zoopa-smart-agency.github.io/authority-boost-90/
- **Página de case studies**: https://zoopa-smart-agency.github.io/authority-boost-90/case-studies.html
- **Equipo core 6 personas**: Carlos Ortet (Strategy) · Mer Canet (Biz) · Mia Ortet (Product) · Matteo Remuzzi (Service) · Guillermo Cardiel (Workflow) · Pol Reyes (New biz)

### Case studies publicados (2)

| Profile | Tipo | DKI baseline | DKI día 90 | Delta |
|---|---|---|---|---|
| **Carlos Ortet** | Senior · Tech / Designer | 356 | 560 | +204 |
| **Guille Cardiel** | Junior · Workflow design | 142 | 385 | +243 |

Demuestran el USP del método: funciona en ambos extremos del seniority. Ver `examples/` para el detalle de cada caso.

## Versionado

- **V1.0** · 2026-05-24 · skill creado. Case study Carlos Ortet
- **V1.1** · 2026-05-25 · case study Guille Cardiel añadido (perfil junior contraste) + sitio público AB90 V1.4
- **V1.2** (próximo) · añadir 5+ sectores con primeros clientes externos
- **V1.5** · integration con GEORadar API para L automático
- **V2.0** · web UI público en `zoopa.es/karma-checker` (audit free como lead gen)

## Contribuir

Este skill se mantiene por el equipo Zoopa / 498A. Para añadir:
- **Nueva plataforma**: PR a `references/platform-catalog-master.md` + actualizar normalizer en `scripts/calculate_dki.py`
- **Nuevo sector**: PR a `references/sector-platform-mappings.md` con pesos validados
- **Lessons aprendidos**: PR a `examples/{client}-case-study.md`

## Licencia

MIT.

## Maintainers

- **Carlos Ortet** ([carlosortet.com](https://carlosortet.com)) · CEO Zoopa · Director 498A
- **Mer Canet** · Operaciones contenido
- **Community lead GEORadar** · Medición LLM visibility

## Links

- [Zoopa](https://zoopa.es) · Innovation & Creative Technology
- [498AS](https://498as.com) · AI R&D Division
- [GEORadar](https://georadar.app) · LLM brand visibility
- [content-factory skill](https://github.com/498AS/content-factory) · skill complementario

---

*Skill iniciado 2026-05-24. Producto de la metodología desarrollada en la agencia Zoopa para Authority Boost 90 service.*
