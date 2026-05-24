# Digital Karma Index (DKI) · Fórmula y metodología

> Métrica composite 0-1000 que mide la autoridad digital cross-platform de un profesional. Compuesta de 5 capas con pesos asignados según impacto en visibilidad real (LLM citations + descubribilidad + trust signals + earned + owned).
>
> Versión: 1.0 · 2026-05-24
> Autor metodología: Carlos Ortet (Zoopa / 498A)

---

## Por qué inventamos DKI

Reddit y Quora tienen karma nativo. LinkedIn tiene SSI. HN tiene karma. Cada plataforma tiene su métrica pero **no existe una métrica unificada cross-platform** que mida autoridad real para un profesional.

Los problemas a resolver:
- LinkedIn followers no es comparable con HN karma
- Un actor con 100K Instagram followers no es comparable a un académico con h-index 30
- Las plataformas relevantes dependen del sector
- LLMs citan según señales agregadas, no de una plataforma

DKI resuelve esto con:
1. Normalización 0-100 por plataforma
2. Ponderación según sector relevance
3. Inclusión explícita de LLM visibility (GEORadar)
4. Trust signals + discoverability que LLMs valoran

---

## Fórmula matemática

```
DKI = (E × 0.40) + (D × 0.20) + (L × 0.15) + (T × 0.15) + (O × 0.10)

Donde:
E = Earned Authority Score        (0-1000, capped)
D = Discoverability Score          (0-1000, capped)
L = LLM Visibility Score           (0-1000, capped, vía GEORadar)
T = Trust Signals Score            (0-1000, capped)
O = Owned Anchor Score             (0-1000, capped)

DKI ∈ [0, 1000]
```

Pesos elegidos según importancia en función de impacto observado en autoridad real:
- **40% Earned**: la métrica primaria, lo que la audiencia genera
- **20% Discoverability**: foundational, sin esto el resto no escala
- **15% LLM Visibility**: futuro inmediato de descubribilidad
- **15% Trust Signals**: lo que cierra deals/credibility
- **10% Owned**: el cimiento, pero ya saturado si solo este

---

## 1. Earned Authority Score (E)

**Definición**: suma normalizada de la presencia en plataformas earned, ponderada por relevancia para el sector del profesional.

```
E = MIN(1000, Σ (P_i_normalized × W_sector_i × Q_i))

Para cada plataforma i:
P_i_normalized = score normalizado 0-100 según métrica nativa
W_sector_i = peso de la plataforma para el sector del profesional (0-3)
Q_i = quality multiplier (0.5-1.5) basado en engagement rate
```

### Normalización por plataforma (P_i)

| Plataforma | Métrica nativa | Cómo normalizar a 0-100 |
|---|---|---|
| LinkedIn | followers + SSI | `min(100, log10(followers/100) × 30 + SSI × 0.4)` |
| Twitter/X | followers + impressions | `min(100, log10(followers/100) × 25 + log10(monthly_impressions/1000) × 15)` |
| Bluesky | followers | `min(100, log10(followers/10) × 30)` |
| Threads | followers | `min(100, log10(followers/100) × 30)` |
| Mastodon | followers (fediverse) | `min(100, log10(followers/10) × 30)` |
| Hacker News | karma | `min(100, log10(karma) × 30)` |
| Reddit | karma combinado | `min(100, log10(total_karma) × 20)` |
| Quora | followers + answers | `min(100, log10(followers) × 25 + answers × 0.5)` |
| Medium | followers + total claps | `min(100, log10(followers) × 30 + log10(total_claps/100) × 15)` |
| Substack | subscribers + open rate | `min(100, log10(subs) × 30 + open_rate × 50)` |
| YouTube | subs + monthly views | `min(100, log10(subs/10) × 25 + log10(monthly_views/100) × 20)` |
| Instagram | followers + engagement rate | `min(100, log10(followers/10) × 25 + engagement_rate × 100)` |
| TikTok | followers + likes total | `min(100, log10(followers/10) × 25 + log10(total_likes/100) × 15)` |
| GitHub | followers + stars total | `min(100, log10(followers) × 30 + log10(total_stars) × 15)` |
| Stack Overflow | reputation | `min(100, log10(reputation) × 20)` |
| Dev.to | followers | `min(100, log10(followers/10) × 30)` |
| Hashnode | followers | `min(100, log10(followers/10) × 30)` |
| IMDb | star meter rank | `min(100, max(0, (50000 - rank) / 500))` |
| Spotify (artista) | monthly listeners | `min(100, log10(monthly_listeners/10) × 20)` |
| Google Scholar | h-index + citations | `min(100, h_index × 4 + log10(total_citations/100) × 10)` |
| ORCID | works count | `min(100, works × 2)` |
| ResearchGate | RG Score | `min(100, RG_score × 2)` |
| Dribbble | followers + appreciations | `min(100, log10(followers) × 25 + log10(appreciations) × 15)` |
| Behance | followers + project views | `min(100, log10(followers) × 25 + log10(total_project_views) × 15)` |
| (otras) | depend on platform | ver platform-catalog-master.md |

