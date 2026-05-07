---
type: project
status: active
tags: [pms, ia, assistant, openclaw]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "Assistant IA du PMS — fusion Mémoire IA + Assistant IA, alimenté par OpenClaw plugin"
ai_writable: false
related:
  - "[[Dev-PMS-Area]]"
  - "[[Plugin-OpenClaw]]"
  - "[[PMS-Settings-Hub]]"
  - "[[OpenClaw-VPS-Reference]]"
id: 202604252031-pms-ai-assistant
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: "✅ Fusion Mémoire IA + Assistant IA appliquée cf. mémoire projectpmsstate.md."
entities: [authentication, dashboard, oauth, pms]
topic_cluster: pms-stack
intent: reference
tier: hot
---

# 🤖 PMS AI Assistant

## État

✅ **Fusion Mémoire IA + Assistant IA** appliquée (cf. mémoire `project_pms_state.md`).

## Architecture

- **Frontend** : interface chat dans `/dashboard/ai`
- **Backend** : routing IA via `/v1/chat/completions` du **Gateway OpenClaw** (loopback `:18789`)
- **Plugin** : [[Plugin-OpenClaw]] Feature 1 (OAuth Codex) livrée

## Fonctionnalités

- Chat avec assistant pour aider aux tâches PMS
- Mémoire conversation persistante par user
- Accès aux données du PMS (résas, clients, ops) pour répondre contextuellement
- (Feature 2 : routines IA — reportée)

## Liens

- [[Plugin-OpenClaw]]
- [[OpenClaw-VPS-Reference]]
- [[Dev-PMS-Area]]
