---
type: project
status: completed
tags: [pms, settings, ui]
created: 2026-04-25
updated: 2026-04-25
relevance: medium
description: "Hub central des paramètres PMS — consolidation de tous les settings dispersés en un point d'entrée"
ai_writable: false
related:
  - "[[Dev-PMS-Area]]"
  - "[[Workflow-API-Integrations]]"
  - "[[PMS-AI-Assistant]]"
id: 202604252030-pms-settings-hub
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: "✅ Consolidé cf. mémoire projectpmsstate.md. Tous les paramètres précédemment dispersés sont maintenant accessibles depui…"
entities: [api, brevo, dashboard, pms]
topic_cluster: pms-stack
intent: reference
tier: hot
---

# ⚙️ PMS Settings Hub

## État

✅ **Consolidé** (cf. mémoire `project_pms_state.md`). Tous les paramètres précédemment dispersés sont maintenant accessibles depuis un point d'entrée unique.

## Structure

- `/dashboard/settings` = hub central
- Sections :
  - **Hôtel** : infos générales, capacité, équipements
  - **Hébergements** : liste bungalows / villas, tarifs par saison
  - **Intégrations** : clés API ([[Workflow-API-Integrations|via UI obligatoirement]])
  - **Email** : Brevo, signatures, templates
  - **Utilisateurs & permissions**
  - **IA** : config [[PMS-AI-Assistant]]

## Décision design

[[User-Raphael-Distefano|Raphaël]] préférait avoir 1 seule URL bookmarkable plutôt que d'avoir à fouiller. Cf. patterns Settings de Notion / Linear.

## Liens

- [[Dev-PMS-Area]]
- [[Workflow-API-Integrations]]
- [[PMS-AI-Assistant]]
