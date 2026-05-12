---
ai_writable: true
backlinks:
- Migration-WP-com-vers-VPS-2026-04-25
- _STUBS-A-ARBITRER-2026-05-12
created: 2026-05-12
description: Stub — curl server-to-server bypasse l'auth utilisateur, pattern à connaître
  et sécuriser
embed_hash: null
embed_model_version: null
entities:
- security
- curl
- auth
id: 202605120009-lesson-server-to-server-curl-bypass-user
intent: log
last-accessed: 2026-05-12
project: Lessons
status: stub
summary: curl server-to-server bypasse l'auth user — pattern utile mais à sécuriser
  (token, IP allowlist)
tags:
- lesson
- security
- auth
tier: cold
type: lesson
updated: 2026-05-12
---

# Lesson Server-to-Server curl bypass user

> **Stub** — Note référencée par wikilinks orphelins, à compléter.

Contexte : appels HTTP server-to-server (curl, PHP, Node) entre le PMS, WP, n8n, OpenClaw. Ces appels n'ont pas de cookie session utilisateur — il faut un mécanisme alternatif (Bearer token, signature HMAC, IP allowlist loopback) sinon endpoint exposé.

## À documenter

- [ ] Cas concrets dans le PMS/WP/OpenClaw où ce pattern est utilisé
- [ ] Mécanisme retenu pour chaque (Bearer ? HMAC ? Loopback Tailscale ?)
- [ ] Anti-pattern : endpoint qui suppose `current_user_id()` côté server-to-server

## Related

- [[Lessons-Learned]]
- [[OpenClaw-VPS-Reference]]