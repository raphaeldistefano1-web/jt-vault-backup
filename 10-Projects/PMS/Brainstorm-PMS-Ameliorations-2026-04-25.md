---
type: project
status: active
tags: [pms, brainstorm, ux, design]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "Brainstorm complet améliorations PMS — quick wins UX/perf + investissements + anti-patterns à éviter"
ai_writable: true
related:
  - "[[Tests-PMS-Batterie-2026-04-25]]"
  - "[[PMS-Stack]]"
  - "[[Dev-PMS-Area]]"
---

# 💡 Brainstorm PMS Améliorations — 2026-04-25

Synthèse de la recherche UX hôtellerie 2026 (HippoRAG-style retrieval) + analyse codebase + tests fonctionnels.

## ⭐ Quick wins (ROI élevé, effort 0.5-2j)

### QW1 — Color + icône + texte sur statuts (a11y daltonisme)
**Impact** : élevé sur a11y + UX pour 8% des hommes (daltonien)
**Effort** : 0.5j
**Plan** :
- Créer `<StatusBadge variant="confirmed|pending|checkedin|noshow|cancelled" />` — affiche bordure colorée + icône Lucide + texte court
- Remplacer progressivement les usages dans Calendar, frontdesk, list reservations
- Tokens dans Tailwind config : `status-confirmed: oklch(...)`, etc.
**Non-irréversibilité** : composant ajouté à côté de l'existant, migration progressive

### QW2 — Command palette Cmd+K
**Impact** : très élevé pour power user solo (Raphaël utilise PMS 4h/jour)
**Effort** : 1j
**Plan** :
- Lib `cmdk` (~3 KB gzip) — déjà présent dans le composant `CommandPalette.tsx` mais probablement basique
- Étendre pour : recherche fuzzy résa par ref/nom/email, "nouvelle résa", "aller à chambre N", filters arrivées/départs, navigate Cmd+G+R
- Activer Cmd+K (macOS) / Ctrl+K (Windows/Linux)
**Non-irréversibilité** : composant déjà présent, ajout de nouvelles commandes

### QW3 — Dark mode (mode soir reception)
**Impact** : moyen-élevé (confort soir frontdesk, tendance 82% adoption 2026)
**Effort** : 0.5j
**Plan** :
- `next-themes` package
- Toggle dans Settings ou raccourci Cmd+J
- Tokens via `dark:` Tailwind variants
- Theme-color meta tag adapté
**Non-irréversibilité** : feature opt-in, défaut clair

### QW4 — Skeleton screens (vs spinners)
**Impact** : moyen (gain 20-30% perceived load)
**Effort** : 1j
**Plan** :
- Identifier pages avec spinners (Suspense fallbacks)
- Remplacer par `<Skeleton>` patterns (déjà présent dans `ui/Skeleton.tsx`)
- Pour data-heavy : tables avec 5-10 lignes skeleton
**Non-irréversibilité** : remplacement local, fallbacks Suspense

### QW5 — Brief journée IA matinal
**Impact** : élevé (valeur concrète quotidienne)
**Effort** : 2j
**Plan** :
- Cron 8h auto-genère prompt structuré : arrivées/départs/encours/météo/spéciales
- LLM appelé via OpenClaw Gateway → réponse stockée
- Affiché en haut du dashboard
- Cache jusqu'à 18h, regen sur demande
**Non-irréversibilité** : feature additive, peut être désactivée via setting

### QW6 — KPI strip dashboard simplifié à 6 métriques
**Impact** : élevé (clarté vs paralysie info)
**Effort** : 1j
**Plan** :
- Réduire à : Occupation jour, Arrivées jour, CA jour (encaissé/dû), Occupation 7j (sparkline), ADR mois vs N-1, Encours impayés
- Détails (RevPAR, ALOS, % direct vs OTA, conversion) → page `/dashboard/reports`
**Non-irréversibilité** : composant `KpiStrip` à update, ancien gardé en `KpiStripFull`

### QW7 — Undo toast 5s sur actions reversibles
**Impact** : élevé (anti-friction, UX moderne)
**Effort** : 0.5j
**Plan** :
- Lib `sonner` (Tailwind native, 4 KB)
- Pattern : check-in, check-out, marquage payé, modif statut → toast avec "Annuler" pendant 5s
- Si cliqué → revert action (delayed dispatch)
**Non-irréversibilité** : feature additive

### QW8 — Optimistic UI sur drag-drop calendar
**Impact** : très élevé (friction calendar = quotidien)
**Effort** : 1j
**Plan** :
- `@tanstack/react-query` (déjà installé probablement)
- `useMutation` avec `onMutate` qui apply localement, `onError` revert
- Calendar feels instantané, no lag UX
**Non-irréversibilité** : pattern à wrapper dans hooks dédiés

