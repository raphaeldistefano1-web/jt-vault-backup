---
ai_writable: true
area: null
backlinks:
- _Index
capture_source: claude-mem
confidence: medium
created: 2026-06-04
cwd: ''
embed_hash: null
embed_model_version: null
entities: []
id: 202606041153-claudemem-ce0b01f9
intent: log
last-accessed: 2026-06-04
moc: null
n_files_edited: 0
n_files_read: 0
project: claude-system
related: []
schema_version: 1
session_id: ce0b01f9-6bfc-46e7-add1-9e2cd5f1a29e
source: claude-mem:session_summaries#96
status: draft
summary: Clarified that no plugin setting provides selective import of content while
  preserving destination accounts; explained WordPress architecture showing why content
  and users are architecturally inseparable;
tags:
- session
- log
- ai-generated
tier: cold
title: Clarify All-in-One WP Migration capabilities for selective content import while
  preserving destination
topic_cluster: session-log
type: meeting
updated: 2026-06-04
---

# Session (claude-mem) — Clarify All-in-One WP Migration capabilities for selective content import while preserving destination

> Capture semantique claude-mem (2026-06-04). Source plus riche que le hook extract_memory (compression LLM). Sera raffinee par le vault-synthesizer.

## Metadonnees

- **Projet** : `raphia`
- **Session ID** : `ce0b01f9-6bfc-46e7-add1-9e2cd5f1a29e`
- **Working dir** : ``
- **Source** : `claude-mem` (session_summaries #96)

## Demande

Clarify All-in-One WP Migration capabilities for selective content import while preserving destination user accounts; address misconceptions about plugin options and actual migration risks

## Investigue

WordPress data storage architecture (content vs. user accounts location); All-in-One WPM export options and their scope; whether selective table-level database import is possible; distinction between perceived risk (access loss) and actual risk (data preservation)

## Appris

WordPress stores both site content and user accounts in the same database (indivisible from migration perspective); All-in-One WPM treats database as single atomic block—cannot selectively migrate content while excluding user accounts; export options like "Do not export database" are all-or-nothing (excluding them excludes all content too, defeating selective import goal); user's fear of access loss is unfounded because source credentials (raphael / Villa-f6a64d34) will work post-import; actual critical risk is whether destination WordPress already hosts other important content that would be completely overwritten

## Realise

Clarified that no plugin setting provides selective import of content while preserving destination accounts; explained WordPress architecture showing why content and users are architecturally inseparable; reframed risk from "losing access" to "what else exists on destination"; provided realistic post-import workflow (30-second reconnect with known credentials)

## Prochaines etapes

Determine destination WordPress status: is it dedicated solely to Villa Saint-Éloi (empty/jetable) or does it already host other sites/content/important accounts; make go/no-go decision on AIO WPM import based on destination status; if destination is purpose-built for Villa Saint-Éloi, proceed with full import; if destination hosts other content, identify alternative migration method

## Notes

User's selective-import expectation stemmed from seeing export-level options, misinterpreting them as import-level granularity; the real decision point is destination WordPress purpose, not technical limitation of access recovery; backup strategy and credential verification remain prerequisites regardless of go/no-go decision

## TODO curator

- [ ] Raffiner le `summary` a partir du contenu reel
- [ ] Decider du `tier` final (hot/warm/cold)
- [ ] Ranger dans le bon projet ou decomposer en notes atomiques
- [ ] Ajouter wikilinks vers MOCs et notes liees
- [ ] Dedup vs note extract_memory de la meme session si presente