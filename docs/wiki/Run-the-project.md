**English** · [Dansk](Run-the-project-da) · [Bahasa Melayu](Run-the-project-ms)

# Run the project

Create a local virtual environment, install the project and run it.

## Set up

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run

```powershell
$env:TMDB_API_KEY = "your-key-here"
python -m flask --app top_movies seed
python -m flask --app top_movies run
```

The TMDB key is only needed for the Add Movie page; tests and screenshots use a fake catalogue.

## Tests, scan and screenshots

```bash
python -m pytest
bash scripts/scan.sh
bash tools/screenshots/run.sh r1-home=/
```
