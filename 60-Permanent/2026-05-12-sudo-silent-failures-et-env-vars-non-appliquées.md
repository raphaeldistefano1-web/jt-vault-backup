---
ai_writable: false
area: null
backlinks:
- 2026-05-09-bug-synthesizer-omet-la-section-signaux-feedback-d
- 2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct
- Bug-Cross-Compile-Linux-MacOS
- PMS-Desktop-Pieges-Dev
- _VAULT-INDEX
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- sudo
- shell
- bash
- zsh
id: 20260512040310-sudo-silent-failures-et-env-vars-non-appliquées
intent: gotcha
last-accessed: '2026-05-12'
moc: null
project: null
related:
- _FEEDBACK-PENDING
- 2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct
- PMS-Desktop-Pieges-Dev
- 2026-05-09-bug-synthesizer-omet-la-section-signaux-feedback-d
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-12-0048-session-13c136f3.md
- 10-Projects/claude-system/2026-05-12-0102-session-13c136f3.md
- 10-Projects/claude-system/2026-05-12-0040-session-13c136f3.md
- 10-Projects/claude-system/2026-05-12-0043-session-13c136f3.md
source_session: 13c136f3-b295-415e-a3a5-7c632218fad1
status: active
summary: Sudo peut échouer silencieusement; toujours vérifier avec `echo $?` ou relancer
  en verbose.
tags:
- permanent
- synthesized
- debugging
- setup
- shell
tier: cold
title: Sudo silent failures et env vars non-appliquées
topic_cluster: mac-setup
type: permanent-note
updated: '2026-05-12'
---

Lors du setup du Mac :

**Observed** : Commandes `sudo` apparemment exécutées sans feedback d'erreur visible, mais les effets attendus (env vars, paths) n'étaient pas appliqués.

**Cause** : `sudo` peut échouer pour des raisons d'auth (timeout, permission, sudoers config) sans message explicite si stdout/stderr est redirigé ou supprimé.

**Best practice** :
1. Toujours tester avec `echo $?` pour vérifier le code de retour
2. Ajouter `-v` ou `-k` à `sudo` pour plus de feedback
3. Tester chaque path/env var juste après avec `which` ou `printenv`
4. Ne pas enchaîner les commandes sudo sans vérifier chacune

## Related

- [[_FEEDBACK-PENDING]] — 📋 Feedback rules en attente — 0 rule
- [[2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct]] — Lesson : Checklist pour diagnostiquer que Crow fonctionne
- [[PMS-Desktop-Pieges-Dev]] — Pièges du dev — Electron PMS Desktop
- [[2026-05-09-bug-synthesizer-omet-la-section-signaux-feedback-d]] — Bug : synthesizer omet la section Signaux feedback détectés