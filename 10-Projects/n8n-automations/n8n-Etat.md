---
id: 20260507-1124-n8n-etat
type: project
title: n8n + Bus d'événements PMS — État (post-session 26-04)
project: n8n
area: null
status: active
confidence: high
summary: 12 workflows actifs + bus events PMS. Refonte avis Google avec IA. 19 events versionnés. Cron 8 tâches automatisées.
intent: log
entities: [n8n, workflow, event-bus, pms, automation, google-reviews]
topic_cluster: n8n
related: ["[[_MOC-n8n]]", "[[n8n-Reference]]"]
moc: "[[_MOC-n8n]]"
source: "memory:project_n8n_automations.md"
tier: hot
created: 2026-05-07
updated: 2026-05-07
last-accessed: 2026-05-07
embed_model_version: null
embed_hash: null
tags: [n8n, automation, workflows]
ai_writable: true
---

# n8n + Bus d'événements PMS — État

> Note portée depuis la mémoire Claude Code `project_n8n_automations.md` le 2026-05-07.

État complet de l'automatisation digitale du Jardin Tropical après les 2 grosses sessions n8n (2026-04-25 setup + 2026-04-26 bibliothèque + refonte).

**Why:** Ne pas redécouvrir à chaque session. État canonique pour repartir directement sur l'évolution (config clés API, ajout workflows, fix bugs).

## Architecture livrée

```
┌─────────────────────────┐         signed HMAC          ┌─────────────────────┐
│  PMS Next.js :3000      │ ──── /webhook/<path> ───→   │  n8n container      │
│  emitPmsEvent('x.y',pl) │                              │  12 workflows actifs│
└─────────────────────────┘                              └─────────┬───────────┘
            ▲                                                       │
            │   X-Cron-Secret + 8 actions                          │
            │ ◄─────── /api/webhooks/n8n ───────────────────────── │
            │                                                       │
            │   pms_event_log = source de vérité + replay          │
            │                                                       │
   /dashboard/automations ← UI admin (workflows, exécutions, events, replay)
   /dashboard/avis        ← UI drafts IA réponses Google (refonte #17)
```

## Sources de vérité

