# Sector → Platform Mappings

> Qué plataformas pesan más para cada sector profesional. Pesos `W_sector` 0-3 usados en fórmula Earned Authority del DKI. Mantener actualizado con feedback de primeros clientes.
>
> Versión: 1.0 · 2026-05-24

---

## Cómo se usan estos pesos

En la fórmula DKI Earned Authority:
```
E = Σ (P_i_normalized × W_sector_i × Q_i)
```

`W_sector` indica importancia relativa de la plataforma para el sector:
- **3.0** = core, donde la audiencia primaria vive
- **2.5** = muy importante, segundo canal
- **2.0** = importante, complementario
- **1.5** = relevante específico
- **1.0** = táctico, opcional
- **0.5** = adyacente, bajo impact
- **0** = irrelevante, excluido del cálculo

Si una plataforma no aparece en un sector, asumir `W=0`.

---

## 1 · Tech / Software / Engineer

| Plataforma | Peso | Rationale |
|---|---|---|
| LinkedIn | 3.0 | Hiring + B2B network |
| GitHub | 3.0 | Code = portfolio |
| Hacker News | 2.5 | Where peers debate |
| Stack Overflow | 2.5 | Reputation técnica |
| Dev.to | 2.0 | Tech writing community |
| Hashnode | 2.0 | Dev blogging |
| Twitter/X | 2.0 | Tech Twitter sigue activo |
| Bluesky | 1.5 | Tech early-adopters |
| Mastodon (fosstodon) | 1.5 | Open source community |
| Medium | 1.5 | Cross-post tech writing |
| Substack | 1.5 | Newsletter tech |
| Reddit (r/programming, r/devops) | 1.5 | Subreddits específicos |
| Lobste.rs | 1.0 | Invite-only, ultra-tech |
| HackerNoon | 1.0 | Editorial tech |
| DZone | 1.0 | Enterprise dev |
| YouTube | 1.0 | Tech tutorials |
| ORCID | 1.0 | Si publica research |
| arXiv | 1.0 | Si publica research |
| Discord (sectorial) | 0.5 | Niche tech communities |
| TikTok | 0.5 | Tech edutainment |

---

## 2 · Legal

| Plataforma | Peso | Rationale |
|---|---|---|
| LinkedIn | 3.0 | Lawyer network primario |
| JD Supra | 2.5 | Published legal articles |
| Above the Law | 2.0 | Legal industry pulse |
| Bar association profile | 2.0 | Trust signal sector |
| Avvo | 2.0 | Legal directory rating |
| Martindale-Hubbell | 2.0 | Established directory |
| Twitter/X (legal Twitter) | 1.5 | Legal community discussion |
| Lex Blog | 1.5 | Niche legal blogging |
| Medium | 1.5 | Long-form analysis |
| Substack | 1.5 | Newsletter legal |
| ABA Journal | 1.5 | Asociación referencia |
| Lex Machina | 1.0 | Litigation analytics |
| YouTube | 1.0 | Legal explainers |
| Quora | 1.0 | Legal Q&A |
| Bluesky | 0.5 | Emerging legal community |

---

## 3 · Medical / Healthcare

| Plataforma | Peso | Rationale |
|---|---|---|
| LinkedIn | 3.0 | Primary professional network |
| Doximity (US) | 3.0 | Verified physician network |
| ResearchGate | 2.5 | Research publications |
| PubMed (autor) | 2.5 | Indexed publications |
| Google Scholar | 2.0 | Citations |
| ORCID | 2.0 | Researcher ID |
| Twitter/X (med Twitter) | 2.0 | #MedTwitter community |
| Medscape | 1.5 | Medical news + community |
| Sermo | 1.5 | Anonymous physician network |
| WebMD | 1.0 | Patient-facing visibility |
| US News Health | 1.0 | Doctor directory US |
| Substack | 1.0 | Newsletter medical |
| YouTube | 1.0 | Health education |
| Instagram | 0.5 | Patient education visual |
| Reddit (r/medicine) | 0.5 | Anonymous discussion |

---

## 4 · Actor / Performing Arts

| Plataforma | Peso | Rationale |
|---|---|---|
| IMDb | 3.0 | The film database |
| Instagram | 3.0 | Visual portfolio + brand |
| LinkedIn (talent agencies) | 2.0 | Agency representation |
| Backstage | 2.5 | Casting platform US |
| Casting Networks | 2.5 | Casting platform |
| Spotlight (UK) | 2.5 | Casting platform UK |
| TikTok | 2.5 | Reach + audition reels |
| Twitter/X | 1.5 | Industry chatter |
| Actors Access | 2.0 | US casting essential |
| Sag-AFTRA profile | 1.5 | Union trust signal |
| Mandy | 1.5 | UK casting platform |
| YouTube | 1.5 | Reel + interviews |
| Variety / Deadline coverage | 1.5 | Press tier-1 |
| BroadwayWorld | 1.0 | Theater specific |
| Threads | 0.5 | Emerging |

