---
ai_writable: false
backlinks:
- 2026-05-11-git-init-empty-baseline-pour-ultrareview-sur-repos
- 2026-05-11-service-worker-offline-pwa-stratégie-cache-first-m
- 2026-05-11-testing-vérification-obligatoires-après-chaque-éta
- Dev-PMS-Area
- PMS
- PMS-Stack
- Workflow-Collaboration-IA
- Workflow-Preview-Then-Apply
- _STUBS-A-ARBITRER-2026-05-12
created: 2026-04-25
description: Séquence de déploiement PMS — migrate, build, pm2 restart
embed_hash: null
embed_model_version: null
entities:
- devops
- migration
- nextjs
- pm2
- pms
- prisma
id: 202604252029-workflow-deploy-pms
intent: how-to
last-accessed: 2026-04-25
related:
- 2026-05-11-testing-vérification-obligatoires-après-chaque-éta
- Workflow-File-Share-Uploads
- '[[Dev-PMS-Area]]'
- '[[PMS-Stack]]'
relevance: high
status: active
summary: 'Après chaque modif code du Dev-PMS-Area|PMS :'
tags:
- workflow
- deploy
- pms
- pm2
tier: warm
topic_cluster: pms-ops
type: workflow
updated: 2026-04-25
---

# 🚀 Workflow Deploy PMS

## Séquence

Après chaque modif code du [[Dev-PMS-Area|PMS]] :

```bash
cd /var/www/pms-jardin-tropical

# 1. Migrer la DB si schema Prisma a changé
npx prisma migrate deploy

# 2. Build Next.js
npm run build

# 3. Restart PM2 (sinon changements invisibles : pm2 tourne sur la build précédente)
pm2 restart pms-jardin-tropical
```

## Pièges

- **PM2 tourne en prod, changements invisibles sinon** → toujours restart après build
- **Si schema Prisma changé sans migration** → l'app crashe à l'init Prisma client. Toujours `migrate deploy` avant `build`.
- **Migrations destructives** : utiliser un fichier `.sql` reviewable + `prisma migrate deploy`, pas `migrate dev` en prod.

## Workflow étendu (déploiement gros)

Cf. [[Workflow-Preview-Then-Apply]] pour les refontes UI.

## Liens

- [[Dev-PMS-Area]]
- [[PMS-Stack]]
- Mémoire référence : `deploy_workflow.md` (mémoire projet PMS)

## Related

- [[Workflow-File-Share-Uploads]] — Workflow-File-Share-Uploads
- [[2026-05-11-testing-vérification-obligatoires-après-chaque-éta]] — Testing + vérification obligatoires après chaque étape migration