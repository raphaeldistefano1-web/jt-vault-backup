---
ai_writable: false
backlinks:
- Dev-PMS-Area
- PMS-Calendar-v2
- Workflow-Preview-Then-Apply
- _Index
- _MOC-pms
- _VAULT-INDEX
created: 2026-04-25
description: Dashboard v2 du PMS — appliqué prod après preview-then-apply, refonte
  centralisée
embed_hash: null
embed_model_version: null
entities:
- calendar
- dashboard
- pms
id: 202604252030-pms-dashboard-v2
intent: reference
last-accessed: 2026-04-25
project: pms-jardin-tropical
related:
- '[[Dev-PMS-Area]]'
- '[[Workflow-Preview-Then-Apply]]'
- '[[PMS-Calendar-v2]]'
- '[[PMS-Settings-Hub]]'
relevance: medium
status: completed
summary: ✅ Appliqué prod cf. mémoire projectpmsstate.md.
tags:
- pms
- ui
- dashboard
- v2
tier: hot
topic_cluster: pms-stack
type: project
updated: 2026-04-25
---

# 📊 PMS Dashboard v2

## État

✅ **Appliqué prod** (cf. mémoire `project_pms_state.md`).

## Workflow

Refonte UI majeure → passé par [[Workflow-Preview-Then-Apply|route _v2 prévisualisable]] avant validation par [[User-Raphael-Distefano|Raphaël]] et bascule prod.

## Composantes

- Vue centrale du PMS, premier écran après login admin
- Centralise : occupation jour / semaine, alertes, prochaines arrivées/départs, KPIs business
- Lie vers [[PMS-Calendar-v2]] (Slide-Panel) et [[PMS-Settings-Hub]]

## Liens

- [[Dev-PMS-Area]]
- [[PMS-Calendar-v2]]
- [[PMS-AI-Assistant]]