---

## 5 · Designer / Creative

| Plataforma | Peso | Rationale |
|---|---|---|
| Dribbble | 3.0 | Visual designers community |
| Behance | 3.0 | Adobe portfolio platform |
| Instagram | 2.5 | Visual portfolio |
| LinkedIn | 2.0 | Hiring + agency |
| Awwwards | 2.0 | Web design recognition |
| Twitter/X (design Twitter) | 2.0 | Discussion community |
| Mastodon (designer.social) | 1.5 | Federated design |
| Medium | 1.5 | Design thinking writing |
| Substack | 1.5 | Newsletter design |
| Site Inspire | 1.5 | Web design showcase |
| Fast Company Innovation | 1.5 | Press tier-1 |
| AIGA | 1.0 | Asociación design US |
| Pinterest | 1.0 | Visual reference |
| YouTube | 1.0 | Tutoriales |
| Figma Community | 1.0 | Component sharing |

---

## 6 · Academic / Researcher

| Plataforma | Peso | Rationale |
|---|---|---|
| Google Scholar | 3.0 | h-index + citations |
| ORCID | 3.0 | Researcher ID universal |
| ResearchGate | 2.5 | Community + papers |
| Wikipedia | 2.5 | Authority signal |
| Wikidata | 2.0 | Structured identity |
| arXiv | 2.5 | Pre-prints (CS, physics, math) |
| SemanticScholar | 2.0 | AI-powered citation |
| LinkedIn | 2.0 | Network + hiring |
| Twitter/X (academic Twitter) | 2.0 | #AcademicTwitter |
| Substack | 1.5 | Newsletter académico |
| AcademicLabs | 1.5 | Researcher discovery |
| Publons / Web of Science | 1.5 | Peer review track |
| Mendeley | 1.0 | Reference manager + profile |
| Medium | 1.0 | Public-facing writing |
| Bluesky | 1.0 | Emerging academic community |
| YouTube | 0.5 | Lectures recordings |

---

## 7 · CEO B2B SaaS / Founder

| Plataforma | Peso | Rationale |
|---|---|---|
| LinkedIn | 3.0 | Primary B2B network |
| Twitter/X | 2.5 | Founder Twitter still alive |
| Crunchbase | 2.5 | Profile + funding history |
| AngelList / Wellfound | 2.0 | Investor matchmaking |
| Hacker News | 2.0 | Tech founder community (cuidado genAI flag) |
| Substack | 2.0 | Founder newsletter trend |
| Medium | 1.5 | Cross-post |
| Indie Hackers | 1.5 | Bootstrap community |
| Product Hunt | 1.5 | Product launches |
| BetaList | 1.0 | Beta launches |
| Forbes Council | 1.5 | Press tier-1 paid |
| Inc.com | 1.0 | Press tier-2 |
| Quora | 1.0 | SaaS Q&A |
| YouTube | 1.0 | Founder content |
| Bluesky | 1.0 | Emerging founder network |
| Reddit (r/startups, r/saas) | 1.0 | Anonymous discussion |

---

## 8 · Chef / Restaurant

| Plataforma | Peso | Rationale |
|---|---|---|
| Instagram | 3.0 | Visual food culture |
| Google Maps Reviews | 3.0 | Local discovery primary |
| Michelin Guide | 3.0 | Industry gold standard |
| Eater | 2.5 | Food editorial |
| TikTok | 2.5 | Food TikTok reach |
| OpenTable | 2.0 | Reservation + reviews |
| Twitter/X | 1.5 | Chef community |
| Tripadvisor | 1.5 | Tourism reviews |
| Yelp (US) | 1.5 | US restaurant reviews |
| Substack newsletter | 1.5 | Chef stories |
| World's 50 Best | 2.0 | Industry ranking |
| Gault Millau | 1.5 | European guide |
| JBF Awards | 1.5 | James Beard Foundation |
| YouTube | 1.5 | Cooking videos |
| LinkedIn | 1.0 | Restaurant industry pros |

---

## 9 · Writer / Author

