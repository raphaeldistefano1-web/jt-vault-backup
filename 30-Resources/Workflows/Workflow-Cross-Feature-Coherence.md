---
ai_writable: false
backlinks:
- 2026-05-11-architecture-jeux-extensible-registry-gameshell-is
- 2026-05-11-brevo-doi-template-erreur-redirection-url-is-missi
- 2026-05-11-layout-nouvelle-saison-3-cartes-alignées-horizonta
- 2026-05-11-testing-vérification-obligatoires-après-chaque-éta
- Dev-PMS-Area
- PMS
- PMS-Calendar-v2
- PMS-Stack
created: 2026-04-25
description: Toute feature doit être exposée à TOUS les points d'entrée pertinents
  + mutualiser composants/API + cascader les MAJ
embed_hash: null
embed_model_version: null
entities:
- api
- calendar
- dashboard
- pms
id: 202604252029-workflow-cross-feature-coherence
intent: how-to
last-accessed: 2026-04-25
related:
- 2026-05-11-brevo-doi-template-erreur-redirection-url-is-missi
- 2026-05-11-layout-nouvelle-saison-3-cartes-alignées-horizonta
- 2026-05-11-testing-vérification-obligatoires-après-chaque-éta
- '[[Dev-PMS-Area]]'
- '[[Workflow-Preview-Then-Apply]]'
relevance: high
status: active
summary: 'Toute feature ajoutée au Dev-PMS-Area|PMS doit être :'
tags:
- workflow
- ux
- coherence
- pms
tier: warm
topic_cluster: pms-architecture
type: workflow
updated: 2026-04-25
---

# 🔄 Workflow Cross-Feature Coherence

## Règle

Toute feature ajoutée au [[Dev-PMS-Area|PMS]] doit être :

1. **Exposée à TOUS les points d'entrée pertinents** (Calendar SlidePanel, frontdesk, détail résa, dashboard, etc.)
2. **Mutualiser composants et API** — pas de duplication
3. **Cascader les mises à jour** — quand une donnée change, tous les points d'affichage reflètent

## Why

Le PMS est utilisé en cross-context permanent (l'user passe Calendar → frontdesk → résa → settings au cours de la journée). Une feature qui n'apparaît que dans 1 point d'entrée crée de la friction et des erreurs.

## Exemples

- **Affichage statut résa** : doit être identique partout (Calendar SlidePanel + frontdesk + détail résa) → composant `ReservationStatusBadge` partagé
- **Modification client** : depuis n'importe quel écran qui affiche le client → API `PUT /api/clients/:id` partagée + invalidation cache React Query partout
- **Notification "nouveau message"** : visible dashboard + tray Electron + badge dock

## Pratique

- Préférer **composants react** réutilisables
- Préférer **API endpoints** REST/RPC partagées
- **React Query / SWR** pour cache cohérent
- Tests : checklist manuelle "vérifier sur Calendar + frontdesk + détail" avant merge

## Liens

- [[Dev-PMS-Area]]
- [[PMS-Calendar-v2]]
- Mémoire référence : `cross_feature_coherence.md` (mémoire projet PMS)

## Related

- [[2026-05-11-brevo-doi-template-erreur-redirection-url-is-missi]] — Brevo DOI template — erreur 'Redirection url is missing'
- [[2026-05-11-testing-vérification-obligatoires-après-chaque-éta]] — Testing + vérification obligatoires après chaque étape migration
- [[2026-05-11-layout-nouvelle-saison-3-cartes-alignées-horizonta]] — Layout 'nouvelle saison' — 3 cartes alignées horizontalement