---
ai_writable: false
backlinks:
- 2026-05-10-supprimer-références-club-med-du-contenu-ljt
- 2026-05-11-layout-nouvelle-saison-3-cartes-alignées-horizonta
- Bug-WP-Link-Blog-404
- Decision-Mu-plugin-vs-RankMath
- Mu-plugin-jt-seo-extras
- Mu-plugin-vs-Theme-Pattern
- Schema-org-LodgingBusiness
- Site-WordPress
- Test-jt-booking-PMS-2026-04-25
- _Index
- _MOC-site-wordpress
- _VAULT-INDEX
created: 2026-04-25
description: Theme custom jardintropical-child du site WP — ultra pro, schema LodgingBusiness
  complet, lazy loading, 74% WebP
embed_hash: null
embed_model_version: null
entities:
- documentation
- reference
id: 202604252032-theme-jardintropical-child
intent: reference
last-accessed: 2026-04-25
project: site-wordpress
related:
- 2026-05-11-layout-nouvelle-saison-3-cartes-alignées-horizonta
- '[[Mu-plugin-jt-seo-extras]]'
- '[[Mu-plugin-vs-Theme-Pattern]]'
- '[[Schema-org-LodgingBusiness]]'
- '[[Site-WordPress]]'
relevance: high
status: active
summary: Theme standalone custom malgré son nom -child qui suggère un theme enfant
  — il n'a en fait pas de parent dépendant.
tags:
- wordpress
- theme
- jardintropical-child
tier: hot
topic_cluster: wordpress-stack
type: project
updated: 2026-04-25
---

# 🎨 Theme jardintropical-child

## Nature

Theme **standalone custom** (malgré son nom `-child` qui suggère un theme enfant — il n'a en fait pas de parent dépendant).

## Ce qu'il fait déjà très bien (pas besoin de plugin SEO commercial)

- ✅ **Schema LodgingBusiness COMPLET** — geo (16.1273, -61.7673 = Bouillante), 8 amenityFeature, sameAs Facebook/Instagram/TripAdvisor, address, telephone, email, priceRange, image, numberOfRooms 14, checkinTime/checkoutTime, availableLanguage FR+EN, paymentAccepted, currenciesAccepted
- ✅ **Open Graph** complet (og:type, og:locale fr_FR, og:title, og:description, og:url, og:image 1200x630, og:image:alt)
- ✅ **Twitter Card** summary_large_image
- ✅ **Canonical link** sur toutes les pages
- ✅ **Viewport** mobile-friendly
- ✅ **Title + meta description** différenciés par page
- ✅ **Locale fr_FR**
- ✅ **Lazy loading natif** sur 29/30 images
- ✅ **74% des images en WebP** (504 webp / 769 total)

## Bugs connus (à fixer côté theme par le dev)

- ❌ **Pas de `srcset`** sur les `<img>` — mobile télécharge les images full-size, ~30% bandwidth gaspillée. À fixer dans le theme (PHP ou via filter `wp_get_attachment_image_attributes`).
- ❌ **Logo schema URL hardcoded** vers `https://lejardintropical.fr` (domaine final) alors qu'on est sur nip.io provisoire. À résoudre à la migration domaine.
- ❌ **Lien `/blog/`** dans la page À propos même sans blog actif. Mitigé via redirect 301 dans [[Mu-plugin-jt-seo-extras]] mais à fixer dans le theme.

## Pourquoi ne pas installer Rank Math / Yoast

Cf. [[Decision-Mu-plugin-vs-RankMath]] — le theme fait déjà tout ce qu'un plugin SEO ferait, en mieux et sans friction. Pattern : compléter via [[Mu-plugin-jt-seo-extras|mu-plugin custom]] plutôt qu'écraser.

## CSS / JS

- 4 fichiers CSS séparés : variables.css, reset.css, typography.css, main.css (modulaire mais 4 round-trips — minify CSS WP-Optimize aide)
- 1 main.js du theme (19 KB) + Swiper bundle CDN (cdn.jsdelivr.net)
- 8 inline `<style>` blocks (CSS custom du theme)

## Liens

- [[Site-WordPress]]
- [[Mu-plugin-jt-seo-extras]]
- [[Schema-org-LodgingBusiness]]
- [[Decision-Mu-plugin-vs-RankMath]]

## Related

- [[2026-05-11-layout-nouvelle-saison-3-cartes-alignées-horizonta]] — Layout 'nouvelle saison' — 3 cartes alignées horizontalement