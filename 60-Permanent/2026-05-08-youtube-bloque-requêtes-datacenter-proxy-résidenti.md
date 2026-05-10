---
ai_writable: false
area: null
backlinks:
- 2026-05-07-youtube-transcript-api-vs-whisper-priorité-natives
- 2026-05-08-pipeline-modulaire-ingestanalyzerenderdigest
- 2026-05-08-pipeline-veille-ia-youtube-ingestanalyzerendersend
confidence: medium
created: '2026-05-08'
embed_hash: null
embed_model_version: null
entities:
- YouTube
- ingest-via-residential.sh
id: 20260508040141-youtube-bloque-requêtes-datacenter-proxy-résidenti
intent: gotcha
last-accessed: '2026-05-08'
moc: null
project: null
related:
- 2026-05-08-pipeline-veille-ia-youtube-ingestanalyzerendersend
- 2026-05-08-pipeline-modulaire-ingestanalyzerenderdigest
- 2026-05-07-youtube-transcript-api-vs-whisper-priorité-natives
- 2026-05-07-critères-filtrage-youtube-veille-ia
- 2026-05-07-cron-23h30-pour-ingestion-veille-timing-off-peak
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-07-1424-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1419-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1416-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1414-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1341-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1445-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1553-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1538-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1319-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1413-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1429-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1511-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1311-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1457-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1543-session-e172a5dd.md
source_session: e172a5dd-5040-43b5-8a0e-4fec08f8f037
status: active
summary: 'YouTube détecte et bloque l''ingestion de transcripts via IP datacenter.
  Contournement : script ingest-via-residential.sh utilisant proxy résidentiel.'
tags:
- permanent
- synthesized
- scraping
- geo-blocking
- workaround
tier: warm
title: YouTube bloque requêtes datacenter — proxy résidentiel
topic_cluster: veille-ia-youtube
type: permanent-note
updated: '2026-05-08'
---

**Le problème** : requêtes d'ingestion directes au service YouTube depuis IP datacenter (VPS) sont détectées et bloquées/throttled.

**La solution** : créer une alternative `ingest-via-residential.sh` qui route les requêtes via un proxy résidentiel (IP résidentielle), contournant les détections géographiques.

**Quand l'utiliser** : si `ingest.py` standard retourne des 429 ou bloquages sur YouTube API/pages. Basculer sur le script résidentiel.

**Implications** : coût de proxy résidentiel (bande passante/quota), latence accrue, mais gain de fiabilité d'ingestion. À préférer à des retries exponentiels qui finissent par timeout.

## Related

- [[2026-05-08-pipeline-veille-ia-youtube-ingestanalyzerendersend]] — Pipeline veille-ia-youtube : ingest→analyze→render→send
- [[2026-05-08-pipeline-modulaire-ingestanalyzerenderdigest]] — Pipeline modulaire ingest→analyze→render→digest
- [[2026-05-07-youtube-transcript-api-vs-whisper-priorité-natives]] — YouTube Transcript API vs Whisper (priorité natives)
- [[2026-05-07-critères-filtrage-youtube-veille-ia]] — Critères filtrage YouTube veille-ia
- [[2026-05-07-cron-23h30-pour-ingestion-veille-timing-off-peak]] — Cron 23h30 pour ingestion veille (timing off-peak)