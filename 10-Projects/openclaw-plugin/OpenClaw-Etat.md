---
ai_writable: true
area: null
backlinks:
- 2026-05-11-service-worker-offline-pwa-stratégie-cache-first-m
- OpenClaw-Pieges-Dev
- OpenClaw-VPS-Reference
- _Index
- _VAULT-INDEX
confidence: high
created: 2026-05-07
embed_hash: null
embed_model_version: null
entities:
- openclaw
- plugin
- oauth-codex
- pms
- gateway
- ai-routing
id: 20260507-1116-openclaw-etat
intent: log
last-accessed: 2026-05-07
moc: '[[_MOC-openclaw]]'
project: openclaw
related:
- 2026-05-16-culsec-premium-validation-serveur
- '[[OpenClaw-Pieges-Dev]]'
- '[[OpenClaw-VPS-Reference]]'
- '[[_MOC-openclaw]]'
source: memory:project_openclaw_plugin.md
status: active
summary: Plugin jardin-tropical-pms avec OAuth OpenAI Codex sur /dashboard/ai, routes
  Gateway, Feature 1 livrée, Feature 2 reportée.
tags:
- openclaw
- plugin
- oauth
- pms
tier: hot
title: Plugin OpenClaw du PMS — État (avr 2026)
topic_cluster: openclaw
type: project
updated: 2026-05-07
---

# Plugin OpenClaw du PMS — État

> Note portée depuis la mémoire Claude Code `project_openclaw_plugin.md` le 2026-05-07.

Initiative démarrée le 2026-04-22 pour brancher l'assistant IA du PMS sur l'abonnement ChatGPT Plus de Raphaël (économie clé API). Plugin externe OpenClaw + UI native dans `/dashboard/ai`.

**Why:** Raphaël veut éviter de payer une clé API OpenAI quand son abonnement ChatGPT Plus inclut déjà l'accès Codex. Plus économique + un seul point de contrôle.

## État actuel (Feature 1 livrée)

- Plugin `/var/www/pms-jardin-tropical/plugins/jardin-tropical-pms/` (TS, build avec `npm run build`)
- Installé dans OpenClaw via `openclaw plugins install <path>` → présent dans `/root/.openclaw/extensions/jardin-tropical-pms/`
- Expose 5 routes Gateway : `/plugin/jtp/auth/{status,start,finish,disconnect,activate}`
- Card React `<OpenAIAuthCard />` dans la page `/dashboard/ai` (au-dessus du grid 2 colonnes existant)
- 4 routes proxy PMS dans `/api/openclaw/auth/*` qui forwardent vers le Gateway avec Bearer token (lu depuis `Integration OPENCLAW` chiffré)
- Routing IA : `src/lib/ai/openai.ts` détecte automatiquement OpenClaw (cache 30s sur le probe) et route les appels OpenAI vers `${gatewayUrl}/v1/chat/completions` avec `model: "openclaw"` quand un compte Codex est actif. Fallback transparent vers `Integration OPENAI` (clé API standard) si aucun compte Codex actif.
- 2 comptes Codex connectés : `raphael.distefano1@gmail.com` et `sandrine.distefano@icloud.com`, switch via bouton "Activer" dans la Card → met à jour `lastGood` dans `auth-profiles.json`
- Modèle par défaut : `openai-codex/gpt-5.4-mini` (configurable dans `~/.openclaw/openclaw.json` → `agents.defaults.model.primary`)

## Feature 2 (Heartbeat & Routines)

**Reportée**, demandée initialement puis explicitement mise de côté par Raphaël ("pour l'instant oublie les heartbit et routine, fait juste la fonctionnalité 1").

## Notes techniques importantes

- Le flux OAuth Codex utilisé est le **paste-back** (pas un vrai redirect) : `/start` retourne une URL ChatGPT, l'utilisateur autorise, il est redirigé vers `http://localhost:1455/auth/callback?code=…` (page d'erreur), il copie l'URL et la colle dans `/finish`. C'est ce qui fonctionne en remote VPS car `redirect_uri` est hardcodé côté OAuth app ChatGPT.
- L'endpoint Gateway `/v1/chat/completions` doit être activé : `openclaw config set gateway.http.endpoints.chatCompletions.enabled true`. Il accepte `model: "openclaw"` (dispatch automatique) ou `model: "openclaw/<agentId>"`.
- Aucune clé API OpenAI n'est configurée actuellement (ni en DB ni en env), donc TOUS les appels IA passent par OpenClaw → OAuth Codex (preuve par l'absence).
- Le compte ChatGPT actif pour les inférences = `lastGood` dans `auth-profiles.json`. Quand Raphaël switch dans l'UI, le cache PMS de 30s peut faire que le changement met jusqu'à 30s à être pris en compte côté assistant.

## Backlog si reprise

- Heartbeat & Routines (Feature 2 du brief original)
- Sélecteur de modèle Codex dans la Card (gpt-5.4 vs gpt-5.4-mini)
- Invalidation immédiate du cache 30s lors d'un "Activer"

## Liens
- MOC parent : [[_MOC-openclaw]]
- Référence VPS : [[OpenClaw-VPS-Reference]]
- Pièges dev : [[OpenClaw-Pieges-Dev]]
- Source : `memory:project_openclaw_plugin.md`

## Related

- [[2026-05-16-culsec-premium-validation-serveur]] — 2026-05-16-culsec-premium-validation-serveur