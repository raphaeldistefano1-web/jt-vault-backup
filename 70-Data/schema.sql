-- Claude Code metrics schema v1
-- Single source of truth for session-level usage data captured by extract_memory.py.
-- Optimised for read-only analytical queries from CLI / Obsidian Bases plugin.

PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
PRAGMA busy_timeout = 30000;
PRAGMA foreign_keys = ON;

-- One row per Claude Code session captured by the Stop hook (or backfill).
-- session_id alone is not unique because /clear inside a session keeps the same id;
-- we keyed on (session_id, transcript_path) which together identify one capture.
CREATE TABLE IF NOT EXISTS sessions (
    id                       INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id               TEXT NOT NULL,
    transcript_path          TEXT NOT NULL,
    cwd                      TEXT,
    project                  TEXT,                 -- detect_project() result (PROJECT_PATTERNS)
    start_ts                 TEXT NOT NULL,        -- ISO 8601 UTC, first message timestamp
    end_ts                   TEXT NOT NULL,        -- ISO 8601 UTC, last message timestamp
    duration_min             REAL,                 -- (end-start) in minutes
    n_prompts_user           INTEGER DEFAULT 0,
    n_messages_assistant     INTEGER DEFAULT 0,
    n_tool_calls             INTEGER DEFAULT 0,
    n_errors_tool            INTEGER DEFAULT 0,    -- tool_result with is_error: true
    n_agents_dispatched      INTEGER DEFAULT 0,    -- Task tool calls
    tokens_in                INTEGER DEFAULT 0,
    tokens_out               INTEGER DEFAULT 0,
    cache_create             INTEGER DEFAULT 0,    -- 5m + 1h ephemeral combined
    cache_read               INTEGER DEFAULT 0,
    ephemeral_5m             INTEGER DEFAULT 0,    -- breakdown of cache_create
    ephemeral_1h             INTEGER DEFAULT 0,
    cache_hit_ratio          REAL,                 -- cache_read / (tokens_in + cache_create + cache_read)
    cost_usd_est             REAL DEFAULT 0,       -- proxy for quota usage on Plan Max
    model_mix_json           TEXT,                 -- {"opus-4-7": 0.6, "haiku-4-5": 0.4}
    truncated                INTEGER DEFAULT 0,    -- 1 if transcript hit MAX_TRANSCRIPT_LINES
    schema_version           INTEGER DEFAULT 1,
    captured_at              TEXT NOT NULL,        -- when this row was inserted
    UNIQUE (session_id, transcript_path)
);

CREATE INDEX IF NOT EXISTS idx_sessions_project ON sessions(project);
CREATE INDEX IF NOT EXISTS idx_sessions_start_ts ON sessions(start_ts);
CREATE INDEX IF NOT EXISTS idx_sessions_session_id ON sessions(session_id);

-- Per-session breakdown by tool name (Bash, Edit, Read, Write, Task, Glob, Grep, mcp__*, ...).
CREATE TABLE IF NOT EXISTS tool_calls (
    session_pk    INTEGER NOT NULL,
    tool_name     TEXT NOT NULL,
    count         INTEGER NOT NULL,
    errors        INTEGER DEFAULT 0,
    PRIMARY KEY (session_pk, tool_name),
    FOREIGN KEY (session_pk) REFERENCES sessions(id) ON DELETE CASCADE
);

-- Per-session breakdown by Task subagent_type (code-explorer, code-architect, ...).
CREATE TABLE IF NOT EXISTS agents_dispatched (
    session_pk    INTEGER NOT NULL,
    agent_type    TEXT NOT NULL,
    count         INTEGER NOT NULL,
    PRIMARY KEY (session_pk, agent_type),
    FOREIGN KEY (session_pk) REFERENCES sessions(id) ON DELETE CASCADE
);

-- Per-session breakdown by MCP server (codex, vault, context7, chrome-devtools, ...).
CREATE TABLE IF NOT EXISTS mcp_calls (
    session_pk    INTEGER NOT NULL,
    server        TEXT NOT NULL,
    tool          TEXT NOT NULL,
    count         INTEGER NOT NULL,
    PRIMARY KEY (session_pk, server, tool),
    FOREIGN KEY (session_pk) REFERENCES sessions(id) ON DELETE CASCADE
);

-- Useful views for ad-hoc analysis (callable from CLI or Obsidian Bases).
CREATE VIEW IF NOT EXISTS v_tokens_by_project_30d AS
SELECT
    project,
    COUNT(*)            AS n_sessions,
    SUM(tokens_in)      AS tokens_in,
    SUM(tokens_out)     AS tokens_out,
    SUM(cache_read)     AS cache_read,
    SUM(cache_create)   AS cache_create,
    ROUND(SUM(cost_usd_est), 2) AS cost_usd_est,
    ROUND(AVG(cache_hit_ratio), 3) AS avg_cache_hit_ratio
FROM sessions
WHERE start_ts >= date('now', '-30 days')
GROUP BY project
ORDER BY tokens_out DESC;

CREATE VIEW IF NOT EXISTS v_top_sessions_7d AS
SELECT
    session_id,
    project,
    start_ts,
    duration_min,
    n_prompts_user,
    tokens_out,
    ROUND(cost_usd_est, 3) AS cost_usd
FROM sessions
WHERE start_ts >= date('now', '-7 days')
ORDER BY cost_usd_est DESC
LIMIT 20;

CREATE VIEW IF NOT EXISTS v_agents_30d AS
SELECT
    a.agent_type,
    SUM(a.count) AS dispatches,
    COUNT(DISTINCT a.session_pk) AS in_n_sessions
FROM agents_dispatched a
JOIN sessions s ON s.id = a.session_pk
WHERE s.start_ts >= date('now', '-30 days')
GROUP BY a.agent_type
ORDER BY dispatches DESC;
