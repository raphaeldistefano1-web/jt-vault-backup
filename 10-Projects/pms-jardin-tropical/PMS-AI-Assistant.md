---
ai_writable: false
backlinks:
- Dev-PMS-Area
- PMS-Dashboard-v2
- PMS-Settings-Hub
- Plugin-OpenClaw
- _Index
- _MOC-pms
created: 2026-04-25
description: Assistant IA du PMS — fusion Mémoire IA + Assistant IA, alimenté par
  OpenClaw plugin
embed_hash: null
embed_model_version: null
entities:
- authentication
- dashboard
- oauth
- pms
id: 202604252031-pms-ai-assistant
intent: reference
last-accessed: 2026-04-25
project: pms-jardin-tropical
related:
- '[[Dev-PMS-Area]]'
- '[[Plugin-OpenClaw]]'
- '[[PMS-Settings-Hub]]'
- '[[OpenClaw-VPS-Reference]]'
relevance: high
status: active
summary: ✅ Fusion Mémoire IA + Assistant IA appliquée cf. mémoire projectpmsstate.md.
tags:
- pms
- ia
- assistant
- openclaw
tier: hot
topic_cluster: pms-stack
type: project
updated: 2026-04-25
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