| Plataforma | Peso | Rationale |
|---|---|---|
| Substack | 3.0 | Newsletter primary |
| Goodreads | 3.0 | Reader community |
| Amazon Author Central | 3.0 | Book distribution + reviews |
| Twitter/X | 2.5 | Lit Twitter |
| Medium | 2.0 | Public writing |
| LinkedIn | 2.0 | Speaking gigs |
| BookBub | 2.0 | Email marketing reader |
| Reedsy | 1.5 | Self-pub community |
| LibraryThing | 1.5 | Alternative Goodreads |
| NetGalley | 1.5 | Reviewer access |
| Bluesky | 1.5 | Writer community |
| Threads | 1.5 | Cross-graph |
| Instagram (bookstagram) | 1.5 | Book visual culture |
| TikTok (booktok) | 2.0 | Massive reader segment |
| LitHub | 1.5 | Editorial coverage |
| Publishers Marketplace | 1.0 | Industry insider |
| YouTube (booktube) | 1.0 | Long-form reviews |

---

## 10 · Musician

| Plataforma | Peso | Rationale |
|---|---|---|
| Spotify (Artist) | 3.0 | Streaming dominant |
| Apple Music (Artist) | 2.5 | iOS premium audience |
| Instagram | 3.0 | Visual + stories |
| YouTube | 2.5 | Music videos + live |
| TikTok | 2.5 | Viral music driver |
| SoundCloud | 2.0 | Indie + remixes |
| Bandcamp | 2.0 | Direct fan support |
| BandsInTown | 1.5 | Tour notifications |
| Songkick | 1.5 | Concert listings |
| LinkedIn (industry) | 1.0 | Music industry pros |
| AllMusic | 1.0 | Editorial bio |
| Pitchfork | 2.0 | Critic reviews tier-1 |
| Rolling Stone | 2.0 | Press tier-1 |
| Discogs | 1.0 | Vinyl + completist |
| ReverbNation | 0.5 | Older platform |
| Twitter/X | 1.5 | Artist community |

---

## 11 · Architect

| Plataforma | Peso | Rationale |
|---|---|---|
| ArchDaily | 3.0 | Industry publication #1 |
| Dezeen | 3.0 | Design + architecture |
| Instagram | 2.5 | Visual portfolio |
| LinkedIn | 2.5 | Firm network |
| Architizer | 2.0 | Portfolio + awards |
| AIA Member Directory | 2.0 | US trust signal |
| Behance | 1.5 | Cross-post visual |
| Twitter/X | 1.5 | Architecture community |
| Pinterest | 1.5 | Reference culture |
| YouTube | 1.0 | Walkthroughs |
| World Architecture Festival | 1.5 | Awards |
| Domus | 1.5 | Italian + global press |
| Mark Magazine | 1.0 | Editorial niche |
| Substack | 1.0 | Newsletter |

---

## 12 · Athlete

| Plataforma | Peso | Rationale |
|---|---|---|
| Instagram | 3.0 | Visual lifestyle |
| Twitter/X | 2.5 | Real-time + interaction |
| TikTok | 2.5 | Reach + content |
| YouTube | 2.0 | Training + behind scenes |
| ESPN profile | 2.0 | US sports authority |
| Sports Reference | 2.0 | Stats authority |
| Team website | 1.5 | Official |
| League directory | 1.5 | Official |
| LinkedIn (post-career) | 1.5 | Transition |
| Olympedia | 1.5 | Olympic athletes |
| Strava | 1.0 | Endurance sports |
| Wikidata | 1.5 | Identity structured |
| Wikipedia | 2.0 | Notable athletes |

---

## 13 · Politician

| Plataforma | Peso | Rationale |
|---|---|---|
| Twitter/X | 3.0 | Political discourse |
| LinkedIn | 1.5 | Professional only |
| Wikipedia | 3.0 | Trust signal critical |
| Official government site | 3.0 | Authoritative |
| Facebook | 2.5 | Older voter reach |
| Instagram | 2.5 | Younger voter reach |
| YouTube | 2.0 | Speeches + interviews |
| Party website | 1.5 | Official |
| BallotPedia | 2.0 | Voter info site |
| OpenSecrets | 1.5 | Funding transparency |
| GovTrack | 1.5 | Voting record |
| TikTok | 2.0 | Gen Z reach |
| Substack | 1.5 | Newsletter to voters |
| Mastodon | 0.5 | Niche |

---

## 14 · Consultant / Coach

| Plataforma | Peso | Rationale |
|---|---|---|
| LinkedIn | 3.0 | Lead gen primary |
| Substack | 2.5 | Newsletter authority |
| YouTube | 2.5 | Long-form authority |
| Twitter/X | 2.0 | Community building |
| Medium | 2.0 | Long-form writing |
| Instagram | 1.5 | Visual brand |
| Podcast guesting | 2.5 | Discovery via others |
| Trustpilot | 2.0 | Reviews trust |
| Google Reviews | 2.0 | Local discovery |
| Calendly (booking) | 1.5 | Conversion tool |
| TikTok | 1.5 | Reach niche |
| Threads | 1.0 | Cross-graph |
| Bluesky | 1.0 | Emerging |
| Quora | 1.0 | Long-tail SEO |

