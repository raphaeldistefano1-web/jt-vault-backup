---
type: bug
status: resolved
tags: [bug, lesson, wordpress, encoding]
created: 2026-04-25
updated: 2026-04-25
relevance: low
description: "Image WebP avec accent dans nom (dressée vs dressee) → 404 → fix par symlink"
ai_writable: false
related:
  - "[[Site-WordPress]]"
id: 202604252038-bug-wp-image-encoding-accent
embed_model_version: null
embed_hash: null
last-accessed: 2026-04-25
summary: "Audit broken links de la page /restauration/ : 1 image en 404 :"
entities: [debugging, documentation, wordpress]
topic_cluster: bug-log
intent: log
tier: cold
---

# 🐛 Bug : URL image avec accent

## Symptôme

Audit broken links de la page /restauration/ : 1 image en 404 :
```
https://wp-46-202-171-204.nip.io/wp-content/uploads/2026/04/repas_terrasse_table-dressée-mer_01.webp
```

## Cause

Le filename sur disque est `repas_terrasse_table-dressee-mer_01.webp` (sans accent — slug sanitization PHP standard). Mais le HTML rendu référence `dressée` (avec accent).

L'attribut référence à l'image vient probablement du `_wp_attachment_metadata` (sérialisé) ou d'un widget — pas trouvé direct dans `post_content` de la page restauration.

## Tentative search-replace

```bash
wp search-replace 'repas_terrasse_table-dressée-mer' 'repas_terrasse_table-dressee-mer' --all-tables --skip-columns=guid
```

→ **0 replacements**. La référence est stockée d'une manière inhabituelle (peut-être HTML-encoded `&eacute;` ou similaire dans une option sérialisée).

## Fix appliqué : symlink

```bash
cd /var/www/wordpress-instance/data/wordpress/wp-content/uploads/2026/04/
ln -sf "repas_terrasse_table-dressee-mer_01.webp" "repas_terrasse_table-dressée-mer_01.webp"
```

Apache résout le symlink → l'image se sert correctement même avec l'URL accentuée.

## 📚 Lesson learned

**Quand search-replace ne trouve pas une référence visible dans le HTML, c'est probablement** :
1. Stockée encodée (HTML entities, URL-encoded)
2. Stockée dans un champ sérialisé (`_wp_attachment_metadata`)
3. Générée dynamiquement par le theme/plugin à partir d'autre chose

Plutôt que chasser la référence pour 1 image, **un symlink** sur le filesystem est une solution pragmatique sans risque.

Pour éviter ça à l'avenir : **slug-sanitize les noms d'attachment** AVANT upload (script post-upload qui retire les accents/espaces du filename ET met à jour la référence DB cohéremment).

## Liens

- [[Site-WordPress]]
- [[Site-WordPress-Optimisation-2026-04-25]]
