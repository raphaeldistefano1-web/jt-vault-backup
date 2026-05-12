---
ai_writable: false
area: null
backlinks:
- 2026-05-11-validation-syntax-gate-avant-commit-sur-plugins-ph
- 2026-05-11-wp-optimize-minify-décision-de-désactivation-insta
- Site-WordPress-Optimisation-2026-04-25
- Workflow-API-Integrations
- Workflow-Cross-Feature-Coherence
- _VAULT-INDEX
confidence: medium
created: '2026-05-11'
embed_hash: null
embed_model_version: null
entities:
- Brevo
- DOI template
- email validation
id: 20260511211534-brevo-doi-template-erreur-redirection-url-is-missi
intent: gotcha
last-accessed: '2026-05-11'
moc: null
project: null
related:
- 2026-05-11-wp-optimize-minify-décision-de-désactivation-insta
- Bug-JT-Migrate-Auth-Loss-After-DB-Restore
- Site-WordPress-Optimisation-2026-04-25
- Stack-Tech
- Workflow-API-Integrations
- Workflow-Cross-Feature-Coherence
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-10-1820-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1941-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1841-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1811-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1911-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1938-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1713-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1853-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1716-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1933-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1907-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-0951-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1858-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1932-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1928-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-0934-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1848-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1828-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1920-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1821-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1843-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1829-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1818-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1902-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-1717-session-0375ba09.md
- 10-Projects/claude-system/2026-05-10-0915-session-0375ba09.md
- 10-Projects/site-wordpress/2026-05-10-0911-session-0375ba09.md
source_session: 0375ba09-478d-4743-8890-c82a03938fb1
status: active
summary: 'Configuration Brevo manquante : URL de redirection DOI non définie.'
tags:
- permanent
- synthesized
- brevo
- integration
- email-config
tier: warm
title: Brevo DOI template — erreur 'Redirection url is missing'
topic_cluster: brevo-integration
type: permanent-note
updated: '2026-05-11'
---

Lors de la création des templates Brevo (DOI + Welcome) sur wp-test-project, erreur : '"Redirection url is missing"'.

Cause : le template DOI (Double Opt-In) exige une URL de redirection vers la page de confirmation email. Brevo API nécessite `redirect_url` paramétrée explicitement (ex: `https://instance.wp-test/brevo/confirm?token=...`).

Fix : ajouter l'endpoint de validation dans Brevo settings avant d'activer DOI.

## Related

- [[Site-WordPress-Optimisation-2026-04-25]] — Site WordPress Optimisation 2026 04 25
- [[Workflow-API-Integrations]] — Workflow API Integrations
- [[Bug-JT-Migrate-Auth-Loss-After-DB-Restore]] — Bug JT Migrate Auth Loss After DB Restore
- [[Stack-Tech]] — Stack Tech
- [[Workflow-Cross-Feature-Coherence]] — Workflow Cross Feature Coherence
- [[2026-05-11-wp-optimize-minify-décision-de-désactivation-insta]] — WP-Optimize Minify — décision de désactivation Instance C