### QW9 — Pre-check-in lien email J-1
**Impact** : très élevé (UX guest + frontdesk)
**Effort** : 2j
**Plan** :
- Cron 18h envoie email J-1 avec lien public signé `/checkin/{token}`
- Page publique demande : ID, signature, demande spécifique chambre
- Frontdesk arrivée = 1 click "Confirmer arrivée" (vs full data entry)
**Non-irréversibilité** : feature opt-in (si activée)

### QW10 — Page `?` raccourcis clavier
**Impact** : moyen (discoverability raccourcis)
**Effort** : 0.5j
**Plan** :
- Modal qui s'ouvre sur `?`
- Liste tous les raccourcis disponibles
- Inspirée de Linear, Notion
**Non-irréversibilité** : modal, désactivable

## 🏗️ Investissements (1-3 semaines)

### INV1 — Calendar Gantt drag-resize-extend complet
- @dnd-kit/core + react-virtual pour 60-90j × 14 rooms
- 3 vues (7j/14j/60j), filtres chips, bulk actions
- 1-2 semaines

### INV2 — Module housekeeping mobile PWA
- Compagnon Electron desktop (déjà fait)
- PWA mobile : task list, status update, push notifs
- 1 semaine

### INV3 — AI assistant contextuel (passe résa courante en context)
- System message enrichi avec données résa
- RGPD : pseudonymisation noms avant LLM
- 1 semaine

### INV4 — Forecasting basique 90j (compare N-1/N-2)
- SQL avec moyenne mobile saisonnière pondérée
- Pas de ML, juste heuristique pertinente
- 1 semaine

### INV5 — Refonte design system tokens @theme Tailwind v4
- Si pas déjà sur Tailwind v4 — mode oklch, native CSS vars
- Migration par batch (composants UI primitives d'abord)
- 1 semaine

## 🚫 Anti-patterns à éviter (waste-of-time)

- **Native iOS/Android app** — PWA suffit, ROI inexistant à 14 chambres
- **AI no-show prediction** — volume insuffisant pour signal statistique
- **AI pricing dynamique custom** — RoomPriceGenie dispo si besoin réel
- **Multi-langue admin interne** — Raphaël francophone solo
- **Chatbot 24/7 client** — nuit perception qualité à cette échelle
- **Reports >10 metrics dashboard quotidien** — paralysie info
- **Modals avec tabs** — c'est une page
- **Confirmation modals abusifs** — toast undo suffit
- **Couleur seule pour statut** — toujours redondance icône + texte
- **Spinners full-screen** — skeleton screens

## 🐛 Fixes simples détectés (pendant tests)

### Fix 1 — Documenter PATCH-only dans `/api/reservations/[id]/route.ts`
Ajouter commentaire en tête expliquant que `PUT` et `DELETE` ne sont pas exposés (annulation = PATCH status='CANCELLED').

### Fix 2 — Inconsistance params `/api/calendar` vs `/api/public/availability-calendar`
Public API utilise `from`/`to`, internal API utilise `start`/`end`. À uniformiser sur `from`/`to` + alias backward-compat.

### Fix 3 — Vérifier seed Bungalow 7 et 8 absents
Confirmer avec Raphaël si volontaire (superstition asiatique skip) ou bug.

### Fix 4 — `HotelConfig.aiActiveProvider = OPENAI` mais pas de clé
Soit configurer OPENAI_API_KEY en env, soit changer aiActiveProvider en ANTHROPIC, soit gracefully error si pas de clé (au lieu de fatal).

## 🎯 Priorité suggérée

**Cette semaine** :
1. Fix 1+2 (documentation + alias params API) — 1h
2. QW10 (raccourcis clavier modal `?`) — 0.5j
3. QW1 (StatusBadge color+icon+texte) — 0.5j

**Semaine suivante** :
4. QW2 (Command palette Cmd+K enrichi) — 1j
5. QW7 (Undo toast) — 0.5j
6. QW6 (KPI strip simplifié) — 1j

**Mois prochain** :
7. QW3 (Dark mode) — 0.5j
8. QW5 (Brief journée IA) — 2j
9. QW8 (Optimistic UI calendar) — 1j

**Quand l'investissement vaudra le coup** :
10. INV1 (Calendar Gantt complet)
11. QW9 (Pre-check-in J-1 email)

## Liens

- [[Tests-PMS-Batterie-2026-04-25]]
- [[PMS-Stack]]
- [[Dev-PMS-Area]]
- [[Workflow-Preview-Then-Apply]]
