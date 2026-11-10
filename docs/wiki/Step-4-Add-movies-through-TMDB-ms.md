[English](Step-4-Add-movies-through-TMDB) · [Dansk](Step-4-Add-movies-through-TMDB-da) · **Bahasa Melayu**

# Langkah 4: Tambah filem melalui TMDB

## Apa yang dibina

Add Movie membuka borang satu medan (`FindMovieForm`). Tajuk dicari di The Movie Database (TMDB); padanan disenaraikan dengan tahunnya. Memilih satu akan mengambil butirannya, menyimpan tajuk, tahun, penerangan dan poster, kemudian membuka halaman sunting supaya anda boleh menambah penilaian dan ulasan.

## Apa yang kita pelajari

- Memanggil API web dengan `requests`: sentiasa ada had masa, `raise_for_status` dan ralat yang jelas.
- Kunci API disimpan dalam persekitaran (`TMDB_API_KEY`), tidak pernah dalam kod.
- Port dan penyesuai: paparan bergantung pada antara muka `MovieCatalogue` yang kecil, jadi ujian dan tangkapan skrin menggunakan palsu dan tidak memerlukan rangkaian atau kunci.
- Halaman ralat mesra: 503 apabila kunci tiada, 502 apabila TMDB gagal.
- Aliran berbilang langkah: cari, pilih, simpan, sunting.

## Cuba

```powershell
$env:TMDB_API_KEY = "your-key-here"
python -m flask --app top_movies run
```

## Tangkapan skrin

![Halaman tambah dengan medan tajuk](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r4-add.png)

![Halaman pilih dengan hasil carian](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r4-select.png)

![Halaman sunting untuk filem baharu](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r4-edit-new.png)

## Langkah seterusnya

[Langkah 5: Susun mengikut penilaian](Step-5-Rank-by-rating-ms)
