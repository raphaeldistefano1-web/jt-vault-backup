---
applies_to: /Users/raphia/veille-ia (pipeline veille IA YouTube)
backlinks:
- 2026-05-07-critères-filtrage-youtube-veille-ia
- 2026-05-07-youtube-transcript-api-vs-whisper-priorité-natives
- 2026-05-08-pipeline-veille-ia-youtube-ingestanalyzerendersend
- 2026-05-08-youtube-bloque-requêtes-datacenter-proxy-résidenti
- Whisper-VPS-Reference
date: 2026-05-18
session_id: veille-ia-incident-2026-05-18
status: pending
target: workflow
type: improvement
urgency: medium
---

# Veille IA : 429 sur subs natifs + fallback Whisper fragile → digests dégradés

## Constat

Incident 2026-05-18 : le run launchd 04:00 a planté (0 transcript → analyze fatal → pas
d'email). Cause racine fixée ce jour (`ingest.py` appelait `whisper-cli.py` via shebang →
python système sans `faster_whisper` → crash silencieux ; corrigé en `sys.executable` +
log d'échec transcribe non-silencieux). MAIS le **déclencheur amont reste non traité** :
YouTube renvoie `HTTP 429 Too Many Requests` sur la récupération des sous-titres natifs
(reproduit plusieurs fois le 18/05 entre 15h et 16h). Quand le 429 frappe, les 50 vidéos
basculent toutes sur Whisper ; or beaucoup d'audio-downloads yt-dlp échouent aussi
(warning `n challenge solving failed`, EJS/deno). Résultat du rerun manuel post-fix :
seulement **2 vidéos** analysées au lieu de ~20 → digest "qualité dégradée" (warning
explicite `[select] seulement 2 IDs retenus (<10)`). Raphaël a explicitement **décliné**
l'option de durcissement anti-429 lors de l'arbitrage (il a retenu seulement l'alerte mail).

Bug connexe observé : `cleanup.sh` finit en `rc=1` (non-fatal, géré par `|| log WARN`,
mais jamais investigué).

## Pourquoi c'est problématique

Tant que le 429 n'est pas géré, **chaque run où il frappe produira un digest quasi vide**
(2 vidéos), sans planter (donc sans alerte — l'alerte ne se déclenche que sur échec dur).
Raphaël recevra des emails "ok" mais vides de valeur, et risque de ne pas comprendre
pourquoi. Le fallback Whisper, censé être le filet de sécurité, est lui-même peu fiable
(n-challenge yt-dlp). Le système paraît fonctionnel mais sa valeur est intermittente.

## How to apply

1. **Anti-429 subs** (~1-2h) : dans `bin/ingest.py`, ajouter sur la récupération des
   sous-titres natifs (a) un throttle (sleep 1-2s entre vidéos), (b) retry avec backoff
   exponentiel sur 429, (c) tester l'option `--impersonate` de yt-dlp / curl_cffi.
2. **Fiabiliser le download audio Whisper** (~1h) : installer le solveur EJS yt-dlp
   (`yt-dlp --remote-components ejs:github` ou package deno) pour supprimer le warning
   `n challenge solving failed` ; vérifier que deno est sur le PATH launchd (il l'est :
   `/opt/homebrew/bin`).
3. **Seuil de qualité → alerte** (~30min) : si `<10` IDs retenus, déclencher l'alerte
   mail "digest dégradé" (réutiliser `bin/alert_send.py`) au lieu d'envoyer un digest vide
   silencieusement.
4. **Investiguer `cleanup.sh rc=1`** (~30min) : lancer `bin/cleanup.sh` à la main, lire
   l'erreur, corriger.
5. Qui agit : Raphaël arbitre (il avait décliné l'anti-429) ; implémentation Claude.
   Temps total estimé : ~3-4h.