---
type: decision
status: accepted
tags: [decision, wordpress, cache, redis]
created: 2026-04-25
updated: 2026-04-25
relevance: medium
description: "Redis Object Cache désactivé suite à conflit advanced-cache.php avec WP-Optimize — conteneur Redis reste up"
ai_writable: false
related:
  - "[[Site-WordPress]]"
  - "[[Site-Plugins-Stack-2026-04-25]]"
  - "[[Bug-Redis-WPO-Advanced-Cache-Conflict]]"
context: "Optim site WP 2026-04-25 — Redis installé puis désactivé"
chosen: "Redis désactivé, conteneur up pour usage futur"
alternatives: ["redis-cache + wp-optimize", "redis-cache seul", "memcached"]
---

# 🎯 Decision : Redis Object Cache désactivé

## Contexte

Pendant Loop 1 optim, ajout du conteneur Redis au docker-compose pour activer un **Object Cache** WP (gain TTFB potentiel sur pages dynamiques admin/booking).

À l'activation du plugin `redis-cache` → **HTTP 500** sur le site.

## Cause

Le drop-in `advanced-cache.php` est utilisé par WP-Optimize (page cache file-based) ET le plugin redis-cache veut son propre `object-cache.php` drop-in. Conflit non documenté → fatal.

## Options considérées

### A. Désactiver WP-Optimize page cache, garder Redis Object Cache
- ✅ Redis fonctionnerait
- ❌ Perte du speedup 22x du page cache (1.17s → 0.054s)
- ❌ Object cache = gain marginal sur pages cached, principal gain sur admin/booking dynamiques
- ❌ TTFB final probablement DEGRADÉ (page cache > object cache pour ce volume)

### B. **Désactiver redis-cache, garder WP-Optimize page cache** ✅
- ✅ Site reste ultra-rapide (37ms warm)
- ✅ Conteneur Redis reste UP (zéro coût) pour usage futur
- ❌ Pas d'object cache (mais peu utile pour ce trafic)

### C. Bascule sur LiteSpeed Cache
- ❌ Demande LiteSpeed serveur (pas Apache)
- Pas d'option pour cette stack

## Choix : **B**

## Rationale

- Le **page cache** est plus impactant que l'**object cache** pour ce site (faible trafic admin, beaucoup de page views statiques)
- Évite le risque de tout casser pour un gain marginal
- Conteneur Redis reste dispo si on bascule sur autre stack plus tard (LiteSpeed Cache, custom plugin)

## Conséquences

- redis-cache plugin désinstallé
- `wp-config.php` garde les `WP_REDIS_*` constants (configurés mais inutilisés)
- Conteneur `jt-wordpress-redis` up, `redis-cli ping` → PONG, mais pas connecté à WP

## Liens

- [[Site-Plugins-Stack-2026-04-25]]
- [[Bug-Redis-WPO-Advanced-Cache-Conflict]]
