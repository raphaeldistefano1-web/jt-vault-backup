---
type: project
status: active
tags: [wordpress, plugins, stack]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "Stack 10 plugins WP actifs au 2026-04-25 + état post-cleanup (akismet/all-in-one-wp-migration/hello/wp-robots-txt désinstallés)"
ai_writable: false
related:
  - "[[Site-WordPress]]"
  - "[[Plugin-jt-booking]]"
  - "[[Plugin-jt-migrate]]"
  - "[[Decision-Akismet-vers-Antispam-Bee]]"
  - "[[Decision-Redis-Object-Cache-Disabled]]"
---

# 📦 Site WP — Plugins stack 2026-04-25

## 10 plugins actifs

| Plugin | Version | Rôle | Notes |
|---|---|---|---|
| `jt-booking-v1.0.4` | 1.0.4 | Booking custom | [[Plugin-jt-booking]] |
| `jt-migrate` | 1.2.1 | Migration full-fidelity | [[Plugin-jt-migrate]] |
| `antispam-bee` | 2.11.11 | Anti-spam RGPD | Remplace akismet (cf. [[Decision-Akismet-vers-Antispam-Bee]]) |
| `wordfence` | 8.1.4 | Firewall + scan + 2FA | Wizard à finir via UI |
| `updraftplus` | 1.26.3 | Backup auto | Destination Drive/Dropbox à choisir |
| `complianz-gdpr` | 7.4.6 | RGPD bannière + politique | Wizard à finir via UI |
| `wp-optimize` | 4.5.2 | Page cache + minify CSS | Cache file 12h TTL, minify JS désactivé |
| `webp-converter-for-media` | 6.5.5 | Conversion auto WebP/AVIF | Bulk convert à lancer via UI |
| `speculation-rules` | 1.6.0 | Speculative Loading prerender | Mode `moderate` au survol |
| `google-site-kit` | 1.177.0 | Search Console + Analytics + PageSpeed | Installé par user, OAuth à connecter |

## Désinstallés post-cleanup

- ❌ **akismet** — licence commerciale exigée pour usage commercial → remplacé par antispam-bee
- ❌ **all-in-one-wp-migration** — remplacé par notre plugin custom [[Plugin-jt-migrate]]
- ❌ **hello** — plugin WP par défaut inutile
- ❌ **wp-robots-txt** — redondant (mu-plugin custom gère robots.txt)
- ❌ **seo-by-rank-math** (installé puis désinstallé) — le theme fait déjà mieux (cf. [[Decision-Mu-plugin-vs-RankMath]])
- ❌ **redis-cache** (installé puis désinstallé) — conflit advanced-cache.php avec WP-Optimize (cf. [[Decision-Redis-Object-Cache-Disabled]])

## Themes default supprimés

- twentytwentyfour, twentytwentythree, twentytwentytwo
- Conservé : twentytwentyfive comme fallback

## Mu-plugin custom

[[Mu-plugin-jt-seo-extras]] — toujours actif, ~600 lignes.

## Conteneur Redis

Ajouté au docker-compose, **up et healthy** mais **pas utilisé** comme object cache (conflit avec WP-Optimize advanced-cache.php). Dispo pour usage futur si on résout le conflit ou bascule sur un autre plugin (LiteSpeed Cache par exemple).

## Liens

- [[Site-WordPress]]
- [[Site-WordPress-Optimisation-2026-04-25]]