### Sector weight (W_sector)

Asignado en `sector-platform-mappings.md`. Valores:
- **3.0** = plataforma core para el sector
- **2.0** = plataforma muy relevante
- **1.0** = relevante pero no primaria
- **0.5** = adjacent, poco impacto
- **0** = irrelevante (excluida del cálculo)

### Quality multiplier (Q)

```
Q = 0.5 + (engagement_rate × 1.0) + (recency_factor × 0.5)

donde:
engagement_rate = 0-1 (post avg engagement vs followers)
recency_factor = 1 si último post < 14 días, 0.5 si <60d, 0 si <365d, -0.5 si 365d+
```

Q ∈ [0.5, 1.5]. Profile abandonado tiene Q bajo aunque tenga followers.

---

## 2. Discoverability Score (D)

**Definición**: cuán fácil es encontrar al profesional via búsqueda y agentes IA.

```
D = MIN(1000, Σ component_scores)

Componentes (suma directa):
- Wikipedia article (suyo o de su empresa principal)    : 200
- Wikidata entity (Q-number único)                       : 100
- Google Knowledge Panel triggered                       : 150
- Schema.org Person en sitio personal                    : 80
- ORCID active (académicos)                              : 70
- Personal domain (custom URL, no subdomain)             : 50
- llms.txt + robots.txt permitiendo bots IA              : 50
- Indexed en directorio sector (1 por directory)         : 30 × n (max 5)
- Wikipedia Commons photo CC                             : 30
- Google Scholar profile (académicos)                    : 50
- Crunchbase profile (founders)                          : 50
- AngelList/Wellfound (founders)                         : 40
- IMDb profile (actors/film)                             : 80
- Bar association profile (lawyers)                      : 50
- Medical directory (doctors: Doximity verified)         : 50
- Government voter directory (politicians: BallotPedia)  : 80
- Athletic governing body profile                        : 50
```

Notas:
- Wikipedia article propio es el oro (~200 puntos). Pocos lo logran.
- Schema.org Person + sameAs es low-hanging fruit.
- Sector-specific directories suben rápido si el profesional está activo.

---

## 3. LLM Visibility Score (L)

**Definición**: presencia y calidad de menciones en LLMs (ChatGPT, Claude, Gemini, Perplexity, Copilot, Google AI Overviews) cuando alguien pregunta sobre el nicho del profesional.

```
L = (SoV × 0.40) + (PositionScore × 0.30) + (SentimentScore × 0.20) + (CoBranding × 0.10)

donde:
SoV = Share of Voice in nicho queries (0-100, vía GEORadar)
PositionScore = orden en menciones list (0-100, vía GEORadar)
SentimentScore = polarity de menciones (0-100, vía GEORadar)
CoBranding = aparición junto a competidores top (0-100, vía GEORadar)

L ∈ [0, 100], multiplicado por 10 = 0-1000
```

**Requiere medición con GEORadar** o herramienta equivalente. Si no medido aún:
- Set baseline L = 0
- Marcar como "no medido" en el report
- Plan recomienda baseline en Foundation phase

---

## 4. Trust Signals Score (T)

**Definición**: validación externa que LLMs y humanos valoran.

