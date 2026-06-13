---
ai_writable: true
area: null
backlinks:
- _Index
capture_source: claude-mem
confidence: medium
created: 2026-06-12
cwd: ''
embed_hash: null
embed_model_version: null
entities: []
id: 202606121300-claudemem-d67ad42c
intent: log
last-accessed: 2026-06-12
moc: null
n_files_edited: 0
n_files_read: 0
project: claude-system
related: []
schema_version: 1
session_id: d67ad42c-df07-4eb9-baa6-d35af5bf1064
source: claude-mem:session_summaries#168
status: draft
summary: 'Strategic feature triage completed: identified 5 core visible features (calendar,
  unified inbox, booking card, invoicing, reception), 4 invisible automated operations
  (OTA sync, satisfaction emails, relance'
tags:
- session
- log
- ai-generated
tier: cold
title: 'Resume Caribbean hotel PMS project with strategic repositioning: shift from
  feature-rich accounting'
topic_cluster: session-log
type: meeting
updated: 2026-06-12
---

# Session (claude-mem) — Resume Caribbean hotel PMS project with strategic repositioning: shift from feature-rich accounting

> Capture semantique claude-mem (2026-06-12). Source plus riche que le hook extract_memory (compression LLM). Sera raffinee par le vault-synthesizer.

## Metadonnees

- **Projet** : `raphia`
- **Session ID** : `d67ad42c-df07-4eb9-baa6-d35af5bf1064`
- **Working dir** : ``
- **Source** : `claude-mem` (session_summaries #168)

## Demande

Resume Caribbean hotel PMS project with strategic repositioning: shift from feature-rich accounting system to simplified, hôtelier-friendly product with unified calendar, booking management, OTA sync, and automated workflows.

## Investigue

Reviewed all existing PMS context (April 2026 state, October pivot, desktop app, 12 n8n workflows, OpenClaw AI routing). Examined feature inventory and categorized by visibility/automation model. Identified two structural decision points: channel manager build-vs-buy approach and mono-tenant vs multi-tenant product architecture.

## Appris

Distinction between "surface simplicity" (what hôtelier sees) vs "feature simplicity" (what functions exist) — the strategy is hide complex operations behind clean UI, not reduce capabilities. Core hôtelier workflow centers on unified calendar view across all OTA channels. Heavy accounting (TVA export, grand-livre, KPIs like RevPAR) misaligned with target user (8-room independent operators). Existing n8n automation workflows (satisfaction emails, conflict alerts, relance) should remain invisible backend operations, not exposed as configuration interface. Critical risk: no validation with actual Caribbean hotel owners beyond founder's father.

## Realise

Strategic feature triage completed: identified 5 core visible features (calendar, unified inbox, booking card, invoicing, reception), 4 invisible automated operations (OTA sync, satisfaction emails, relance flows, weekly reports), and features to defer/cut (heavy compta module, TVA export, RevPAR dashboards, AI memory config UI). Proposed 5 new capabilities (proprietary booking engine on website, digital check-in, one-click payment links, done-for-you onboarding, mobile-first interface).

## Prochaines etapes

Awaiting decision on: (1) Channel manager strategy — build in-house vs integrate existing API (Channex/Beds24/Smoobu). (2) Whether to audit current PMS codebase first to understand actual vs stubbed functionality (especially OTA sync maturity and invoicing). Two blockers before architecture/code work begins.

## Notes

Session is strategic framing, not implementation. Critical unknowns: current OTA sync implementation state unknown (ota.sync_failed events exist but maturity unclear). Product positioning shift from complexity-hiding (LJT-specific) to simplicity-first (multi-hôtelier market) requires architectural decision on multi-tenancy. Founder has not validated core assumptions with target market (Caribbean hotel owners) beyond family. Strategic risk of building perfect solution for wrongly-assumed problem.

## TODO curator

- [ ] Raffiner le `summary` a partir du contenu reel
- [ ] Decider du `tier` final (hot/warm/cold)
- [ ] Ranger dans le bon projet ou decomposer en notes atomiques
- [ ] Ajouter wikilinks vers MOCs et notes liees
- [ ] Dedup vs note extract_memory de la meme session si presente