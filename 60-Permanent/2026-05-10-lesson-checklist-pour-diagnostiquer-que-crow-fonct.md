---
ai_writable: false
area: null
backlinks:
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-08-vault-synthesizer-synthèse-auto-des-session-logs
- 2026-05-12-auditer-et-arbitrer-les-wikilinks-orphelins-réguli
- 2026-05-12-mcp-health-check-timeout-ssh-cold-start-python-imp
- 2026-05-12-procédure-daudit-disque-vps-diagnostic-standard
- 2026-05-12-sudo-silent-failures-et-env-vars-non-appliquées
- RUNBOOK-disaster-recovery
- _VAULT-INDEX
confidence: medium
created: '2026-05-10'
embed_hash: null
embed_model_version: null
entities:
- vault-obsidian
- monitoring
- troubleshooting
id: 20260510040229-lesson-checklist-pour-diagnostiquer-que-crow-fonct
intent: lesson
last-accessed: '2026-05-10'
moc: null
project: null
related:
- 2026-05-08-vault-synthesizer-synthèse-auto-des-session-logs
- 2026-05-12-auditer-et-arbitrer-les-wikilinks-orphelins-réguli
- 2026-05-12-mcp-health-check-timeout-ssh-cold-start-python-imp
- 2026-05-12-procédure-daudit-disque-vps-diagnostic-standard
- 2026-05-12-sudo-silent-failures-et-env-vars-non-appliquées
- RUNBOOK-disaster-recovery
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-09-0856-session-7ba133d2.md
- 10-Projects/claude-system/2026-05-09-0841-session-7ba133d2.md
- 10-Projects/claude-system/2026-05-09-0825-session-7ba133d2.md
- 10-Projects/claude-system/2026-05-09-0835-session-7ba133d2.md
- 10-Projects/claude-system/2026-05-09-0855-session-7ba133d2.md
- 10-Projects/claude-system/2026-05-09-0809-session-7ba133d2.md
- 10-Projects/pms-jardin-tropical/2026-05-09-0822-session-7ba133d2.md
source_session: 7ba133d2-b9f1-4723-9e12-61b69f771a1b
status: active
summary: Procédure pour vérifier que curator + synthesizer tournent normalement et
  la vault est saine.
tags:
- permanent
- synthesized
- operations
- maintenance
- diagnostic
tier: warm
title: 'Lesson : Checklist pour diagnostiquer que Crow fonctionne'
topic_cluster: vault-obsidian-operations
type: permanent-note
updated: '2026-05-10'
---

Quand demande « vérifie que le Crow a bien fait son travail » :

1. **Processus actifs** : `ps aux | grep -E "curator|synthesizer|ollama"`
   - Chercher curator en cours, synthé en cours, ollama vivant

2. **Logs récents** :
   ```bash
   tail -30 /var/log/vault-curator.log
   tail -30 /var/log/vault-synthesizer.log
   ```
   - Chercher `[2026...] Done in X seconds` (succès) ou `Errors` (fails)

3. **Inbox** : `ls /srv/vault/00-Inbox/ | wc -l`
   - Vide/quasi-vide : curator a traité les notes ✓
   - Beaucoup : blocage ou crash ✗

4. **Health check** : `/usr/local/bin/vault-doctor`
   - Output : notes count, embeddings count, orphans, DB size
   - Mismatch count → RUN `vault-build-index`

5. **Dernière exécution** : `stat /var/log/vault-curator.log | grep Modify`
   - Si > 4h ago : cron a échoué
   ```bash
   journalctl -u cron 2>/dev/null | tail -20
   ```

Cette checklist autorise diagnostic autonome sans fouiller manuellement les logs bruts.

## Related

- [[RUNBOOK-disaster-recovery]] — Runbook — Disaster Recovery vault
- [[2026-05-08-vault-synthesizer-synthèse-auto-des-session-logs]] — Vault synthesizer — synthèse auto des session-logs
- [[2026-05-12-sudo-silent-failures-et-env-vars-non-appliquées]] — Sudo silent failures et env vars non-appliquées
- [[2026-05-12-mcp-health-check-timeout-ssh-cold-start-python-imp]] — MCP health-check timeout : SSH cold start + Python imports
- [[2026-05-12-auditer-et-arbitrer-les-wikilinks-orphelins-réguli]] — Auditer et arbitrer les wikilinks orphelins régulièrement
- [[2026-05-12-procédure-daudit-disque-vps-diagnostic-standard]] — Procédure d'audit disque VPS — diagnostic standard