---
id: 20260511-rules-applied
schema_version: 1
type: report
title: "📋 Rules apprises cette semaine — 6 appliquées, 0 archivées"
project: claude-system
status: active
summary: "6 rules auto-appliquées par le synthesizer, 0 archivées par le curator (cette semaine)."
intent: monitor
tier: cold
tags: [rules, applied, ai-generated]
ai_writable: false
auto-generated: true
created: 2026-05-11
---

# 📋 Rules apprises — semaine du 2026-05-04 au 2026-05-11

**Résumé** : 6 rule(s) auto-appliquée(s) · 0 archivée(s) par le curator · 0 conflit(s) en attente.

## ✅ Auto-appliquées cette semaine

### MEDIUM (6)

- **Toute interface doit être responsive et testée sur 375px, 768px, 1024px+. Valider via Chrome devtools mobile AVANT déclaré terminé.** — `2026-05-09-responsive-design-obligatoire-pour-toute-interface` _(usage: 0x)_
- **Avant de déclarer un système de dispatch/suggestion (hook, agent, skill) prêt à la production, exécuter 3-5 sessions de test sur instances vierges via team Agent, documenter anomalies, puis générer recommandations et ajustements.** — `2026-05-09-valider-systèmes-de-dispatch-via-test-instances-vi` _(usage: 0x)_
- **Quand capturant des infos/décisions, respecter le tier proposé par l'utilisateur : hot (actionner immédiatement, ajouter todo), warm (mémoriser, relire 1-2 semaines), cold (archive). Ne pas traiter cold comme hot (waste motionnel).** — `2026-05-09-trier-items-capturés-hot-immédiat-vs-warmcold-mémo` _(usage: 0x)_
- **Avant analyse de données métier (taux, statistiques, financière), accéder directement aux sources (API, BDD) plutôt que mémoire. Déclarer explicitement si données partielles ou stale.** — `2026-05-10-analyse-métier-valider-source-de-données-réelle` _(usage: 0x)_
- **Les agents doivent auto-découvrir les skills disponibles via le registry (file-based ou API) au lieu d'une liste statique à mettre à jour manuellement.** — `2026-05-09-nouveaux-skills-doivent-être-auto-découverts-par-a` _(usage: 0x)_
- **Avant de déclarer un système de dispatch/hooks/suggestion finalisé, tester via instances vierges.** — `2026-05-10-valider-systèmes-de-dispatch-via-instances-vierges` _(usage: 0x)_

---

**Comment retirer une rule** : `/revoke-rule <id>` dans une session Claude Code.
**Comment voir toutes les rules actives** : `cat /root/.claude/CLAUDE.md | grep -A 200 'Rules apprises'`.

_Rapport généré le 2026-05-11 09:00 par `vault-rules-applied` (cron lundi 9h Paris)._