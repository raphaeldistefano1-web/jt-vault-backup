---
ai_writable: false
area: dev-tooling
backlinks:
- 2026-05-08-audit-one-shot-déduplication-39-mémoires-cc-vs-vau
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-10-config-cron-jobs-pour-curator-et-synthesizer
- 2026-05-10-decision-defensive-truncation-et-sync-check-vault-
- 2026-05-10-gotcha-fichiers-temporaires-indexés-par-rag
- 2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct
- 2026-05-12-vault-rag-multi-instance-trade-off-ssh-wrapper-vs-
confidence: high
created: 2026-05-07
embed_hash: null
embed_model_version: null
entities:
- vault
- sqlite-vec
- ollama
- syncthing
- tar
- git
id: 20260507-runbook-disaster-recovery
intent: runbook
last-accessed: 2026-05-07
moc: null
project: claude-system
related:
- 2026-05-08-audit-one-shot-déduplication-39-mémoires-cc-vs-vau
- 2026-05-10-config-cron-jobs-pour-curator-et-synthesizer
- 2026-05-10-decision-defensive-truncation-et-sync-check-vault-
- 2026-05-10-gotcha-fichiers-temporaires-indexés-par-rag
- 2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct
- 2026-05-10-pattern-scripts-maintenance-et-diagnostic-vault
- 2026-05-12-vault-rag-multi-instance-trade-off-ssh-wrapper-vs-
- '[[Stack-Tech]]'
- '[[_MOC-claude-system]]'
schema_version: 1
status: active
summary: Procédures step-by-step pour restaurer le vault Obsidian et la stack RAG
  en cas de panne.
tags:
- runbook
- recovery
- ops
- ai-generated
tier: hot
title: Runbook — Disaster Recovery vault
topic_cluster: ops-recovery
type: reference
updated: 2026-05-07
---

# 🚑 Runbook — Disaster Recovery

> Procédures pour restaurer le vault et le RAG en cas de panne. Garder à jour à chaque évolution de stack.

## 1. `vault.db` corrompue (PRAGMA integrity_check ≠ ok)

**Détection** : `vault-doctor` flag `[KO]` sur DB integrity, ou MCP search renvoie une erreur SQLite.

**Procédure** :
```bash
# Lister les backups
ls -lh /opt/vault-rag/data/vault.db.bak.*

# Option A : restaurer depuis la dernière sauvegarde
cp /opt/vault-rag/data/vault.db.bak.<latest> /opt/vault-rag/data/vault.db
sqlite3 /opt/vault-rag/data/vault.db "PRAGMA integrity_check;"  # doit dire 'ok'

# Option B (recommandé : reconstruction complète depuis les markdown)
mv /opt/vault-rag/data/vault.db /opt/vault-rag/data/vault.db.broken.$(date +%F)
/opt/vault-rag/bin/vault-rag-index --full
```

**Validation** :
```bash
/opt/vault-rag/bin/vault-rag-index --stats
/opt/vault-rag/bin/vault-rag-search "test query"
```

## 2. Suppression accidentelle d'une note

**Détection** : Tu as fait `rm` ou Claude a `delete` une note.

**Sources de récupération (par ordre de fraîcheur)** :

```bash
# 1. Trashcan Syncthing (30 jours)
ls /srv/vault/.stversions/

# 2. Mac trashcan (Syncthing aussi)
# → Côté Mac : ~/Documents/vault/.stversions/

# 3. Git history du vault
cd /srv/vault
git log --diff-filter=D --name-only --until=now | head -20
git show HEAD~N:path/to/note.md > path/to/note.md  # restaurer

# 4. Backup tar quotidien
ls /var/backups/vault/
tar xzf /var/backups/vault/vault-<date>.tgz -C /tmp/restore
cp /tmp/restore/srv/vault/path/to/note.md /srv/vault/path/to/note.md
```

## 3. `/srv/vault/` complètement perdu

**Détection** : `ls /srv/vault/` renvoie vide ou n'existe plus.

### A. Si Syncthing Mac est sain
```bash
# 1. Stop syncthing VPS (sinon il propage la suppression côté Mac)
systemctl stop syncthing@root

# 2. Restore depuis Mac : récupérer un dump du Mac
# → Sur le Mac : `cd ~/Documents/vault && tar czf /tmp/vault.tgz .`
# → Copier vers VPS : `scp ~/.../vault.tgz vps-pms:/tmp/`

# 3. Restore VPS
mkdir -p /srv/vault
tar xzf /tmp/vault.tgz -C /srv/vault

# 4. Reprendre syncthing
systemctl start syncthing@root
```

### B. Sinon : depuis le tar local
```bash
ls /var/backups/vault/
tar xzf /var/backups/vault/vault-<latest>.tgz -C /
```

### C. Sinon : depuis git remote (si configuré)
```bash
cd /srv && git clone git@github.com:<user>/vault-private.git vault
```

## 4. VPS perdu (machine entière)

