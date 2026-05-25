# Platform Maintenance System

> Cómo mantenemos viva `platform-authority-db.yaml`. Versión: 1.0 · 2026-05-25.

---

## Por qué un sistema, no solo "actualizamos cuando nos acordamos"

La autoridad de las plataformas **cambia trimestre a trimestre**:

- **2024 Q2**: Reddit firma deal con Google → Reddit SERP authority sube 30 puntos en 90 días
- **2024 Q3**: HARO se vende a Connectively → mecánica cambia, brand reset
- **2024 Q4**: Hugging Face supera Stack Overflow en consultas ML → reordenamiento
- **2025 Q2**: Substack lanza Notes → engagement metric nueva, peso a recalibrar
- **2025 Q3**: AIO production-ready → nueva surface a integrar en scoring

Sin un sistema disciplinado, el skill envejece y los planes que recomienda quedan stale en 12 meses.

---

## Cadencia

### Review trimestral (canónico)

| Trimestre | Fecha objetivo | Owner |
|---|---|---|
| Q1 | 25 enero | Carlos Ortet + Mer Canet |
| Q2 | 25 abril | Carlos Ortet + Mer Canet |
| Q3 | 25 julio | Carlos Ortet + Mer Canet |
| Q4 | 25 octubre | Carlos Ortet + Mer Canet |

Cada review = 90 min en agenda. Output: PR al repo con cambios + commit message firmado.

### Triggers de revisión ad-hoc (fuera de trimestre)

- **Plataforma muere o pivota** (HARO → Connectively, Twitter → X, etc.)
- **Major algorithm change Google** confirmado (e.g. Helpful Content Update)
- **GEORadar reporta cambio detectable** en cuáles fuentes citan los LLMs
- **Cliente nuevo en sector no cubierto** (cargamos plataformas faltantes del sector)
- **Nueva plataforma con crecimiento >100% YoY** o con coverage en major press tier-1

---

## Checklist de review trimestral

Cada trimestre, recorrer en este orden:

### Bloque 1 · Health check de las 86 plataformas existentes (45 min)

Para cada platform en el YAML:

- [ ] **DNS + URL alive**: `curl -sI https://[platform-domain]` retorna 2xx/3xx
- [ ] **Status actual** sigue siendo correcto (live / emerging / declining / dead)
- [ ] **Authority scores** siguen aproximadamente correctos (cambio >10pt = ajuste obligatorio)
- [ ] **LLMs citing** sigue siendo correcto (sample manual: pedir "describe [persona conocida]" a cada LLM y ver si la fuente aparece)
- [ ] **Notes** siguen siendo verdaderas (cambios en pricing, features, scope)
- [ ] **Last_reviewed** actualizado a fecha de review

**Automatización útil**: `scripts/maintenance_check.py` (future V1.1) hará el health-check DNS + URL en bulk.

### Bloque 2 · Scan de candidatas (20 min)

Buscar plataformas NUEVAS que merezcan entrar al catálogo. Fuentes:

- **Product Hunt** trending últimos 90 días filtrado por categoría `social-media`, `community`, `professional-network`, `creator-tools`
- **Hacker News** búsqueda `show hn` últimos 90 días filtrada por upvotes ≥200
- **TechCrunch / Sifted** announcements de plataformas raised >$5M Series A en categorías relevantes
- **GEORadar** reportes cliente: si una marca aparece en una plataforma que no teníamos en BD, candidate
- **Twitter/Bluesky listening**: si journalists/founders mencionan plataforma nueva 3+ veces en discussions

Criterio para entrada al catálogo:

- ✓ ≥6 meses operativa
- ✓ MAU declared o estimado >100K
- ✓ Casos reales de profesionales construyendo presencia ahí
- ✓ Differentiation clara vs incumbents (no es "another LinkedIn clone")

### Bloque 3 · Demotion de plataformas en decline (10 min)

Revisar las que estén en status `declining` o sospechosas:

- [ ] ¿Sigue siendo `declining` o pasa a `dead`?
- [ ] Si `dead`: bajar todos los scores a 0, mantener entry con `status: dead` (no eliminar, para referencias históricas)
- [ ] Si `declining` pero todavía operativa: ¿algún uso justificable? Si no, marcar para review en Q+2

Plataformas en riesgo actualmente (Q2 2026):
- Mirror.xyz (Web3 audience contracted)
- HackerNoon (LLM authority eroding)
- Forbes Contributor (program scaled back)
- HARO → Connectively (rebrand, mecánica idéntica)

### Bloque 4 · Re-scoring evidence pass (15 min)

Para 5-10 platforms seleccionadas (rotación, no todas cada trimestre), ejecutar verificación más profunda:

