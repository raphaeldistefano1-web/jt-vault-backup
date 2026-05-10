---
ai_writable: false
area: null
backlinks:
- Brainstorm-PMS-Ameliorations-2026-04-25
- Test-jt-booking-PMS-2026-04-25
- Tests-PMS-Batterie-2026-04-25
- n8n-Etat
confidence: medium
created: '2026-05-10'
embed_hash: null
embed_model_version: null
entities:
- HBook
- Le Jardin Tropical
- réservations
id: 20260510040342-accès-données-hbook-source-unique-de-vérité
intent: gotcha
last-accessed: '2026-05-10'
moc: null
project: null
related:
- Brainstorm-PMS-Ameliorations-2026-04-25
- Tests-PMS-Batterie-2026-04-25
- _Index
- n8n-Reference
- Test-jt-booking-PMS-2026-04-25
schema_version: 1
source_notes:
- 10-Projects/pms-jardin-tropical/2026-05-09-1524-session-b53ba567.md
- 10-Projects/pms-jardin-tropical/2026-05-09-1506-session-b53ba567.md
- 10-Projects/pms-jardin-tropical/2026-05-09-1522-session-b53ba567.md
- 10-Projects/pms-jardin-tropical/2026-05-09-1516-session-b53ba567.md
source_session: b53ba567-cec1-4390-a306-dc625e77c91e
status: active
summary: Analyser réservations sans accès direct API HBook risque inexactitude; mémoire
  Claude peut être stale ou partielle.
tags:
- permanent
- synthesized
- data-integrity
- pms
- analytics
tier: warm
title: Accès données HBook — source unique de vérité
topic_cluster: pms-data-sources
type: permanent-note
updated: '2026-05-10'
---

**Piège détecté** : quand Raphaël demande une analyse de taux d'occupation basée sur HBook, accéder directement à l'API ou BDD HBook plutôt que s'appuyer sur des données synthétisées en mémoire.

Le doute exprimé (« tu es sur de tout les chiffres ? ca me parrait pas grand chose ») indique que l'analyse fournie était soit incomplète, soit basée sur des données périmées.

**Pourquoi** : Les réservations changent en temps réel, les annulations/modifications ne sont pas reflétées dans la mémoire, et les analyses financières exigent de la précision.

**Appliquer** : avant toute analyse métier (taux, financière, statistique) sur le PMS, vérifier qu'on a accès aux vraies sources (API HBook, exports BDD) et décider si on peut vraiment analyser ou juste montrer ce qu'on a.

## Related

- [[Brainstorm-PMS-Ameliorations-2026-04-25]] — Brainstorm PMS Ameliorations 2026 04 25
- [[Tests-PMS-Batterie-2026-04-25]] — Tests PMS Batterie 2026 04 25
- [[_Index]] — Index — pms-jardin-tropical
- [[n8n-Reference]] — n8n self-hosted — URLs, paths, credentials, commandes
- [[Test-jt-booking-PMS-2026-04-25]] — Test jt booking PMS 2026 04 25