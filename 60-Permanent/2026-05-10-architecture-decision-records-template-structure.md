---
ai_writable: false
area: null
backlinks:
- 2026-05-09-3-régimes-dintégration-plugin-distincts
- 2026-05-09-adr-template-et-pattern-docsadr
- Sub-agents-internes-PMS
confidence: medium
created: '2026-05-10'
embed_hash: null
embed_model_version: null
entities:
- ADR
- template
- documentation
id: 20260510040620-architecture-decision-records-template-structure
intent: config
last-accessed: '2026-05-10'
moc: null
project: null
related:
- _MOC-pms
- _Index
- 2026-05-09-3-régimes-dintégration-plugin-distincts
- Sub-agents-internes-PMS
- PMS
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-09-0904-session-21c4cfc3.md
source_session: 21c4cfc3-93d1-4d4d-9bab-ab7b63ed0c6a
status: active
summary: Template ADR standard pour structurer décisions architecturales durables
  (>6 mois d'impact).
tags:
- permanent
- synthesized
- documentation
- template
- architecture
- adr
tier: warm
title: Architecture Decision Records template structure
topic_cluster: documentation-adr
type: permanent-note
updated: '2026-05-10'
---

Template créé à `/var/www/pms-jardin-tropical/docs/adr/0000-template.md`.

Structure :
- **Title** : ADR NNN: <slug>
- **Date** : YYYY-MM-DD
- **Status** : proposed | accepted | superseded by NNN
- **Context** : situation motivant la décision
- **Decision** : choix fait
- **Consequences** : impacts positifs/négatifs
- **Alternatives considered** : autres options évaluées

Zéro overhead, ROI absolue sur traçabilité long terme. Utiliser pour toute décision archi durable.

## Related

- [[_MOC-pms]] — MOC PMS Le Jardin Tropical
- [[_Index]] — Index — pms-jardin-tropical
- [[2026-05-09-3-régimes-dintégration-plugin-distincts]] — 3 régimes d'intégration plugin distincts
- [[Sub-agents-internes-PMS]] — Sub agents internes PMS
- [[PMS]] — PMS