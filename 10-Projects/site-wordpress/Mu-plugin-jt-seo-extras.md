---
ai_writable: false
backlinks:
- 2026-05-09-instance-d-wordpress-en-rotation-test
- 2026-05-09-synchronisation-manuelle-fragile-entre-instances-w
- 2026-05-10-ajouter-google-business-à-côté-de-tripadvisor
- 2026-05-10-carousel-hbook-boutons-surdimensionnés-et-mal-espa
- 2026-05-10-structure-paths-uploads-wordpress-instance-acd
- Bug-WP-Link-Blog-404
- Decision-Disable-WP-Cron-cron-Linux
- Decision-Mu-plugin-vs-RankMath
- Decision-Robots-txt-LLM-Aware
- Mu-plugin-vs-Theme-Pattern
- Robots-txt-LLM-Aware
- Schema-FAQPage
- Schema-org-LodgingBusiness
- Site-Plugins-Stack-2026-04-25
- Site-WordPress
- Site-WordPress-Optimisation-2026-04-25
- Theme-jardintropical-child
- _Index
- _MOC-site-wordpress
- _VAULT-INDEX
created: 2026-04-25
description: Mu-plugin custom ~600 lignes 16 sections — robots.txt LLM-aware, security
  headers, schemas, GEO, redirects, A11y
embed_hash: null
embed_model_version: null
entities:
- llm
- site-wordpress
- wordpress
id: 202604252032-mu-plugin-jt-seo-extras
intent: reference
last-accessed: 2026-04-25
project: site-wordpress
related:
- 2026-05-09-synchronisation-manuelle-fragile-entre-instances-w
- 2026-05-10-ajouter-google-business-à-côté-de-tripadvisor
- 2026-05-10-carousel-hbook-boutons-surdimensionnés-et-mal-espa
- 2026-05-10-page-hébergements-tableau-structuré-type-emplaceme
- 2026-05-10-structure-paths-uploads-wordpress-instance-acd
- '[[GEO-Generative-Engine-Optimization]]'
- '[[Mu-plugin-vs-Theme-Pattern]]'
- '[[Robots-txt-LLM-Aware]]'
- '[[Schema-FAQPage]]'
- '[[Site-WordPress]]'
- '[[Theme-jardintropical-child]]'
relevance: high
status: active
summary: /var/www/wordpress-instance/data/wordpress/wp-content/mu-plugins/jt-seo-extras.php
tags:
- wordpress
- mu-plugin
- seo
- security
tier: hot
topic_cluster: wordpress-stack
type: project
updated: 2026-04-25
---

# 🔧 Mu-plugin jt-seo-extras

## Localisation

`/var/www/wordpress-instance/data/wordpress/wp-content/mu-plugins/jt-seo-extras.php`

(Mounted dans le conteneur Apache : `/var/www/html/wp-content/mu-plugins/jt-seo-extras.php`)

## Caractéristiques

- **~600 lignes**
- **16 sections** numérotées
- **Always-active** (mu-plugin = ne peut pas être désactivé via admin)
- Suit le pattern [[Mu-plugin-vs-Theme-Pattern|compléter le theme via mu-plugin]]

## Sections (par numéro)

1. **robots.txt LLM-aware** — bloque GPTBot/Google-Extended/CCBot/ClaudeBot/anthropic-ai/Bytespider/Amazonbot/FacebookBot, autorise OAI-SearchBot/PerplexityBot/ChatGPT-User/Perplexity-User/Google-CloudVertexBot/Applebot-Extended (cf. [[Robots-txt-LLM-Aware]])
2. **/llms.txt** : commentaire — fichier physique racine WP, pas via routing (pour éviter 301 trailing slash)
3. **Security headers** : HSTS 1 an, X-Content-Type-Options nosniff, X-Frame-Options SAMEORIGIN, Referrer-Policy strict-origin-when-cross-origin, Permissions-Policy (geo/mic/cam désactivés)
4. **xmlrpc disabled** + remove X-Pingback header
5. **WP fingerprint reduction** : remove generator/wlwmanifest/RSD/shortlink/REST-link/feed_links
6. **wp-emoji disabled** (économise ~12 KB JS+CSS)
7. **Anti-énumération users** : `/wp-json/wp/v2/users` → 404 via rest_endpoints filter, `?author=` redirect home
8. **Pages noindex** : mentions/CGV/PDC en `noindex,follow`, merci-reservation/reservation-annulee en `noindex,nofollow`
9. **Hero preload + fetchpriority="high"** sur 1ère image
10. **Favicons + apple-touch + manifest.json + theme-color #0a7d4f**
11. **Schema FAQPage** sur /faq/ (12 Q/R)
12. **Schema Offer.priceValidUntil** sur home
13. **Schema BreadcrumbList** automatique sur pages internes
14. **Schema TouristAttraction + TouristTrip** sur /reserve-cousteau/
15. **Sitemap** : lastmod précis (DATE_W3C), exclusion 5 pages techniques
16. **Sticky booking widget mobile + WhatsApp CTA** (RGPD-safe, hidden desktop)
17. **Skip-to-content link + focus-visible CSS** (a11y WCAG 2.2)
18. **Lazy load iframes natif** via the_content filter
19. **preconnect** cdn.jsdelivr + GTM ; **dns-prefetch** Facebook/Instagram/TripAdvisor/Maps/WhatsApp
20. **Redirects 301** : /confidentialite/, /blog/, /mentions/, /privacy/, /legal/, /terms/, /conditions/
21. **Disable Application Passwords** + **hide WP version REST API root**

## Pourquoi un mu-plugin (vs theme functions.php)

- Survit aux changements de theme
- Versionnable indépendamment
- Pas désactivable par erreur via admin (sécurité)

## Tests

- 0 broken links sur 441 vérifiés (cf. [[Site-WordPress-Optimisation-2026-04-25]])
- TTFB cached 33-58 ms
- Home gzipped 27 KB

## Liens

- [[Site-WordPress]]
- [[Theme-jardintropical-child]]
- [[Mu-plugin-vs-Theme-Pattern]]

## Related

- [[2026-05-09-synchronisation-manuelle-fragile-entre-instances-w]] — Synchronisation manuelle fragile entre instances WordPress
- [[2026-05-10-carousel-hbook-boutons-surdimensionnés-et-mal-espa]] — Carousel HBook : boutons surdimensionnés et mal espacés
- [[2026-05-10-ajouter-google-business-à-côté-de-tripadvisor]] — Ajouter Google Business à côté de TripAdvisor
- [[2026-05-10-page-hébergements-tableau-structuré-type-emplaceme]] — Page hébergements : tableau structuré (Type | Emplacement | Prix/Saison)
- [[2026-05-10-structure-paths-uploads-wordpress-instance-acd]] — Structure paths uploads WordPress (Instance A/C/D)