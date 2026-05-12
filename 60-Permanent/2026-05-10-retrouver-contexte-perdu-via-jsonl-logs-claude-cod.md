---
ai_writable: false
area: null
backlinks:
- 2026-05-12-architecture-du-hook-extract-memory-capture-du-tra
- 2026-05-12-mcp-reconnect-workflow-mcp-oauth-browser
confidence: medium
created: '2026-05-10'
embed_hash: null
embed_model_version: null
entities:
- claude-code
- jsonl
- jq
id: 20260510040713-retrouver-contexte-perdu-via-jsonl-logs-claude-cod
intent: pattern
last-accessed: '2026-05-10'
moc: null
project: null
related:
- 2026-05-12-architecture-du-hook-extract-memory-capture-du-tra
schema_version: 1
source_notes:
- 10-Projects/site-wordpress/2026-05-09-1608-session-0375ba09.md
source_session: 0375ba09-478d-4743-8890-c82a03938fb1
status: active
summary: Technique pour fouiller les transcripts JSONL quand une session est interrompue.
tags:
- permanent
- synthesized
- debugging
- session-recovery
- logs
tier: warm
title: Retrouver contexte perdu via JSONL logs Claude Code
topic_cluster: devops-logging
type: permanent-note
updated: '2026-05-10'
---

Pour retrouver le contexte d'une session Claude Code interrompue, accéder aux logs JSONL dans `~/.claude/projects/` ou `~/.claude/projects/<project-id>/`. Utiliser `jq` pour extraire messages user/assistant :

```bash
jq -r 'select(.type == "user") | .message.content | ...' file.jsonl
jq -c 'select(.type == "assistant") | {ts, content}' file.jsonl
```

Cette approche reconstruit le fil sans dépendre de la session actuelle. Utile après timeouts, redémarrages, ou changements de contexte projet.

## Related

- [[2026-05-12-architecture-du-hook-extract-memory-capture-du-tra]] — Architecture du hook extract_memory : capture du transcript et fin de session