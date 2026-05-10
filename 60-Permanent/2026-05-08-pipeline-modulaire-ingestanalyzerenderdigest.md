---
ai_writable: false
area: null
backlinks:
- 2026-05-07-structure-répertoires-srvveille-ia-config-external
- 2026-05-08-automatiser-envoi-digest-via-email-avec-date
- 2026-05-08-youtube-bloque-requêtes-datacenter-proxy-résidenti
- 2026-05-09-hook-dispatch-advisor-pour-suggestions-intelligent
- 2026-05-10-valider-systèmes-de-dispatch-via-instances-vierges
confidence: medium
created: '2026-05-08'
embed_hash: null
embed_model_version: null
entities:
- ingest.py
- analyze.py
- render.py
- digest
id: 20260508040141-pipeline-modulaire-ingestanalyzerenderdigest
intent: pattern
last-accessed: '2026-05-08'
moc: null
project: null
related:
- 2026-05-07-haiku-pour-curation-veille-ia-économie-tokens
- 2026-05-07-structure-répertoires-srvveille-ia-config-external
- 2026-05-08-automatiser-envoi-digest-via-email-avec-date
- 2026-05-08-youtube-bloque-requêtes-datacenter-proxy-résidenti
- 2026-05-09-hook-dispatch-advisor-pour-suggestions-intelligent
- 2026-05-10-valider-systèmes-de-dispatch-via-instances-vierges
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
summary: 'Système 4 étapes séparées : ingestion transcripts → analyse Claude → rendu
  Jinja2 → digest final. Chaque étape peut tourner indépendamment.'
tags:
- permanent
- synthesized
- pipeline
- modularity
- workflow
- architecture
tier: warm
title: Pipeline modulaire ingest→analyze→render→digest
topic_cluster: veille-ia-youtube
type: permanent-note
updated: '2026-05-08'
---

**Étapes** :
1. **ingest.py** : récupère transcripts YouTube (Couche 1 ou direct), stocke candidats crus.
2. **analyze.py** : passe 20 candidats à Sonnet pour finalisation, score + summary.
3. **render.py** : appelle Haiku pour résumé final, applique template Jinja2 (`digest.html.j2`).
4. Sortie : markdown `digests/YYYY-MM-DD.md` + HTML.

**Modularité** : chaque étape a `.py` séparé + config séparé (prompts en `config/prompts/digest.md`). Permet itérer un étage sans re-courir les autres.

**Config prompts** : prompts centralisés en fichier séparé `config/prompts/digest.md`, chargés dynamiquement par `analyze.py` + `render.py`. Facilite A/B testing et ajustements rapides.

**Avantage** : cacheable par étape, parallélisable, debug granulaire, evite re-runs coûteux (Sonnet).

## Related

- [[2026-05-07-structure-répertoires-srvveille-ia-config-external]] — Structure répertoires /srv/veille-ia (config externalisée)
- [[2026-05-08-automatiser-envoi-digest-via-email-avec-date]] — Automatiser envoi digest via email avec date
- [[2026-05-08-youtube-bloque-requêtes-datacenter-proxy-résidenti]] — YouTube bloque requêtes datacenter — proxy résidentiel
- [[2026-05-09-hook-dispatch-advisor-pour-suggestions-intelligent]] — Hook dispatch_advisor pour suggestions intelligentes
- [[2026-05-07-haiku-pour-curation-veille-ia-économie-tokens]] — Haiku pour curation veille IA (économie tokens)
- [[2026-05-10-valider-systèmes-de-dispatch-via-instances-vierges]] — Valider systèmes de dispatch via instances vierges