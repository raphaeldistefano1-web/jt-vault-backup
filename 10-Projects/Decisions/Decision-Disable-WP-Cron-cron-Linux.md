---
type: decision
status: accepted
tags: [decision, wordpress, cron, perf]
created: 2026-04-25
updated: 2026-04-25
relevance: medium
description: "DISABLE_WP_CRON=true + cron Linux host */15min — fiable, pas de pageload trigger"
ai_writable: false
related:
  - "[[Site-WordPress]]"
  - "[[Mu-plugin-jt-seo-extras]]"
context: "Optim site WP 2026-04-25 — wp-cron au pageload est unfair"
chosen: "Cron Linux host"
alternatives: ["wp-cron pageload", "cron systemd timer", "cron dans conteneur"]
---

# 🎯 Decision : DISABLE_WP_CRON + cron Linux host

## Contexte

WordPress par défaut déclenche `wp-cron.php` à chaque pageload. Problèmes :

1. **Performance** : ralentit la page chargée pour exécuter les cron jobs
2. **Si pas de trafic** : les cron ne tournent jamais
3. **Sécurité** : `wp-cron.php` est public, peut être DoS-é

## Options considérées

### A. Statu quo (wp-cron au pageload)
- ❌ Tous les problèmes ci-dessus

### B. Cron systemd timer
- ✅ Fiable
- ❌ Plus complexe à configurer

### C. Cron dans le conteneur Apache
- ✅ Encapsulé
- ❌ apt-get install cron pas fluide dans le conteneur officiel WordPress

### D. **Cron Linux host via crontab root** ✅
- ✅ Fiable (cron host garantit l'exécution même si conteneur down brièvement)
- ✅ Simple : 1 ligne de crontab
- ✅ Logs accessibles (`grep cron /var/log/syslog`)

## Choix : **D**

## Implementation

```bash
# Sur le VPS host
crontab -e
*/15 * * * * docker exec -u www-data jt-wordpress php -d disable_functions= /var/www/html/wp-cron.php > /dev/null 2>&1 # wp-cron lejardin tropical
```

Côté `wp-config.php` :
```php
define('DISABLE_WP_CRON', true);
```

## Conséquences

- ✅ `wp-cron.php` n'est plus déclenché par les visiteurs
- ✅ Cron tournent toutes les 15 min, fiable
- ✅ Le mu-plugin bloque l'accès public à `/wp-cron.php` (sauf depuis loopback / réseau Docker interne)

## Liens

- [[Site-WordPress]]
- [[Mu-plugin-jt-seo-extras]]
