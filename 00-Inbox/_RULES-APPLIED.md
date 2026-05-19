---
id: 20260518-rules-applied
schema_version: 1
type: report
title: "📋 Rules apprises cette semaine — 2 appliquées, 0 archivées"
project: claude-system
status: active
summary: "2 rules auto-appliquées par le synthesizer, 0 archivées par le curator (cette semaine)."
intent: monitor
tier: cold
tags: [rules, applied, ai-generated]
ai_writable: false
auto-generated: true
created: 2026-05-18
---

# 📋 Rules apprises — semaine du 2026-05-11 au 2026-05-18

**Résumé** : 2 rule(s) auto-appliquée(s) · 0 archivée(s) par le curator · 0 conflit(s) en attente.

## ✅ Auto-appliquées cette semaine

### HIGH (1)

- **Tout VPS en production doit avoir un watchdog CPU qui arrête services préemptivement à 80% et envoie email rapport.** — `2026-05-12-auto-arrêt-à-80-cpu-notification-email` _(usage: 0x)_

### MEDIUM (1)

- **Pour les migrations et features multi-phase, valider chaque étape avant de planifier la suivante. Ne pas assumer un grand plan ; laisser le feedback utilisateur décider la trajectoire.** — `2026-05-12-workflow-itératif-valider-par-phase-plutôt-que-bat` _(usage: 0x)_

---

**Comment retirer une rule** : `/revoke-rule <id>` dans une session Claude Code.
**Comment voir toutes les rules actives** : `cat /root/.claude/CLAUDE.md | grep -A 200 'Rules apprises'`.

_Rapport généré le 2026-05-18 09:00 par `vault-rules-applied` (cron lundi 9h Paris)._