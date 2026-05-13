---
applies_to: ~/Library/LaunchAgents/com.raphael.veille-ia.daily.plist
backlinks:
- 2026-05-07-cron-23h30-pour-ingestion-veille-timing-off-peak
- 2026-05-08-automatiser-envoi-digest-via-email-avec-date
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- '2026-05-12'
- 2026-05-12-auto-arrêt-à-80-cpu-notification-email
date: 2026-05-12
session_id: 9b59e5d9-ac11-4228-906f-1c63d145eeb8
status: pending
target: infra
type: improvement
urgency: medium
---

# Monitorer le succès du launchd veille-ia (alerte en cas de fail silencieux)

## Constat

Le pipeline veille IA tourne désormais via `launchd` sur Mac Mini, planifié 04h00 chaque jour. Si le job échoue (Mac éteint, exception Python, erreur réseau), **personne n'est notifié** — pas d'email reçu le matin, c'est tout. Raphaël devrait remarquer mais il pourrait penser que la veille a juste rien trouvé.

Idem pour `com.raphael.improvements.weekly` (dimanche 18h).

## Pourquoi

Un pipeline qui tombe en silence est pire qu'un pipeline qui plante visiblement : on s'habitue au silence, on rate les vraies infos quand ça revient marcher partiellement.

Pas critique : la veille IA n'est pas vitale. Mais facile à blinder avec un health-check léger.

## How to apply

**Estimation : 30-45 min, à ma charge (Claude)**

Plusieurs options possibles, à arbitrer :

**Option A — Sentinel email** (le plus simple)
1. Ajouter à la fin de `run-daily.sh` un envoi email "✅ Pipeline OK" (ou "❌ Pipeline FAILED rc=X" si une étape a échoué)
2. Sujet distinctif (`[VEILLE-IA HEALTH]`) pour filtrer ces emails dans Gmail (label auto-classé)
3. Si Raphaël ne reçoit pas l'email santé 2 jours d'affilée → il sait qu'il y a un problème

**Option B — Push notification iPhone** (plus immédiat)
1. Compte Pushover (gratuit ou ~5€ one-time) ou ntfy.sh self-hosted
2. `run-daily.sh` envoie en fin de pipeline un push si rc != 0
3. Notification iPhone instantanée

**Option C — Cron de surveillance externe**
1. Sur le VPS, créer un cron qui scrute `~/Documents/vault/30-Resources/Veille-IA/` (sync Syncthing) — si pas de nouveau fichier pour la date du jour avant 06h → alerte

Recommandation : **Option A** pour démarrer (zero infra ajoutée, réutilise SMTP Gmail déjà branché). Migrer Option B si l'option A devient bruit.

## Liens

- [[project_veille_ia]]