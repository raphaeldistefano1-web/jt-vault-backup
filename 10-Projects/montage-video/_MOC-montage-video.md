---
id: 20260507-1107-moc-montage-video
type: moc
title: "MOC Montage Vidéo automatique"
project: montage-video
area: null
status: active
confidence: medium
summary: "Pipeline auto-montage Whisper→Claude→FFmpeg pour vidéo cours marketing (Agents IA Marketing)."
intent: reference
entities: [whisper, ffmpeg, video, marketing, montage]
topic_cluster: content-pipeline
related: []
moc: "[[INDEX]]"
source: null
tier: warm
created: 2026-05-07
updated: 2026-05-07
last-accessed: 2026-05-07
embed_model_version: null
embed_hash: null
tags: [video, ai, moc]
ai_writable: false
---

# 🎬 MOC — Montage Vidéo automatique

> Pipeline auto-montage **Whisper → Claude → FFmpeg** pour vidéo cours marketing.

## Mémoire CC associée
- `project_montage_video.md` — Base reçue via partage code ZDRFCGB7 le 2026-05-03

## Stack envisagée
- **Transcription** : Whisper large-v3-turbo (déjà installé sur VPS, cf. `reference_whisper_vps.md`)
- **Analyse** : Claude (sélection moments forts, génération cuts)
- **Montage** : FFmpeg (cuts + transitions)

## TODO
- Définir l'architecture du pipeline
- Atomic notes : prompt patterns, FFmpeg commands recipes
