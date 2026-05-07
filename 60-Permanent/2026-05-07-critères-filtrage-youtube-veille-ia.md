---
ai_writable: false
area: null
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
related: []
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