---
ai_writable: false
backlinks:
- 2026-05-12-les-slugs-moc-sont-sensibles-aux-typos-et-créent-d
- Decisions-Log
- INDEX
- Lesson-Apache-Timeout-defaut-trop-court
- Lesson-PharData-charge-tout-en-RAM
- Lesson-Pipeline-Auth-vs-DB-Restore
- Lesson-Server-to-Server-curl-bypass-user
- Lesson-mu-plugins-WP-com-toxiques-sur-standalone
- _VAULT-INDEX
created: 2026-04-25
description: MOC apprentissages transversaux — bugs résolus, patterns à retenir, anti-patterns
  identifiés
embed_hash: null
embed_model_version: null
entities:
- debugging
- redis
- site-wordpress
- wordpress
- wordpress-optimization
id: 202604252041-lessons-learned
intent: reference
last-accessed: 2026-04-25
related:
- 2026-05-12-les-slugs-moc-sont-sensibles-aux-typos-et-créent-d
- '[[Decisions-Log]]'
- '[[INDEX]]'
relevance: high
status: active
summary: MOC apprentissages — PharData RAM, Redis vs WPO, streaming uploads, pipelines
  auth-safe, atomic notes patterns.
tags:
- lessons
- moc
- learnings
tier: warm
topic_cluster: vault-navigation
type: moc
updated: 2026-04-25
---

# 💡 MOC Lessons Learned

## PHP / WordPress

- **`PharData` n'est pas scalable** : charge tout en RAM. Pour > 100 MB, utiliser streaming `gzopen` + USTAR custom. Cf. [[Bug-PharData-RAM-OOM]]
- **Drop-ins WP mutuellement exclusifs** (`advanced-cache.php`, `object-cache.php`, `db.php`, `sunrise.php`) — vérifier avant d'activer un plugin qui touche un drop-in. Cf. [[Bug-Redis-WPO-Advanced-Cache-Conflict]]
- **`parse_request` > `template_redirect`** pour les redirects 301 sur slugs inexistants. `template_redirect` est trop tard. Cf. [[Bug-WP-Link-Blog-404]]
- **Symlink quand search-replace ne trouve pas** : pragmatique pour les fichiers media avec accents/caractères spéciaux. Cf. [[Bug-WP-Image-Encoding-Accent]]
- **Mu-plugins sont always-active** : idéal pour les ajouts qui ne doivent jamais "disparaître par accident". Cf. [[Mu-plugin-vs-Theme-Pattern]]

## Apache / Infra

- **Apache `Timeout 300` par défaut tue les gros uploads** sur connexion résidentielle. Pour > 50 MB, augmenter à 1800. Cf. [[Bug-Apache-Timeout-300-vs-Uploads]]
- **`RequestReadTimeout body=10,minrate=500` par défaut** est trop strict. `body=60,minrate=200` plus permissif pour liens lents.
- **Pour gros uploads, prévoir bypass HTTP** : SCP, server-to-server curl, S3 multipart. Cf. [[JT-Migrate-v1.2.0]]

## Design pipelines

- **Modifs auth-affecting EN DERNIER** dans un pipeline multi-step. Sinon les steps suivants perdent l'auth. Cf. [[Bug-JT-Migrate-Auth-Loss-After-DB-Restore]]
- **Pipelines AJAX résistants à la déconnexion** : utiliser un nonce one-shot ou exécuter en CLI sans dépendance auth web.
- **Shutdown handler pour capturer les fatals** : `register_shutdown_function` qui persiste l'erreur dans un état lisible avant que le process meure. Cf. [[JT-Migrate-v1.1.0]]

## SEO / GEO 2026

- **Theme custom > plugin SEO** : si le theme injecte déjà schema/OG/meta complets, ne pas installer Rank Math/Yoast. Cf. [[Decision-Mu-plugin-vs-RankMath]]
- **GEO bloque training, autorise retrieval** : maximise citations LLM sans donner gratuitement le contenu pour training. Cf. [[Decision-Robots-txt-LLM-Aware]]
- **Schema.org `Offer.priceValidUntil` obligatoire** pour fix les warnings Google Search Console.
- **mu-plugins WP.com toxiques sur standalone** : `wpcomsh-loader.php` etc. essaient de joindre des services qui n'existent pas → exclude pendant migration.

## Vault / Knowledge graph

- **Atomic notes 200-1500 mots** (sweet spot embeddings + readability)
- **5-15 wikilinks par note** = densité neuronale optimale
- **Frontmatter `description:`** = semantic compression native, économie tokens
- **MOCs comme hubs** : entry points, pas notes en prose
- **`updated:` strict** pour mitigation drift (notes obsolètes citées comme vraies)

## Liens

- [[INDEX]]
- [[Decisions-Log]]
- Tous les bugs : [[Bug-PharData-RAM-OOM]], [[Bug-JT-Migrate-Auth-Loss-After-DB-Restore]], [[Bug-Apache-Timeout-300-vs-Uploads]], [[Bug-Redis-WPO-Advanced-Cache-Conflict]], [[Bug-WP-Image-Encoding-Accent]], [[Bug-WP-Link-Blog-404]]

## Related

- [[2026-05-12-les-slugs-moc-sont-sensibles-aux-typos-et-créent-d]] — Les slugs MOC sont sensibles aux typos et créent des dangling links