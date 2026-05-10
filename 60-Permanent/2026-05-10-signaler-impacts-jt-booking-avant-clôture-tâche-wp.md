---
ai_writable: false
area: null
backlinks:
- 2026-05-09-synchronisation-manuelle-fragile-entre-instances-w
- PMS-Calendar-v2
- Plugin-jt-booking
- Test-jt-booking-PMS-2026-04-25
confidence: medium
created: '2026-05-10'
embed_hash: null
embed_model_version: null
entities:
- jt-booking
- hbook
- wordpress
id: 20260510040716-signaler-impacts-jt-booking-avant-clôture-tâche-wp
intent: lesson
last-accessed: '2026-05-10'
moc: null
project: null
related:
- Plugin-jt-booking
- Test-jt-booking-PMS-2026-04-25
- PMS-Calendar-v2
- _Index
- 2026-05-09-synchronisation-manuelle-fragile-entre-instances-w
schema_version: 1
source_notes:
- 10-Projects/site-wordpress/2026-05-09-1608-session-0375ba09.md
source_session: 0375ba09-478d-4743-8890-c82a03938fb1
status: active
summary: Avant clôturer tâche WP modifiant tarifs, signaler explicitement impact jt-booking.
tags:
- permanent
- synthesized
- integration
- booking-system
- workflow
tier: warm
title: Signaler impacts jt-booking avant clôture tâche WP
topic_cluster: wp-integration
type: permanent-note
updated: '2026-05-10'
---

Quand une session WP modifie tarifs hébergements (bungalow-junior, bungalows, villa-*), cela impacte potentiellement jt-booking/HBook. Bien que pages soient source de vérité WP, **signaler explicitement** avant fin de tâche que changements jt-booking sont peut-être requis, plutôt que les appliquer silencieusement. Prévient écarts WP↔booking et donne visibilité user sur décisions à prendre côté booking system.

## Related

- [[Plugin-jt-booking]] — Plugin jt booking
- [[Test-jt-booking-PMS-2026-04-25]] — Test jt booking PMS 2026 04 25
- [[PMS-Calendar-v2]] — PMS Calendar v2
- [[_Index]] — Index — site-wordpress
- [[2026-05-09-synchronisation-manuelle-fragile-entre-instances-w]] — Synchronisation manuelle fragile entre instances WordPress