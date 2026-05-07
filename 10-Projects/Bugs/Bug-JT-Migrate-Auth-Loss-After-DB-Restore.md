---
type: bug
status: workaround
tags: [bug, lesson, design, jt-migrate]
created: 2026-04-25
updated: 2026-04-25
relevance: high
description: "Pipeline d'import écrase wp_users AVANT search-replace+files → cookie session admin invalidé → steps 403. Workaround wp-cli, fix v1.3.0."
ai_writable: false
related:
  - "[[Plugin-jt-migrate]]"
  - "[[JT-Migrate-v1.2.1]]"
  - "[[Migration-WP-com-vers-VPS-2026-04-25]]"
id: 202604252038-bug-jt-migrate-auth-loss-after-db-restore
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: "Pendant l'import d'un site sur le VPS :"
entities: [authentication, debugging, migration, site-wordpress]
topic_cluster: bug-log
intent: log
tier: cold
---

# 🐛 Bug : JT Migrate auth loss after DB restore

## Symptôme

Pendant l'import d'un site sur le VPS :
- Step `extract` : OK
- Step `db_restore` : OK (table `wp_users` remplacée par celle du site source)
- Step `replace` (search-replace URLs) : **403 silencieux** côté frontend
- Step `files` : jamais exécuté
- Cleanup : jamais exécuté

Résultat : DB importée mais search-replace non fait + fichiers (themes, plugins, uploads) **non copiés**.

## Cause racine

Le pipeline ordonné `extract → db → replace → files → cleanup` a un défaut **de design** :

Quand `db_restore` exécute, la table `wp_users` est **remplacée** par celle du site source. L'admin actuel (qui était logué pour lancer l'import) n'existe plus dans la DB importée → son cookie de session devient invalide → `current_user_can('manage_options')` returns false sur les steps suivants.

Le step `replace` AJAX retourne 403 sans message. Le frontend voit juste un fail.

## Workaround utilisé

Pendant la migration dealmfr → VPS, Claude a fini l'import manuellement via wp-cli :

```bash
docker exec -u 33 jt-wordpress-cli wp --path=/var/www/html search-replace ...
cp -r extracted/wp-content/themes/* /var/www/html/wp-content/themes/
# etc.
```

Et reset du password de l'admin importé `diphael` (ID 2) car son ancien password n'était pas connu.

## Fix v1.3.0 à venir

Deux options :

### Option A : reordonner le pipeline
`extract → files → replace → db_restore (en dernier)` : la DB est restaurée APRÈS que tout soit en place. L'admin actuel reste valide jusqu'au dernier step.

### Option B : mode CLI-only
Exposer un bouton "Generate import command" qui produit une commande wp-cli à copier-coller dans le terminal du serveur. Pas de dépendance auth web.

L'option A est plus user-friendly. Préférée pour v1.3.0.

## 📚 Lesson learned

**Quand un pipeline modifie l'authentification au milieu, les steps suivants doivent être resilient.**

Patterns à appliquer :
- **Toujours faire les modifs auth-affecting EN DERNIER**
- **Utiliser un token/nonce one-shot** pour le pipeline complet (au lieu du cookie session)
- **Ou : refresh la session côté JS** après chaque step (mais fragile)
- **Ou : exécuter en mode CLI** (sans dépendance auth web)

Plus généralement : tout pipeline AJAX en plusieurs steps doit être **résistant à la déconnexion**. Sinon on accumule des silences inexploitables.

## Liens

- [[Plugin-jt-migrate]]
- [[JT-Migrate-v1.2.1]]
- [[Migration-WP-com-vers-VPS-2026-04-25]]
