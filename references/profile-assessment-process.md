# Profile Assessment Process

> Cómo procesar la información del profesional input para producir la estructura YAML necesaria para calcular DKI + plan personalizado.
>
> Versión: 1.0 · 2026-05-24

---

## Inputs aceptados

### Input 1: LinkedIn URL (preferido)

Usuario proporciona URL pública: `linkedin.com/in/{slug}`

Procesar con `scripts/assess_profile.py`:
1. Verificar acceso público (no login required)
2. Extraer (via HTML parsing + selectores estables):
   - Nombre + título
   - Headline
   - About text
   - Experience (companies + roles + dates)
   - Education
   - Skills top 10
   - Recommendations count
   - Followers/connections estimate
   - Custom URL detection
   - Featured section items
3. Algunas métricas SOLO accesibles por user logueado: SSI Score (cliente debe proveer)

### Input 2: CV / Resume PDF

Usuario proporciona PDF (idealmente <5MB):
1. Convert PDF → text (PyPDF2 o `pdftotext`)
2. Detect formato (chrono, functional, hybrid)
3. Extract:
   - Nombre + contacto
   - Roles + companies + dates
   - Education + degrees
   - Skills + certifications
   - Languages
   - Publications mencionadas
   - Awards
   - Speaking engagements

### Input 3: Sitio web personal (URL)

Usuario proporciona URL: `{personal-domain}.com`
1. Scrape About section + bio
2. Extract publications/talks/projects mencionados
3. Detect Schema.org Person markup (si existe)
4. Get domain authority via Moz/Ahrefs (si disponible)
5. Find sameAs links a otras plataformas (cross-platform map)

### Input 4: Cuestionario manual (fallback)

Si no hay ninguno de los anteriores, o complementar:

## Cuestionario interactivo

**Estrategia de preguntas**: NUNCA bombardear con todas a la vez. Hacer 3-5 preguntas por turno con `AskUserQuestion`, agrupadas por tema. Total ~6 turnos.

### Turno 1 · Identidad básica

```yaml
- name: "Cuál es tu nombre completo + título profesional actual?"
- sector: "En cuál sector estás?" (options: Tech, Legal, Medical, Actor, Designer, Academic, Founder/CEO, Chef, Writer, Musician, Architect, Athlete, Politician, Consultant, Journalist, Influencer, Investor, Real Estate, Financial, Otro)
- geografia: "Dónde estás basado?" (país + ciudad principal)
- idiomas: "Qué idiomas usas profesionalmente?" (multiSelect: ES, EN, CA, FR, DE, IT, PT, Otro)
```

### Turno 2 · Career stage + diferencial

```yaml
- career_stage: "Stage de tu carrera" (options: Junior 0-3y, Mid 4-8y, Senior 8-15y, Executive 15y+)
- audiencia_objetivo: "Quién es tu audiencia primaria?" (text free, ej. "Founders B2B SaaS EU")
- diferenciador: "Qué te diferencia de otros 100 que hacen lo mismo?" (text free, 1-3 frases)
```

### Turno 3 · Plataformas actuales

```yaml
- platforms_active: "En qué plataformas estás activo?" (multiSelect dinámica según sector)
  Para cada platform activa: pedir handle/URL
```

### Turno 4 · Followers + métricas

Para cada platform activa del turno 3:
```yaml
- followers: "Followers/connections en {platform}?" (number)
- last_post_date: "Cuándo publicaste por última vez ahí?" (este mes / últimos 3m / últimos 12m / >1 año)
- (si LinkedIn) ssi_score: "Cuál es tu SSI Score actual?" (linkedin.com/sales/ssi · 0-100 · 'no medido' OK)
```

### Turno 5 · Discoverability

```yaml
- wikipedia: "Tienes article en Wikipedia (tú o tu empresa)?" (sí/no/no estoy seguro)
- wikidata: "Tienes Wikidata Q-number?" (sí/no/desconozco)
- knowledge_panel: "Aparece tu Knowledge Panel cuando buscan tu nombre en Google?" (sí/no/desconozco)
- personal_domain: "Tienes web personal con dominio propio?" (URL si sí)
- crunchbase: "Tienes profile en Crunchbase? (founders/CEOs)" (URL si sí)
- google_scholar: "Tienes profile Google Scholar? (académicos)" (URL si sí)
```

### Turno 6 · Trust signals + assets owned

```yaml
- linkedin_recommendations: "Cuántas recommendations tienes en LinkedIn?" (number)
- press_tier1: "Cuántas press mentions en medios tier-1 (FT, Bloomberg, Wired, NYT, El País, etc.)?" (number)
- speaking: "Has dado charlas en conferencias/TEDx?" (count + plataforma si TEDx/TED)
- newsletter: "Tienes newsletter propia?" (URL + subs estimate)
- book_published: "Has publicado libro?" (count + ISBN si possible)
- podcast_own: "Tienes podcast propio activo (último 3 meses)?" (URL si sí)
```

---

## Output YAML estructurado

Tras procesar inputs, generar archivo:

