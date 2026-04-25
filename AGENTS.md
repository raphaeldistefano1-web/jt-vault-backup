# AGENTS.md — orientation universelle pour les IA

> Standard Linux Foundation Agentic AI Foundation. Lu par défaut par Cursor, Codex CLI, Gemini CLI, Aider, et — par symlink vers `CLAUDE.md` — par Claude Desktop / Claude Code.

## Identité utilisateur

- **Raphaël Distefano**, owner-operator de l'hôtel **Le Jardin Tropical** (Bouillante, Guadeloupe).
- Stack quotidienne : PMS Next.js custom + site WordPress + dev quotidien avec Claude Code.
- Préférences : explications **concrètes, en français**. À l'aise avec docker / CLI / Linux mais pas dev full-time.
- Mode de collaboration : préfère **agir** plutôt que sur-planifier. Ne pas demander confirmation pour des actions safe et réversibles.

## Pointeurs vault — orientation rapide

- `50-MOCs/Hotel.md` — entry point sujets hôtel et opérations
- `50-MOCs/PMS.md` — entry point dev PMS Next.js
- `50-MOCs/Site-WordPress.md` — entry point site web optimisations + plugins
- `20-Areas/Hotel-Operations.md` — ops courantes, planning, fournisseurs
- `20-Areas/Dev-PMS.md` — décisions tech, architecture, TODO
- `30-Resources/Stack-Tech.md` — VPS, domaines, credentials (références path)
- `10-Projects/` — projets actifs avec deadline
- `40-Archives/` — **NE JAMAIS modifier** (historique read-only)

## Règles d'écriture pour les IA

1. **Toute note créée par IA** va dans `00-Inbox/` avec préfixe `ai-` et frontmatter `status: draft, source: ai`.
2. **Ne JAMAIS modifier** un fichier sans frontmatter `ai_writable: true` ou en `40-Archives/`.
3. **Mode append-only** pour les notes critiques (decisions, contracts). Ajouter en bas, ne pas réécrire le contenu existant.
4. **Frontmatter YAML obligatoire** pour toute note nouvelle (cf. `90-Meta/templates/note.md`).
5. **`updated:` strict** : à actualiser à chaque modif.
6. **Notes > 6 mois sans update** → considérer comme potentiellement obsolète, vérifier avant de citer.

## FAQ qu'aucune IA ne doit me redemander

- **Hébergement principal** : VPS Hostinger, IP 46.202.171.204
- **Site WordPress** : https://wp-46-202-171-204.nip.io (en attendant domaine final `lejardintropical.fr`)
- **PMS** : https://pms-46-202-171-204.nip.io
- **Email pro** : `lejardintropical@orange.fr` (à migrer vers domaine pro pour DKIM propre — cf. `30-Resources/Email-infra.md`)
- **Téléphone** : +590 690 75 44 73
- **Stack PMS** : Next.js 15 + PostgreSQL + Prisma 6 + Tailwind, Nginx port 8080, Traefik Docker pour 80/443
- **Stack site** : WordPress 6.6 / PHP 8.3 / MariaDB 11 / Apache, theme custom `jardintropical-child`, plugin booking custom `jt-booking`
- **Outils dev** : Claude Code en daily, Cursor occasionnel, ChatGPT/Gemini parfois

## Conventions techniques

- **Commits** : conventional commits (`feat:`, `fix:`, `docs:`, etc.)
- **Branches** : feature branches courtes, merge sur `main`
- **Code review** : auto-review avec `code-reviewer` agent avant merge
- **Workflow refonte UI** : preview-then-apply via route `_v2` jamais modif directe sur shell prod
- **Permissions** : actions destructives nécessitent confirmation (rm -rf, force push, drop table)
