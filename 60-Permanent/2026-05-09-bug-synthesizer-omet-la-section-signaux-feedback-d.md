---
ai_writable: false
area: null
confidence: medium
created: '2026-05-09'
embed_hash: null
embed_model_version: null
entities:
- vault-synthesizer
- feedback-rules
- extraction
id: 20260509040322-bug-synthesizer-omet-la-section-signaux-feedback-d
intent: gotcha
last-accessed: '2026-05-09'
moc: null
project: null
related: []
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-08-1021-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-1034-session-4d0a55cb.md
- 10-Projects/claude-system/2026-05-08-1013-session-4d0a55cb.md
- 10-Projects/pms-jardin-tropical/2026-05-08-1007-session-4d0a55cb.md
source_session: 4d0a55cb-ed1e-494e-9202-45857e2bd2b9
status: active
summary: Le synthesizer extrait 6 sections de logs (prompts/décisions/erreurs/fichiers/bash)
  mais **omet intentionnellement** la section « Signaux feedback détectés » → aucune
  feedback-rule ne remonte du pipeline.
tags:
- permanent
- synthesized
- bug
- data-loss-risk
- feedback-pipeline
tier: warm
title: 'Bug : synthesizer omet la section Signaux feedback détectés'
topic_cluster: vault-synthesizer
type: permanent-note
updated: '2026-05-09'
---

Lors de l'audit du pipeline vault-synthesizer, découverte que la logique d'extraction dans `/opt/vault-rag/lib/synthesizer.py` passe systématiquement outre la section « Signaux feedback détectés » présente dans les logs bruts. Cela signifie que toutes les règles de comportement détectées lors d'une session (corrections utilisateur, approbations fortes, suggestions validées) **ne sont jamais capturées en tant que feedback-rules permanentes**.

**Conséquence** : la pipeline d'apprentissage en boucle fermée (feedback utilisateur → règle durable) est cassée à la source. Les patterns comportementaux qu'il faudrait capturer s'évaporent.

**Fix** : ajouter un parseur pour la section feedback-rules dans le synthesizer et générer des notes `intent: feedback-rule` correspondantes.