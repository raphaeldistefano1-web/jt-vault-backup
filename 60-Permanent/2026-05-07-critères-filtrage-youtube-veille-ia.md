---
ai_writable: false
area: null
backlinks:
- 2026-05-07-cron-23h30-pour-ingestion-veille-timing-off-peak
- 2026-05-07-haiku-pour-curation-veille-ia-économie-tokens
- 2026-05-07-pipeline-3-couches-ingestion-curation-livraison
- 2026-05-07-structure-répertoires-srvveille-ia-config-external
- 2026-05-07-youtube-transcript-api-vs-whisper-priorité-natives
- 2026-05-08-pipeline-veille-ia-youtube-ingestanalyzerendersend
- 2026-05-08-team-interne-task-list-pour-paralléliser-multi-fin
- 2026-05-08-youtube-bloque-requêtes-datacenter-proxy-résidenti
- 2026-05-11-stack-cul-sec-nextjs-14-app-router-framer-motion-p
- _VAULT-INDEX
confidence: medium
created: '2026-05-07'
embed_hash: null
embed_model_version: null
entities:
- YouTube
- Couche 1
- criteria.json
id: 20260507132310-critères-filtrage-youtube-veille-ia
intent: config
last-accessed: '2026-05-07'
moc: null
project: null
related:
- 2026-05-07-pipeline-3-couches-ingestion-curation-livraison
- 2026-05-07-structure-répertoires-srvveille-ia-config-external
- 2026-05-07-youtube-transcript-api-vs-whisper-priorité-natives
- 2026-05-08-pipeline-veille-ia-youtube-ingestanalyzerendersend
- 2026-05-08-team-interne-task-list-pour-paralléliser-multi-fin
- session
source_notes:
- 10-Projects/claude-system/2026-05-07-1126-session-9416e8cf.md
- 10-Projects/claude-system/2026-05-07-1128-session-9416e8cf.md
source_session: 9416e8cf-0e57-49ee-8bcf-07142a66cca6
status: active
summary: '>10k vues, 10-30 min, <3 mois, thèmes IA/business/marketing, FR+EN.'
tags:
- permanent
- synthesized
- filtering
- threshold
- scope
tier: warm
title: Critères filtrage YouTube veille-ia
topic_cluster: veille-ia-youtube
type: permanent-note
updated: '2026-05-07'
---

**Critères de Couche 1** (ingestion YouTube) :
- **Vues** : >10k (qualité baseline)
- **Durée** : 10–30 min (contenu dense, excluant courts TikTok-like et confs 2h)
- **Date** : <3 mois (veille = récent)
- **Thèmes** : agents IA + business/marketing (scope défini)
- **Langues** : FR + EN (audience mixte)

**Lieu** : `config/criteria.json` (versionnable, modifiable sans redeploy).

**Implication** : ces seuils sont des dégagements de business logic (pas technique). Si Raphaël veut baisser à >5k vues ou allonger à 45 min, éditer criteria.json et re-lancer ingestion. Ne pas hard-coder en Python.

## Related

- [[2026-05-07-pipeline-3-couches-ingestion-curation-livraison]] — Pipeline 3-couches ingestion → curation → livraison
- [[2026-05-07-structure-répertoires-srvveille-ia-config-external]] — Structure répertoires /srv/veille-ia (config externalisée)
- [[2026-05-08-pipeline-veille-ia-youtube-ingestanalyzerendersend]] — Pipeline veille-ia-youtube : ingest→analyze→render→send
- [[2026-05-08-team-interne-task-list-pour-paralléliser-multi-fin]] — Team interne + task-list pour paralléliser multi-findings
- [[2026-05-07-youtube-transcript-api-vs-whisper-priorité-natives]] — YouTube Transcript API vs Whisper (priorité natives)
- [[session]] — session