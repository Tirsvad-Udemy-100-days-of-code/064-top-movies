[English](Run-the-project) · [Dansk](Run-the-project-da) · **Bahasa Melayu**

# Jalankan projek

Cipta persekitaran maya setempat, pasang projek dan jalankannya.

## Persediaan

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Jalankan

```powershell
$env:TMDB_API_KEY = "your-key-here"
python -m flask --app top_movies seed
python -m flask --app top_movies run
```

Kunci TMDB hanya diperlukan untuk halaman Add Movie; ujian dan tangkapan skrin menggunakan katalog palsu.

## Ujian, imbasan dan tangkapan skrin

```bash
python -m pytest
bash scripts/scan.sh
bash tools/screenshots/run.sh r1-home=/
```
