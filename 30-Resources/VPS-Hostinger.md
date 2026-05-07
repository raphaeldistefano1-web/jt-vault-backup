---
type: resource
status: active
tags: [vps, infra, hostinger]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "VPS Hostinger 46.202.171.204 — host pour PMS + Site WP + Vault + Traefik"
ai_writable: false
related:
  - "[[Stack-Tech]]"
  - "[[Site-WordPress]]"
  - "[[Dev-PMS-Area]]"
  - "[[Vault-Setup]]"
aliases: [VPS]
id: 202604252031-vps-hostinger
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: "VPS Hostinger host — WordPress Docker, PMS Next.js, OpenClaw Gateway, Vault Obsidian, Traefik reverse proxy."
entities: [docker, nextjs, obsidian, pms, postgres, site-wordpress, wordpress]
topic_cluster: infrastructure
intent: reference
tier: warm
---

# 🖥️ VPS Hostinger

## Specs

- **IP** : 46.202.171.204
- **OS** : Linux (Debian-based)
- **Disque** : 96 GB (~22% utilisé en avril 2026)
- **RAM** : 7.7 GB

## Services hébergés

- [[Site-WordPress]] — Docker stack `/var/www/wordpress-instance/`
- [[PMS-Stack]] — `/var/www/pms-jardin-tropical/` (Next.js + Postgres)
- [[Plugin-OpenClaw|OpenClaw Gateway]] — service systemd loopback `:18789`
- [[Vault-Setup|Vault Obsidian]] — `/srv/vault-jardin-tropical/`
- **Traefik** — `/docker/traefik/` (reverse proxy + Let's Encrypt)

## Domaines provisoires

- `wp-46-202-171-204.nip.io` → site WP
- `pms-46-202-171-204.nip.io` → PMS

À migrer vers `lejardintropical.fr` (cf. todo).

## Backups

- Hostinger panel : à activer (cf. todo)
- WP : UpdraftPlus (à configurer destination)
- PMS : pg_dump cron quotidien (à vérifier)
- Vault : git push (à pusher vers GitHub privé)

## Accès

- SSH root + clé (cf. credentials path `/root/.ssh/`)
- Credentials sensibles : `/root/.jt-credentials/`

## Liens

- [[Stack-Tech]]
- [[Site-WordPress]]
- [[Dev-PMS-Area]]