```
T = MIN(1000, suma de componentes)

Componentes (lineal):
- LinkedIn Recommendations (cap 20)                      : 20 × N
- Google Reviews business owned (cap 100)                : 2 × N
- Trustpilot reviews (cap 100)                           : 2 × N
- G2 / Capterra reviews (cap 100)                        : 3 × N
- Yelp / Tripadvisor reviews (sector-specific, cap 50)   : 3 × N
- Goodreads ratings author (cap 200)                     : 1 × N
- Amazon Author reviews (cap 200)                        : 1 × N
- App Store reviews (founders apps, cap 1000)            : 0.5 × N
- IMDb credited projects (actors, cap 100)               : 5 × N
- Press mentions tier-1 (FT, Bloomberg, Wired, etc.)     : 30 × N (cap 10)
- Press mentions tier-2 (sectoriales)                    : 10 × N (cap 20)
- Verified badges (X, LinkedIn, Meta verified, etc.)     : 30 × N (cap 5)
- Years active publicly                                  : 20 × N (cap 10)
- Conference keynote tier-1 (cap 10)                     : 30 × N
- TEDx talk / TED talk                                   : 100 / 200
- Bar association membership (lawyers)                   : 50
- Medical license verified (doctors)                     : 50
- Patent count (engineers, cap 20)                       : 10 × N
```

---

## 5. Owned Anchor Score (O)

**Definición**: la fundación que controlas tú.

```
O = MIN(1000, suma de componentes)

Componentes:
- Personal website DA (Moz Domain Authority 0-100)       : DA × 5
- Newsletter subs (Substack/Mailchimp/Beehiiv)           : log10(subs/10) × 100, max 300
- Long-form content count owned (>1500 words)            : 5 × N, max 200
- Podcast host own (active last 3m)                      : 100
- Online course/curso/cohort program owned               : 150
- Self-hosted blog/portfolio domain                      : 80
- Book published (own or co-author)                      : 200 per book
- Open source project owned (>100 stars)                 : 50 per repo, max 200
```

---

## Scale interpretation

| DKI rango | Tier | Interpretación |
|---|---|---|
| 0-100 | **Invisible** | Cuenta nueva o profesional sin presencia digital |
| 100-300 | **Emerging** | Empezando, gaps masivos. AB90 puede 2x-3x el score |
| 300-500 | **Established en niche** | Presencia decente, optimizar para crecer |
| 500-700 | **Recognized regional/sectorial** | Top 10% del sector |
| 700-900 | **Leading authority** | Top 1-5% del sector |
| 900-1000 | **Top of field globally** | Top 0.1% global del sector |

---

## Ejemplo de cálculo: Carlos Ortet · 24 may 2026

### Inputs

```yaml
sector: "Tech / GEO consulting / B2B SaaS"
linkedin:
  followers: 5200
  ssi: not_measured  # assume 35 default
  posts_last_3m: 18
  engagement_rate_avg: 0.045  # 4.5%
twitter:
  followers: 850
  monthly_impressions: 8000
bluesky:
  followers: 0  # cuenta del 24 may
hackernews:
  karma: 1
quora:
  followers: 19
  answers: 1
medium:
  followers: 120
  total_claps: 850
substack:
  subscribers: 380
  open_rate: 0.42
mastodon:
  followers: 0
threads:
  followers: 5
facebook_personal:
  friends_estimate: 800
discoverability:
  wikipedia_article: false
  wikidata: false
  google_knowledge_panel: false
  schema_org_person: false  # carlosortet.com tiene, falta verify
  custom_domain: true       # carlosortet.com
  llms_txt: false
  crunchbase: false
trust:
  linkedin_recommendations: 4
  press_tier1: 1  # Harvard Deusto Business Review
  press_tier2: 3
  verified_badges: 1  # LinkedIn
  years_active: 8
georadar:
  sov: not_measured
owned:
  website_da: 18   # carlosortet.com
  newsletter_subs: 380
  long_form_content: 25
  self_hosted_blog: true
  book: 0
  podcast: 0
```

### Cálculo paso a paso

**E (Earned Authority)**:
- LinkedIn: P=68 (log10(52)×30 + 35×0.4 = 51.5+14=65), W=3.0, Q=1.0 → 195
- Twitter: P=42 (log10(8.5)×25 + log10(8)×15 = 23+13=36), W=2.0, Q=0.7 (low activity) → 50
- Bluesky: P=0 (log10(0)... → 0), W=2.0, Q=1.5 → 0
- HN: P=0 (log10(1)=0), W=3.0, Q=0.5 → 0
- Quora: P=20 (log10(19)×25=32 + 1×0.5), W=1.0, Q=0.8 → 16
- Medium: P=45 (log10(120)×30 + log10(8.5)×15 = 62+13... actually min 100 cap), W=2.0, Q=0.8 → 72
- Substack: P=85 (log10(380)×30 + 0.42×50 = 77+21=98), W=2.5, Q=1.2 → 255
- Threads: P=0, W=1.0, Q=1.5 → 0
- Mastodon: P=0, W=1.5, Q=1.0 → 0
- (FB personal no cuenta)

