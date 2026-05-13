---
ai_writable: false
area: null
backlinks:
- 2026-05-08-pipeline-modulaire-ingestanalyzerenderdigest
- 2026-05-08-pipeline-veille-ia-youtube-ingestanalyzerendersend
- 2026-05-09-claude-max-5x-fenêtre-courte-à-réserver
confidence: medium
created: '2026-05-07'
embed_hash: null
embed_model_version: null
entities:
- veille-ia
- Couche 2
- Haiku
id: 20260507132310-haiku-pour-curation-veille-ia-économie-tokens
intent: decision
last-accessed: '2026-05-07'
moc: null
project: null
related:
- '2026-05-07'
- 2026-05-07-critères-filtrage-youtube-veille-ia
- 2026-05-08-pipeline-veille-ia-youtube-ingestanalyzerendersend
- 2026-05-08-vault-synthesizer-synthèse-auto-des-session-logs
- 2026-05-09-claude-max-5x-fenêtre-courte-à-réserver
- '2026-05-12'
source_notes:
- 10-Projects/claude-system/2026-05-07-1126-session-9416e8cf.md
- 10-Projects/claude-system/2026-05-07-1128-session-9416e8cf.md
source_session: 9416e8cf-0e57-49ee-8bcf-07142a66cca6
status: active
summary: Couche 2 (résumé 20 finalistes) utilise Haiku au lieu de Sonnet pour réduire
  consommation tokens.
tags:
- permanent
- synthesized
- cost-optimization
- model-selection
- curation
tier: warm
title: Haiku pour curation veille IA (économie tokens)
topic_cluster: veille-ia-youtube
type: permanent-note
updated: '2026-05-07'
---

**Décision** : La Couche 2 (sélection + résumé de 20 vidéos finales) utilise Claude Haiku pour les résumés, au lieu d'un modèle plus gros.

**Pourquoi** : réduire la consommation tokens tout en gardant qualité suffisante pour un digest de veille. Haiku est ~8× moins coûteux que Sonnet, acceptable pour du résumé/extraction faces à un corpus pré-filtré par Sonnet en amont.

**Implication** : ce ratio économique s'applique aussi à futurs pipelines de veille (documents, articles, podcasts). Préférer filtrage amont (agent coûteux) + résumé aval (agent économe).

## Related

- [[2026-05-08-pipeline-veille-ia-youtube-ingestanalyzerendersend]] — Pipeline veille-ia-youtube : ingest→analyze→render→send
- [[2026-05-07-critères-filtrage-youtube-veille-ia]] — Critères filtrage YouTube veille-ia
- [[2026-05-08-vault-synthesizer-synthèse-auto-des-session-logs]] — Vault synthesizer — synthèse auto des session-logs
- [[2026-05-09-claude-max-5x-fenêtre-courte-à-réserver]] — Claude Max 5x : fenêtre courte, à réserver
- [[2026-05-07]] — Veille IA — Jeudi 7 mai 2026
- [[2026-05-12]] — Veille IA — Mardi 12 mai 2026