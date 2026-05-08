---
ai_writable: false
created: 2026-04-25
description: 'Theme link vers /blog/ même sans blog actif → 404. Workaround : redirect
  301 vers home dans mu-plugin.'
embed_hash: null
embed_model_version: null
entities:
- debugging
- documentation
- wordpress
id: 202604252039-bug-wp-link-blog-404
intent: log
last-accessed: 2026-04-25
project: Bugs
related:
- '[[Theme-jardintropical-child]]'
- '[[Mu-plugin-jt-seo-extras]]'
relevance: low
status: workaround
summary: Audit broken links détecte un lien vers /blog/ dans la page À propos. Le
  slug blog n'existe pas comme page WP → 404.
tags:
- bug
- lesson
- wordpress
- theme
tier: cold
topic_cluster: bug-log
type: bug
updated: 2026-04-25
---

# 🐛 Bug : Lien /blog/ dans theme sans blog actif

## Symptôme

Audit broken links détecte un lien vers `/blog/` dans la page À propos. Le slug `blog` n'existe pas comme page WP → 404.

## Cause

Le theme `jardintropical-child` link vers `/blog/` dans son template (probablement le footer ou la page À propos), même si le user n'a pas créé de page Blog. Bug du theme.

## Workaround

Dans [[Mu-plugin-jt-seo-extras]] section redirects :

```php
$redirects = [
    '/blog/' => '/',
    '/blog'  => '/',
    // autres...
];
add_action('parse_request', function($wp) use ($redirects) {
    $request_uri = strtok($_SERVER['REQUEST_URI'], '?');
    if (isset($redirects[$request_uri])) {
        wp_redirect(home_url($redirects[$request_uri]), 301);
        exit;
    }
});
```

Hook **`parse_request`** (pas `template_redirect` qui s'exécute trop tard, après que WP ait déjà décidé 404).

## Fix propre (à faire côté theme)

Le theme dev devrait :
- Soit créer dynamiquement la page Blog si non existante
- Soit afficher le lien Blog seulement si la page existe (`if (get_page_by_path('blog'))`)
- Soit retirer le lien hardcoded

Optionnellement : si [[User-Raphael-Distefano|Raphaël]] décide GO blog, les 3 drafts dans `/root/site-content-drafts/` peuvent être publiés et `/blog/` deviendra une vraie page (le redirect 301 sera alors à retirer).

## 📚 Lesson learned

**Hook `parse_request` > `template_redirect` pour les redirects 301 sur slugs inexistants.** `template_redirect` est trop tard — WP a déjà décidé que c'est un 404 et la rediredict ne s'exécute pas correctement.

Plus généralement : **ne jamais hardcoder des slugs dans un theme**. Toujours vérifier l'existence de la page cible. C'est une discipline de theme dev.

## Liens

- [[Theme-jardintropical-child]]
- [[Mu-plugin-jt-seo-extras]]