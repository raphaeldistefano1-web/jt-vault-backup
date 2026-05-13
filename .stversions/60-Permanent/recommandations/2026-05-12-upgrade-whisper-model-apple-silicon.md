---
type: improvement
target: system
status: pending
urgency: low
date: 2026-05-12
session_id: 9b59e5d9-ac11-4228-906f-1c63d145eeb8
applies_to: ~/veille-ia/config/.env (WHISPER_MODEL)
---
# Upgrader WHISPER_MODEL vers large-v3-turbo sur Mac Mini

## Constat

Actuellement `WHISPER_MODEL=base` (~150 MB, ~1.3× realtime sur CPU VPS Hostinger). Le choix datait du VPS où on voulait économiser CPU/RAM la nuit (cf. mémoire `project_veille_ia.md` "Whisper passé en `base` 2026-05-07").

Sur Mac Mini Apple Silicon (M1/M2/M3, ARM64 natif), `faster-whisper` + `ctranslate2` tournent **plus rapidement** qu'un VPS 2 vCPU AMD EPYC. Le compromis vitesse/qualité n'est plus le même.

`large-v3-turbo` (~1.6 GB, qualité supérieure surtout sur non-anglais : thaï, chinois, japonais, coréen) tournerait probablement à ~0.5-1× realtime sur Mac, ce qui reste largement acceptable pour 20 vidéos/nuit.

## Pourquoi

Qualité de transcription meilleure → meilleur input pour Sonnet en analyse → digest plus précis (surtout pour les vidéos asiatiques que Raphaël veut suivre). Coût : 1.6 GB de download initial + ~30 sec/vidéo de plus en moyenne.

Pas urgent : l'ingest passe à 90% sur subs natifs YouTube (testé E2E le 2026-05-12 : 2/2 anglais via subs, Whisper jamais déclenché). Whisper n'intervient qu'en fallback pour les rares vidéos sans subs.

## How to apply

**Estimation : 5 min de modif + ~5-10 min de download au 1er run, à ma charge (Claude)**

1. Éditer `~/veille-ia/config/.env` : `WHISPER_MODEL=base` → `WHISPER_MODEL=large-v3-turbo`
2. Lancer un test avec une vidéo sans subs natifs (ex : vidéo thaï) :
   ```bash
   ~/veille-ia/.venv/bin/python ~/veille-ia/bin/whisper-cli.py <audio.mp3> --model large-v3-turbo
   ```
3. Mesurer le temps réel vs la durée audio (objectif < 1× realtime)
4. Si OK : laisser en config. Sinon : revert à `base`.

Alternative envisageable plus tard : utiliser `whisper.cpp` avec Metal pour accélération GPU Apple Silicon (faster-whisper / CTranslate2 n'a pas de backend Metal natif). Plus de boulot (refactor `whisper-cli.py`), à creuser si la qualité de `large-v3-turbo` en CPU est insuffisante.

## Liens

- [[project_veille_ia]]
- [[reference_whisper_vps]] — ancienne config Whisper VPS (à dépréc)
