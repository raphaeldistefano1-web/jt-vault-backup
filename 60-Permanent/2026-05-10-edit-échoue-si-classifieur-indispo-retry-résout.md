---
ai_writable: false
area: null
backlinks:
- 2026-05-09-synchronisation-manuelle-fragile-entre-instances-w
- Bug-Redis-WPO-Advanced-Cache-Conflict
- Bug-WP-Link-Blog-404
- Decision-Redis-Object-Cache-Disabled
confidence: medium
created: '2026-05-10'
embed_hash: null
embed_model_version: null
entities:
- wordpress-edit-tool
id: 20260510040715-edit-échoue-si-classifieur-indispo-retry-résout
intent: gotcha
last-accessed: '2026-05-10'
moc: null
project: null
related:
- 2026-05-09-synchronisation-manuelle-fragile-entre-instances-w
- Bug-Redis-WPO-Advanced-Cache-Conflict
- Bug-WP-Link-Blog-404
- _Index
- Decision-Redis-Object-Cache-Disabled
schema_version: 1
source_notes:
- 10-Projects/site-wordpress/2026-05-09-1608-session-0375ba09.md
source_session: 0375ba09-478d-4743-8890-c82a03938fb1
status: active
summary: Outil Edit peut échouer temporairement si classifieur indisponible ; relancer
  résout.
tags:
- permanent
- synthesized
- wordpress
- theming
- troubleshooting
tier: cold
title: Edit échoue si classifieur indispo, retry résout
topic_cluster: wordpress-tooling
type: permanent-note
updated: '2026-05-10'
---

Lors de modifications sur fichiers child theme WordPress, l'outil Edit peut échouer avec message « classifieur indisponible ». Ce n'est pas un blocage permanent : relancer l'opération résout le problème. Indisponibilité temporaire du service de classification interne.

## Related

- [[2026-05-09-synchronisation-manuelle-fragile-entre-instances-w]] — Synchronisation manuelle fragile entre instances WordPress
- [[Bug-Redis-WPO-Advanced-Cache-Conflict]] — Bug Redis WPO Advanced Cache Conflict
- [[Bug-WP-Link-Blog-404]] — Bug WP Link Blog 404
- [[_Index]] — Index — site-wordpress
- [[Decision-Redis-Object-Cache-Disabled]] — Decision Redis Object Cache Disabled