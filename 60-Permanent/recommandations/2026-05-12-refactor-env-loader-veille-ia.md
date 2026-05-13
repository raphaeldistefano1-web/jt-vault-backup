---
applies_to: ~/veille-ia/bin/
backlinks:
- 2026-05-07-structure-répertoires-srvveille-ia-config-external
- 2026-05-08-automatiser-envoi-digest-via-email-avec-date
- 2026-05-08-config-externalisée-env-prompts-markdown-séparés-d
- 2026-05-08-pipeline-veille-ia-youtube-ingestanalyzerendersend
- 2026-05-12-chemins-daccumulation-disque-connus-docker-node-mo
date: 2026-05-12
session_id: 9b59e5d9-ac11-4228-906f-1c63d145eeb8
status: pending
target: workflow
type: improvement
urgency: low
---

# Factoriser le loader .env dupliqué dans les scripts veille-ia

## Constat

Pendant la migration VPS→Mac du pipeline veille IA, on a dû ajouter un loader `.env` inline (~7 lignes) dans 4 scripts : `analyze.py`, `archive.py`, `render.py`, `email_send.py`. `ingest.py` avait déjà le sien depuis le début. Le bloc est strictement identique partout :

```python
_env_file = Path(__file__).resolve().parent.parent / "config" / ".env"
if _env_file.exists():
    for _line in _env_file.read_text().splitlines():
        if "=" in _line and not _line.lstrip().startswith("#"):
            _k, _, _v = _line.partition("=")
            os.environ.setdefault(_k.strip(), _v.strip())
```

5 copies au total, pas DRY. Si le format `.env` évolue (ex : support quoted values, exports), il faut patcher 5 endroits.

## Pourquoi

ROI faible mais réel : un bug futur dans le parsing (ex : valeurs avec `=` comme `EMAIL_FROM_NAME=A=B`) se réparerait à 5 endroits au lieu d'1. Et un newcomer (Raphaël qui revient sur le projet dans 6 mois) trouvera plus clair un `from _envloader import load_env; load_env()`.

Pas urgent : le code marche, on a validé E2E. À traiter quand on retouche les scripts pour autre raison.

## How to apply

**Estimation : 15 min, à ma charge (Claude)**

1. Créer `~/veille-ia/bin/_envloader.py` avec une fonction `load_env(env_file: Path | None = None) -> None` qui encapsule le bloc actuel
2. Dans les 5 scripts (`ingest.py`, `analyze.py`, `archive.py`, `render.py`, `email_send.py`), remplacer le bloc inline par :
   ```python
   from _envloader import load_env
   load_env()
   ```
3. Lancer `bin/run-daily.sh` en mode test (1 vidéo) pour vérifier que le pipeline tourne toujours
4. Si OK, commit (si on met le projet sous git un jour)

## Liens

- [[project_veille_ia]] — mémoire architecture pipeline