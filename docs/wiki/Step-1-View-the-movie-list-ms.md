[English](Step-1-View-the-movie-list) · [Dansk](Step-1-View-the-movie-list-da) · **Bahasa Melayu**

# Langkah 1: Lihat senarai filem

## Apa yang dibina

Halaman utama menyenaraikan semua filem dalam pangkalan data SQLite. Setiap kad memaparkan poster dan kedudukan di depan, serta tajuk, tahun, ulasan, penilaian dan penerangan di belakang. Pangkalan data mempunyai jadual `Movie` dengan tajuk unik, dan arahan seed memasukkan dua filem contoh daripada kuliah.

## Apa yang kita pelajari

- Kilang aplikasi Flask (`create_app`) dan satu blueprint menempatkan halaman.
- Model gaya SQLAlchemy 2 dengan `Mapped` dan `mapped_column`; tajuk unik menghalang pendua.
- Pertanyaan dengan `db.session.execute(db.select(Movie)).scalars()`.
- Pewarisan templat Jinja dengan Bootstrap-Flask.
- Seed idempoten: dijalankan dua kali tidak pernah menyebabkan ralat integriti.

## Cuba

```bash
python -m flask --app top_movies seed
python -m flask --app top_movies run
```

## Tangkapan skrin

![Halaman utama dengan dua kad filem](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r1-home.png)

## Langkah seterusnya

[Langkah 2: Sunting penilaian dan ulasan](Step-2-Edit-rating-and-review-ms)
