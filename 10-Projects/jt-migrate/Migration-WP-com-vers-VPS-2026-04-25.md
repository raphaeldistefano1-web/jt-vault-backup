---
ai_writable: false
created: 2026-04-25
description: Migration site dealmfr.wpcomstaging.com → VPS Hostinger via JT Migrate
  v1.2.1 — 321 MB d'archive, succès après bug séquence
embed_hash: null
embed_model_version: null
entities:
- debugging
- migration
- wordpress
id: 202604252034-migration-wp-com-vers-vps-2026-04-25
intent: reference
last-accessed: 2026-04-25
project: jt-migrate
related:
- '[[Plugin-jt-migrate]]'
- '[[Site-WordPress]]'
- '[[JT-Migrate-v1.0.0]]'
- '[[JT-Migrate-v1.2.1]]'
- '[[Bug-JT-Migrate-Auth-Loss-After-DB-Restore]]'
- '[[Bug-Apache-Timeout-300-vs-Uploads]]'
relevance: high
status: completed
summary: Migration 321 MB WP.com → VPS Hostinger réussie — 5 bugs résolus (PharData
  RAM, Apache Timeout, auth loss).
tags:
- wordpress
- migration
- jt-migrate
tier: warm
topic_cluster: wp-migration
type: project
updated: 2026-04-25
---

# 🚚 Migration WP.com → VPS — 2026-04-25

## Source / Destination

- **Source** : `dealmfr.wpcomstaging.com` (WP.com Business plan)
- **Destination** : VPS Hostinger 46.202.171.204 — `https://wp-46-202-171-204.nip.io`
- **Volume** : 321 MB d'archive .tar.gz, 1795 entrées (DB + wp-content)

## Séquence des bugs résolus pendant la migration

### 1. Export bloqué (v1.0.0)

[[JT-Migrate-v1.0.0]] : `PharData::compress()` chargeait le `.tar` complet en mémoire avant compression. 332 MB d'uploads → memory_limit explose → fatal PHP silencieux (frontend voyait juste "Étape échouée").

→ **Fix** : [[JT-Migrate-v1.1.0]] streaming tar.gz custom (gzopen + USTAR headers à la main).

### 2. Upload bloqué (HTTP 502)

L'archive 321 MB téléchargée du WP.com a refusé d'uploader sur le VPS via UI WP (`/wp-admin → Plugins → Téléverser`). HTTP 502 Bad Gateway après ~10 min.

[[Bug-Apache-Timeout-300-vs-Uploads]] : Apache `Timeout 300s` par défaut tuait l'upload en plein milieu sur connexion résidentielle.

→ **Fix infra** : Apache `Timeout 1800s` + `RequestReadTimeout body=60,minrate=200`.

### 3. Bypass upload HTTP

[[JT-Migrate-v1.2.0]] : ajout du mode **import-from-server-path** — déposer l'archive dans `wp-content/uploads/jt-migrate/incoming/` via SCP, puis bouton "Importer" dans l'UI. Bypass total des limites HTTP.

→ **Pratique** : Claude a téléchargé directement l'archive depuis WP.com vers le VPS via `curl` sur l'URL publique de l'attachment.

### 4. Import extract crash (v1.1.0)

[[JT-Migrate-v1.1.0]] : `PharData::extractTo()` en lecture chargeait l'index complet en RAM. 321 MB → memory exhausted (le shutdown handler v1.1 a permis de capturer le fatal).

→ **Fix** : [[JT-Migrate-v1.2.1]] streaming extract avec parser USTAR custom (miroir du fix v1.1.0 mais en lecture).

### 5. Import auth invalidée

[[Bug-JT-Migrate-Auth-Loss-After-DB-Restore]] : pipeline d'import écrasait la table `wp_users` AVANT search-replace + files copy → cookie de session admin invalidé → steps suivants 403 silencieux.

→ **Workaround** : Claude a fini l'import manuellement via wp-cli (bypass auth web). Fix v1.3.0 à venir.

## État final

- ✅ Site WP fonctionnel sur le VPS avec contenu de dealmfr
- ✅ Theme `jardintropical-child` actif
- ✅ Plugins importés filtrés (mu-plugin WP.com `wpcomsh-loader.php` exclu — toxique sur standalone)
- ✅ User admin `diphael` (ID 2) créé/réutilisé avec password reset
- ✅ Optimisation site lancée immédiatement après ([[Site-WordPress-Optimisation-2026-04-25]])

## Apprentissages capitalisés

- [[Lesson-PharData-charge-tout-en-RAM]]
- [[Lesson-Apache-Timeout-defaut-trop-court]]
- [[Lesson-Pipeline-Auth-vs-DB-Restore]]
- [[Lesson-Server-to-Server-curl-bypass-user]]
- [[Lesson-mu-plugins-WP-com-toxiques-sur-standalone]]

## Liens

- [[Plugin-jt-migrate]]
- [[Site-WordPress]]
- [[Site-WordPress-Optimisation-2026-04-25]]