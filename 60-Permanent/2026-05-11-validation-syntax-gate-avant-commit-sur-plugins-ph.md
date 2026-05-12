---
ai_writable: false
area: null
backlinks:
- 2026-05-11-git-init-empty-baseline-pour-ultrareview-sur-repos
- 2026-05-11-utiliser-ultrareview-avant-merge-de-changements-pl
- 2026-05-12-les-slugs-moc-sont-sensibles-aux-typos-et-créent-d
- 2026-05-12-vérification-pre-cutover-systématique-perf-et-diff
- Bug-PharData-RAM-OOM
- Plugin-jt-migrate
confidence: medium
created: '2026-05-11'
embed_hash: null
embed_model_version: null
entities:
- PHP
- WordPress plugin
- Node.js
id: 20260511212047-validation-syntax-gate-avant-commit-sur-plugins-ph
intent: pattern
last-accessed: '2026-05-11'
moc: null
project: null
related:
- 2026-05-11-brevo-doi-template-erreur-redirection-url-is-missi
- 2026-05-11-git-init-empty-baseline-pour-ultrareview-sur-repos
- 2026-05-11-utiliser-ultrareview-avant-merge-de-changements-pl
- 2026-05-12-les-slugs-moc-sont-sensibles-aux-typos-et-créent-d
- 2026-05-12-vérification-pre-cutover-systématique-perf-et-diff
- Bug-JT-Migrate-Auth-Loss-After-DB-Restore
- Bug-PharData-RAM-OOM
- OpenClaw-Pieges-Dev
- Plugin-jt-migrate
- _MOC-jt-migrate
schema_version: 1
source_notes:
- 10-Projects/jt-migrate/2026-05-10-0817-session-4fd4bfe4.md
source_session: 4fd4bfe4-3f6f-4405-ae32-6d3603b75c92
status: active
summary: Exécuter `php -l` et `node --check` sur les fichiers modifiés avant commit
  pour détecter erreurs syntax.
tags:
- permanent
- synthesized
- quality-gate
- pre-commit
- syntax-check
tier: warm
title: Validation syntax gate avant commit sur plugins PHP
topic_cluster: wordpress-plugin-dev
type: permanent-note
updated: '2026-05-11'
---

Avant de déclarer un changement sur un plugin WordPress complet, vérifier la syntaxe PHP et JS des fichiers modifiés :

```bash
# PHP lint
php -l admin/js/jt-migrate.js
for f in includes/class-jt-migrate-import.php includes/class-jt-migrate-export.php; do php -l "$f"; done

# JS lint
node --check /var/www/jt-migrate/admin/js/jt-migrate.js && echo "JS syntax OK"
```

Ce gate élimine les erreurs parse/syntax immédiatement, évitant les white-screen-of-death sur le site de production. Ajouter cette vérification dans le workflow pre-commit ou pré-review.

Applicable à tout plugin PHP/JS multifile où l'erreur syntax cassera le site.

## Related

- [[Plugin-jt-migrate]] — Plugin jt migrate
- [[Bug-PharData-RAM-OOM]] — Bug PharData RAM OOM
- [[OpenClaw-Pieges-Dev]] — Pièges du dev — Plugin OpenClaw + PMS
- [[Bug-JT-Migrate-Auth-Loss-After-DB-Restore]] — Bug JT Migrate Auth Loss After DB Restore
- [[_MOC-jt-migrate]] — MOC JT-Migrate Plugin
- [[2026-05-11-brevo-doi-template-erreur-redirection-url-is-missi]] — Brevo DOI template — erreur 'Redirection url is missing'
- [[2026-05-11-git-init-empty-baseline-pour-ultrareview-sur-repos]] — Git init empty baseline pour ultrareview sur repos existants
- [[2026-05-11-utiliser-ultrareview-avant-merge-de-changements-pl]] — Utiliser /ultrareview avant merge de changements plugin
- [[2026-05-12-les-slugs-moc-sont-sensibles-aux-typos-et-créent-d]] — Les slugs MOC sont sensibles aux typos et créent des dangling links
- [[2026-05-12-vérification-pre-cutover-systématique-perf-et-diff]] — Vérification pre-cutover systématique : perf et différences