```yaml
# {client-slug}-profile-data-{YYYYMMDD}.yaml
client:
  slug: "carlos-ortet"
  name: "Carlos Ortet"
  title: "Senior Innovation Engineer @ Zoopa & 498A"
  assessment_date: "2026-05-24"
  
identity:
  sector_primario: "Tech / Software / Engineer"
  sub_sector: "AI / GEO / LLM brand visibility"
  geografia: "EU · Catalunya / España"
  ciudad: "Barcelona"
  idiomas: ["ES", "EN", "CA"]
  career_stage: "Senior · CEO/Founder"
  audiencia_objetivo: "C-level B2B, founders SaaS, agencias EU"
  diferenciador_principal: "Única persona uniendo GEO + producción audiovisual + I+D LLM"
  
platforms:
  linkedin:
    handle: "in/carlosortet"
    followers: 5200
    ssi_score: null  # not measured
    last_post: "2026-05-24"
    posts_last_3m: 18
    engagement_rate_avg: 0.045
    recommendations: 4
    verified: true
  twitter_x:
    handle: "carlos_ortet"
    followers: 850
    monthly_impressions_est: 8000
    last_post: "2026-05-24"
  bluesky:
    handle: "carlosortet.bsky.social"
    followers: 0
    last_post: "2026-05-24"
  threads:
    handle: "carlosortet.i"
    followers: 5
    last_post: "2026-05-24"
  mastodon:
    handle: "CarlosOrtet@mastodon.social"
    followers: 0
    last_post: "2026-05-24"
  hackernews:
    handle: "carlosortet"
    karma: 1
    last_post: "2026-05-24"
  quora:
    handle: "carlos-ortet"
    followers: 19
    answers: 1
  medium:
    handle: "carlosortet"
    followers: 120
    total_claps: 850
  substack:
    handle: "carlosortet"
    subscribers: 380
    open_rate: 0.42

discoverability:
  wikipedia_article: false
  wikidata_entity: false
  google_knowledge_panel: false
  schema_org_person: true  # carlosortet.com tiene
  custom_domain: "carlosortet.com"
  llms_txt: false
  crunchbase: false
  google_scholar: false
  orcid: false

trust_signals:
  linkedin_recommendations: 4
  press_tier1: 1   # Harvard Deusto Business Review
  press_tier2: 3
  verified_badges: 1  # LinkedIn
  years_active_public: 8
  conference_keynote_tier1: 0
  ted_talk: 0
  tedx_talk: 0
  patents: 0
  
owned_anchor:
  website_da: 18
  newsletter_subscribers: 380
  long_form_content_count: 25
  self_hosted_blog: true
  podcast_own: false
  book_published: 0
  online_course_owned: false

georadar:
  measured: false
  sov: null
  position_score: null
  sentiment_score: null
  cobranding_score: null
```

---

## Flow operativo en la sesión

### Cuando el usuario invoca el skill

1. Saludo + pregunta: "Para empezar a evaluar tu perfil digital, ¿con qué input prefieres empezar?"
   - LinkedIn URL pública
   - CV / Resume PDF
   - URL sitio web personal
   - Cuestionario interactivo (~6 turnos)

2. Procesar input recibido con scripts/

3. Si datos insuficientes, complementar con turnos del cuestionario manual

4. Generar el YAML del cliente

5. Pasar al PASO 3 del SKILL.md (DKI baseline calculation)

### Validación de datos antes del cálculo

Antes de calcular DKI, verificar:

- [ ] Sector identificado (sin sector = no se pueden aplicar weights)
- [ ] Al menos 3 plataformas mapeadas (sin esto, Earned demasiado sesgado)
- [ ] Career stage identificado (afecta benchmarks)
- [ ] Geografía + idiomas (afecta búsquedas dinámicas)
- [ ] LinkedIn data (la plataforma con más peso en mayoría de sectores)

Si falta cualquiera, hacer preguntas específicas antes de calcular.

---

## Procesar inputs sensibles

### Datos personales (GDPR)

- El YAML del cliente se guarda LOCAL en `~/Documents/claudecode-proj/karma-booster-clients/{slug}/`
- NO commit al repo
- Retención: 30 días post-cierre cliente, luego borrar
- Si cliente solicita acceso/borrado/portabilidad, atender en 72h

### CVs / Resumes

- Procesar PDF en memoria
- Guardar SOLO el YAML extraído (no el PDF original)
- Si user lo quiere conservar, indicarle que lo guarde él mismo

### Métricas privadas (SSI, ssi_score)

- LinkedIn SSI solo es accesible por el propio user
- Si user dice "no medido" o no lo provee, usar default por sector + career stage:
  - C-level B2B: 35
  - Senior consultant: 40
  - Junior pro: 25
  - Academic: 25

---

## Anti-patrones de input

| Anti-patrón | Por qué evitar | Acción |
|---|---|---|
| Scraping LinkedIn sin consentimiento | TOS violation + ban | Solo URL pública si user la provee explícito |
| Asumir sector sin preguntar | Pesos incorrectos | Siempre confirmar sector |
| Calcular DKI sin LinkedIn data | Sesgo masivo | Pedir LinkedIn antes |
| Inventar followers si user no sabe | Distorsiona baseline | Marcar "no medido" + default |
| Procesar CV con info sensible (DNI, números privados) | GDPR risk | Pedir CV sanitizado o saltar la sección |

---

## Referencias cruzadas

- `digital-karma-formula.md` — qué hacer con el YAML después
- `sector-platform-mappings.md` — qué plataformas pedir según sector
- `phase-system.md` — cómo construir plan desde el baseline
- `templates/profile-assessment-output.md` — formato del reporte al cliente
