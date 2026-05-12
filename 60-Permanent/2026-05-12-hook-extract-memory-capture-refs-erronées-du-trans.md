---
ai_writable: false
area: null
backlinks:
- 2026-05-09-anti-pattern-redonder-info-du-contexte-injecté
- 2026-05-09-bug-synthesizer-omet-la-section-signaux-feedback-d
- 2026-05-10-gotcha-fichiers-temporaires-indexés-par-rag
- Bug-OpenClaw-Plugin-Sandbox
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- extract_memory
- transcript
- wikilinks
id: 20260512040144-hook-extract-memory-capture-refs-erronées-du-trans
intent: gotcha
last-accessed: '2026-05-12'
moc: null
project: null
related:
- 2026-05-09-anti-pattern-redonder-info-du-contexte-injecté
- 2026-05-09-bug-synthesizer-omet-la-section-signaux-feedback-d
- _STUBS-A-ARBITRER-2026-05-12
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
summary: Hook capture littéralement les mentions erronées du texte conversationnel,
  créant des stubs orphelins dans 00-Inbox.
tags:
- permanent
- synthesized
- vault
- hooks
- noise
- deduplication
tier: warm
title: Hook extract_memory capture refs erronées du transcript
topic_cluster: vault-system
type: permanent-note
updated: '2026-05-12'
---

Quand on mentionne accidentellement une fausse référence en parlant (ex: `_MOC-openclaw-plugin` au lieu de `_MOC-openclaw`), le hook extract_memory la capture du transcript brut et crée une note stub correspondante, polluant 00-Inbox. Le hook fonctionne en mode « capture everything » sans validation que la cible wikilink existe réellement. Conséquence : accumulation de stubs orphelins à arbitrer manuellement. Solution possible : ajouter une étape de validation (vérifier que le slug cible existe) avant d'écrire la note, ou faire des audits réguliers de cleanup 00-Inbox.

## Related

- [[2026-05-09-anti-pattern-redonder-info-du-contexte-injecté]] — Anti-pattern : redonder info du contexte injecté
- [[2026-05-09-bug-synthesizer-omet-la-section-signaux-feedback-d]] — Bug : synthesizer omet la section Signaux feedback détectés
- [[_STUBS-A-ARBITRER-2026-05-12]] —  STUBS A ARBITRER 2026 05 12