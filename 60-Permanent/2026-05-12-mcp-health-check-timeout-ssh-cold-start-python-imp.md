---
ai_writable: false
area: null
backlinks:
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct
- 2026-05-11-defensive-architecture-pour-import-fail-safe-optio
- Bug-Apache-Timeout-300-vs-Uploads
- Lesson-Apache-Timeout-defaut-trop-court
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- MCP
- SSH
- Python
- health-check
id: 20260512040307-mcp-health-check-timeout-ssh-cold-start-python-imp
intent: gotcha
last-accessed: '2026-05-12'
moc: null
project: null
related:
- Lesson-Apache-Timeout-defaut-trop-court
- 2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct
- Bug-Apache-Timeout-300-vs-Uploads
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-11-defensive-architecture-pour-import-fail-safe-optio
schema_version: 1
source_notes:
- 10-Projects/claude-system/2026-05-12-0048-session-13c136f3.md
- 10-Projects/claude-system/2026-05-12-0102-session-13c136f3.md
- 10-Projects/claude-system/2026-05-12-0040-session-13c136f3.md
- 10-Projects/claude-system/2026-05-12-0043-session-13c136f3.md
source_session: 13c136f3-b295-415e-a3a5-7c632218fad1
status: active
summary: MCP report « Failed to connect » masque un timeout du health-check (SSH +
  imports > 5s).
tags:
- permanent
- synthesized
- mcp
- timeout
- debugging
- performance
tier: warm
title: 'MCP health-check timeout : SSH cold start + Python imports'
topic_cluster: mcp-diagnostics
type: permanent-note
updated: '2026-05-12'
---

**Symptôme** : 3 MCP serveurs reportent « Failed to connect » ou timeout.

**Root cause** : Le health-check par le client MCP attend une réponse du serveur; sur une connexion SSH froide (cold start) + Python imports (Anthropic SDK, vault, etc.) > 5 secondes, le timeout du health-check expire avant que le serveur soit prêt.

**Diagnostic** : Ne pas supposer une erreur réseau réelle — vérifier d'abord les imports Python et la latence SSH (tester `ssh <host> python3 -c 'import anthropic'` manuellement).

**Mitigation** : Pré-charger les modules Python, augmenter le timeout du health-check, ou utiliser un serveur persistent au lieu de cold-start à chaque fois.

## Related

- [[Lesson-Apache-Timeout-defaut-trop-court]] — Lesson Apache Timeout defaut trop court
- [[2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct]] — Lesson : Checklist pour diagnostiquer que Crow fonctionne
- [[Bug-Apache-Timeout-300-vs-Uploads]] — Bug Apache Timeout 300 vs Uploads
- [[2026-05-08-vault-rag-curator-synthesizer-crons-schedule]] — vault-rag curator synthesizer crons schedule
- [[2026-05-11-defensive-architecture-pour-import-fail-safe-optio]] — Defensive architecture pour import: fail-safe optional steps