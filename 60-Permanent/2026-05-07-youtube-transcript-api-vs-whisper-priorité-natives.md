---
ai_writable: false
area: null
confidence: medium
created: '2026-05-07'
embed_hash: null
embed_model_version: null
entities:
- youtube-transcript-api
- Whisper
- Couche 1
id: 20260507132310-youtube-transcript-api-vs-whisper-priorité-natives
intent: gotcha
last-accessed: '2026-05-07'
moc: null
project: null
related: []
source_notes:
- 10-Projects/claude-system/2026-05-07-1126-session-9416e8cf.md
- 10-Projects/claude-system/2026-05-07-1128-session-9416e8cf.md
source_session: 9416e8cf-0e57-49ee-8bcf-07142a66cca6
status: active
summary: Utilise YouTube Transcript API (sous-titres natifs) en priorité ; Whisper
  seulement en fallback.
tags:
- permanent
- synthesized
- transcription
- latency
- cost
- fallback
tier: warm
title: YouTube Transcript API vs Whisper (priorité natives)
topic_cluster: veille-ia-youtube
type: permanent-note
updated: '2026-05-07'
---

**Piège évité** : transcrire d'emblée via Whisper toutes les vidéos YouTube.

**Meilleure pratique** : 
- **Priorité 1** : Récupérer sous-titres natifs via `youtube-transcript-api` (instantané, pas de coûts GPU).
- **Fallback** : Whisper uniquement si pas de sous-titres disponibles (rares pour >10k vues).

**Raison** : Whisper large-v3-turbo sur GPU coûte latence (0.29× realtime) + ressources. Les natives YouTube sont quasi-toujours dispo pour vidéos populaires (critère >10k vues appliqué).

**Implication** : pour futurs scraping médias, tester l'API native avant fallback transcription.