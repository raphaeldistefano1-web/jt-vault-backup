---
ai_writable: false
area: null
backlinks:
- 2026-05-11-defensive-architecture-pour-import-fail-safe-optio
- 2026-05-11-hbook-placeholder-names-corrupted-lors-exportimpor
- 2026-05-11-scripts-pre-cutover-cleanup-et-post-import-reenabl
- Bug-JT-Migrate-v1.1-Import-Extract-Fail
- Bug-PharData-RAM-OOM
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- jt-migrate
- WordPress
- migration
id: 20260512040620-approche-défensive-pour-cutover-jt-migrate
intent: pattern
last-accessed: '2026-05-12'
moc: null
project: null
related:
- Bug-JT-Migrate-v1.1-Import-Extract-Fail
- Bug-PharData-RAM-OOM
- 2026-05-11-hbook-placeholder-names-corrupted-lors-exportimpor
- _Index
- 2026-05-08-config-externalisée-env-prompts-markdown-séparés-d
schema_version: 1
source_notes:
- 10-Projects/jt-migrate/2026-05-11-1747-session-f978e4ee.md
source_session: f978e4ee-8378-4961-a70b-ecc2e9ede8d3
status: active
summary: Steps optionnels et isolés qui ne cassent jamais l'import même en cas d'erreur
  ; scripts pre/post-cutover séparés.
tags:
- permanent
- synthesized
- migration
- safety
- plugin
- defensive-coding
- error-isolation
tier: warm
title: Approche défensive pour cutover jt-migrate
topic_cluster: jt-migrate-cutover
type: permanent-note
updated: '2026-05-12'
---

Lors du cutover jt-migrate (Instance B→A), adoption d'une approche défensive : tout step qui touche aux données est optionnel et ne peut pas faire échouer l'import même en cas d'erreur. Scripts shell séparés (`pre-cutover-cleanup.sh`, `post-import-reenable-emails.sh`) découplent les opérations. Cela prévient un rollback involontaire si une étape annexe échoue.

**Pourquoi** : sur une migration prod avec données réelles, une exception inattendue = interruption impossible à gérer. En isolant les opérations en steps optionnels, on maximise les chances que la donnée arrive intacte, même dégradée.

## Related

- [[Bug-JT-Migrate-v1.1-Import-Extract-Fail]] — Bug JT Migrate v1.1 Import Extract Fail
- [[Bug-PharData-RAM-OOM]] — Bug PharData RAM OOM
- [[2026-05-11-hbook-placeholder-names-corrupted-lors-exportimpor]] — HBook placeholder names corrupted lors export/import entre instances
- [[_Index]] — Index — jt-migrate
- [[2026-05-08-config-externalisée-env-prompts-markdown-séparés-d]] — Config externalisée : .env + prompts markdown séparés du code