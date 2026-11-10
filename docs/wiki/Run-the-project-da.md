[English](Run-the-project) · **Dansk** · [Bahasa Melayu](Run-the-project-ms)

# Kør projektet

Opret et lokalt virtuelt miljø, installér projektet og kør det.

## Opsætning

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Kør

```powershell
$env:TMDB_API_KEY = "your-key-here"
python -m flask --app top_movies seed
python -m flask --app top_movies run
```

TMDB-nøglen er kun nødvendig til siden Add Movie; test og skærmbilleder bruger et falsk katalog.

## Test, scanning og skærmbilleder

```bash
python -m pytest
bash scripts/scan.sh
bash tools/screenshots/run.sh r1-home=/
```
