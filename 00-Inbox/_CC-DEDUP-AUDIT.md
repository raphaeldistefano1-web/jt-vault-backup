---
title: Audit doublons mémoire CC ↔ vault
type: meeting
created: '2026-05-08'
updated: '2026-05-08'
id: cc-dedup-audit-20260508
schema_version: 1
tier: hot
status: report
intent: log
topic_cluster: vault-architecture
project: claude-system
tags: [audit, canonicity, dedup, ai-generated]
ai_writable: false
---

# 🔍 Audit doublons CC ↔ vault — 2026-05-08

Score threshold : **0.78** (hybrid score, nomic-v2-moe).

## Bilan

- 🔵 **Whitelist hot** (gardés en CC) : **12** fichiers
- 🟢 **Doublons** (candidats à retrait) : **14**
- 🟡 **Sans doublon** (candidats à promotion vault) : **6**

## 🔵 Whitelist (cf. CANONICITY.md)

- `feedback_openclaw_plugin_dev.md`
- `feedback_pms_desktop_dev.md`
- `feedback_pms_nextauth.md`
- `feedback_preview_gate.md`
- `feedback_todo_list.md`
- `feedback_vps_memory_guardrails.md`
- `feedback_workflow_terminal.md`
- `feedback_wp_optimization.md`
- `reference_claude_subscription.md`
- `reference_vps_access.md`
- `todo_raphael.md`
- `user_role.md`

## 🟢 Doublons détectés — candidats à retrait de CC

> Ces mémoires CC sont déjà couvertes par le vault. Action : valider chaque cas et retirer manuellement de `/root/.claude/projects/-root/memory/` après vérification.

### `project_hotel_team.md` (score **0.84**)

- **Titre CC** : Équipe Le Jardin Tropical
- **Vault match** : `202604252023-user-raphael-distefano` — User Raphael Distefano
- **Vault summary** : Owner-operator Le Jardin Tropical, pilote PMS Next.js + WordPress, daily driver Claude Code, base Bouillante.
- **Extrait CC** : Effectif au 26 avril 2026 : **4 personnes** (gérant + 3 salariés). **Why:** Toutes les features qui touchent au personnel doivent refléter cette taille réelle. Pas de SaaS multi-tenant, pas de modules

### `project_n8n_automations.md` (score **0.84**)

- **Titre CC** : n8n + bus d'événements PMS (état post-session 2026-04-26)
- **Vault match** : `20260507-1124-n8n-etat` — n8n + Bus d'événements PMS — État (post-session 26-04)
- **Vault summary** : 12 workflows actifs + bus events PMS. Refonte avis Google avec IA. 19 events versionnés. Cron 8 tâches automatisées.
- **Extrait CC** : État complet de l'automatisation digitale du Jardin Tropical après les 2 grosses sessions n8n (2026-04-25 setup + 2026-04-26 bibliothèque + refonte). **Why:** Ne pas redécouvrir à chaque session. État

### `project_openclaw_plugin.md` (score **0.84**)

- **Titre CC** : Plugin OpenClaw du PMS Le Jardin Tropical (avr 2026)
- **Vault match** : `20260507-1116-openclaw-etat` — Plugin OpenClaw du PMS — État (avr 2026)
- **Vault summary** : Plugin jardin-tropical-pms avec OAuth OpenAI Codex sur /dashboard/ai, routes Gateway, Feature 1 livrée, Feature 2 reportée.
- **Extrait CC** : Initiative démarrée le 2026-04-22 pour brancher l'assistant IA du PMS sur l'abonnement ChatGPT Plus de Raphaël (économie clé API). Plugin externe OpenClaw + UI native dans `/dashboard/ai`. **Why:** Ra

### `project_pms_desktop_app.md` (score **0.84**)

- **Titre CC** : Logiciel desktop PMS Le Jardin Tropical (Electron v1.3.0)
- **Vault match** : `20260507-1110-pms-desktop-etat` — Logiciel desktop PMS Le Jardin Tropical — État (Electron v1.3.0)
- **Vault summary** : Wrapper Electron v1.3.0 stable pour le PMS Next.js avec notifs macOS, tray menu bar, deep links, offline mode et auto-update manuel.
- **Extrait CC** : État du logiciel desktop macOS du PMS au 22 avril 2026, version actuelle **1.3.0**. **Why:** Référence pour les futures évolutions du wrapper Electron. La structure est entièrement fonctionnelle, les 

