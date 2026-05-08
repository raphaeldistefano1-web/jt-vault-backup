---
ai_writable: false
area: null
confidence: medium
created: '2026-05-08'
embed_hash: null
embed_model_version: null
entities:
- email_send.py
- cron
- digest automation
id: 20260508040141-automatiser-envoi-digest-via-email-avec-date
intent: pattern
last-accessed: '2026-05-08'
moc: null
project: null
related: []
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-07-1424-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1419-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1416-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1414-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1341-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1445-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1553-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1538-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1319-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1413-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1429-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1511-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1311-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1457-session-e172a5dd.md
- 10-Projects/claude-system/2026-05-07-1543-session-e172a5dd.md
source_session: e172a5dd-5040-43b5-8a0e-4fec08f8f037
status: active
summary: Script `email_send.py` envoie digest IA généré par date, intégrable en cron
  quotidienne ou trigger manuel.
tags:
- permanent
- synthesized
- automation
- email
- scheduling
- CLI
tier: warm
title: Automatiser envoi digest via email avec date
topic_cluster: veille-ia-youtube
type: permanent-note
updated: '2026-05-08'
---

**Architecture** : `/srv/veille-ia/bin/email_send.py --date YYYY-MM-DD` envoie le digest généré pour une date donnée via email.

**Usage** :
- Manuel : `python email_send.py --date 2026-05-07` (envoie digest du jour spécifié).
- Automatisé : cron job quotidien lance le script avec date du jour précédent (digests générés nuit).

**Dépendances** : `.env` contient credentials SMTP + destinataires. Vérifier chemin digest en local (`/srv/veille-ia/digests/YYYY-MM-DD.md`).

**Avantage** : découple génération (batch nuit) de distribution (matin), permet reprise sur erreur et dry-run précis.