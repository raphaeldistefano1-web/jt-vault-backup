---
type: decision
status: accepted
tags: [decision, jt-migrate, performance, php]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "Décision : remplacer PharData par streaming gzopen + USTAR custom dans JT Migrate (export ET import)"
ai_writable: false
related:
  - "[[Plugin-jt-migrate]]"
  - "[[JT-Migrate-v1.0.0]]"
  - "[[JT-Migrate-v1.1.0]]"
  - "[[JT-Migrate-v1.2.1]]"
  - "[[Bug-PharData-RAM-OOM]]"
context: "Bug v1.0.0 : PharData::compress() + PharData::extract() chargent tout en RAM, fail sur > 100 MB"
chosen: "Streaming gzopen + USTAR custom"
alternatives: ["PharData", "exec(tar)", "ZipArchive"]
---

# 🎯 Decision : Streaming tar.gz vs PharData

## Contexte

JT Migrate v1.0.0 utilisait `PharData` (Phar built-in PHP) pour créer/extraire les archives `.tar.gz`. Bug fatal sur sites > 100 MB : memory exhausted.

## Options considérées

### A. Garder PharData, augmenter memory_limit
- ❌ Sur WP.com Business pas modifiable
- ❌ Sur VPS standard, 1 GB+ requis pour archives > 300 MB → coûteux et fragile
- ❌ Ne scale pas avec la taille des sites

### B. `exec('tar -czf ...')` shell
- ✅ Très rapide, scalable
- ❌ Nécessite shell access — **WP.com Business interdit shell**
- ❌ Pas portable

### C. `ZipArchive` (PHP built-in)
- ✅ Streaming partiel
- ❌ Format ZIP pas idéal pour permissions Unix
- ❌ Pas optimisé pour gros fichiers (still loads index in RAM)

### D. **Streaming gzopen + USTAR custom** ✅
- ✅ Pure PHP, marche partout (WP.com Business OK)
- ✅ Memory constante quelle que soit la taille de l'archive (peak 0.6 MB sur 239 MB)
- ✅ Format USTAR standard, compatible `tar -tzf` GNU
- ❌ ~150 lignes PHP de header USTAR à écrire à la main (one-time effort)

## Choix : **D**

## Rationale

- Compatible avec **toutes** les configs WP (cloud + VPS + shared hosting)
- Scaling **constant** en mémoire (0.6 MB) quelle que soit l'archive (1 MB ou 10 GB)
- Format **portable** (USTAR = standard POSIX, lu par tous les outils)
- Code **maintenable** (~80 lignes d'écriture, ~80 lignes de lecture, bien commenté)

## Implementation

- Export streaming en [[JT-Migrate-v1.1.0]]
- Extract streaming en [[JT-Migrate-v1.2.1]] (miroir)
- Headers USTAR via `pack('a100a8a8a8a12a12A8a1a100a6a2a32a32a8a8a155a12', ...)` + checksum manuel
- Lecture par chunks de 64 KB

## Tests

- Round-trip md5 : OK sur 1795 fichiers / 321 MB
- Compatible `tar -tzvf` GNU : OK
- Compatible `PharData::extract` (qui peut être utilisé en lecture sur petits fichiers) : OK

## Liens

- [[Plugin-jt-migrate]]
- [[Bug-PharData-RAM-OOM]]
