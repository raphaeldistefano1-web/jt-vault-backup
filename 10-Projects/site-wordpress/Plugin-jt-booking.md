---
ai_writable: false
created: 2026-04-25
description: Plugin WP custom de réservation v1.0.4 — module booking connecté au PMS
  (en théorie)
embed_hash: null
embed_model_version: null
entities:
- api
- booking
- debugging
- site-wordpress
- wordpress
id: 202604252033-plugin-jt-booking
intent: reference
last-accessed: 2026-04-25
project: site-wordpress
related:
- '[[Site-WordPress]]'
- '[[PMS-Calendar-v2]]'
relevance: high
status: active
summary: Plugin WordPress custom dev par User-Raphael-Distefano|Raphaël. Module de
  réservation pour le site WP de l'hôtel.
tags:
- wordpress
- plugin
- booking
- custom
tier: hot
topic_cluster: wordpress-stack
type: project
updated: 2026-04-25
---

# 🛏️ Plugin jt-booking v1.0.4

## Nature

Plugin WordPress **custom** dev par [[User-Raphael-Distefano|Raphaël]]. Module de réservation pour le site WP de l'hôtel.

## Path

`/var/www/wordpress-instance/data/wordpress/wp-content/plugins/jt-booking-v1.0.4/`

(Le suffixe `-v1.0.4` dans le nom du dossier est inhabituel mais conservé — c'est le slug WP officiel.)

## Architecture

- **N'utilise PAS REST API** WP — préfère admin-post.php / shortcodes / form HTML POST classique
- Cohabite OK avec mu-plugin custom + plugins de cache (page /reservation/ exclue du cache WP-Optimize pour éviter de servir un état périmé)
- Affiche probablement une UI de calendar dispo + form de saisie

## Connexion PMS (théorique)

Idée à wirer : les résas entrantes via jt-booking devraient remonter vers le [[PMS-Calendar-v2|PMS Calendar]] et déclencher email J+1 post-checkout via Brevo.

État réel à valider lors d'une session future.

## Fichiers

```
plugins/jt-booking-v1.0.4/
├── README.md
├── jt-booking.php       # main plugin file (defined ABSPATH check)
├── readme.txt
├── uninstall.php
├── assets/
├── includes/
└── templates/
```

## Liens

- [[Site-WordPress]]
- [[PMS-Calendar-v2]]