---
ai_writable: false
backlinks:
- 2026-05-11-état-global-zustand-hook-usegamesession-pour-logiq
- Dev-PMS-Area
- PMS
- PMS-AI-Assistant
- PMS-Dashboard-v2
- Workflow-API-Integrations
- Workflow-Preview-Then-Apply
- _Index
- _MOC-pms
- _STUBS-A-ARBITRER-2026-05-12
created: 2026-04-25
description: Hub central des paramètres PMS — consolidation de tous les settings dispersés
  en un point d'entrée
embed_hash: null
embed_model_version: null
entities:
- api
- brevo
- dashboard
- pms
id: 202604252030-pms-settings-hub
intent: reference
last-accessed: 2026-04-25
project: pms-jardin-tropical
related:
- 2026-05-11-état-global-zustand-hook-usegamesession-pour-logiq
- '[[Dev-PMS-Area]]'
- '[[PMS-AI-Assistant]]'
- '[[Workflow-API-Integrations]]'
relevance: medium
status: completed
summary: ✅ Consolidé cf. mémoire projectpmsstate.md. Tous les paramètres précédemment
  dispersés sont maintenant accessibles depui…
tags:
- pms
- settings
- ui
tier: hot
topic_cluster: pms-stack
type: project
updated: 2026-04-25
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

## Related

- [[2026-05-11-état-global-zustand-hook-usegamesession-pour-logiq]] — État global Zustand + hook useGameSession pour logique jeu