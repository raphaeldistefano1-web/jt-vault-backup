---
ai_writable: false
area: null
backlinks:
- 2026-05-11-validation-syntax-gate-avant-commit-sur-plugins-ph
- Lessons-Learned
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- MOCs
- slugs
- wikilinks
- naming-convention
id: 20260512040148-les-slugs-moc-sont-sensibles-aux-typos-et-créent-d
intent: lesson
last-accessed: '2026-05-12'
moc: null
project: null
related:
- Lessons-Learned
- _MOC-openclaw
- _Index
- _VAULT-INDEX
- 2026-05-11-validation-syntax-gate-avant-commit-sur-plugins-ph
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
summary: 'Chaque typo dans un slug `_MOC-*` (ex: `-plugin` oublié) crée un lien mort
  irréupérable jusqu''à cleanup.'
tags:
- permanent
- synthesized
- vault
- conventions
- naming
- gotcha
tier: warm
title: Les slugs MOC sont sensibles aux typos et créent des dangling links
topic_cluster: vault-naming
type: permanent-note
updated: '2026-05-12'
---

Les wikilinks `[[_MOC-openclaw-plugin]]` ne résolvent pas si le vrai slug est `_MOC-openclaw`. Cette distinction (singulier/pluriel, suffixes) est critique. Lors d'un refactor vault où on mentionne des refs en parlant, les typos se retrouvent dans les logs et créent des stubs fantômes. Bonnes pratiques : (1) établir une liste officielle de slugs MOC et les coller près du début de la vault, (2) vérifier les wikilinks avant de commit, (3) utiliser des aliases frontmatter pour accommoder les variantes courantes (ex: `aliases: [_MOC-openclaw-plugin, openclaw-MOC]`), (4) documenter le pattern exact (`_MOC-<projet>` ou `_MOC-<domain>`).

## Related

- [[Lessons-Learned]] — Lessons Learned
- [[_MOC-openclaw]] — MOC OpenClaw Plugin
- [[_Index]] — Index — openclaw-plugin
- [[_VAULT-INDEX]] — Vault Index — point d'entrée racine
- [[2026-05-11-validation-syntax-gate-avant-commit-sur-plugins-ph]] — Validation syntax gate avant commit sur plugins PHP