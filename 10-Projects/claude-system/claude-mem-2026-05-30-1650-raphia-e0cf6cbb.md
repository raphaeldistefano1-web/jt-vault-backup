---
ai_writable: true
area: null
backlinks:
- _Index
capture_source: claude-mem
confidence: medium
created: 2026-05-30
cwd: ''
embed_hash: null
embed_model_version: null
entities: []
id: 202605301650-claudemem-e0cf6cbb
intent: log
last-accessed: 2026-05-30
moc: null
n_files_edited: 0
n_files_read: 0
project: claude-system
related: []
schema_version: 1
session_id: e0cf6cbb-2c5f-4958-96f8-098b02089226
source: claude-mem:session_summaries#35
status: draft
summary: 'User formalized content quality requirements in rf-feedback-distilled.md
  capturing: problem (repetitive lazy penalty formulas), required varied mechanics
  (winner distributes, same-answer penalties, voting, duels, conditional success/failure),
  intensity'
tags:
- session
- log
- ai-generated
tier: cold
title: 'Resume Cyclone question bank overhaul: refactor Rapid Fire + all 5 modes'
topic_cluster: session-log
type: meeting
updated: 2026-05-30
---

# Session (claude-mem) — Resume Cyclone question bank overhaul: refactor Rapid Fire + all 5 modes

> Capture semantique claude-mem (2026-05-30). Source plus riche que le hook extract_memory (compression LLM). Sera raffinee par le vault-synthesizer.

## Metadonnees

- **Projet** : `raphia`
- **Session ID** : `e0cf6cbb-2c5f-4958-96f8-098b02089226`
- **Working dir** : ``
- **Source** : `claude-mem` (session_summaries #35)

## Demande

Resume Cyclone question bank overhaul: refactor Rapid Fire + all 5 modes with refined content quality rules and fix crew member selection to be equitable

## Investigue

User explored existing codebase: AppModel architecture, PromptMode UI layer, GameBank.swift player substitution logic (PromptTokenizer.interpolate and firstTarget), PromptDrawer session management, CycloneEngine game selection, Mulberry32 RNG. Analyzed existing 6 question banks (1,407 total questions across rapid-fire, action-verite, je-nai-jamais, most-likely, shes-a-ten, tu-preferes) and confirmed current deficiencies: hard intensity at 12–19% (target 35%), repetitive Cyclone penalty formulas ("si tu te dégonfles", "refuse = X", "le perdant"), excessive duplicates, bland soft questions. Validated schema: flat JSON arrays with exactly 4 fields (id, text, intensity, theme), no separate gage field.

## Appris

Cyclone penalty mechanics (tokens {p1}/{p2}) are applied in PromptMode.swift:refreshInterpolation() using a seed-based shuffle per card. Current shuffle-based approach refactors players on every card → clustering and unequal distribution. Player selection issues: (1) PromptTokenizer.interpolate creates new shuffle each time, (2) firstTarget does independent shuffle → mismatch between "À TOI" header player and {p1} in text, (3) no shuffle-bag state across session. Existing code architecture is modular: PromptDrawer manages session state, TasteEngine handles flavor scoring, Mulberry32 provides deterministic RNG. Content schema is strict: intensity ∈ {soft, medium, hard}, no alcohol words, Cyclone written in text not as separate field.

## Realise

User formalized content quality requirements in rf-feedback-distilled.md capturing: problem (repetitive lazy penalty formulas), required varied mechanics (winner distributes, same-answer penalties, voting, duels, conditional success/failure), intensity targets (30% soft / 35% medium / 35% hard), Cyclone prevalence (~50% of cards only), deduplication rules, formulation specificity. Launched Workflow v2 (wf_63ceb8f9-1fb) with 3-phase orchestration: Phase 1 = bugfix crew selection (shuffle-bag equitable algorithm for 1–15+ players, no consecutive duplicates, {p2}≠{p1}, cohesive "À TOI" pastille), Phase 2 = parallel regeneration of 6 game modes (~210–240 questions each, precise content rules), Phase 3 = QC validation (JSON schema, intensity distribution ≥30% hard, zero alcohol words, zero banned formulas, deduplication, ID uniqueness).

## Prochaines etapes

Workflow agents executing asynchronously (bugfix agent working on PromptScheduler redesign for shuffle-bag, 6 generation agents rebuilding question banks in parallel, 6 QC agents validating). Awaiting: (1) crew selection bugfix implementation + test results, (2) regenerated JSON files for all 6 modes + content reports, (3) QC pass/fail verdicts per mode. User will review output, iterate on any QC failures or content quality issues.

## Notes

User excluded Imposteur (7th mode) from refonte as it's a word-secret game, not a question-gage game—mechanically incompatible with hard/sexual content overhaul. Decision point deferred: user to confirm if Imposteur word list should be enriched separately. Workflow v2 incorporates corrected understanding of actual JSON schema (flat arrays, no separate "cyclone" field) and precise file locations (GameBank.swift lines 178–200 for crew fix). Session baseline: ~1,407 existing questions, current hard% 12–19%, target hard% ≥35%, zero duplicates post-overhaul.

## TODO curator

- [ ] Raffiner le `summary` a partir du contenu reel
- [ ] Decider du `tier` final (hot/warm/cold)
- [ ] Ranger dans le bon projet ou decomposer en notes atomiques
- [ ] Ajouter wikilinks vers MOCs et notes liees
- [ ] Dedup vs note extract_memory de la meme session si presente