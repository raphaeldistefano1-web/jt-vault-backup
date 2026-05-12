---
ai_writable: false
area: null
backlinks:
- 2026-05-09-bug-synthesizer-omet-la-section-signaux-feedback-d
- 2026-05-10-retrouver-contexte-perdu-via-jsonl-logs-claude-cod
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- extract_memory
- transcript_path
- session-logging
- deduplication
id: 20260512040149-architecture-du-hook-extract-memory-capture-du-tra
intent: decision
last-accessed: '2026-05-12'
moc: null
project: null
related:
- 2026-05-10-retrouver-contexte-perdu-via-jsonl-logs-claude-cod
- 2026-05-09-bug-synthesizer-omet-la-section-signaux-feedback-d
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-12-0112-session-af662ef1.md
- 10-Projects/claude-system/2026-05-12-0127-session-af662ef1.md
- 10-Projects/jt-migrate/2026-05-12-0108-session-af662ef1.md
- 10-Projects/jt-migrate/2026-05-12-0054-session-af662ef1.md
- 10-Projects/jt-migrate/2026-05-12-0104-session-af662ef1.md
- 10-Projects/jt-migrate/2026-05-12-0110-session-af662ef1.md
- 10-Projects/jt-migrate/2026-05-12-0051-session-af662ef1.md
- 10-Projects/jt-migrate/2026-05-12-0106-session-af662ef1.md
- 10-Projects/jt-migrate/2026-05-12-0056-session-af662ef1.md
source_session: af662ef1-632e-46c8-ab2b-93c93f14ca24
status: active
summary: Hook extract_memory parcourt le transcript complet sans mécanisme natif de
  dedup ou de validation des références capturées.
tags:
- permanent
- synthesized
- hooks
- logging
- architecture
- transcript
tier: cold
title: 'Architecture du hook extract_memory : capture du transcript et fin de session'
topic_cluster: system-architecture
type: permanent-note
updated: '2026-05-12'
---

La session soulève deux questions : (1) Y a-t-il un hook de logs qui trie automatiquement les notes générées ?, (2) Comment le système sait quand c'est la fin de la session ? Cela révèle que le hook fonctionne sur un fichier `.jsonl` complet (transcript_path) et cherche les mentions de wikilinks, décisions, artifacts. Actuellement pas de filtrage natif des mentions erronées (celles mentionnées accidentellement en parlant). La fin de session est probablement détectée via un sentinel explicite (ex: `# Bilan`) ou l'archivage du fichier transcript, pas en temps réel. Implication architecturale : la validation et la deduplication des stubs doivent être externalisées (manuel ou via script post-extraction). À clarifier : le hook s'exécute-t-il immédiatement après la session ou sur un cron timer (ex: 00:00 daily) ?

## Related

- [[2026-05-10-retrouver-contexte-perdu-via-jsonl-logs-claude-cod]] — Retrouver contexte perdu via JSONL logs Claude Code
- [[2026-05-09-bug-synthesizer-omet-la-section-signaux-feedback-d]] — Bug : synthesizer omet la section Signaux feedback détectés