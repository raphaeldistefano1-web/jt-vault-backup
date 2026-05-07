---
ai_writable: false
area: null
confidence: medium
created: '2026-05-07'
embed_hash: null
embed_model_version: null
entities:
- veille-ia
- architecture
- Claude
id: 20260507132310-pipeline-3-couches-ingestion-curation-livraison
intent: lesson
last-accessed: '2026-05-07'
moc: null
project: null
related: []
source_notes:
- 10-Projects/claude-system/2026-05-07-1126-session-9416e8cf.md
- 10-Projects/claude-system/2026-05-07-1128-session-9416e8cf.md
source_session: 9416e8cf-0e57-49ee-8bcf-07142a66cca6
status: active
summary: Couche 1 (ingest YouTube+filter), Couche 2 (curate Sonnet 20 finalistes+Haiku
  résumé), Couche 3 (PDF+email+archive).
tags:
- permanent
- synthesized
- architecture
- separation-concerns
- reusable
tier: warm
title: Pipeline 3-couches ingestion → curation → livraison
topic_cluster: veille-ia-youtube
type: permanent-note
updated: '2026-05-07'
---

**Architecture robuste** :

**Couche 1 — Ingestion** : YouTube API → appliquer criteria.json → 50–100 candidats bruts.
- Sortie : `candidates/`
- Coût : API YouTube (gratuit tier)

**Couche 2 — Curation** : 
- Pré-filter 20 finalistes via Claude Sonnet (coûteux, précision max)
- Résumer chacun via Claude Haiku (économe)
- Sortie : `digests/` (markdown + metadata)
- Coût : Sonnet 1× + Haiku 20×

**Couche 3 — Livraison** :
- Render markdown → PDF (Weasyprint, Jinja2 templates)
- Email digest via SMTP
- Archive versionnée (git ou S3)

**Avantage** : si critères changent, re-run Couche 1 seule (pas re-transcription). Si templates changent, re-run Couche 3 seule (pas re-curation). Chaque couche = idempotente + rejoignable.

**Réutilisable** pour news feeds, paper summaries, podcast digests.