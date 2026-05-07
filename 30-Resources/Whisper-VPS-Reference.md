---
id: 20260507-1130-whisper-ref
type: reference
title: Whisper large-v3-turbo VPS — Paths, usage, performances
project: null
area: null
status: active
confidence: high
summary: faster-whisper + modèle 1.6GB. CLI /usr/local/bin/whisper. ~0.29x realtime CPU int8. Formats txt/srt/vtt/json.
intent: how-to
entities: [whisper, transcription, faster-whisper, vps, cli, performance]
topic_cluster: null
related: ["[[Stack-Tech]]", "[[project_montage_video]]"]
moc: "[[Stack-Tech]]"
source: "memory:reference_whisper_vps.md"
tier: warm
created: 2026-05-07
updated: 2026-05-07
last-accessed: 2026-05-07
embed_model_version: null
embed_hash: null
tags: [whisper, transcription, vps]
ai_writable: true
---

# Whisper large-v3-turbo VPS — Paths, usage, performances

> Note portée depuis la mémoire Claude Code `reference_whisper_vps.md` le 2026-05-07.

Installé le 2026-05-06 sur le VPS Hostinger srv1524600. Backend = `faster-whisper` (CTranslate2), modèle = `mobiuslabsgmbh/faster-whisper-large-v3-turbo`.

## Paths

- Venv Python : `/opt/whisper/venv` (Python 3.12, faster-whisper 1.2.1, CTranslate2 4.7.1)
- Cache modèles : `/opt/whisper/models/` (1.6 GB pour large-v3-turbo)
- Script Python : `/opt/whisper/transcribe.py` (CLI complet, formats txt/srt/vtt/json)
- Wrapper PATH : `/usr/local/bin/whisper` (chmod 755)

## Usage

```bash
whisper audio.mp3                              # défaut: large-v3-turbo, lang auto, sortie .txt
whisper audio.mp3 --lang fr --out-format srt   # forcer FR + sous-titres
whisper audio.mp3 --out-format json --out /tmp/out.json
whisper audio.mp3 --compute-type int8_float16  # plus précis, plus lent
whisper audio.mp3 --threads 2                  # forcer threads CPU (défaut: auto)
whisper audio.mp3 --no-vad                     # désactiver VAD silero
```

Sortie écrite à côté du fichier source (même basename, extension du format).

## Performances mesurées

- Chargement modèle : 6-7s (premier load)
- Inférence CPU 2 cores int8 : **~0.29x realtime** → 1h d'audio ≈ 3.5h de transcription
- RAM utilisée pendant inférence : ~1.5-2 GB (sur 7.8 GB total, 0 swap)
- Pour audio long > 30 min : lancer en background ou via tmux

## Modèles dispo (téléchargement automatique au 1er appel)

- `tiny` (75 MB), `base` (140 MB), `small` (460 MB), `medium` (1.5 GB), `large-v3` (3 GB), `large-v3-turbo` (1.6 GB) **← installé**
- Pour changer : `whisper audio.mp3 --model small` (download au 1er run)

## Pièges connus

- **Pas de GPU** sur ce VPS → impossible d'utiliser `device=cuda` ou `compute_type=float16`. Toujours `device=cpu` + `compute_type=int8`.
- **RAM tight** : si PMS Next.js + n8n + OpenClaw tournent en parallèle d'une transcription longue, surveiller `free -h`. Pas de swap configuré.
- **Pas réinstallé pip global** : tout est dans `/opt/whisper/venv`, donc invisible aux autres `python3` du système.
- **Test espeak-ng peu représentatif** : la voix synthétique espeak donne une transcription dégueulasse, mais Whisper est entraîné sur de la vraie voix → qualité réelle bien meilleure sur audio humain.

## Cas d'usage prévus

- Pipeline montage vidéo Marketing IA : transcription des cours pour découpe automatique via Claude
- Transcription de réunions ou notes vocales si besoin

## Liens
- MOC parent : [[Stack-Tech]]
- Référence vidéo : [[project_montage_video]]
- Source : `memory:reference_whisper_vps.md`
