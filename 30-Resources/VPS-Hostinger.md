---
ai_writable: false
aliases:
- VPS
backlinks:
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
- 2026-05-12-accès-vps-culsec-via-tailscale-ssh-alias-monvpsvps
- 2026-05-12-chemins-daccumulation-disque-connus-docker-node-mo
- 2026-05-12-cpu-throttling-vps-hostinger-monitoring-via-sar
- Bug-Apache-Timeout-300-vs-Uploads
- Email-Infra
- OpenClaw-VPS-Reference
- PMS-Stack
- User-Raphael-Distefano
created: 2026-04-25
description: VPS Hostinger 46.202.171.204 — host pour PMS + Site WP + Vault + Traefik
embed_hash: null
embed_model_version: null
entities:
- docker
- nextjs
- obsidian
- pms
- postgres
- site-wordpress
- wordpress
id: 202604252031-vps-hostinger
intent: reference
last-accessed: 2026-04-25
related:
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
- 2026-05-12-chemins-daccumulation-disque-connus-docker-node-mo
- 2026-05-12-cpu-throttling-vps-hostinger-monitoring-via-sar
- VPS-Access-Tailscale
- '[[Dev-PMS-Area]]'
- '[[Site-WordPress]]'
- '[[Stack-Tech]]'
- '[[Vault-Setup]]'
relevance: high
status: active
summary: VPS Hostinger host — WordPress Docker, PMS Next.js, OpenClaw Gateway, Vault
  Obsidian, Traefik reverse proxy.
tags:
- vps
- infra
- hostinger
tier: warm
topic_cluster: infrastructure
type: resource
updated: 2026-04-25
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

## Related

- [[VPS-Access-Tailscale]] — Accès VPS via Tailscale (depuis 2026-05-06)
- [[2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms]] — Path `/var/www/culsec/` — homogénéité infra VPS avec PMS
- [[2026-05-12-cpu-throttling-vps-hostinger-monitoring-via-sar]] — CPU throttling VPS Hostinger — monitoring via sar
- [[2026-05-12-chemins-daccumulation-disque-connus-docker-node-mo]] — Chemins d'accumulation disque connus: Docker, node_modules, logs