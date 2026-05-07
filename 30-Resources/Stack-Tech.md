---
type: resource
status: active
tags: [infra, stack, credentials]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "Stack technique complète Le Jardin Tropical : VPS, domaines, ports, paths"
ai_writable: false
id: 202604252021-stack-tech
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: "Stack complète VPS — Hostinger 46.202.171.204, Traefik, WordPress Docker, PMS Next.js, OpenClaw, vault."
entities: [docker, pms, site-wordpress, traefik, wordpress]
topic_cluster: infrastructure
intent: reference
tier: warm
---

# 🔧 Stack technique

## VPS principal

- **Hébergeur** : Hostinger
- **IP** : 46.202.171.204
- **OS** : Linux (cf. uname côté VPS)
- **Disque** : 96 GB (~22% utilisé)
- **RAM** : 7.7 GB

## Domaines

| Domaine | Usage | Status |
|---|---|---|
| `lejardintropical.fr` | Domaine final site WP + email pro | À acheter et configurer |
| `wp-46-202-171-204.nip.io` | Site WP provisoire | Actif |
| `pms-46-202-171-204.nip.io` | PMS provisoire | Actif |

## Reverse proxy

- **Traefik** dans `/docker/traefik/`
- Config dynamique : `/docker/traefik/dynamic/` (wordpress.yml, pms.yml)
- Auto Let's Encrypt

## Site WordPress

- Stack : Apache 2.4 + PHP 8.3 + MariaDB 11 (docker compose dans `/var/www/wordpress-instance/`)
- Volumes :
  - `./data/wordpress/` → `/var/www/html` (install WP, wp-content, wp-config.php)
  - `./data/mariadb/` → `/var/lib/mysql`
  - `./config/uploads.ini` → PHP limites 512M
  - `./config/apache-uploads.conf` → Timeout 1800, gzip, cache, blocs sensibles
  - `./config/mariadb-tuning.cnf` → innodb_buffer_pool 256M, warm-up
  - `./config/php-opcache-prod.ini` → OPcache 256M / 20000 files
- Helper CLI : `jt-wp` = `docker exec -u 33 jt-wordpress-cli wp --path=/var/www/html ...`
- Credentials : `/root/.jt-credentials/wordpress-instance.txt` (root only, chmod 600)

## PMS

- Path : `/var/www/pms-jardin-tropical/`
- Port Nginx : 8080
- DB : PostgreSQL local
- Process manager : PM2
- Page partage fichiers : `/uploads` (code 8 chars, public/shares/<CODE>/)

## OpenClaw Gateway (plugin IA PMS)

- Loopback `:18789`
- Path config + auth-profiles : (cf. mémoire `reference_openclaw_vps.md`)

## Email

- **Actuel** : `lejardintropical@orange.fr` (orange.fr, pas DKIM custom possible)
- **Cible** : email pro sur domaine `lejardintropical.fr` chez Infomaniak ou Mailbox.org

## Backup

- Niveau VPS : Hostinger panel (à activer si pas déjà fait)
- Niveau WP : UpdraftPlus (à configurer destination)
- Niveau PMS : pg_dump cron quotidien (à vérifier)

## Domaines email annexes

- Brevo (PMS transactionnel)
- (à compléter)
