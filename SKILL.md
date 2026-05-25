# Skill: karma-booster

> Servicio sistemático para impulsar la autoridad digital de un profesional. Toma un perfil de entrada (LinkedIn URL, CV, sitio personal o cuestionario), lo evalúa contra el catálogo de 40+ plataformas, identifica las relevantes para el sector específico, calcula el Digital Karma Index (DKI) actual y target, y produce un plan personalizado por fases.
>
> Producto orientado a profesionales de cualquier sector: actores, ingenieros, abogados, CEOs B2B, académicos, médicos, diseñadores, chefs, escritores, músicos, arquitectos, atletas, políticos, consultores, periodistas, founders.
>
> Maintained by Zoopa / 498A. Public repo: https://github.com/ZOOPA-Smart-Agency/karma-booster

## Cuándo invocar este skill

- Cuando el usuario dice "calcula mi digital karma" / "evalúa mi perfil online" / "qué plataformas debería trabajar"
- Cuando el usuario es un cliente nuevo de Authority Boost 90 y necesita audit inicial
- Cuando se necesita comparar el perfil del cliente vs benchmarks del sector
- Cuando hay que generar plan personalizado de presencia digital
- Para revisión trimestral del DKI de un cliente activo

## Flujo principal (overview)

```
1. INPUT  → Profile assessment
            (LinkedIn URL · CV PDF · sitio web · cuestionario)
2. PARSE  → Sector identification + platform inventory
3. CALC   → DKI baseline + benchmarks sector
4. SEARCH → Platforms especializadas del sector (si no en catálogo base)
5. PLAN   → Phases Foundation/Build/Scale personalizadas
6. OUTPUT → Reporte de baseline + plan personalizado + cadencia operativa
```

## PASO 1: Profile assessment (input)

El usuario proporciona AL MENOS UNO de:

| Input | Procesado por |
|---|---|
| LinkedIn profile URL | scripts/assess_profile.py (parser HTML público) |
| CV / Resume PDF | OCR + extract estructurado |
| Sitio web personal (About section) | scraper + extract |
| Cuestionario interactivo | references/profile-assessment-process.md § "Cuestionario manual" |

Si faltan inputs, pregunta de forma estructurada (NO bombardear con 20 preguntas a la vez). Ver `references/profile-assessment-process.md` para el cuestionario óptimo.

## PASO 2: Sector identification

Output esperado:

```yaml
sector_primario: "Tech / Software Engineering"     # de la lista canónica
sub_sector: "AI / GEO / LLM brand visibility"
geografia: "EU · Catalunya / España"
idiomas: ["ES", "EN", "CA"]
career_stage: "Senior · CEO/Founder"
audiencia_objetivo: "C-level B2B, founders SaaS, agencias EU"
diferenciador_principal: "Única persona uniendo GEO + producción audiovisual + I+D LLM"
```

Sectores canónicos en `references/sector-platform-mappings.md`:
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
20. (catch-all: dynamic search via web)

## PASO 3: DKI baseline calculation

Aplicar fórmula completa en `references/digital-karma-formula.md`. Output:

```yaml
DKI_baseline: 285   # score 0-1000
DKI_tier: "Emerging" # 100-300
breakdown:
  earned_authority: 145  # max 400
  discoverability:  35   # max 200
  llm_visibility:   12   # max 150
  trust_signals:    65   # max 150
  owned_anchor:     28   # max 100
benchmarks_sector:
  promedio:        420
  top_10_percent:  680
  top_1_percent:   850
gap_to_close: 135     # tier objetivo - DKI baseline
```

## PASO 4: Platform search dinámico

Para sectores fuera del catálogo base o sub-sectores muy específicos, usar WebSearch:

```
"top platforms for [sub_sector] professionals 2026"
"where do [sub_sector] [career_stage] publish in [geografia]"
"[sub_sector] community sites high authority"
```

Documentar hallazgos en el output. Si encuentras 2+ plataformas relevantes nuevas, proponer añadirlas al `platform-catalog-master.md`.

## PASO 5: Plan personalizado por fases

Aplicar `references/phase-system.md` adaptado al sector + DKI baseline:

- **Foundation (días 1-30)**: las 2-3 capas más urgentes según gap analysis
- **Build (días 31-60)**: cadencia operativa multi-plataforma
- **Scale (días 61-90)**: leverage + new asset launches

## PASO 6: Output al usuario

