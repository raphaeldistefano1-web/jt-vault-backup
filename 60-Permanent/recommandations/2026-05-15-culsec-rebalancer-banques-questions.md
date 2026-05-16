---
applies_to: /Users/raphia/Documents/dev/culsec/data/questions/*
backlinks:
- 2026-05-07-pipeline-3-couches-ingestion-curation-livraison
- 2026-05-09-anti-pattern-redonder-info-du-contexte-injecté
- 2026-05-10-page-à-propos-couleur-fond-nos-valeurs-trop-foncée
date: 2026-05-15
session_id: culsec-algo-adaptatif
status: pending
target: pms
type: improvement
urgency: medium
---

## Constat

La simulation 3-personas de l'algo adaptatif (`npm run sim:personas`) montre que les profils décisifs (chill, trash) adaptent nettement (thèmes aimés ×1.2, détestés ×0.6) mais qu'un profil aux goûts "quotidien/léger" (boulot, argent, culture-fr) reste plat. Cause isolée : **déséquilibre des banques**. Dans `picolo` (200 prompts) : `sexe`=66 (33%), `amitié`=24, `honte`=20… mais `culture-fr`=4, `famille`=8, `argent`=9, `voyage`=0. En mode normal (soft+medium éligibles), les thèmes "wholesome" ne pèsent que ~20% du pool servable. L'algo ne peut (ni ne doit, anti-répétition) servir beaucoup d'un thème quasi-absent.

## Pourquoi c'est utile

L'algo adaptatif est plafonné par l'offre : un segment d'utilisateurs réel (soirées famille/amis, humour bureau, pas-trash) aura une expérience peu personnalisée non par faute d'algo mais de catalogue. Rééquilibrer le contenu a un ROI bien supérieur à tout réglage de paramètre, et élargit l'audience (pas que les groupes "chauds"). Risque inverse : sur-représentation `sexe` peut rebuter/segmenter.

## How to apply

1. Auditer les 9 banques `data/questions/*.ts` : compter prompts par (theme × intensity) — réutiliser le snippet du harnais (`scripts/persona-sim.mjs`, bloc "ground truth").
2. Cibler un plancher par thème non-marginal : viser ≥ 25-30 prompts pour `culture-fr`, `famille`, `argent`, `voyage`, `ado` dans picolo (vs 4-9 aujourd'hui), en intensités soft+medium prioritairement.
3. Réduire la part `sexe` de ~33% à ~20-22% (ne pas supprimer, redistribuer l'effort de rédaction des prochains ajouts).
4. Re-run `npm run sim:personas` : le persona "mixte/quotidien" doit passer de 🟡 OFFRE-LIMITÉ à ✅ (offre max des thèmes aimés > 24%).
5. Idem rapide pour `je-nai-jamais` / `action-verite` (mêmes ratios observés).
Temps estimé : rédaction contenu ~3-4 h (ou délégable à Codex/IA pour la génération de prompts, relecture humaine). Qui agit : Raphaël (curation éditoriale).