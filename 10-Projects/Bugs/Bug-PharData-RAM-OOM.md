---
ai_writable: false
backlinks:
- 2026-05-07-ollama-bge-m3-consomme-56-gb-sans-limite
- 2026-05-11-defensive-architecture-pour-import-fail-safe-optio
- 2026-05-11-hbook-placeholder-names-corrupted-lors-exportimpor
- 2026-05-11-validation-syntax-gate-avant-commit-sur-plugins-ph
- 2026-05-12-approche-défensive-pour-cutover-jt-migrate
- Bug-JT-Migrate-v1.1-Import-Extract-Fail
- Decision-Streaming-tar-gz-vs-PharData
- JT-Migrate-v1.0.0
- Lesson-PharData-charge-tout-en-RAM
- Lessons-Learned
- _MOC-jt-migrate
- _VAULT-INDEX
created: 2026-04-25
description: 'PharData::compress() et ::extract() chargent tout en RAM → OOM sur archives
  > 100 MB. Fix : streaming gzopen + USTAR custom.'
embed_hash: null
embed_model_version: null
entities:
- debugging
- migration
- site-wordpress
id: 202604252037-bug-phardata-ram-oom
intent: log
last-accessed: 2026-04-25
project: Bugs
related:
- 2026-05-11-defensive-architecture-pour-import-fail-safe-optio
- 2026-05-11-hbook-placeholder-names-corrupted-lors-exportimpor
- 2026-05-11-validation-syntax-gate-avant-commit-sur-plugins-ph
- 2026-05-12-approche-défensive-pour-cutover-jt-migrate
- '[[Decision-Streaming-tar-gz-vs-PharData]]'
- '[[JT-Migrate-v1.0.0]]'
- '[[Plugin-jt-migrate]]'
relevance: high
status: resolved
summary: 'Le plugin JT-Migrate-v1.0.0|JT Migrate v1.0.0 crashait à l''export d''un
  site WP > 100 MB :'
tags:
- bug
- lesson
- php
- jt-migrate
tier: cold
topic_cluster: bug-log
type: bug
updated: 2026-04-25
---

# 🐛 Bug : PharData OOM sur > 100 MB

## Symptôme

Le plugin [[JT-Migrate-v1.0.0|JT Migrate v1.0.0]] crashait à l'export d'un site WP > 100 MB :
- Frontend voyait juste "❌ Étape échouée" sans message
- Logs Apache vides (PHP fatal silencieux)
- `state.json` du job reste au stage `files_done`

Sur dealmfr (305 MB d'uploads) → fail systématique.

Idem en lecture pour `JT_Migrate_Archive::extract()` qui utilisait `PharData::extractTo()`.

## Cause racine

`PharData::compress(Phar::GZ)` charge le `.tar` complet en RAM avant de le re-écrire compressé. `PharData::extractTo()` charge l'index complet de l'archive en RAM.

Sur 300+ MB, dépasse le `memory_limit` (512M ne suffit pas, il faut ~1 GB+ pour les overheads).

## Investigation

Phase 1 systematic-debugging :
- Pas de logs PHP (fatal court-circuite output)
- Pas de logs Apache (HTTP 500 silencieux)
- Examen `state.json` : pipeline s'arrête juste après `files_done`
- → suspect = phase `archive`
- Test isolé `PharData::compress` avec memory_get_peak_usage → confirmation OOM

## Fix

[[Decision-Streaming-tar-gz-vs-PharData]] : réécrire en streaming.

- Export : [[JT-Migrate-v1.1.0]] — gzopen + USTAR headers à la main, lecture chunks 64 KB
- Import : [[JT-Migrate-v1.2.1]] — parser USTAR custom en lecture (miroir)

Résultat : peak mem **0.6 MB** sur archive 239 MB (vs OOM avant).

## 📚 Lesson learned

**`PharData` n'est PAS scalable.** À éviter pour fichiers > 100 MB. Quand on doit faire du tar.gz en pure PHP sans accès shell :
- Pour l'écriture : `gzopen` + `gzwrite` + format USTAR à la main
- Pour la lecture : `gzopen` + `gzread` par chunks + parsing USTAR header par header

C'est ~150 lignes de PHP, vraiment pas compliqué, et **scale infinie** en RAM (constante).

Vérifier toujours la doc PHP du module avant de l'utiliser sur gros volume : `PharData` est documenté comme "convenient for small archives", pas "scalable".

## Liens

- [[Plugin-jt-migrate]]
- [[Decision-Streaming-tar-gz-vs-PharData]]
- [[JT-Migrate-v1.0.0]]

## Related

- [[2026-05-11-defensive-architecture-pour-import-fail-safe-optio]] — Defensive architecture pour import: fail-safe optional steps
- [[2026-05-11-hbook-placeholder-names-corrupted-lors-exportimpor]] — HBook placeholder names corrupted lors export/import entre instances
- [[2026-05-11-validation-syntax-gate-avant-commit-sur-plugins-ph]] — Validation syntax gate avant commit sur plugins PHP
- [[2026-05-12-approche-défensive-pour-cutover-jt-migrate]] — Approche défensive pour cutover jt-migrate