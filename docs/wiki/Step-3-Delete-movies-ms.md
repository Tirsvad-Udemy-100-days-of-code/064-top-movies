[English](Step-3-Delete-movies) · [Dansk](Step-3-Delete-movies-da) · **Bahasa Melayu**

# Langkah 3: Padam filem

## Apa yang dibina

Butang Delete pada kad membuang filem itu daripada pangkalan data dan kembali ke halaman utama. Tangkapan skrin menunjukkan senarai selepas Avatar dipadam.

## Apa yang kita pelajari

- Memadam satu baris dengan `db.session.delete` dan `commit`.
- Membaca parameter query-string dengan `request.args` dan menolak id yang tiada atau bukan angka dengan 400.
- Id yang tidak dikenali memberi 404 dan tiada apa dipadam.
- Kuliah menggunakan pautan GET untuk memadam. Ia mudah, tetapi perubahan keadaan melalui GET tidak selamat dalam pengeluaran; POST dengan token CSRF lebih baik.

## Cuba

`/delete?id=2`

## Tangkapan skrin

![Halaman utama selepas memadam filem](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r3-delete.png)

## Langkah seterusnya

[Langkah 4: Tambah filem melalui TMDB](Step-4-Add-movies-through-TMDB-ms)
