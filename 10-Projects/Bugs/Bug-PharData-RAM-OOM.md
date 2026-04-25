---
type: bug
status: resolved
tags: [bug, lesson, php, jt-migrate]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "PharData::compress() et ::extract() chargent tout en RAM → OOM sur archives > 100 MB. Fix : streaming gzopen + USTAR custom."
ai_writable: false
related:
  - "[[Plugin-jt-migrate]]"
  - "[[JT-Migrate-v1.0.0]]"
  - "[[Decision-Streaming-tar-gz-vs-PharData]]"
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
