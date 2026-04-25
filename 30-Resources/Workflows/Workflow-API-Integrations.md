---
type: workflow
status: active
tags: [workflow, api, integrations, security]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "Toute clé API externe passe par /dashboard/settings/integrations — jamais d'édition .env côté user"
ai_writable: false
related:
  - "[[PMS-Settings-Hub]]"
  - "[[Dev-PMS-Area]]"
---

# 🔑 Workflow API Integrations

## Règle

Toute clé API externe (Stripe, Brevo, OVH, Claude, OpenAI…) **doit** passer par l'UI `/dashboard/settings/integrations` du [[Dev-PMS-Area|PMS]].

**Jamais** d'édition `.env` côté user ni de hardcoding dans le code.

## Why

- Sécurité : clés stockées chiffrées en DB, pas en plain text dans un fichier
- UX : [[User-Raphael-Distefano|Raphaël]] peut changer une clé sans toucher au déploiement
- Audit : trace de qui/quand a changé quoi
- Multi-env : prod / staging / dev avec clés différentes propres

## Implémentation

- Page UI : `/dashboard/settings/integrations` — formulaire pour chaque service
- Storage : table `integrations` en DB Prisma, valeurs **chiffrées** (clé maître via env var serveur)
- Code : helper `getApiKey('stripe')` qui décrypte à la volée, jamais de lecture directe `process.env.STRIPE_KEY` dans la logique métier

## Services couverts

- Stripe (paiements)
- Brevo (emails transactionnels)
- OVH (DNS, mail)
- Claude / OpenAI (IA via [[Plugin-OpenClaw]])
- (à compléter)

## Liens

- [[PMS-Settings-Hub]]
- Mémoire référence : `api_integrations_rule.md` (mémoire projet PMS)