---

## 15 · Journalist / Analyst

| Plataforma | Peso | Rationale |
|---|---|---|
| Twitter/X | 3.0 | Breaking news + community |
| LinkedIn | 2.5 | Source network |
| Substack | 3.0 | Independent journalism |
| Bluesky | 2.5 | Journalist exodus from X |
| Medium | 2.0 | Cross-post |
| Mastodon | 2.0 | Press federation |
| Threads | 1.5 | Cross-graph |
| Instagram | 1.5 | Brand |
| YouTube | 1.5 | Video journalism |
| TikTok | 1.5 | News TikTok |
| Wikipedia | 2.0 | Trust + verifiability |
| ORCID | 1.0 | Research-style journos |
| Muck Rack | 2.0 | Journalist directory |

---

## 16 · Influencer / Creator

| Plataforma | Peso | Rationale |
|---|---|---|
| Instagram | 3.0 | Visual primary |
| TikTok | 3.0 | Reach primary |
| YouTube | 3.0 | Long-form authority |
| Twitter/X | 2.0 | Community |
| Threads | 2.0 | Cross-graph |
| Substack | 2.0 | Owned audience |
| Patreon | 2.5 | Monetization direct |
| Twitch | 2.0 (gaming) | Live |
| LinkedIn | 1.0 | Brand partnership |
| Cameo | 1.5 | Personalized |
| Linktree / Bio.link | 1.0 | Hub |

---

## 17 · Investor / VC

| Plataforma | Peso | Rationale |
|---|---|---|
| Twitter/X | 3.0 | Deal flow + signaling |
| LinkedIn | 3.0 | Network primary |
| Substack | 2.5 | Thesis publishing |
| Crunchbase | 3.0 | Investor track record |
| AngelList / Wellfound | 2.5 | Syndicate + deal flow |
| Medium | 2.0 | Long-form thesis |
| Hacker News | 2.0 | Founder discovery |
| Forbes Midas List | 2.5 | Press tier-1 |
| TechCrunch coverage | 2.0 | Press |
| Bluesky | 1.5 | Emerging |
| Threads | 1.0 | Cross-graph |
| YouTube | 1.0 | Deep dive pitches |

---

## 18 · Real Estate Pro

| Plataforma | Peso | Rationale |
|---|---|---|
| LinkedIn | 2.5 | Industry network |
| Zillow / Realtor.com (US) | 3.0 | Buyer/seller discovery |
| Idealista / Fotocasa (ES) | 3.0 | Spanish RE platform |
| Instagram | 2.5 | Property visual + brand |
| TikTok | 2.5 | Property tours viral |
| YouTube | 2.0 | Walkthrough video |
| Google Reviews | 2.5 | Local trust |
| Facebook | 1.5 | Older buyer demo |
| Twitter/X | 1.0 | Market commentary |

---

## 19 · Financial Pro (advisor, accountant, banker)

| Plataforma | Peso | Rationale |
|---|---|---|
| LinkedIn | 3.0 | Wealth network primary |
| Twitter/X | 2.0 | FinTwit community |
| Substack | 2.5 | Newsletter authority |
| Bloomberg coverage | 2.5 | Press tier-1 |
| FT coverage | 2.5 | Press tier-1 |
| YouTube | 2.0 | Education long-form |
| Medium | 1.5 | Analysis writing |
| Bluesky | 1.5 | Emerging FinSky |
| Threads | 1.0 | Cross-graph |
| Instagram | 1.0 | Personal brand |
| TikTok | 1.5 | FinTok younger demo |
| Industry-specific (Bloomberg Terminal etc) | 1.5 | Pro tools |

---

## 20 · Catch-all dinámico

Si el sector del cliente no encaja en ninguno de los 19 anteriores:

1. Ejecutar `scripts/platform_search.py` con búsquedas:
   - `"top platforms for [sector] professionals 2026"`
   - `"where do [sector] [career_stage] publish in [geografia]"`
   - `"[sector] community sites high authority"`
   - `"directory [sector] [country]"`

2. Evaluar las plataformas encontradas:
   - ¿Tiene métrica nativa visible?
   - ¿Audiencia ≥10K activos?
   - ¿Tier-1 en el sector?

3. Documentar nuevo mapping aquí (PR a este file)

4. Asignar pesos provisionales y validar con 2-3 perfiles del sector

---

## Iteración del mapping

Tras cada 5 clientes nuevos del mismo sector, revisar:
- ¿Algún sector necesita refinamiento? (pesos imprecisos)
- ¿Plataformas emergentes a añadir?
- ¿Plataformas declinando a degradar peso?

Actualizaciones documentadas con timestamp + cliente que motivó el cambio.
