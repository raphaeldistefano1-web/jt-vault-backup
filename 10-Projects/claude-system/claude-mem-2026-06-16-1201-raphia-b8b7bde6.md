---
ai_writable: true
area: null
backlinks:
- _Index
capture_source: claude-mem
confidence: medium
created: 2026-06-16
cwd: ''
embed_hash: null
embed_model_version: null
entities: []
id: 202606161201-claudemem-b8b7bde6
intent: log
last-accessed: 2026-06-16
moc: null
n_files_edited: 0
n_files_read: 0
project: claude-system
related: []
schema_version: 1
session_id: b8b7bde6-c066-4f94-96c0-90a3b094a872
source: claude-mem:session_summaries#194
status: draft
summary: RESTORE.md created with step-by-step restoration procedures for all 5 service
  categories (PMS Le Jardin Tropical, 3 WordPress instances, n8n automation, Traefik
  proxy, internal services); SECRETS-INDEX.md
tags:
- session
- log
- ai-generated
tier: cold
title: Map all memory consumption on Mac Mini and propose deletions; archive VPS
topic_cluster: session-log
type: meeting
updated: 2026-06-16
---

# Session (claude-mem) — Map all memory consumption on Mac Mini and propose deletions; archive VPS

> Capture semantique claude-mem (2026-06-16). Source plus riche que le hook extract_memory (compression LLM). Sera raffinee par le vault-synthesizer.

## Metadonnees

- **Projet** : `raphia`
- **Session ID** : `b8b7bde6-c066-4f94-96c0-90a3b094a872`
- **Working dir** : ``
- **Source** : `claude-mem` (session_summaries #194)

## Demande

Map all memory consumption on Mac Mini and propose deletions; archive VPS infrastructure before complete migration

## Investigue

VPS service architecture (5 service categories: booking system, WordPress CMS, automation, reverse proxy, internal tools); file structure and storage allocation; plaintext secrets distribution; current transfer progress and bottlenecks

## Appris

VPS contains ~7.5GB of application data across multiple service types; transfer to Mac Mini is uneven (opt directory 72% complete, var-www only 8% complete, root not yet started); plaintext secrets (DB passwords, OAuth tokens, SSH keys, encryption keys) scattered across .env files and root directories; transfer bottleneck is var-www with large node_modules and WordPress site data

## Realise

RESTORE.md created with step-by-step restoration procedures for all 5 service categories (PMS Le Jardin Tropical, 3 WordPress instances, n8n automation, Traefik proxy, internal services); SECRETS-INDEX.md created with complete inventory of plaintext secrets and security hardening recommendations; VPS infrastructure fully mapped; partial file transfer in progress (databases already dumped as most critical)

## Prochaines etapes

Complete background file transfers (var-www, opt, root directories); generate MANIFEST.md with checksums for all critical files; perform end-to-end integrity verification (compare VPS source against Mac destination file-by-file on critical components); conduct pre-mortem review; obtain approval before shutting down VPS

## Notes

Transfer is running in background — var-www represents bulk of remaining work due to node_modules and WordPress site data; database dumps (most critical) already secured; secrets require post-transfer encryption or migration to password manager; pre-mortem review will identify any missing pieces before VPS decommission

## TODO curator

- [ ] Raffiner le `summary` a partir du contenu reel
- [ ] Decider du `tier` final (hot/warm/cold)
- [ ] Ranger dans le bon projet ou decomposer en notes atomiques
- [ ] Ajouter wikilinks vers MOCs et notes liees
- [ ] Dedup vs note extract_memory de la meme session si presente