**Stack à reconstruire** :
1. Provision nouveau VPS Hostinger Ubuntu 24.04
2. Installer Tailscale + relier au tailnet existant
3. `apt install ollama syncthing python3-venv git sqlite3`
4. `ollama pull nomic-embed-text-v2-moe`
5. Restaurer `/srv/vault/` (cf. section 3.A depuis Mac)
6. Restaurer `/opt/vault-rag/` :
   - `git clone <repo>` ou recopier depuis backup
   - `python3 -m venv venv && venv/bin/pip install -r requirements-frozen.txt`
7. Recréer les crons (`/etc/cron.d/vault-curator`, `vault-synthesizer`, `vault-backup`, `vault-doctor`, `vault-warmup`)
8. Redémarrer Syncthing avec le device VPS, accepter le folder shared depuis Mac
9. Run `/opt/vault-rag/bin/vault-rag-index --full` pour reconstruire `vault.db`
10. Validation : `pytest /opt/vault-rag/tests/` + `vault-doctor`

## 5. Migration vers nouveau modèle d'embedding

**Cas d'usage** : nomic publie un v3 plus performant, ou on veut tester un autre modèle.

```bash
# 1. Pull le nouveau modèle dans Ollama
ollama pull <new-model>:<tag>

# 2. Sniff la dim (l'API renvoie l'embedding, on lit len)
curl -s http://127.0.0.1:11434/api/embed \
  -d '{"model":"<new-model>","input":["test"]}' | jq '.embeddings[0] | length'

# 3. Migrer les embeddings (script blue-green)
/opt/vault-rag/bin/vault-rag-migrate-embeddings --to <new-model> --dry-run
/opt/vault-rag/bin/vault-rag-migrate-embeddings --to <new-model>

# 4. Mettre à jour la config
# Éditer /opt/vault-rag/lib/config.py :
#   EMBED_MODEL = "<new-model>"
#   EMBED_DIM = <new-dim>

# 5. Validation : run golden queries (ne doit pas régresser)
/opt/vault-rag/venv/bin/pytest /opt/vault-rag/tests/test_golden_queries.py -v
```

## 6. Cron silencieusement HS

**Détection** : `_HEALTH.md` flagge `[alert]` sur "last curator run" ou "last synthesizer run" > 36h.

```bash
# Voir le statut
cat /srv/vault/00-Inbox/_HEALTH.md

# Logs des crons
tail -50 /var/log/vault-curator.log
tail -50 /var/log/vault-synthesizer.log
tail -50 /var/log/vault-backup.log
tail -50 /var/log/vault-doctor.log

# Run manuel pour debug
/opt/vault-rag/bin/vault-rag-curator
/opt/vault-rag/bin/vault-synthesizer

# Si Ollama est down :
systemctl status ollama
systemctl restart ollama

# Si Syncthing est down :
systemctl status syncthing@root
systemctl restart syncthing@root
```

## 7. Quota Plan Max épuisé sur le synthesizer

**Détection** : `vault-synthesizer` log `LLMUnavailable: claude CLI failed: ...`

**Options** :
1. **Attendre la fenêtre suivante** (5h depuis la 1re consommation)
2. **Configurer ANTHROPIC_API_KEY** : ajouter `Environment="ANTHROPIC_API_KEY=sk-ant-..."` dans `/etc/cron.d/vault-synthesizer` + `pip install anthropic` dans le venv
3. **Activer backend Ollama** : `export OLLAMA_CHAT_MODEL=qwen2.5:3b-instruct-q4_K_M` + `ollama pull qwen2.5:3b-instruct-q4_K_M` (qualité moindre)

## Contacts / refs

- **Tailscale tailnet** : `ssh monvps` (Mac), Termius (iPhone)
- **Syncthing GUI** : `https://100.98.218.10:8384` (auth raphael / cf. `/root/.config/syncthing/gui-password.txt`)
- **Ollama API** : `http://127.0.0.1:11434`
- **MCP server vault** : déclaré dans `/root/.claude.json`
- **Hooks Claude Code** : `/root/.claude/hooks/extract_memory.py` + `inject_context.py`
- **Schémas frontmatter** : `/srv/vault/90-Meta/schemas/note-schema.md`

## Related

- [[2026-05-08-audit-one-shot-déduplication-39-mémoires-cc-vs-vau]] — Audit one-shot — déduplication 39 mémoires CC vs vault
- [[2026-05-10-decision-defensive-truncation-et-sync-check-vault-]] — Decision : Defensive truncation et sync-check vault RAG
- [[2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct]] — Lesson : Checklist pour diagnostiquer que Crow fonctionne
- [[2026-05-10-config-cron-jobs-pour-curator-et-synthesizer]] — Config : Cron jobs pour curator et synthesizer
- [[2026-05-10-pattern-scripts-maintenance-et-diagnostic-vault]] — Pattern : Scripts maintenance et diagnostic vault
- [[2026-05-10-gotcha-fichiers-temporaires-indexés-par-rag]] — Gotcha : Fichiers temporaires indexés par RAG
- [[2026-05-12-vault-rag-multi-instance-trade-off-ssh-wrapper-vs-]] — vault-rag multi-instance : trade-off SSH wrapper vs install local