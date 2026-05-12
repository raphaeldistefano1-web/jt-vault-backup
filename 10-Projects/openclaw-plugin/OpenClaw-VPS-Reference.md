---
ai_writable: true
area: null
backlinks:
- 2026-05-12-accès-vps-culsec-via-tailscale-ssh-alias-monvpsvps
- 2026-05-12-mcp-reconnect-workflow-mcp-oauth-browser
- Bug-OpenClaw-Plugin-Sandbox
- Lesson-Server-to-Server-curl-bypass-user
- OpenClaw-Etat
- OpenClaw-Pieges-Dev
- PMS-AI-Assistant
- PMS-Desktop-Reference
- PMS-Stack
- Plugin-OpenClaw
- _Index
- n8n-Reference
confidence: high
created: 2026-05-07
embed_hash: null
embed_model_version: null
entities:
- openclaw
- gateway
- vps
- paths
- systemd
- oauth-codex
id: 20260507-1118-openclaw-vps-ref
intent: how-to
last-accessed: 2026-05-07
moc: '[[_MOC-openclaw]]'
project: openclaw
related:
- 2026-05-12-accès-vps-culsec-via-tailscale-ssh-alias-monvpsvps
- 2026-05-12-mcp-reconnect-workflow-mcp-oauth-browser
- OpenClaw-VPS-Reference
- VPS-Access-Tailscale
- '[[OpenClaw-Etat]]'
- '[[_MOC-openclaw]]'
source: memory:reference_openclaw_vps.md
status: active
summary: Gateway loopback :18789, paths config auth-profiles, fix systemd ExecStart
  NVM, Codex OAuth lib.
tags:
- openclaw
- vps
- gateway
- config
tier: hot
title: OpenClaw sur le VPS — Paths, ports, config
topic_cluster: openclaw
type: reference
updated: 2026-05-07
---

# OpenClaw sur le VPS — Paths, ports, config

> Note portée depuis la mémoire Claude Code `reference_openclaw_vps.md` le 2026-05-07.

OpenClaw v2026.3.24 installé sur le VPS Hostinger qui héberge le PMS.

## Gateway HTTP

- Port : `127.0.0.1:18789` (bind=loopback, mode=local) — non exposé publiquement
- Token d'auth : lu dans `/root/.openclaw/openclaw.json` → `gateway.auth.token` (header `Authorization: Bearer <token>`)
- Côté PMS, ce token est stocké chiffré dans `Integration OPENCLAW` (champ `gatewayToken`)

## Endpoints natifs utiles

- `POST /v1/chat/completions` — façade OpenAI-compat (à activer via `openclaw config set gateway.http.endpoints.chatCompletions.enabled true`). `model: "openclaw"` dispatche vers le compte Codex actif.
- `POST /v1/responses` — variante OpenResponses
- `GET  /v1/models`
- `POST /hooks/wake`, `/hooks/agent`, `/hooks/<name>` — hooks génériques (auth via `hooks.token`)
- `GET  /` — Control UI HTML

## Paths

- Binaire CLI : `/usr/bin/openclaw` (wrapper qui charge `/usr/lib/node_modules/openclaw/dist/index.js`)
- Config principale : `/root/.openclaw/openclaw.json`
- Auth profiles OAuth Codex : `/root/.openclaw/agents/main/agent/auth-profiles.json` (chmod 0600, contient access/refresh tokens en clair)
- Workspace : `/root/.openclaw/workspace/`
- Plugins installés : `/root/.openclaw/extensions/<id>/`
- Logs : `/tmp/openclaw/openclaw-YYYY-MM-DD.log` (verbose JSON par ligne)
- Service systemd user : `~/.config/systemd/user/openclaw-gateway.service`

## Fix systemd appliqué le 2026-04-22

Le service file pointait par défaut vers `/usr/bin/node` (inexistant sur ce VPS — node est en NVM). Patché manuellement :
`ExecStart=/root/.nvm/versions/node/v22.22.2/bin/node /usr/lib/node_modules/openclaw/dist/index.js gateway --port 18789`
→ Ne pas refaire un `openclaw daemon install` aveuglement, ça réécrira le path en `/usr/bin/node` et cassera le service.

## Lib OAuth Codex (modèle pour ré-implémenter)

`@mariozechner/pi-ai` bundlé sous `/usr/lib/node_modules/openclaw/node_modules/@mariozechner/pi-ai/dist/utils/oauth/openai-codex.js` — contient `CLIENT_ID`, `AUTHORIZE_URL`, `TOKEN_URL`, `REDIRECT_URI=http://localhost:1455/auth/callback`, scopes, endpoint exchange. Référence si on doit re-générer un flow OAuth Codex propre.

## Liens
- MOC parent : [[_MOC-openclaw]]
- État du plugin : [[OpenClaw-Etat]]
- Source : `memory:reference_openclaw_vps.md`

## Related

- [[VPS-Access-Tailscale]] — Accès VPS via Tailscale (depuis 2026-05-06)
- [[OpenClaw-VPS-Reference]] — OpenClaw-VPS-Reference
- [[2026-05-12-mcp-reconnect-workflow-mcp-oauth-browser]] — MCP reconnect workflow : /mcp + OAuth browser
- [[2026-05-12-accès-vps-culsec-via-tailscale-ssh-alias-monvpsvps]] — Accès VPS culsec via Tailscale + SSH (alias monvps/vps-pms)