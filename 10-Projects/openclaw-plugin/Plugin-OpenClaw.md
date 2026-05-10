---
ai_writable: false
backlinks:
- Dev-PMS-Area
- OpenClaw-VPS-Reference
- PMS
- PMS-AI-Assistant
- PMS-Stack
- VPS-Hostinger
- Workflow-API-Integrations
- _Index
- _MOC-openclaw
created: 2026-04-25
description: Plugin OpenClaw du PMS — IA assistant, Feature 1 OAuth Codex livrée,
  Feature 2 routines reportée
embed_hash: null
embed_model_version: null
entities:
- authentication
- dashboard
- oauth
- pms
id: 202604252031-plugin-openclaw
intent: reference
last-accessed: 2026-04-25
project: openclaw-plugin
related:
- '[[PMS-AI-Assistant]]'
- '[[OpenClaw-VPS-Reference]]'
- '[[Bug-OpenClaw-Plugin-Sandbox]]'
relevance: high
status: partial
summary: Plugin IA du PMS — Feature 1 OAuth Codex livrée sur /dashboard/ai, Feature
  2 routines en attente.
tags:
- pms
- plugin
- ia
- openclaw
tier: warm
topic_cluster: openclaw-integration
type: project
updated: 2026-04-25
---

# 🔌 Plugin OpenClaw PMS

## État (avril 2026)

- ✅ **Feature 1** — OAuth Codex livrée, exposée sur `/dashboard/ai` du PMS
- ⏳ **Feature 2** — routines IA, **reportée** (date à déterminer)

Cf. mémoire `project_openclaw_plugin.md`.

## Architecture

- **Plugin OpenClaw** intégré au PMS (npm package)
- **Routing IA** via `/v1/chat/completions` du **Gateway OpenClaw**
- **Gateway** : loopback `:18789` sur le VPS (cf. [[OpenClaw-VPS-Reference]])

## Composantes

- OAuth Codex pour authentification user → IA (token cohérent, pas re-login)
- Auth profiles paths
- Systemd service avec ExecStart node NVM (fix appliqué)

## Pièges dev

[[Bug-OpenClaw-Plugin-Sandbox]] :
- ⚠️ **Pas openclaw en devDeps** (à mettre dans deps prod)
- Redeploy via `cp dist` (pas via npm publish)
- Prisma migrate via fichier `.sql` + deploy (pas migrate dev)

## Liens

- [[PMS-AI-Assistant]]
- [[OpenClaw-VPS-Reference]]
- Mémoire référence : `project_openclaw_plugin.md` + `reference_openclaw_vps.md`