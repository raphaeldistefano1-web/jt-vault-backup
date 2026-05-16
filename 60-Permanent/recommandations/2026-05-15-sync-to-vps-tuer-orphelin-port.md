---
applies_to: /Users/raphia/Documents/dev/culsec/scripts/sync-to-vps.sh
backlinks:
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
- 2026-05-12-accès-vps-culsec-via-tailscale-ssh-alias-monvpsvps
date: 2026-05-15
session_id: culsec-algo-adaptatif
status: pending
target: infra
type: improvement
urgency: medium
---

## Constat

Lors du déploiement de l'algo adaptatif culsec, `sync-to-vps.sh` a fait `systemctl restart culsec.service` mais le service est entré en **crash-loop** (`EADDRINUSE` port 3002). Cause : un arbre de process orphelin (`npm exec next start -p 3002` → `sh` → `next-server v16.2.6`, PPID=1, tournant depuis ~3h47) squattait le port 3002 et servait l'**ancien build** (le `curl` public renvoyait 200 mais du code stale). Le service systemd ne pouvait pas binder. Résolu manuellement : `kill` ciblé des 3 PID de l'arbre orphelin (en évitant un `next-server v14.2.35` d'une autre appli), puis `systemctl restart`.

## Pourquoi c'est problématique

Friction récurrente connue (cf. mémoire Claude `feedback_dev_server_runtime` "ne jamais laisser next orphelin"). Le déploiement paraît réussir (`✓ Deploy done.`, public 200) alors que l'ancien code tourne encore → faux positif dangereux : on croit avoir déployé, ce n'est pas le cas. Sans intervention manuelle, chaque déploiement futur avec un orphelin actif échouera silencieusement.

## How to apply

1. Dans `scripts/sync-to-vps.sh`, avant `systemctl restart culsec.service`, ajouter une étape qui libère le port 3002 des process NON gérés par systemd :
   - Récupérer le MainPID systemd : `SVC_PID=$(systemctl show culsec.service -p MainPID --value)`
   - Lister les listeners de :3002 (`ss -tlnpH 'sport = :3002'`), extraire les PID, et `kill` ceux dont le PID ≠ `$SVC_PID` ET dont la cmd matche `next start -p 3002` (ne PAS toucher le `next-server v14` d'une autre appli).
   - Re-vérifier `ss` après 2s, `kill -9` si toujours occupé.
2. Après `systemctl restart`, ajouter une **vérification post-deploy** : `sleep 7 && systemctl is-active culsec.service` doit renvoyer `active` (pas `activating`), sinon `exit 1` avec dump `journalctl -u culsec.service -n 20`.
3. Optionnel : un health-check HTTP réel post-deploy (`curl -fsS http://localhost:3002/ -o /dev/null`) pour ne plus jamais avoir un "Deploy done" mensonger.
Temps estimé : ~30 min. Qui agit : Raphaël (ou Claude sur sa demande), à faire avant le prochain déploiement culsec.