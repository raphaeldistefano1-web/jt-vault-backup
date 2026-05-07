---
id: 20260507-1102-moc-site-wp
type: moc
title: "MOC Site WordPress — lejardintropical"
project: site-wordpress
area: null
status: active
confidence: high
summary: "Hub pour le site vitrine WordPress lejardintropical.com et son écosystème (theme, mu-plugins, booking)."
intent: reference
entities: [wordpress, lejardintropical, jt-booking, theme-child, mu-plugins, hbook]
topic_cluster: web-marketing
related: ["[[Site-WordPress-Optimisation-2026-04-25]]", "[[Theme-jardintropical-child]]", "[[Plugin-jt-booking]]"]
moc: "[[INDEX]]"
source: null
tier: hot
created: 2026-05-07
updated: 2026-05-07
last-accessed: 2026-05-07
embed_model_version: null
embed_hash: null
tags: [wordpress, web, moc]
ai_writable: false
---

# 🌐 MOC — Site WordPress

> Hub pour le site vitrine **lejardintropical.com** : theme custom, mu-plugins, plugin booking, optimisations.

## Notes du projet

### Stack & architecture
- [[Site-Plugins-Stack-2026-04-25]] — Stack plugins après audit
- [[Theme-jardintropical-child]] — Theme custom enfant
- [[Mu-plugin-jt-seo-extras]] — MU-plugin SEO (vs RankMath)

### Plugins custom
- [[Plugin-jt-booking]] — Plugin booking interne ↔ PMS

### Optimisations
- [[Site-WordPress-Optimisation-2026-04-25]] — 3 phases optim 2026-04-25
- [[Test-jt-booking-PMS-2026-04-25]] — Test connexion booking ↔ PMS

### Migration
- Voir [[_MOC-jt-migrate]]

## Décisions liées
- [[Decision-Mu-plugin-vs-RankMath]]
- [[Decision-Akismet-vers-Antispam-Bee]]
- [[Decision-Disable-WP-Cron-cron-Linux]]
- [[Decision-Robots-txt-LLM-Aware]]
- [[Decision-Redis-Object-Cache-Disabled]]

## Bugs résolus
- [[Bug-WP-Image-Encoding-Accent]]
- [[Bug-WP-Link-Blog-404]]
- [[Bug-Apache-Timeout-300-vs-Uploads]]
- [[Bug-Redis-WPO-Advanced-Cache-Conflict]]