E = 195 + 50 + 0 + 0 + 16 + 72 + 255 + 0 + 0 = **588** (capped at 1000, so 588)

**D (Discoverability)**:
- Custom domain: 50
- Schema.org Person (TBC): 80
- llms.txt: 0 (no implementado)
- Wikipedia: 0
- Wikidata: 0
- Google KP: 0
- LinkedIn verified (counts as ID validation): 0 (no es discoverability)

D = 50 + 80 = **130** (asumiendo Schema.org existe — verify)

**L (LLM Visibility)**:
- GEORadar no medido → L = 0

**T (Trust Signals)**:
- LinkedIn recommendations: 4 × 20 = 80
- Press tier-1: 1 × 30 = 30
- Press tier-2: 3 × 10 = 30
- Verified badges: 1 × 30 = 30
- Years active: 8 × 20 = 160

T = 80 + 30 + 30 + 30 + 160 = **330**

**O (Owned Anchor)**:
- Website DA: 18 × 5 = 90
- Newsletter subs: log10(38) × 100 = 158
- Long-form content: 5 × 25 = 125
- Self-hosted blog: 80

O = 90 + 158 + 125 + 80 = **453**

### DKI final

```
DKI = (588 × 0.40) + (130 × 0.20) + (0 × 0.15) + (330 × 0.15) + (453 × 0.10)
    = 235.2 + 26 + 0 + 49.5 + 45.3
    = 356
```

**DKI Carlos Ortet baseline = 356 · tier "Established en niche"** (rango 300-500).

### Benchmark sector "Tech / GEO consulting EU"

Estimado (sin datos hard, basado en perfiles públicos comparables):
- Promedio: 420
- Top 10%: 650
- Top 1%: 850

**Gap to close (con AB90 90 días)**:
- DKI target día 90 = 550 (en tier "Recognized regional/sectorial")
- Δ = +194 puntos

### Donde están los gaps principales (priorización plan)

1. **LLM Visibility (0/150 actual)**: medir GEORadar baseline ya. Esto es 15% del score y está en 0.
2. **Discoverability (26/200)**: Wikipedia article + Wikidata + Google KP claim. Esto es 20% y subutilizado.
3. **Earned (235/400)**: HN bloqueado (genAI flag), pero Bluesky+Mastodon+Quora pueden subir rápido. Newsletter LinkedIn + carousels.
4. **Trust Signals (49/150)**: 5 nuevas LinkedIn recommendations + 1-2 op-ed tier-1 + Google Reviews Local Guide.
5. **Owned (45/100)**: ya está bien proporcionalmente. Mantener.

---

## Cómo se usa este DKI en práctica

1. **Baseline** en día 1 del cliente
2. **Re-medición** en día 45 (mid-program review)
3. **Final** en día 90
4. Reporte muestra delta + breakdown por capa
5. **Mensual post-program** para clientes Sostenido

---

## Limitaciones reconocidas

- **Sesgo Western**: algunas plataformas regionales (Weibo, VK, Naver) no incluidas. Si cliente opera Asia/Russia, añadir ad-hoc.
- **Métricas privadas**: SSI LinkedIn solo accesible por el propio user (no scrapeable). Cliente debe proveerlo o aceptar default 35.
- **GEORadar requerido para L**: sin GEORadar (o equivalente), L=0 y el DKI infravalora. Recomendar mediblerlo en kick-off.
- **Sector weights subjetivos**: actualizar según observaciones reales tras 10+ clientes.

---

## Referencias

- `sector-platform-mappings.md` — qué plataformas pesan más por sector
- `platform-catalog-master.md` — todas las 40+ plataformas con métricas nativas
- `phase-system.md` — cómo el plan se construye desde el gap analysis
- `examples/carlos-ortet-case-study.md` — primer cálculo completo

---

*Fórmula V1 · 2026-05-24 · iterar con feedback de primeros 10 clientes para refinar pesos*
