---
ai_writable: false
backlinks:
- 2026-05-10-instance-c-images-affichées-mais-absentes-de-la-mé
- JT-Migrate-v1.2.0
- Lessons-Learned
- Migration-WP-com-vers-VPS-2026-04-25
- Site-WordPress-Optimisation-2026-04-25
- _MOC-site-wordpress
created: 2026-04-25
description: Apache Timeout=300s (default) tue les uploads > 5 min sur connexion résidentielle
  → Traefik retourne 502. Fix Timeout 1800s.
embed_hash: null
embed_model_version: null
entities:
- debugging
- site-wordpress
- wordpress
id: 202604252038-bug-apache-timeout-300-vs-uploads
intent: log
last-accessed: 2026-04-25
project: Bugs
related:
- 2026-05-10-instance-c-images-affichées-mais-absentes-de-la-mé
- '[[Migration-WP-com-vers-VPS-2026-04-25]]'
- '[[Plugin-jt-migrate]]'
- '[[VPS-Hostinger]]'
relevance: medium
status: resolved
summary: 'Pendant l''import d''une archive 321 MB via UI WordPress, l''upload abandonnait
  après ~10 minutes avec :'
tags:
- bug
- lesson
- apache
- infra
tier: cold
topic_cluster: bug-log
type: bug
updated: 2026-04-25
---

# 🐛 Bug : Apache Timeout=300 vs gros uploads

## Symptôme

Pendant l'import d'une archive 321 MB via UI WordPress, l'upload abandonnait après ~10 minutes avec :
```
HTTP 502 Bad Gateway
```

Le frontend voyait l'upload progresser jusqu'à un certain pourcentage puis fail.

## Cause racine

Apache `Timeout 300` (5 min) par défaut dans le conteneur `wordpress:6.6-php8.3-apache`. Sur connexion résidentielle (~1-5 Mbit/s upload), 321 MB prend 8-30 minutes. Apache ferme la connexion en plein milieu → Traefik retourne 502 au navigateur.

Ce n'est pas un timeout PHP (set_time_limit) — c'est Apache qui kick.

## Fix

Override Apache config dans `/var/www/wordpress-instance/config/apache-uploads.conf`, monté en `/etc/apache2/conf-enabled/zz-jt-uploads.conf` :

```apache
Timeout 1800
RequestReadTimeout body=60,minrate=200
```

- `Timeout 1800` = 30 min
- `RequestReadTimeout body=60,minrate=200` = 60s pour le 1er byte du body, puis minimum 200 b/s

Restart conteneur → fix immédiat.

## Alternative découverte

Plus pragmatique pour les très gros uploads : [[JT-Migrate-v1.2.0|mode import-from-server-path]] qui bypass complètement l'upload HTTP. L'archive est déposée directement sur le serveur via SCP ou téléchargée server-to-server.

C'est la solution préférée pour les futurs imports > 200 MB.

## 📚 Lesson learned

**Apache `Timeout 300` par défaut tue les gros uploads sur connexion résidentielle.**

Dès qu'on prévoit des uploads > 50 MB :
- Augmenter `Timeout` (1800 = 30 min raisonnable)
- Vérifier `RequestReadTimeout` (`body=60,minrate=200` permet 200 b/s minimum, tolère les liens lents)
- Plus généralement : prévoir un **bypass HTTP** (SCP, server-to-server curl, S3 multipart upload) pour les vrais gros volumes

Sur Traefik, pas de timeout particulier à modifier (les valeurs par défaut sont OK). Le timeout vient bien d'Apache.

## Liens

- [[VPS-Hostinger]]
- [[Migration-WP-com-vers-VPS-2026-04-25]]
- [[JT-Migrate-v1.2.0]]

## Related

- [[2026-05-10-instance-c-images-affichées-mais-absentes-de-la-mé]] — Instance C : images affichées mais absentes de la médiathèque