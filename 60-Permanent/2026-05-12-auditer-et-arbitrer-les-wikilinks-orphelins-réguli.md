---
ai_writable: false
area: null
backlinks:
- 2026-05-09-anti-pattern-redonder-info-du-contexte-injecté
- 2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct
- 2026-05-10-pattern-scripts-maintenance-et-diagnostic-vault
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- vault
- wikilinks
- dangling-links
- cleanup
id: 20260512040146-auditer-et-arbitrer-les-wikilinks-orphelins-réguli
intent: pattern
last-accessed: '2026-05-12'
moc: null
project: null
related:
- _STUBS-A-ARBITRER-2026-05-12
- 2026-05-09-anti-pattern-redonder-info-du-contexte-injecté
- 2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct
- 2026-05-10-pattern-scripts-maintenance-et-diagnostic-vault
- _Index
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
summary: Process récurrent pour détecter et arbitrer les 99+ wikilinks pointant vers
  des notes inexistantes.
tags:
- permanent
- synthesized
- vault
- maintenance
- audit
- script
tier: warm
title: Auditer et arbitrer les wikilinks orphelins régulièrement
topic_cluster: vault-maintenance
type: permanent-note
updated: '2026-05-12'
---

Lancer régulièrement un audit des wikilinks dangling dans la vault (tous les 2-3 mois ou après refactor majeur). Techniques : (1) grep pour trouver `[[_MOC-*]]` et vérifier que chaque slug existe, (2) find pour détecter les fichiers avec liens morts, (3) créer une note d'arbitrage `_STUBS-A-ARBITRER-DATE.md` listant les liens problématiques. Trois actions possibles par lien : créer la note vraie, supprimer le lien erroné, ou ignorer si c'est un alias volontaire. Exemple : `[[_MOC-openclaw-plugin]]` n'existe pas (le vrai slug est `_MOC-openclaw`) → soit corriger le lien, soit créer un alias frontmatter dans `_MOC-openclaw.md`.

## Related

- [[_STUBS-A-ARBITRER-2026-05-12]] —  STUBS A ARBITRER 2026 05 12
- [[2026-05-09-anti-pattern-redonder-info-du-contexte-injecté]] — Anti-pattern : redonder info du contexte injecté
- [[2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct]] — Lesson : Checklist pour diagnostiquer que Crow fonctionne
- [[2026-05-10-pattern-scripts-maintenance-et-diagnostic-vault]] — Pattern : Scripts maintenance et diagnostic vault
- [[_Index]] — Index — openclaw-plugin