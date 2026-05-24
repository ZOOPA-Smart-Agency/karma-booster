# Platform Catalog Master · 45 plataformas

> Catálogo canónico de plataformas relevantes para autoridad digital profesional. Cada entrada incluye métrica nativa, fórmula de normalización a 0-100, y notas de uso. Mantener actualizado cuando se descubren nuevas plataformas relevantes.
>
> Versión: 1.0 · 2026-05-24

---

## 1 · Generales de distribución

### LinkedIn

- **Métrica nativa**: followers + SSI Score (0-100)
- **Normalización**: `min(100, log10(followers/100) × 30 + SSI × 0.4)`
- **Acceso métricas**: SSI propio en `linkedin.com/sales/ssi` (solo cliente accede)
- **Notas**: la #1 para B2B. Profile + Newsletter + Carousels son los assets clave 2026

### Twitter / X

- **Métrica nativa**: followers + monthly impressions
- **Normalización**: `min(100, log10(followers/100) × 25 + log10(monthly_impressions/1000) × 15)`
- **Acceso métricas**: dashboard analytics propio
- **Notas**: hilos asimétricos sirven. Reglas anti-LLM aplican. Verified badge $8/mes

### Bluesky

- **Métrica nativa**: followers
- **Normalización**: `min(100, log10(followers/10) × 30)`
- **Acceso métricas**: público en perfil
- **Notas**: 30M users 2026. Tech/journalist/academic. Email verification gate. Custom DID handle disponible

### Threads (Meta)

- **Métrica nativa**: followers
- **Normalización**: `min(100, log10(followers/100) × 30)`
- **Acceso métricas**: insights básico
- **Notas**: cross-graph IG. Char limit 500. Domain `threads.com` (no .net)

### Mastodon (Fediverso)

- **Métrica nativa**: followers (instance + remote)
- **Normalización**: `min(100, log10(followers/10) × 30)`
- **Acceso métricas**: API REST por instance
- **Notas**: EU tech + open source community. Anti-corporate. UTM links castigados

### Facebook (personal + Pages)

- **Métrica nativa**: friends (personal) + page followers
- **Normalización**: `min(100, log10(page_followers/100) × 20)` (personal no cuenta)
- **Acceso métricas**: Insights de Page
- **Notas**: solo Page cuenta para autoridad pro. Native long-form > link card

### Instagram

- **Métrica nativa**: followers + engagement rate
- **Normalización**: `min(100, log10(followers/10) × 25 + engagement_rate × 100)`
- **Acceso métricas**: Insights Business account
- **Notas**: Reels + Stories + carousels. Critical para creators, chefs, actors

### TikTok

- **Métrica nativa**: followers + total likes
- **Normalización**: `min(100, log10(followers/10) × 25 + log10(total_likes/100) × 15)`
- **Acceso métricas**: Pro account analytics
- **Notas**: dominante en Gen Z reach. Algoritmo agnóstico de followers (puede explotar cualquiera)

### YouTube

- **Métrica nativa**: subs + monthly views
- **Normalización**: `min(100, log10(subs/10) × 25 + log10(monthly_views/100) × 20)`
- **Acceso métricas**: YouTube Studio
- **Notas**: long-form video sigue siendo top para authority

---

## 2 · Comunidad / Q&A

### Hacker News

- **Métrica nativa**: karma (post + comment combined)
- **Normalización**: `min(100, log10(karma) × 30)`
- **Acceso métricas**: profile público
- **Notas**: ⚠️ clasificador genAI activo. Contenido debe ser 100% manual (24 may 2026)

### Reddit

- **Métrica nativa**: total karma (post + comment + subreddit-specific)
- **Normalización**: `min(100, log10(total_karma) × 20)`
- **Acceso métricas**: profile público + RedditMetis
- **Notas**: karma combinado + por subreddit. Anti self-promotion fuerte

### Quora

