---
ai_writable: false
area: null
backlinks:
- 2026-05-08-décision-canonicitymd-pour-déduplication-vaultmémo
- 2026-05-09-anti-pattern-redonder-info-du-contexte-injecté
- 2026-05-09-hiérarchie-persistance-mémoire-vs-vault-vs-todo
- 2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo
- CANONICITY
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- MEMORY.md
- memory files
- Git
id: 20260512040449-mémoire-claude-accumule-sans-archivage-audit-pério
intent: lesson
last-accessed: '2026-05-12'
moc: null
project: null
related:
- 2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo
- 2026-05-09-anti-pattern-redonder-info-du-contexte-injecté
- CANONICITY
- 2026-05-09-hiérarchie-persistance-mémoire-vs-vault-vs-todo
- 2026-05-08-décision-canonicitymd-pour-déduplication-vaultmémo
schema_version: 1
source_notes:
- 10-Projects/jt-migrate/2026-05-11-2118-session-8bb149e5.md
- 10-Projects/jt-migrate/2026-05-11-2122-session-8bb149e5.md
- 10-Projects/pms-jardin-tropical/2026-05-11-2109-session-8bb149e5.md
- 10-Projects/pms-jardin-tropical/2026-05-11-2059-session-8bb149e5.md
source_session: 8bb149e5-9777-4d3a-88e6-d87fb5848961
status: active
summary: Les fichiers mémoire Claude s'accumulent progressivement; sans archivage
  actif, ils dégradent la perf et la clarté du système
tags:
- permanent
- synthesized
- data-management
- scaling
- operations
tier: warm
title: Mémoire Claude accumule sans archivage — audit périodique requis
topic_cluster: claude-memory-management
type: permanent-note
updated: '2026-05-12'
---

Observation de session: Raphaël a découvert qu'une accumulation de mémoire/stockage (« trop de giga ») rendait le système difficile à naviguer et probablement à charger. 

La mémoire Claude n'a pas de TTL natif — les notes perdurent tant qu'elles existent dans le fichier. À long terme (>3 mois), un MEMORY.md avec >30 fichiers cause:
- Lenteur au chargement (toutes les notes en contexte)
- Bruit cognitif (trop de refs pour retrouver l'info pertinente)
- Stagnation de notes devenues obsolètes

Stratégie: **archivage semi-annuel**. Chaque 6 mois, trier MEMORY.md en deux catégories:
1. **Hot** (< 3 mois, utilisée régulièrement): rester en MEMORY.md
2. **Warm/Cold** (> 3 mois, rarement consulté): mover vers `memory/archive/` + créer une note index `MEMORY-ARCHIVE.md`

Version minimale: juste avant un big refactor du projet, faire le tri.

## Related

- [[2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo]] — Trier items capturés : hot (immédiat) vs warm/cold (mémoire)
- [[2026-05-09-anti-pattern-redonder-info-du-contexte-injecté]] — Anti-pattern : redonder info du contexte injecté
- [[CANONICITY]] — Canonicité vault ↔ mémoire Claude Code
- [[2026-05-09-hiérarchie-persistance-mémoire-vs-vault-vs-todo]] — Hiérarchie persistance : Mémoire vs Vault vs Todo
- [[2026-05-08-décision-canonicitymd-pour-déduplication-vaultmémo]] — Décision — CANONICITY.md pour déduplication vault↔mémoires CC