---
ai_writable: true
backlinks:
- 2026-05-10-analyse-métier-valider-source-de-données-réelle
created: 2026-05-10
id: 70-data-queries
project: claude-system
tags:
- data
- metrics
- sql
- reference
tier: warm
title: 70-Data — requêtes SQL utiles
type: index
updated: 2026-05-10
---

# Bibliothèque de requêtes SQL — `metrics.db`

Lance avec `sqlite3 /srv/vault/70-Data/metrics.db "<query>"` (ajouter `-header -column` pour la lisibilité).

## Vue d'ensemble

```sql
-- Tokens et coût estimé par projet sur 30 jours
SELECT * FROM v_tokens_by_project_30d;

-- Top 20 sessions les plus coûteuses des 7 derniers jours
SELECT * FROM v_top_sessions_7d;

-- Sub-agents les plus dispatchés sur 30 jours
SELECT * FROM v_agents_30d;
```

## Quotas Plan Max

```sql
-- Tokens output par jour (proxy direct du quota Plan Max)
SELECT
    date(start_ts) AS day,
    SUM(tokens_out) AS tokens_out,
    ROUND(SUM(cost_usd_est), 2) AS cost_usd_est,
    COUNT(*) AS n_sessions
FROM sessions
WHERE start_ts >= date('now', '-14 days')
GROUP BY day
ORDER BY day DESC;

-- Cache hit ratio moyen par projet (plus c'est haut, mieux)
SELECT
    project,
    ROUND(AVG(cache_hit_ratio), 3) AS avg_cache_hit_ratio,
    COUNT(*) AS n_sessions
FROM sessions
WHERE cache_hit_ratio IS NOT NULL
  AND start_ts >= date('now', '-30 days')
GROUP BY project
ORDER BY avg_cache_hit_ratio DESC;
```

## Délégation Codex effective ?

```sql
-- Compte les appels MCP codex sur 30 jours par session
SELECT
    s.project,
    SUM(m.count) AS codex_calls,
    COUNT(DISTINCT m.session_pk) AS in_n_sessions
FROM mcp_calls m
JOIN sessions s ON s.id = m.session_pk
WHERE m.server = 'codex'
  AND s.start_ts >= date('now', '-30 days')
GROUP BY s.project
ORDER BY codex_calls DESC;
```

## Tools les plus utilisés

```sql
-- Top tools tous projets (30 jours)
SELECT
    tool_name,
    SUM(count) AS calls,
    SUM(errors) AS errors,
    ROUND(100.0 * SUM(errors) / NULLIF(SUM(count), 0), 1) AS error_pct
FROM tool_calls t
JOIN sessions s ON s.id = t.session_pk
WHERE s.start_ts >= date('now', '-30 days')
GROUP BY tool_name
ORDER BY calls DESC
LIMIT 20;
```

## Sessions par modèle dominant

```sql
-- Mix modèle moyen (opus/sonnet/haiku) — vérifie si on délègue assez à Haiku
SELECT
    project,
    COUNT(*) AS n_sessions,
    -- approximations à partir du JSON model_mix
    ROUND(AVG(json_extract(model_mix_json, '$.opus')), 2)   AS pct_opus,
    ROUND(AVG(json_extract(model_mix_json, '$.sonnet')), 2) AS pct_sonnet,
    ROUND(AVG(json_extract(model_mix_json, '$.haiku')), 2)  AS pct_haiku
FROM sessions
WHERE start_ts >= date('now', '-30 days')
GROUP BY project;
```

## Sessions longues vs courtes

```sql
-- Distribution durée
SELECT
    CASE
        WHEN duration_min < 5   THEN '< 5min'
        WHEN duration_min < 30  THEN '5-30min'
        WHEN duration_min < 120 THEN '30min-2h'
        ELSE '> 2h'
    END AS bucket,
    COUNT(*) AS n_sessions,
    SUM(tokens_out) AS tokens_out_total
FROM sessions
WHERE start_ts >= date('now', '-30 days')
  AND duration_min IS NOT NULL
GROUP BY bucket;
```