3 documentos:

1. `{client}-profile-assessment.md` (en directorio del cliente)
2. `{client}-dki-baseline-report.md`
3. `{client}-personalized-plan.md`

Si el cliente es de Authority Boost 90, los 3 docs se integran al deliverable de fase 1.

## Reglas operativas críticas

### Privacidad y consentimiento

- **NUNCA** scrapear LinkedIn sin consentimiento explícito del usuario
- **NO** almacenar CVs ni perfiles en este repo (gitignore)
- Outputs cliente van a `~/Documents/claudecode-proj/karma-booster-clients/{client_slug}/` (LOCAL, gitignored)
- GDPR-compliant: borrar datos del cliente cuando deja de ser cliente activo (+30 días retention)

### Reglas globales heredadas de content-factory

Aplicar siempre `references/content-styles-imports/orthography-rules.md` § 3:
- Sin em-dash (`—`)
- Sin referencias temporales relativas (esta semana, este año, hoy)
- Sin frases formulaicas LLM

### HN auto-flag warning (24 may 2026)

Plataformas que detectan contenido LLM y bloquean: **Hacker News** (clasificador genAI activo). Para HN, el cliente debe escribir 100% manual. Documentado en `references/content-styles-imports/lessons-hn-genai-flag.md`.

## Files del skill

| File | Purpose |
|---|---|
| `SKILL.md` | Este archivo (orchestrator) |
| `README.md` | Public-facing |
| `references/digital-karma-formula.md` | DKI formula completa con fórmula matemática |
| `references/platform-authority-db.yaml` | **86 plataformas scored** (Google/LLM/Trust 0-100) · canonical source V1.2+ |
| `references/platform-authority-methodology.md` | Cómo se asignan los scores · evidencia · honestidad sobre límites V1 |
| `references/platform-maintenance-system.md` | Cadencia trimestral · checklist · template PR · fuentes a consultar |
| `references/platform-catalog-master.md` | Catalog legacy V1.0-V1.1 (prosa rica, mantener como vista detallada) |
| `references/sector-platform-mappings.md` | Mapping sectores → plataformas (legacy, será absorbido en V2) |
| `references/profile-assessment-process.md` | Cómo procesar inputs + cuestionario manual |
| `references/phase-system.md` | Foundation/Build/Scale adaptable |
| `references/content-styles-imports/*` | Copias de content-factory (style guides) |
| `scripts/calculate_dki.py` | Implementation de la fórmula DKI |
| `scripts/authority_score.py` | **Compute scoring compuesto** según objective + sector + bandwidth |
| `templates/*.md` | Output templates |
| `examples/carlos-ortet-case-study.md` | Case study V1 (senior · Tech/Designer) |
| `examples/guillermo-cardiel-case-study.md` | Case study V1.1 (junior · Workflow design) |

## Integración con otros skills

- **content-factory**: el plan generado lista canales específicos. Cuando se ejecuta contenido para esos canales, content-factory hace el drafting con voces apropiadas
- **GEORadar** (Zoopa producto): integra como Capa 5 (LLM visibility) del DKI
- **DOC** (Zoopa): optimiza la AX del sitio personal del cliente como parte de Foundation phase
- **Authority Boost 90** (servicio Zoopa): karma-booster es la herramienta de evaluación inicial del servicio AB90
  - Sitio público compartible: https://zoopa-smart-agency.github.io/authority-boost-90/
  - Page case studies: https://zoopa-smart-agency.github.io/authority-boost-90/case-studies.html

## Versionado

- **V1.0** · 2026-05-24 · skill creado. Case study Carlos Ortet (senior, DKI 356 → 560)
- **V1.1** · 2026-05-25 · case study Guille Cardiel añadido (junior, DKI 142 → 385) · sitio público AB90 desplegado V1.4
- **V1.2** · 2026-05-25 · **Platform Authority Database** · 86 platforms scored en 3 dims (Google/LLM/Trust) · methodology doc + maintenance system trimestral + script `authority_score.py`

Próximas iteraciones:
- V1.3: añadir 5+ sectores especializados con primeros clientes externos
- V1.5: integration con GEORadar API para LLM visibility automático (scores empíricos en lugar de estimados)
- V1.7: integration Common Crawl + Ahrefs free check para auto-update trimestral
- V2.0: web UI público en zoopa.es/karma-checker (audit free como lead gen)
