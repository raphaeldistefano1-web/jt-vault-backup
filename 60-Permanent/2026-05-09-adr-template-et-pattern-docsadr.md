---
ai_writable: false
area: null
backlinks:
- 2026-05-09-3-régimes-dintégration-plugin-distincts
- 2026-05-10-registry-pattern-centralisateur-jeux-modulaires
confidence: medium
created: '2026-05-09'
embed_hash: null
embed_model_version: null
entities:
- ADR
- docs/adr/
- RFC 5242
id: 20260509040128-adr-template-et-pattern-docsadr
intent: pattern
last-accessed: '2026-05-09'
moc: null
project: null
related:
- 2026-05-08-décision-canonicitymd-pour-déduplication-vaultmémo
- 2026-05-09-3-régimes-dintégration-plugin-distincts
- 2026-05-09-hiérarchie-persistance-mémoire-vs-vault-vs-todo
- 2026-05-10-architecture-decision-records-template-structure
- 2026-05-10-registry-pattern-centralisateur-jeux-modulaires
- AGENTS
- note-schema
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-08-1442-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1802-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1721-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1459-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1649-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1605-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1613-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1452-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1444-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1433-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1604-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1828-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1449-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1651-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1440-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1616-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1822-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1454-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1622-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1619-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1437-session-21c4cfc3.md
- 10-Projects/claude-system/2026-05-08-1656-session-21c4cfc3.md
- 10-Projects/pms-jardin-tropical/2026-05-08-1625-session-21c4cfc3.md
source_session: 21c4cfc3-93d1-4d4d-9bab-ab7b63ed0c6a
status: active
summary: 'Template ADR créé à docs/adr/0000-template.md, structure RFC 5242 standard
  : titre + date + status + context + decision + consequences.'
tags:
- permanent
- synthesized
- architecture-decisions
- documentation-pattern
tier: warm
title: ADR template et pattern docs/adr/
topic_cluster: documentation
type: permanent-note
updated: '2026-05-09'
---

Structure :
```
# ADR NNNN: <titre>
Date: YYYY-MM-DD
Status: proposed | accepted | superseded
Context: ...
Decision: ...
Consequences: ...
Alternatives considered: ...
```

**Usage** : chaque décision archi stratégique (tech stack, patterns, migrations) → une ADR horodatée, searchable, versionnable.

**Retour** : zéro coût quota, ROI énorme à long terme. Audit trail complet, évite redécisions, désolidarise du CLAUDE.md qui devient volatile.

Référence : Nat Pryce/Michael Nygard (ThoughtWorks), popularisée par 7tonshark.

## Related

- [[2026-05-09-3-régimes-dintégration-plugin-distincts]] — 3 régimes d'intégration plugin distincts
- [[note-schema]] — note schema
- [[2026-05-09-hiérarchie-persistance-mémoire-vs-vault-vs-todo]] — Hiérarchie persistance : Mémoire vs Vault vs Todo
- [[AGENTS]] — AGENTS
- [[2026-05-08-décision-canonicitymd-pour-déduplication-vaultmémo]] — Décision — CANONICITY.md pour déduplication vault↔mémoires CC
- [[2026-05-10-registry-pattern-centralisateur-jeux-modulaires]] — Registry pattern — centralisateur jeux modulaires
- [[2026-05-10-architecture-decision-records-template-structure]] — Architecture Decision Records template structure