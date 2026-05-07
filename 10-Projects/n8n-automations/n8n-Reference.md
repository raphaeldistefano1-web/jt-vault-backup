---
id: 20260507-1126-n8n-ref
type: reference
title: n8n self-hosted — URLs, paths, credentials, commandes
project: n8n
area: null
status: active
confidence: high
summary: URL HTTPS Traefik, paths docker-compose/env/.n8n, owner setup, N8N_API_KEY, PMS HMAC secret, backup restore.
intent: how-to
entities: [n8n, docker, traefik, api-key, hmac, backup]
topic_cluster: n8n
related: ["[[_MOC-n8n]]", "[[n8n-Etat]]"]
moc: "[[_MOC-n8n]]"
source: "memory:reference_n8n.md"
tier: hot
created: 2026-05-07
updated: 2026-05-07
last-accessed: 2026-05-07
embed_model_version: null
embed_hash: null
tags: [n8n, docker, api, reference]
ai_writable: true
---

# n8n self-hosted — URLs, paths, credentials, commandes

> Note portée depuis la mémoire Claude Code `reference_n8n.md` le 2026-05-07.

n8n self-hosted déployé sur le VPS pour orchestrer toute l'automatisation digitale de l'hôtel. Connecté en bidirectionnel au PMS (events sortants + actions entrantes).

**Why:** Référence stable pour les futures sessions — éviter de re-chercher les paths/credentials/commandes à chaque interaction n8n.

## URLs

- **UI publique** : https://n8n-46-202-171-204.nip.io (HTTPS via Traefik + Let's Encrypt)
- **API REST publique** : `https://n8n-46-202-171-204.nip.io/api/v1/` — header `X-N8N-API-KEY`
- **API privée (cookie session)** : `/rest/...` — pour login + admin user mgmt
- **Loopback interne** : http://127.0.0.1:5678 (utilisé par Traefik)

## Owner / login

- Email : `raphael.distefano1@gmail.com`
- Password initial : voir `/docker/n8n/.env` → `N8N_INITIAL_ADMIN_PASSWORD`
- Demander à Raphaël de **changer ce password à la première connexion** (UI → Settings → Personal)

## Paths fichiers

- **Docker compose** : `/docker/n8n/docker-compose.yml`
- **Env (chmod 600)** : `/docker/n8n/.env` — contient tous les secrets (POSTGRES_PASSWORD, N8N_ENCRYPTION_KEY, N8N_API_KEY, PMS_N8N_HMAC_SECRET, owner password)
- **Routage Traefik** : `/docker/traefik/dynamic/n8n.yml`
- **Backup workflows (git)** : `/srv/n8n-workflows/` (workflows/, scripts/, files/)
- **Backup DB** : `/srv/backups/n8n/n8n_<ts>.pgdump` (rotation 30 jours)
- **Cron backup** : `/etc/cron.d/n8n-backup` → script `/srv/n8n-workflows/scripts/backup.sh` à 03h UTC

## Volumes Docker

- `n8n_n8n_data` : `/home/node/.n8n` (config, custom nodes)
- `n8n_n8n_postgres` : `/var/lib/postgresql/data` (DB n8n)
- Bind mount `/srv/n8n-workflows/files` → `/files` (fichiers partagés)

## Containers

- `jt-n8n` : n8n v1.107.4 — port 127.0.0.1:5678
- `jt-n8n-postgres` : Postgres 16-alpine — pas exposé sur host

## Commandes utiles

```bash
# Status
docker ps --filter 'name=n8n'

# Logs
docker logs jt-n8n --tail 50 -f
docker logs jt-n8n-postgres --tail 30

# Restart
cd /docker/n8n && docker compose restart n8n

# Update n8n version
cd /docker/n8n && docker compose pull && docker compose up -d

# Backup manuel
/srv/n8n-workflows/scripts/backup.sh

# Restaurer DB
docker exec -i jt-n8n-postgres pg_restore -U n8n -d n8n --clean --if-exists < /srv/backups/n8n/n8n_<ts>.pgdump

# Pousser vers n8n via API
curl -X POST https://n8n-46-202-171-204.nip.io/api/v1/workflows \
  -H "X-N8N-API-KEY: <key>" -H "Content-Type: application/json" \
  -d @workflow.json
```

## Lien PMS ↔ n8n

- Côté PMS : provider `N8N` à ajouter dans `IntegrationProvider` enum + `PROVIDER_REGISTRY`
- 3 secrets partagés :
  - `N8N_API_KEY` (côté PMS pour appeler API n8n) — JWT 207 chars
  - `PMS_N8N_HMAC_SECRET` (signature des webhooks PMS→n8n et n8n→PMS) — hex 64 chars
  - `N8N_BASE_URL` = https://n8n-46-202-171-204.nip.io
- Webhooks entrants n8n : `POST /api/webhooks/n8n` côté PMS
- Webhooks sortants : depuis le PMS, on POST vers `https://n8n-46-202-171-204.nip.io/webhook/<path>` quand un event hôtel se produit

## Pièges connus (setup 2026-04-25)

- API keys n8n exigent des scopes parmi une liste fixe (`/rest/api-keys/scopes`) — `execution:get` n'existe pas, c'est `execution:read`
- Owner setup possible via `POST /rest/owner/setup` sans auth au premier démarrage (gain de temps vs UI manuel)
- `N8N_PROXY_HOPS=1` requis derrière Traefik sinon redirections cassent
- `extra_hosts: host.docker.internal:host-gateway` permet aux workflows d'appeler le PMS sur le port host (3000)
- Timezone : `GENERIC_TIMEZONE=America/Guadeloupe` ET `TZ=America/Guadeloupe` (les deux nécessaires)

## Liens
- MOC parent : [[_MOC-n8n]]
- État du projet : [[n8n-Etat]]
- Source : `memory:reference_n8n.md`
