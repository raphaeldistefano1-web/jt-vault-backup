---
id: autonomy_log
title: Log autonomie Claude — 2 semaines d'observation
created: 2026-05-12
end_date: 2026-05-26
status: active
purpose: Mesurer si construire un Claude autonome 24/7 sur Mac Mini en vaut le coup
related: [[60-Permanent/decision-claude-autonomy-mac-mini]]
---

# Log autonomie Claude (2026-05-12 → 2026-05-26)

## Pourquoi ce log

Avant d'investir dans un système d'agent autonome 24/7 sur le Mac Mini dédié, mesurer si le backlog réel de tâches "délégables à un stagiaire nocturne" justifie l'effort.

Deux peer-reviews indépendants (Codex + idea-critic adversarial) ont convergé sur ce verdict : **construire l'autonomie d'abord et mesurer après = piège classique**. Probabilité forte que le coût de maintenance > gains, surtout avec Claude Code Cloud qui arrive d'ici 6-12 mois.

## Seuil de décision (le 2026-05-26)

- **<8h/semaine** de tâches mécaniques + réversibles + non-prod → **KILL** le projet d'autonomie. On attend Claude Code Cloud, on garde le Mac Mini comme booster compute (Ollama, Whisper, embeddings).
- **>8h/semaine** → **PURSUE** version scopée "stagiaire nocturne avec liste de courses bornée" — avec les 5 garde-fous obligatoires d'abord (trust boundary content/instructions, permission model computer-use, job ledger idempotent, fallback quota, scope email client).

## Comment logger (téléphone-friendly)

Chaque fois que tu te dis **"j'aimerais qu'un agent fasse ça pendant la nuit"**, ajoute une ligne en bas du tableau. Pas besoin d'être exhaustif — vise les tâches mécaniques que tu reportes parce que tu n'as pas le temps.

## Critères de "délégable à un stagiaire nocturne"

- **Mécanique** : refactor de masse, tests unitaires sur module stable, conversion format (JSON↔YAML, OpenAPI→TS), scaffolding CRUD, doc auto JSDoc, boilerplate Zod/Prisma, recherche cross-fichiers
- **Réversible** : passe par branche dédiée, jamais commit direct sur main, dry-run par défaut
- **Non-prod** : pas le PMS en prod, pas envoi email client, pas dépense, pas DB production write
- **Exclus** : architecture, debug profond, code review qualité, communication externe, décisions stratégiques

## Tableau de log

| Date | Tâche | Projet | Durée est. | Critique ? | Réversible ? | Délégable ? |
|------|-------|--------|------------|------------|--------------|-------------|
| 2026-05-12 | _(exemple)_ Ajouter tests Vitest sur module pricing PMS | pms-jardin-tropical | 2h | Non-prod | Oui (branche) | ✅ |
|      |       |        |            |            |              |             |

## Bilan provisoire

_(mis à jour automatiquement chaque dimanche soir par le synthesizer vault)_

- Semaine 1 (12 → 18 mai) : à remplir
- Semaine 2 (19 → 25 mai) : à remplir
- **Total heures délégables identifiées** : 0h
- **Verdict provisoire** : trop tôt pour conclure

## Décision finale

À écrire le 2026-05-26 après bilan. Format ADR : `~/Documents/vault/10-Projects/claude-system/Decisions/0001-claude-autonomy-go-no-go.md`.