- **Métrica nativa**: followers + answers count + views totales
- **Normalización**: `min(100, log10(followers) × 25 + answers × 0.5)`
- **Acceso métricas**: stats panel propio
- **Notas**: long-tail SEO + LLM citation source. Cadencia 48h entre answers

### Stack Overflow

- **Métrica nativa**: reputation
- **Normalización**: `min(100, log10(reputation) × 20)`
- **Acceso métricas**: profile público
- **Notas**: aplicable solo a developers. Reputation se gana con respuestas técnicas

---

## 3 · Editorial / Newsletter

### Substack

- **Métrica nativa**: subscribers + open rate
- **Normalización**: `min(100, log10(subs) × 30 + open_rate × 50)`
- **Acceso métricas**: dashboard publisher
- **Notas**: gold standard newsletter B2B + thought leadership

### Medium

- **Métrica nativa**: followers + total claps + reads
- **Normalización**: `min(100, log10(followers) × 30 + log10(total_claps/100) × 15)`
- **Acceso métricas**: Medium Stats
- **Notas**: SEO orgánico fuerte. Canonical URL al blog propio para no duplicate

### LinkedIn Newsletter (nativo)

- **Métrica nativa**: subscribers + post avg impressions
- **Normalización**: cuenta dentro del LinkedIn score (parte de SSI Brand)
- **Acceso métricas**: LinkedIn analytics
- **Notas**: distribución algorítmica gratis. Cadencia regular crítica

### Beehiiv

- **Métrica nativa**: subs + open rate
- **Normalización**: igual que Substack
- **Acceso métricas**: dashboard
- **Notas**: alternativa moderna a Substack. Mejor para creators que venden cursos

---

## 4 · Tech / Developers

### GitHub

- **Métrica nativa**: followers + total stars repos
- **Normalización**: `min(100, log10(followers) × 30 + log10(total_stars) × 15)`
- **Acceso métricas**: profile API
- **Notas**: core para developers + open source maintainers

### Dev.to

- **Métrica nativa**: followers + posts
- **Normalización**: `min(100, log10(followers/10) × 30)`
- **Acceso métricas**: profile dashboard
- **Notas**: tech writing comunidad. Editor Markdown

### Hashnode

- **Métrica nativa**: followers + posts views
- **Normalización**: `min(100, log10(followers/10) × 30)`
- **Acceso métricas**: dashboard
- **Notas**: dev blogging con dominio custom

### Lobste.rs

- **Métrica nativa**: hat color + posts
- **Normalización**: muy nicho, no normalizar (binary: tiene cuenta o no)
- **Notas**: invite-only. Requiere ser invitado por user existente

### HackerNoon

- **Métrica nativa**: followers + reads
- **Normalización**: `min(100, log10(followers/10) × 25)`
- **Notas**: editors revisan submissions. Estilo Wired tech

### DZone

- **Métrica nativa**: followers + zones
- **Normalización**: `min(100, log10(followers/10) × 25)`
- **Notas**: audiencia enterprise dev. Incluir "Key Takeaways"

---

## 5 · Académicos / Investigadores

### Google Scholar

- **Métrica nativa**: h-index + citations totales
- **Normalización**: `min(100, h_index × 4 + log10(total_citations/100) × 10)`
- **Acceso métricas**: scholar profile (debe estar claimed)
- **Notas**: gold standard for academic authority

### ORCID

- **Métrica nativa**: works count + funded grants
- **Normalización**: `min(100, works × 2)`
- **Acceso métricas**: profile público
- **Notas**: researcher ID unificado. Conectar con publicaciones

### ResearchGate

- **Métrica nativa**: RG Score + citations + reads
- **Normalización**: `min(100, RG_score × 2)`
- **Acceso métricas**: profile
- **Notas**: comunidad de researchers. RG Score deprecated parcialmente pero sigue señal

### SemanticScholar

- **Métrica nativa**: citations + influential citations
- **Normalización**: `min(100, log10(citations) × 25)`
- **Acceso métricas**: author profile
- **Notas**: AI-powered, citado por LLMs frecuentemente

### arXiv

