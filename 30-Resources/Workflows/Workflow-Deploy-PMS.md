---
type: workflow
status: active
tags: [workflow, deploy, pms, pm2]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "Séquence de déploiement PMS — migrate, build, pm2 restart"
ai_writable: false
related:
  - "[[Dev-PMS-Area]]"
  - "[[PMS-Stack]]"
id: 202604252029-workflow-deploy-pms
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: "Après chaque modif code du Dev-PMS-Area|PMS :"
entities: [devops, migration, nextjs, pm2, pms, prisma]
topic_cluster: pms-ops
intent: how-to
tier: warm
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
