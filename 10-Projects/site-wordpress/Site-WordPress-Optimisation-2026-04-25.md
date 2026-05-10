---
ai_writable: false
backlinks:
- 2026-04-25-session-context
- 2026-04-25-session-context 2
- Bug-WP-Image-Encoding-Accent
- Decision-Mu-plugin-vs-RankMath
- Decisions-Log
- GEO-Generative-Engine-Optimization
- Hotel-Le-Jardin-Tropical
- Migration-WP-com-vers-VPS-2026-04-25
- Mu-plugin-jt-seo-extras
- Robots-txt-LLM-Aware
- Site-Plugins-Stack-2026-04-25
- Site-WordPress
- _Index
- _MOC-site-wordpress
- llms-txt-standard
created: 2026-04-25
description: Optimisation complète site WP — 3 loops vérification/recherche/application
  — TTFB 1170ms→33ms, gzip -81%, 0 broken links/441
embed_hash: null
embed_model_version: null
entities:
- migration
- site-wordpress
- wordpress
id: 202604252033-site-wordpress-optimisation-2026-04-25
intent: reference
last-accessed: 2026-04-25
project: site-wordpress
related:
- 2026-04-25-session-context 2
- '[[Migration-WP-com-vers-VPS-2026-04-25]]'
- '[[Mu-plugin-jt-seo-extras]]'
- '[[Site-Plugins-Stack-2026-04-25]]'
- '[[Site-WordPress]]'
relevance: high
status: completed
summary: Suite à la migration depuis dealmfr.wpcomstaging.com vers le VPS Hostinger
  Migration-WP-com-vers-VPS-2026-04-25, User-Ra…
tags:
- wordpress
- optimisation
- perf
- seo
- security
tier: hot
topic_cluster: wordpress-stack
type: project
updated: 2026-04-25
---

# 🚀 Optimisation site WP — 2026-04-25

## Contexte

Suite à la migration depuis dealmfr.wpcomstaging.com vers le VPS Hostinger ([[Migration-WP-com-vers-VPS-2026-04-25]]), [[User-Raphael-Distefano|Raphaël]] a demandé une optimisation complète du site sur tous les axes (SEO, GEO, perf, sécurité, RGPD, accessibility).

## Méthodologie 3 loops

Chaque loop = vérification → recherche web (agents avec WebSearch) → application + tests.

### Loop 1 (initiale)

- Audit complet : plugins actuels, theme, pages, robots.txt, meta, schema, performance
- Recherche : SEO/GEO 2026 hôtellerie + plugins WP recommandés 2026
- Application : install plugins essentiels (antispam-bee, wordfence, updraftplus, complianz, wp-optimize, webp-converter), mu-plugin custom v1, security headers, robots LLM-aware, llms.txt

### Loop 2 (approfondissement)

- Vérification : 22/22 pages OK, 5 security headers, schemas
- Recherche : optimisations avancées 2026 (Speculation Rules, Brotli, OPcache prod, Redis, Schema Trip/Service)
- Application : Speculation Rules plugin, OPcache 256M/20000, MariaDB tuning, Schema Offer/BreadcrumbList/TouristAttraction, sticky CTA mobile, focus-visible a11y, Redis (puis désinstallé pour conflit)

### Loop 3 (finitions)

- Vérification : audit broken links 441 vérifiés
- Recherche : finitions niche 2026 (sitemap lastmod, REST API hardening, dns-prefetch, schema TouristAttraction)
- Application : `lastmod` sitemap, sitemap exclusion pages techniques, redirects 301 liens obsolètes, fix encodage URL accent (symlink WebP)

## Métriques avant/après

| | Avant | Après | Gain |
|---|---|---|---|
| TTFB cached | ~1170 ms | **33-58 ms** | -95% |
| Home gzipped | 142 KB | **27 KB** | -81% |
| Plugins actifs | 4 dont 2 obsolètes | **10** prod-grade | propre |
| Schemas | 2 (theme) | **3 à 7 selon page** | +250% |
| Headers sécurité | 0 | **5** | ∞ |
| DB autoload | 0.13 MB | **0.044 MB** | -83% |
| Broken links | inconnus | **0/441** | ✅ |
| Pages publiques | 17 + 7 doublons | **22** (4 nouvelles + cleanup) | propre |
| robots.txt | 4 lignes | **53 lignes** LLM-aware | GEO-ready |

## Décisions clés liées

- [[Decision-Mu-plugin-vs-RankMath]]
- [[Decision-Redis-Object-Cache-Disabled]]
- [[Decision-Akismet-vers-Antispam-Bee]]
- [[Decision-Robots-txt-LLM-Aware]]
- [[Decision-Disable-WP-Cron-cron-Linux]]

## Bugs résolus pendant

- [[Bug-Apache-Timeout-300-vs-Uploads]]
- [[Bug-WP-Image-Encoding-Accent]]
- [[Bug-WP-Link-Blog-404]]

## Pages créées

- `/faq/` — 12 Q/R + schema FAQPage
- `/mentions-legales/` — template France 2026 (LCEN + DSA)
- `/politique-confidentialite/` — template RGPD
- `/cgv/` — template Code conso (incl. art. L.221-28 12° pas de droit rétractation hébergement)

## Reste à faire (cf. todo)

- Site Kit by Google wizard OAuth
- Wordfence wizard + 2FA
- UpdraftPlus destination
- Complianz wizard
- WebP bulk convert via UI
- Migration domaine final
- Décisions GO/NO-GO blog + bilingue

## Liens

- [[Site-WordPress]]
- [[Mu-plugin-jt-seo-extras]]
- [[Site-Plugins-Stack-2026-04-25]]

## Related

- [[2026-04-25-session-context 2]] — 2026-04-25-session-context 2