- **Métrica nativa**: papers submitted
- **Normalización**: lineal: 5 puntos por paper, cap 100
- **Notas**: pre-prints. Author endorsement requerido para nuevas categorías

---

## 6 · Reviews / Trust

### Google Reviews / Local Guide

- **Métrica nativa**: reviews count + photos count + Local Guide level (1-10)
- **Normalización**: `min(100, reviews_business × 2 + lg_level × 5)`
- **Acceso métricas**: Google Maps profile + Local Guide dashboard
- **Notas**: clave para negocios locales + Local Guide para profesionales que reseñan

### Trustpilot

- **Métrica nativa**: reviews + TrustScore
- **Normalización**: para business: `min(100, log10(reviews) × 25 + trustscore × 10)`
- **Notas**: business listing requiere claim + verify

### G2 / Capterra (B2B SaaS)

- **Métrica nativa**: reviews + leader badges
- **Normalización**: `min(100, reviews × 3 + badges × 20)`
- **Notas**: solo para software comercial listado

### Glassdoor

- **Métrica nativa**: rating + reviews + CEO approval (si CEO)
- **Normalización**: para founder/CEO: `min(100, rating × 15 + ceo_approval × 30)`
- **Notas**: employer brand signal

### Goodreads (author)

- **Métrica nativa**: ratings + reviews + followers
- **Normalización**: `min(100, log10(ratings) × 25 + log10(reviews) × 15)`
- **Notas**: gold for writers

### Amazon Author Central

- **Métrica nativa**: reviews + ranking
- **Normalización**: `min(100, log10(reviews) × 25)`
- **Notas**: claim para visibility en libros

---

## 7 · Sector-specialized

### IMDb (actores/cineastas)

- **Métrica nativa**: STARmeter rank + credits
- **Normalización**: `min(100, max(0, (50000 - rank) / 500) + credits × 0.5)`
- **Acceso**: IMDb Pro requerido para detalle
- **Notas**: gold para industria del cine

### Backstage / Casting Networks / Spotlight (UK)

- **Métrica nativa**: profile views + bookings
- **Normalización**: binary tiene profile activo + views log
- **Notas**: critical para acting jobs

### Doximity (médicos US)

- **Métrica nativa**: profile completeness + colleagues
- **Normalización**: binary + log
- **Notas**: peer network médico US verificado

### Sermo

- **Métrica nativa**: anonymous, no public metric
- **Normalización**: binary presence
- **Notas**: anonymous physician network

### JD Supra / Above the Law (legal)

- **Métrica nativa**: published articles + mentions
- **Normalización**: `min(100, articles × 5 + log10(mentions) × 15)`
- **Notas**: legal thought leadership

### Avvo / Martindale-Hubbell

- **Métrica nativa**: rating + reviews
- **Normalización**: `min(100, rating × 15 + reviews × 2)`
- **Notas**: lawyer directories US

### Spotify (artista)

- **Métrica nativa**: monthly listeners
- **Normalización**: `min(100, log10(monthly_listeners/10) × 20)`
- **Acceso**: Spotify for Artists
- **Notas**: dominante para músicos

### Bandcamp / SoundCloud / Apple Music

- **Métrica nativa**: followers + plays
- **Normalización**: `min(100, log10(followers/10) × 25)`
- **Notas**: complementarias a Spotify

### Dribbble (designers)

- **Métrica nativa**: followers + likes
- **Normalización**: `min(100, log10(followers) × 25 + log10(appreciations) × 15)`
- **Notas**: visual designers, UI/UX

### Behance (designers)

- **Métrica nativa**: followers + project views
- **Normalización**: `min(100, log10(followers) × 25 + log10(total_project_views) × 15)`
- **Notas**: portfolio platform, Adobe-owned

### ArchDaily / Dezeen (architects)

- **Métrica nativa**: published projects
- **Normalización**: `min(100, projects × 10)`
- **Notas**: visibility en arquitectura

### Crunchbase (founders/execs)

