---
type: project
status: completed
tags: [pms, ui, calendar, v2]
created: 2026-04-25
updated: 2026-04-25
relevance: medium
description: "Calendar v2 du PMS — vue calendrier centralisée pour gestion réservations, appliqué prod"
ai_writable: false
related:
  - "[[Dev-PMS-Area]]"
  - "[[Workflow-Preview-Then-Apply]]"
  - "[[PMS-Dashboard-v2]]"
  - "[[Plugin-jt-booking]]"
  - "[[Workflow-Cross-Feature-Coherence]]"
id: 202604252030-pms-calendar-v2
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: "✅ Appliqué prod cf. mémoire projectpmsstate.md."
entities: [calendar, dashboard, pms, rag]
topic_cluster: pms-stack
intent: reference
tier: hot
---

# 📅 PMS Calendar v2

## État

✅ **Appliqué prod** (cf. mémoire `project_pms_state.md`).

## Composantes

- Vue calendrier des réservations (mensuelle, hebdo, jour)
- **Slide-panel** latéral pour détail résa (composant partagé avec frontdesk)
- Drag-and-drop pour déplacer une résa
- Filtres : statut, hébergement, source

## Cohérence cross-feature

Selon [[Workflow-Cross-Feature-Coherence]], toute modif d'une résa via le Slide-Panel doit cascader :
- Frontdesk
- Détail résa
- Dashboard occupation

## Lien avec [[Plugin-jt-booking]]

Les réservations entrantes via le plugin WP `jt-booking` doivent (en théorie) remonter vers le PMS Calendar. État de connexion à vérifier (todo : connecter PMS ↔ jt-booking, email J+1 via Brevo).

## Liens

- [[PMS-Dashboard-v2]]
- [[Plugin-jt-booking]]
- [[Workflow-Cross-Feature-Coherence]]
