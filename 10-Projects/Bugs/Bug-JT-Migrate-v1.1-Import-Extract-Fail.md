---
ai_writable: true
backlinks:
- 2026-05-12-approche-défensive-pour-cutover-jt-migrate
- 2026-05-12-cleanup-post-cutover-supprimer-plugins-temporaires
- JT-Migrate-v1.1.0
- JT-Migrate-v1.2.1
- _STUBS-A-ARBITRER-2026-05-12
created: 2026-05-12
description: Stub — import de l'archive échoue à l'étape extract sur jt-migrate v1.1
embed_hash: null
embed_model_version: null
entities:
- jt-migrate
- migration
- wordpress
id: 202605120001-bug-jt-migrate-v11-import-extract-fail
intent: log
last-accessed: 2026-05-12
project: Bugs
related:
- 2026-05-12-approche-défensive-pour-cutover-jt-migrate
- 2026-05-12-cleanup-post-cutover-supprimer-plugins-temporaires
status: stub
summary: Import de l'archive échoue à l'étape extract sur le plugin jt-migrate v1.1
tags:
- bug
- migration
- wordpress
tier: cold
type: bug
updated: 2026-05-12
---

# Bug JT-Migrate v1.1 Import Extract Fail

> **Stub** — Note référencée par wikilinks orphelins, à compléter.

Contexte : régression apparue sur la v1.1 du plugin `jt-migrate` lors de l'étape `extract` de l'import. Plugin de migration full-fidelity WP custom (cf. [[Plugin-jt-migrate]]).

## À documenter

- [ ] Reproduction exacte
- [ ] Diff v1.0 vs v1.1 sur la fonction extract
- [ ] Logs d'erreur PHP
- [ ] Fix retenu (downgrade ou patch)

## Related

- [[_MOC-jt-migrate]]
- [[Bug-PharData-RAM-OOM]]
- [[Bug-JT-Migrate-Auth-Loss-After-DB-Restore]]
- [[2026-05-12-cleanup-post-cutover-supprimer-plugins-temporaires]] — Cleanup post-cutover : supprimer plugins temporaires
- [[2026-05-12-approche-défensive-pour-cutover-jt-migrate]] — Approche défensive pour cutover jt-migrate