- **Métrica nativa**: profile complete + investor connections
- **Normalización**: binary complete + log connections
- **Acceso**: Premium para edits avanzados
- **Notas**: founders + execs B2B

### AngelList / Wellfound (founders)

- **Métrica nativa**: company profile + investor matches
- **Normalización**: binary + log
- **Notas**: vincular con LinkedIn

### Indie Hackers (founders)

- **Métrica nativa**: posts + revenue stripe verified
- **Normalización**: `min(100, posts × 3 + revenue_verified × 30)`
- **Notas**: bootstrap founder community

### Product Hunt

- **Métrica nativa**: launches + upvotes
- **Normalización**: `min(100, launches × 10 + log10(total_upvotes) × 15)`
- **Notas**: para product launches

---

## 8 · Discoverability / Identity

### Wikipedia

- **Métrica nativa**: article propio (binary)
- **Discoverability score**: 200 puntos si tiene article
- **Notas**: notabilidad requiere 3+ fuentes secundarias

### Wikidata

- **Métrica nativa**: Q-number único
- **Discoverability score**: 100 puntos
- **Notas**: structured data citado por todos los LLMs

### Google Knowledge Panel

- **Métrica nativa**: trigger en SERP (binary)
- **Discoverability score**: 150 puntos
- **Notas**: trigger requiere entity consistency cross-platform

### Schema.org Person (sitio personal)

- **Métrica nativa**: JSON-LD presente (binary)
- **Discoverability score**: 80 puntos
- **Notas**: lo más fácil de implementar

---

## 9 · Eventos / Speaking

### TED / TEDx

- **Métrica nativa**: charlas dadas + views
- **Trust score**: 200 (TED main), 100 (TEDx)
- **Notas**: máximo trust signal en speaking

### Conference circuit (sectoriales)

- **Métrica nativa**: keynotes count
- **Trust score**: 30 × N (cap 10)
- **Notas**: depende del sector cuál cuenta tier-1

---

## 10 · Niche / Special

### Wikipedia Commons

- **Métrica nativa**: photo CC propia uploaded
- **Discoverability score**: 30 puntos
- **Notas**: photo propia con licencia Creative Commons

### About.me / Bio.link

- **Métrica nativa**: profile complete
- **Discoverability score**: 20 puntos cada
- **Notas**: hubs secundarios. Útil para sameAs schema

### Carrd / Linktree (link-in-bio)

- **Métrica nativa**: presence
- **Discoverability score**: 10 puntos
- **Notas**: hub básico. Carrd > Linktree por SEO

### IFTTT / Zapier (automation hub)

- **No cuenta para DKI**, herramienta operativa

---

## Sectores sin plataformas establecidas

Algunos profesionales operan en sectores sin plataformas digitales claras:

- **Trades** (electricistas, plomeros): Google Reviews + Yelp + Nextdoor + Foursquare
- **Real Estate**: Zillow + Trulia + Realtor.com (US) + Idealista + Fotocasa (ES)
- **Insurance**: específico por país, generalmente LinkedIn + corporate
- **Religious leaders**: específico por tradición
- **Government officials**: BallotPedia + GovTrack + official site
- **Military**: LinkedIn + service records + DD-214 verified

Para estos casos, el skill activa `platform_search.py` dinámico vía web.

---

## Cómo añadir nueva plataforma al catálogo

1. Identificar métrica nativa (lo que muestra el profile público)
2. Definir fórmula de normalización a 0-100 (log-scale para followers/contadores grandes)
3. Asignar a sectores en `sector-platform-mappings.md`
4. Documentar acceso a métricas (gratis vs paywall)
5. Notas operativas (anti-patrones, rate limits, etc.)
6. Add to this file con misma estructura
7. Update `scripts/calculate_dki.py` si afecta cálculo

---

## Total: 45 plataformas catalogadas

10 generales · 4 community · 4 editorial · 6 tech · 5 academic · 6 reviews · 14 sector-specialized · 4 discoverability · 2 events · 4 niche
