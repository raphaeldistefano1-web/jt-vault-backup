---
ai_writable: false
area: null
backlinks:
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct
- 2026-05-10-pattern-scripts-maintenance-et-diagnostic-vault
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
- Whisper-VPS-Reference
confidence: medium
created: '2026-05-12'
embed_hash: null
embed_model_version: null
entities:
- VPS
- du
- docker
- systemd
id: 20260512040447-procédure-daudit-disque-vps-diagnostic-standard
intent: pattern
last-accessed: '2026-05-12'
moc: null
project: null
related:
- 2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct
- 2026-05-10-pattern-scripts-maintenance-et-diagnostic-vault
- Whisper-VPS-Reference
- 2026-05-08-vault-rag-curator-synthesizer-crons-schedule
- 2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms
schema_version: 1
source_notes:
- 10-Projects/jt-migrate/2026-05-11-2118-session-8bb149e5.md
- 10-Projects/jt-migrate/2026-05-11-2122-session-8bb149e5.md
- 10-Projects/pms-jardin-tropical/2026-05-11-2109-session-8bb149e5.md
- 10-Projects/pms-jardin-tropical/2026-05-11-2059-session-8bb149e5.md
source_session: 8bb149e5-9777-4d3a-88e6-d87fb5848961
status: active
summary: Checklist reproductible pour diagnostiquer l'occupation disque par domaine
  (root, /var/www, /var/lib, Docker)
tags:
- permanent
- synthesized
- troubleshooting
- disk-usage
- monitoring
tier: warm
title: Procédure d'audit disque VPS — diagnostic standard
topic_cluster: infrastructure-vps
type: permanent-note
updated: '2026-05-12'
---

Quand une question du type 'pourquoi le disque est plein?' émerge, exécuter en séquence:
```bash
df -h / /home /var /tmp                 # vue globale
du -sh /* 2>/dev/null | sort -hr      # top-level dirs
du -sh /root/.* /root/* 2>/dev/null   # home user
du -sh /var/* 2>/dev/null | sort -hr  # var subtree
du -sh /var/www/* 2>/dev/null         # web root
du -sh /var/lib/* 2>/dev/null         # services data
du -sh /opt/* 2>/dev/null             # custom installs
du -sh /usr/* 2>/dev/null             # system packages
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}\t{{.CreatedSince}}"
docker images -f dangling=true        # orphaned images
```
Ce pattern fait émerger rapidement le culprit (Docker, npm caches, node_modules, logs, etc.). Applicable à tout VPS, a priori exécutable mensuellement ou avant scaling.

## Related

- [[2026-05-10-lesson-checklist-pour-diagnostiquer-que-crow-fonct]] — Lesson : Checklist pour diagnostiquer que Crow fonctionne
- [[2026-05-10-pattern-scripts-maintenance-et-diagnostic-vault]] — Pattern : Scripts maintenance et diagnostic vault
- [[Whisper-VPS-Reference]] — Whisper large-v3-turbo VPS — Paths, usage, performances
- [[2026-05-08-vault-rag-curator-synthesizer-crons-schedule]] — vault-rag curator synthesizer crons schedule
- [[2026-05-11-path-varwwwculsec-homogénéité-infra-vps-avec-pms]] — Path `/var/www/culsec/` — homogénéité infra VPS avec PMS