### `project_pms_state.md` (score **0.84**)

- **Titre CC** : État global du PMS Le Jardin Tropical (post-session avr 2026)
- **Vault match** : `202604252024-dev-pms-area` — Dev PMS Area
- **Vault summary** : PMS-Area|PMS = Property Management System custom Next.js mono-tenant pour piloter Le Jardin Tropical au quotidien. Pas d…
- **Extrait CC** : État du PMS au 22 avril 2026, après une grosse session de refonte UI + applications prod + livraison du logiciel desktop. **Why:** Référence canonique pour les futures sessions, pour ne pas refaire la

### `project_vault_rebuild.md` (score **0.84**)

- **Titre CC** : Refonte vault Obsidian multi-projets (mai 2026)
- **Vault match** : `20260507-1110-index-root` — INDEX racine — cerveau multi-projets
- **Vault summary** : Entry point racine du vault — navigation par couches PARA + MOCs par projet.
- **Extrait CC** : Refonte initiée 2026-05-07 du vault `/srv/vault-jardin-tropical/` (à renommer `/srv/vault/`) : **Objectif final** Cerveau Obsidian multi-projets (PMS + claude-system + site-wp + n8n + montage-vidéo + 

### `project_wp_migration.md` (score **0.84**)

- **Titre CC** : Migration WordPress ancien → nouveau site
- **Vault match** : `20260507-1122-wp-migration` — Migration WordPress — État post-audit (2026-05-05)
- **Vault summary** : Migration OVH(Divi) → NEW(theme custom) livrée sur Instance C. HBook 1120 résas, theme bugs fixés, 4 mu-plugins créés, 3 findings critiques résolus.
- **Extrait CC** : ## État au 2026-05-06 (Instance C = brouillon prod final) Raphaël migre l'ancien site OVH (`www.lejardintropical.fr`, theme Divi 4.27.4, 1120 résas HBook) vers le nouveau site (production `https://wp-

### `reference_hbook_redesign.md` (score **0.84**)

- **Titre CC** : HBook redesign Instance C — état final
- **Vault match** : `20260507-1122-wp-migration` — Migration WordPress — État post-audit (2026-05-05)
- **Vault summary** : Migration OVH(Divi) → NEW(theme custom) livrée sur Instance C. HBook 1120 résas, theme bugs fixés, 4 mu-plugins créés, 3 findings critiques résolus.
- **Extrait CC** : ## URL et accès - **Instance C** : https://wp-c-46-202-171-204.nip.io/reservation/ - **Login admin** : `diphael` / `2K0q8LVpFG6OcWqdWMuG` ## Mu-plugin custom : `jt-hbook-redesign.php` Path : `/var/www

### `reference_n8n.md` (score **0.84**)

- **Titre CC** : n8n self-hosted Le Jardin Tropical
- **Vault match** : `20260507-1126-n8n-ref` — n8n self-hosted — URLs, paths, credentials, commandes
- **Vault summary** : URL HTTPS Traefik, paths docker-compose/env/.n8n, owner setup, N8N_API_KEY, PMS HMAC secret, backup restore.
- **Extrait CC** : n8n self-hosted déployé sur le VPS pour orchestrer toute l'automatisation digitale de l'hôtel. Connecté en bidirectionnel au PMS (events sortants + actions entrantes). **Why:** Référence stable pour l

### `reference_openclaw_vps.md` (score **0.84**)

- **Titre CC** : OpenClaw sur le VPS PMS Le Jardin Tropical
- **Vault match** : `20260507-1118-openclaw-vps-ref` — OpenClaw sur le VPS — Paths, ports, config
- **Vault summary** : Gateway loopback :18789, paths config auth-profiles, fix systemd ExecStart NVM, Codex OAuth lib.
- **Extrait CC** : OpenClaw v2026.3.24 installé sur le VPS Hostinger qui héberge le PMS. **Gateway HTTP** - Port : `127.0.0.1:18789` (bind=loopback, mode=local) — non exposé publiquement - Token d'auth : lu dans `/root/

### `reference_pms_desktop.md` (score **0.84**)

- **Titre CC** : PMS Desktop — paths, endpoints, commandes
- **Vault match** : `20260507-1112-pms-desktop-ref` — PMS Desktop — Paths, endpoints, commandes
- **Vault summary** : Endpoints API tray-summary et hotel-config, version manifest, commandes build/deploy VPS, xattr Gatekeeper.
- **Extrait CC** : Référence rapide pour intervenir sur le wrapper Electron du PMS. ## URLs publiques - **PMS web** : `http://46.202.171.204:3000` (IP VPS Hostinger, hardcodée dans `desktop/main.js:PMS_URL`) - **Page té

### `reference_vault_obsidian.md` (score **0.84**)

- **Titre CC** : Vault Obsidian Le Jardin Tropical
- **Vault match** : `20260507-1110-index-root` — INDEX racine — cerveau multi-projets
- **Vault summary** : Entry point racine du vault — navigation par couches PARA + MOCs par projet.
- **Extrait CC** : # Vault Obsidian — cerveau IA unifié ## Path et accès - **Localisation canonique** : `/srv/vault-jardin-tropical/` (sur le VPS Hostinger) - **Format** : Markdown + frontmatter YAML, structure PARA + c

### `reference_wp_lejardintropical.md` (score **0.84**)

- **Titre CC** : WordPress lejardintropical (état post-optimisation)
- **Vault match** : `202604252024-site-wordpress` — Site WordPress
- **Vault summary** : Site WordPress optimisé LodgingBusiness — Docker Apache/PHP/MariaDB, theme custom, mu-plugin SEO, TTFB 33ms.
- **Extrait CC** : Site WordPress de l'hôtel Le Jardin Tropical (Bouillante, Guadeloupe), accessible sur https://wp-46-202-171-204.nip.io en attendant le domaine final `lejardintropical.fr`. ## Stack et accès - **VPS Ho

### `project_pms_accounting.md` (score **0.83**)

- **Titre CC** : Module comptabilité PMS Le Jardin Tropical
- **Vault match** : `20260507-1100-moc-pms` — MOC PMS Le Jardin Tropical
- **Vault summary** : Hub d'entrée pour le PMS Next.js custom de l'hôtel Le Jardin Tropical (Bouillante).
- **Extrait CC** : Module compta : LIVRÉ END-TO-END session 2026-04-27 (suite session 2026-04-26). Backend + UI + IA + mobile PWA + ultra-review v1+v2 + 2 vagues fixes + doc. Plan complet : `/var/www/pms-jardin-tropical

## 🟡 Sans doublon — candidats à promotion vers vault

> Ces mémoires CC ne sont PAS dupliquées dans le vault. Si elles sont long-terme, créer une note vault correspondante puis retirer de CC.

- `project_montage_video.md` — top-1 score 0.70 < 0.78 — pas de doublon, candidat promotion
  - meilleur match vault : `20260507-1107-moc-montage-video` (score 0.70)
- `reference_pms_uploads.md` — top-1 score 0.70 < 0.78 — pas de doublon, candidat promotion
  - meilleur match vault : `202604252029-workflow-file-share-uploads` (score 0.70)
- `reference_superpowers_plugin.md` — top-1 score 0.70 < 0.78 — pas de doublon, candidat promotion
  - meilleur match vault : `202604252031-sub-agents-internes-pms` (score 0.70)
- `reference_syncthing_vault.md` — top-1 score 0.70 < 0.78 — pas de doublon, candidat promotion
  - meilleur match vault : `20260508040101-syncthing-p2p-vault-sync-tailscale-only` (score 0.70)
- `reference_whisper_vps.md` — top-1 score 0.70 < 0.78 — pas de doublon, candidat promotion
  - meilleur match vault : `20260507-1130-whisper-ref` (score 0.70)
- `reference_wp_test_project.md` — top-1 score 0.70 < 0.78 — pas de doublon, candidat promotion
  - meilleur match vault : `20260507-1105-moc-jt-migrate` (score 0.70)

---
_Généré par `vault-cc-dedup-audit` le 2026-05-08 10:16 UTC._

Cf. `/srv/vault/90-Meta/CANONICITY.md` pour la règle.