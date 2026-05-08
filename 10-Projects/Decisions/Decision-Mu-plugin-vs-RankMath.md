---
ai_writable: false
alternatives:
- Rank Math
- Yoast
- SEOPress
- Slim SEO
chosen: Mu-plugin custom + theme existant
context: Optim site WP 2026-04-25 — Rank Math testé puis désinstallé
created: 2026-04-25
description: 'Décision : NE PAS installer Rank Math/Yoast — utiliser un mu-plugin
  custom à la place'
embed_hash: null
embed_model_version: null
entities:
- documentation
- site-wordpress
- wordpress-optimization
id: 202604252036-decision-mu-plugin-vs-rankmath
intent: decision
last-accessed: 2026-04-25
project: Decisions
related:
- '[[Mu-plugin-vs-Theme-Pattern]]'
- '[[Mu-plugin-jt-seo-extras]]'
- '[[Theme-jardintropical-child]]'
relevance: high
status: accepted
summary: Pendant l'optim site WP 2026-04-25, j'ai initialement installé Rank Math
  comme plugin SEO recommandé par les guides 2026…
tags:
- decision
- wordpress
- seo
- plugin
tier: warm
topic_cluster: decision-log
type: decision
updated: 2026-04-25
---

# 🎯 Decision : Mu-plugin custom vs RankMath

## Contexte

Pendant l'optim site WP 2026-04-25, j'ai initialement installé **Rank Math** comme plugin SEO (recommandé par les guides 2026 standards).

Après audit du theme `jardintropical-child` : il fournit déjà :
- Schema LodgingBusiness COMPLET (geo, amenityFeature x8, sameAs, etc.)
- OG + Twitter Card
- Title + meta différenciés par page
- Lazy loading, 74% WebP, viewport mobile

Rank Math aurait écrasé ou dupliqué ces meta tags → conflits + bruit dans le HTML.

## Options considérées

### A. Garder Rank Math, configurer pour ne pas écraser
- ✅ UI pour edit meta facilement
- ❌ Configuration complexe (désactiver chaque module qui interfère)
- ❌ Risque de duplication subtile (2 schemas LodgingBusiness)
- ❌ 22 MB de plugin pour des features dont 80% sont déjà dans le theme

### B. Yoast / SEOPress / Slim SEO
- Mêmes problèmes que Rank Math (écrasement meta theme)

### C. **Mu-plugin custom + theme existant** ✅
- ✅ Theme fait son boulot sans interférence
- ✅ Mu-plugin ajoute UNIQUEMENT ce qui manque (FAQPage, Offer, BreadcrumbList, robots LLM-aware, security headers, etc.)
- ✅ Versionnable, testable, mu = always-active
- ❌ Demande discipline d'écriture PHP propre

## Choix : **C**

## Rationale

- Le theme custom est **ultra pro**, l'écraser est un anti-pattern
- Le mu-plugin ne fait QUE l'incrément, pas de redondance
- Performance : mu-plugin custom (~600 lignes) vs Rank Math (22 MB) = ordre de grandeur de différence
- Maintenance : 1 fichier à comprendre vs un plugin tiers à debug

## Conséquences

- Rank Math désinstallé fin Loop 1
- Mu-plugin `jt-seo-extras.php` créé à `wp-content/mu-plugins/`
- Pattern documenté dans [[Mu-plugin-vs-Theme-Pattern]]

## Liens

- [[Mu-plugin-jt-seo-extras]]
- [[Theme-jardintropical-child]]
- [[Site-WordPress-Optimisation-2026-04-25]]