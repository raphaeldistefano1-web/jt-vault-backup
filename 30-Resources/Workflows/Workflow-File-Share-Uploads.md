---
type: workflow
status: active
tags: [workflow, file-sharing, claude]
created: 2026-04-25
updated: 2026-04-25
relevance: medium
description: "Page /uploads du PMS pour partager des fichiers à Claude (code 8 chars, public/shares/<CODE>/)"
ai_writable: false
related:
  - "[[PMS-Stack]]"
  - "[[Plugin-jt-migrate]]"
id: 202604252029-workflow-file-share-uploads
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: "Le Dev-PMS-Area|PMS expose une page /uploads publique permettant à User-Raphael-Distefano|Raphaël ou n'importe qui avec …"
entities: [configuration, infrastructure, pms]
topic_cluster: pms-features
intent: how-to
tier: warm
---

# 📤 Workflow File Share Uploads

## Principe

Le [[Dev-PMS-Area|PMS]] expose une page **`/uploads`** publique permettant à [[User-Raphael-Distefano|Raphaël]] (ou n'importe qui avec le lien) d'uploader un fichier que Claude pourra ensuite lire côté serveur.

## Mécanisme

1. User va sur `https://pms-46-202-171-204.nip.io/uploads`
2. Upload un fichier
3. Reçoit un **code 8 chars** (ex: `aB3xK9pQ`)
4. Donne le code à Claude
5. Claude lit le fichier dans `/var/www/pms-jardin-tropical/public/shares/<CODE>/<filename>`

## Utilisations

- Partager un dump SQL pour analyse
- Donner un export d'autre système à intégrer
- Partager une archive .tar.gz pour le [[Plugin-jt-migrate]] (workflow contourné depuis qu'on télécharge directement de WP.com vers le VPS — cf. [[Migration-WP-com-vers-VPS-2026-04-25]])

## Limite découverte 2026-04-25

Pendant la migration WP, l'archive de 321 MB depuis WP.com a échoué à passer par cette page (limite Next.js sur upload). Solution : downloader directement de serveur à serveur via `curl` (cf. [[Migration-WP-com-vers-VPS-2026-04-25]]).

## Liens

- [[PMS-Stack]]
- Mémoire référence : `file_share_uploads.md` (mémoire projet PMS)