- **Définition events** : `src/lib/events/types.ts` (20 events versionnés v1)
- **Émetteur** : `src/lib/events/emitter.ts` (fire-and-forget, retry cron 5min)
- **Client n8n outbound** : `src/lib/n8n.ts` (HMAC sign + listWorkflows + activate)
- **Webhook entrant n8n→PMS** : `src/app/api/webhooks/n8n/route.ts` (8 actions + idempotency + filter @pms.internal/@guest.airbnb.com)
- **Helper timezone Guadeloupe** : `src/lib/date-guadeloupe.ts` (UTC-4)
- **UI hub automatisations** : `src/app/(dashboard)/dashboard/automations/`
- **UI avis Google** : `src/app/(dashboard)/dashboard/avis/` (refonte #17)
- **Cron Linux** : `/etc/cron.d/pms-jardin` (8 lignes : no-show 03h, cleanup-pending hourly, ota-sync :15, reminders 09h, invoices-overdue 09h05, n8n-retry */5min, daily-summary 11h UTC, evening-recap 01h UTC)
- **Bibliothèque workflows** : `/srv/n8n-workflows/templates/` (versionnée git, backupée daily)

## Workflows actifs (12) + 1 désactivé

| # | Nom | Trigger | Statut | Dépendance externe |
|---|---|---|---|---|
| 01 | PMS Event Router (HMAC + observability log) | webhook `/pms-event` | actif | — |
| 03 | Post-checkout demande avis Google J+3 | event `reservation.checked_out` | actif | BREVO |
| 12 | Evening recap Raphaël (21h Guadeloupe) | cron `0 1 * * *` | actif | BREVO |
| 13 | OTA conflict alert (WhatsApp + notification) | event `ota.conflict_detected` | actif | WhatsApp (notif fallback) |
| 14 | OTA sync failed (email Raphaël) | event `ota.sync_failed` | actif | BREVO |
| 15 | Daily backup DB (Backblaze) | cron `0 7 * * *` | désactivé | endpoint `/api/cron/db-backup` à créer |
| 17 | Avis Google — draft IA adapté + validation PMS | webhook externe `/google-review-inbound` | actif | Anthropic |
| 19 | Weather storm alert (cyclone Bouillante) | cron `0 10 * * *` | actif | OPENWEATHER + BREVO + WhatsApp |
| 20 | Fidélisation J+30 (email + offre) | event `reservation.checked_out` | actif | BREVO |
| 21 | Weekly occupancy report (dimanche 19h) | cron `0 23 * * 0` | actif | BREVO |
| 22 | Monthly TVA FEC export (1er du mois 07h) | cron `0 11 1 * *` | actif | BREVO (sinon fallback lien) |
| 23 | Inbound email triage (Claude classify + draft) | event `guest.message.received` | actif | Anthropic |
| 24 | Inbound WhatsApp triage (Meta + Claude) | webhook `/inbound-whatsapp` | actif | WhatsApp + Anthropic |
| 25 | Monthly paie prep | cron `0 11 25 * *` | désactivé | endpoint `/api/staff/monthly-hours` à créer |

## Refonte #17 (avis Google) — détail

Au lieu de drafter uniquement les avis < 4★, le workflow drafte pour TOUS les avis avec ton adapté au rating :
- **5★** : warm_thanks (chaleureux + invitation à revenir)
- **4★** : thanks_with_acknowledgment (remerciements + reconnaissance points d'amélioration)
- **3★** : balanced_acknowledgment (acknowledgement honnête + invitation dialogue)
- **1-2★** : empathy_resolution (empathie sincère + proposition résolution privée)

**Flow** :
1. Webhook externe `/google-review-inbound` (placeholder, à connecter à Google Business webhook)
2. Code node "extract & determine tone" — détermine système prompt selon rating
3. HTTP POST Anthropic (claude-sonnet-4-6, max 600 tokens)
4. POST `/api/reviews/inbound` (PMS) → crée draft en DB

**Côté PMS** :
- Table `google_review_drafts` (Prisma model `GoogleReviewDraft`, enum `ReviewDraftStatus`)
- 5 routes API :
  - `POST /api/reviews/inbound` (cron-secret/HMAC, idempotent par googleReviewId)
  - `GET /api/reviews/drafts?status=` (session auth)
  - `PATCH /api/reviews/drafts/[id]` (modifier draft)
  - `POST /api/reviews/drafts/[id]/send` (marque SENT — pas de publication Google API auto pour l'instant)
  - `POST /api/reviews/drafts/[id]/dismiss`
- Page `/dashboard/avis` : tabs filtre (À valider/Modifié/Envoyé/Ignoré), card par avis avec étoiles colorées + textarea inline + boutons (Enregistrer/Ouvrir Google/Ignorer/Marquer envoyé)

**Limite actuelle** : la publication automatique sur Google nécessite Google My Business API + OAuth (à charge dans to-do future).

## Migrations Prisma de la session

- `20260425230000_add_n8n_provider/migration.sql` — ALTER TYPE enum
- `20260425230100_pms_event_log/migration.sql` — table + 3 index
- `20260426110000_add_isvip_birthdate/migration.sql` — Reservation.isVip + Guest.birthdate
- `20260426120000_add_birthdate_index/migration.sql` — index fonctionnel EXTRACT(MONTH/DAY) sur birthdate
- `20260426130000_add_google_review_drafts/migration.sql` — GoogleReviewDraft + enum

## Comment ajouter un nouveau workflow

1. Créer `templates/NN-slug.json` en suivant le pattern d'un existant
2. Pattern HMAC verify obligatoire si event-driven
3. Pattern `jsonBody: "={{ JSON.stringify({...}) }}"` pour les HTTP POST
4. Idempotency : `X-Request-Id` + `requestId` dans body
5. `bash /srv/n8n-workflows/scripts/import-all.sh` (skip déjà importés)
6. Activation auto incluse
7. Sauvegarde auto dans `/srv/n8n-workflows/workflows/`
8. Documenter dans `/srv/n8n-workflows/templates/README.md`

## Pièges rencontrés et résolus

- **n8n v1.107+ refuse `require('crypto')` dans Code nodes** → ajout `NODE_FUNCTION_ALLOW_BUILTIN=crypto,buffer` dans docker-compose env
- **Pattern `jsonBody: "={...}"` (object literal direct) ne marche pas en v1.107** → utiliser `={{ JSON.stringify({...}) }}`
- **Pattern `??` (nullish coalescing) ne fonctionne pas dans expressions n8n** → remplacer par `||`
- **Pattern `?.` (optional chaining) idem** → remplacer par `($json.X && $json.X.Y)`
- **Bug timezone Guadeloupe (UTC vs UTC-4)** → helper `getTodayGuadeloupe()` créé
- **Stripe webhook n'émettait aucun event PMS** → patché avec emit `payment.succeeded`/`failed`/`refunded`
- **Doublons workflow 01 et 02** lors du re-import → désactiver via API avant nouveau import

## Liens
- MOC parent : [[_MOC-n8n]]
- Référence technique : [[n8n-Reference]]
- Source : `memory:project_n8n_automations.md`
