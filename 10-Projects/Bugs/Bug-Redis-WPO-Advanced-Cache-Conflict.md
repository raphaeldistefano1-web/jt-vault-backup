---
type: bug
status: workaround
tags: [bug, lesson, wordpress, redis, cache]
created: 2026-04-25
updated: 2026-04-25
relevance: medium
description: "Plugin redis-cache + WP-Optimize page cache = conflit advanced-cache.php → site HTTP 500. Workaround : redis-cache désactivé."
ai_writable: false
related:
  - "[[Decision-Redis-Object-Cache-Disabled]]"
  - "[[Site-Plugins-Stack-2026-04-25]]"
---

# 🐛 Bug : Redis Object Cache + WP-Optimize conflit

## Symptôme

Lors de l'activation du plugin `redis-cache` (sur stack avec WP-Optimize page cache déjà actif) :
- Site retourne **HTTP 500** sur toutes les pages
- Drop-ins listés : `advanced-cache.php` (WP-Optimize) + `Redis Object Cache Drop-In v2.7.0`

## Cause racine

Le drop-in `advanced-cache.php` est exclusif (un seul plugin peut l'utiliser). WP-Optimize l'occupe pour son page cache file-based. À l'activation, redis-cache veut son `object-cache.php` drop-in et fait quelque chose qui crashe.

(Conflit non documenté dans la doc des deux plugins.)

## Workaround

[[Decision-Redis-Object-Cache-Disabled]] : redis-cache désinstallé. Le **conteneur Redis serveur** reste up et healthy au cas où on bascule sur un autre plugin de cache plus tard (LiteSpeed Cache, Object Cache Pro).

Le site WP fonctionne avec WP-Optimize page cache (37ms warm, 22x speedup), c'est largement suffisant pour le trafic actuel.

## Fix possible (non implémenté)

Pour avoir Redis Object Cache + page cache fichier :
1. Désinstaller WP-Optimize (perd le page cache file-based)
2. Installer un autre plugin de page cache (qui n'utilise pas advanced-cache.php) — ex: WP Super Cache, Cache Enabler
3. Réactiver redis-cache

À évaluer si on rencontre des limites de perf admin/booking dynamiques.

## 📚 Lesson learned

**Les drop-ins WordPress (`advanced-cache.php`, `object-cache.php`, `db.php`, `sunrise.php`) sont mutuellement exclusifs.** Avant d'activer un plugin qui touche à un drop-in, vérifier qu'aucun autre plugin ne l'utilise déjà.

Le `wp redis status` affiche les drop-ins en place — pratique pour diagnostiquer.

Pour un site solo, **page cache file-based > object cache Redis** sur trafic faible-modéré (le page cache économise un round-trip PHP+DB complet).

## Liens

- [[Decision-Redis-Object-Cache-Disabled]]
- [[Site-Plugins-Stack-2026-04-25]]
