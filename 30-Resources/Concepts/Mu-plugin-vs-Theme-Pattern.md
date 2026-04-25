---
type: concept
status: active
tags: [wordpress, pattern, mu-plugin]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "Pattern : compléter le theme via un mu-plugin custom plutôt qu'un plugin SEO commercial qui écraserait"
ai_writable: false
related:
  - "[[Mu-plugin-jt-seo-extras]]"
  - "[[Theme-jardintropical-child]]"
  - "[[Decision-Mu-plugin-vs-RankMath]]"
  - "[[Site-WordPress]]"
---

# 🔧 Pattern : mu-plugin vs theme

## Principe

Quand un theme custom fait déjà bien son boulot (meta, OG, schema, lazy load), **ne PAS installer un plugin SEO commercial** (Rank Math, Yoast, SEOPress) qui voudrait l'écraser ou dupliquer.

À la place : **mu-plugin custom** dans `wp-content/mu-plugins/`. Always-active, ne peut pas être désactivé via admin, idéal pour les ajouts qui ne doivent jamais "disparaître par accident".

## Pourquoi le mu-plugin (vs theme functions.php)

- Survit au changement de theme
- Versionnable indépendamment
- Pas de dépendance Customizer / Customizer hooks
- Pas de risque que le user désactive par erreur

## Pourquoi pas un plugin classique

- Un plugin classique peut être **désactivé** depuis l'admin → trou de sécurité ou perte de fonctionnalité
- Risque de doublons si plusieurs plugins font la même chose
- Plus de fingerprint pour les attaquants

## Quand utiliser mu-plugin

- ✅ Security headers (HSTS, X-Frame-Options, etc.)
- ✅ Robots.txt étendu (LLM-aware)
- ✅ llms.txt routing
- ✅ Schema additionnel (BreadcrumbList, FAQPage, TouristAttraction)
- ✅ Hide WP version / fingerprint reduction
- ✅ Anti-énumération users (REST API filter, ?author= redirect)
- ✅ Sticky booking widget mobile
- ✅ Skip-to-content link
- ✅ Redirects 301 pour fixer liens internes obsolètes
- ✅ A11y CSS (focus-visible)
- ✅ Preconnect / dns-prefetch resources

## Quand NE PAS utiliser mu-plugin

- ❌ Logique métier complexe (utilise un plugin classique structuré)
- ❌ Quelque chose que le user devrait pouvoir désactiver facilement
- ❌ Quelque chose qui dépend d'options DB modifiables via UI

## Implementation Le Jardin Tropical

Cf. [[Mu-plugin-jt-seo-extras]] (~600 lignes, 14 sections).

## Liens

- [[Site-WordPress]]
- [[Theme-jardintropical-child]]
- [[Decision-Mu-plugin-vs-RankMath]]