- **Sample SERP**: 5 queries de profesionales conocidos en sectores diferentes → ¿la plataforma aparece? Si baja del esperado, ajustar `authority.google`
- **Sample LLM**: pedir a ChatGPT + Claude + Perplexity + Gemini "describe [profesional notable]" → ¿citan la plataforma? Ajustar `authority.llm` y `llms_citing`
- **Trust signal**: ¿algún cliente mencionó esta plataforma como "señal de credibilidad" en último trimestre? Ajustar `authority.trust`

---

## Template de PR (para añadir / modificar plataforma)

```markdown
## Tipo de cambio

- [ ] Añadir plataforma nueva
- [ ] Modificar scores (≥5pt en alguna dimensión)
- [ ] Cambiar status (live/emerging/declining/dead)
- [ ] Update notes/audience/sectors_bonus

## Plataforma afectada

`slug: ...`

## Evidencia

Citar **al menos una fuente verificable**:

- [ ] Sample SERP de [profesional notable] que muestra la plataforma → screenshot o URL
- [ ] Respuesta LLM real citando la plataforma → URL del thread (si es shareable) o pasted excerpt
- [ ] Datos públicos: MAU declared, Ahrefs/Similarweb data, press article
- [ ] Cambio operativo: announcement oficial, blog post, pricing change

## Cambios propuestos

```diff
- authority: {google: 85, llm: 70, trust: 70}
+ authority: {google: 88, llm: 75, trust: 75}
```

## Justificación

[2-4 frases explicando por qué los nuevos scores reflejan mejor la realidad]

## Impacto en planes existentes

- [ ] Ninguno (cambio menor)
- [ ] Plans recomiendan ahora más esta plataforma (impacto positivo)
- [ ] Plans deberían reducir reliance en esta plataforma (impacto correctivo)
```

---

## Criterios para promociones / demociones de status

### `emerging` → `live`

- ≥12 meses operativa
- ≥1M MAU declared o estimado
- ≥2 case studies en BD (Carlos, Guille, futuros clientes) que la usan con éxito
- ≥1 LLM principal la cita consistentemente

### `live` → `declining`

- MAU declared cae ≥20% YoY (3 trimestres consecutivos)
- Authority Google y/o LLM bajan ≥10pt en review
- Major announcement de retirada de features/funding/leadership
- Cliente reports: "ya no me funciona como antes" (3+ casos)

### `declining` → `dead`

- Plataforma cerrada (dominio fuera, twitter handle eliminado, etc.)
- No respuesta a comunicación cliente >60 días
- API rota sin remediación

### `dead` permanente

- Entry permanece en YAML con `status: dead` y scores en 0
- No eliminar (rompe referencias históricas en case studies de vault)

---

## Fuentes públicas a consultar en cada review

| Fuente | Para qué | URL |
|---|---|---|
| **Common Crawl Index** | Domain frequency en corpus de training LLM | https://commoncrawl.org/ |
| **Ahrefs free DR check** | Domain Rating quick check | https://ahrefs.com/website-authority-checker |
| **Similarweb free** | MAU + traffic estimate | https://www.similarweb.com/ |
| **BuiltWith Trends** | Adopción tech por dominio (medir si plataforma growing) | https://trends.builtwith.com/ |
| **Perplexity public reports** | Most-cited sources cuarterly | https://www.perplexity.ai/blog/ |
| **Google Search Central** | Algorithm updates oficiales | https://developers.google.com/search/updates/ |
| **GEORadar internal** | Citation patterns en estudios cliente Zoopa | runs internas |

---

## Histórico de reviews

Cada review se documenta aquí:

### 2026-05-25 · Review inicial · V1.0

- 86 plataformas catalogadas con scores iniciales
- 4 categorías nuevas vs catalog legacy (`emerging_ai_native`, `press_research`, `events_speaking`, `creator_economy`)
- Plataformas marcadas `declining`: Medium, Facebook Page, Mirror.xyz, HackerNoon, Forbes Contributor
- Plataformas marcadas `emerging`: Bluesky, Beehiiv, Read.cv, Hugging Face, Replicate
- Owners: Carlos Ortet (signoff) · methodology by Mer Canet + Carlos

### 2026-08-25 · Q3 2026 review (próximo)

(Pendiente)

### 2026-10-25 · Q4 2026 review

(Pendiente)

---

## Edge case: cliente con plataforma fuera del catálogo

Si un cliente menciona una plataforma que no está en el YAML:

1. **No bloquear el assessment** — usar default scores (50/50/50) marcado como provisional
2. **Crear issue en repo** con plataforma + sector cliente + evidencia
3. **Programar review express** (≤2 semanas) si el cliente es active
4. **Después del review**: PR al YAML con scores fundamentados + cierre del issue

---

## Referencias

- `references/platform-authority-db.yaml` — la BD canónica
- `references/platform-authority-methodology.md` — cómo se asignan los scores
- `scripts/authority_score.py` — compute scoring compuesto
- `scripts/maintenance_check.py` (futuro V1.1) — automated health check
