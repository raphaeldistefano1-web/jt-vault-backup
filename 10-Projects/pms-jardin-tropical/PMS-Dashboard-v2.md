---
type: project
status: completed
tags: [pms, ui, dashboard, v2]
created: 2026-04-25
updated: 2026-04-25
relevance: medium
description: "Dashboard v2 du PMS — appliqué prod après preview-then-apply, refonte centralisée"
ai_writable: false
related:
  - "[[Dev-PMS-Area]]"
  - "[[Workflow-Preview-Then-Apply]]"
  - "[[PMS-Calendar-v2]]"
  - "[[PMS-Settings-Hub]]"
id: 202604252030-pms-dashboard-v2
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: "✅ Appliqué prod cf. mémoire projectpmsstate.md."
entities: [calendar, dashboard, pms]
topic_cluster: pms-stack
intent: reference
tier: hot
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
