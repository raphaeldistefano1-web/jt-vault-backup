---
ai_writable: false
backlinks:
- 2026-05-10-signaler-impacts-jt-booking-avant-clôture-tâche-wp
- Dev-PMS-Area
- PMS-Dashboard-v2
- Plugin-jt-booking
- Workflow-Cross-Feature-Coherence
- Workflow-Preview-Then-Apply
- _Index
- _MOC-pms
created: 2026-04-25
description: Calendar v2 du PMS — vue calendrier centralisée pour gestion réservations,
  appliqué prod
embed_hash: null
embed_model_version: null
entities:
- calendar
- dashboard
- pms
- rag
id: 202604252030-pms-calendar-v2
intent: reference
last-accessed: 2026-04-25
project: pms-jardin-tropical
related:
- 2026-05-10-signaler-impacts-jt-booking-avant-clôture-tâche-wp
- '[[Dev-PMS-Area]]'
- '[[PMS-Dashboard-v2]]'
- '[[Plugin-jt-booking]]'
- '[[Workflow-Cross-Feature-Coherence]]'
- '[[Workflow-Preview-Then-Apply]]'
relevance: medium
status: completed
summary: ✅ Appliqué prod cf. mémoire projectpmsstate.md.
tags:
- pms
- ui
- calendar
- v2
tier: hot
topic_cluster: pms-stack
type: project
updated: 2026-04-25
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

## Related

- [[2026-05-10-signaler-impacts-jt-booking-avant-clôture-tâche-wp]] — Signaler impacts jt-booking avant clôture tâche WP