[English](Step-2-Edit-rating-and-review) · [Dansk](Step-2-Edit-rating-and-review-da) · **Bahasa Melayu**

# Langkah 2: Sunting penilaian dan ulasan

## Apa yang dibina

Butang Update pada kad membuka borang untuk menukar penilaian dan ulasan. `RateMovieForm` ialah borang WTForms yang dipaparkan oleh Bootstrap-Flask dengan `render_form`. Penghantaran yang sah mengemas kini filem dan kembali ke halaman utama.

## Apa yang kita pelajari

- Borang dengan Flask-WTF dan WTForms, termasuk perlindungan CSRF.
- Pengesah: `NumberRange(0, 10)` untuk penilaian dan had panjang untuk ulasan. `InputRequired` digunakan dan bukan `DataRequired`, kerana penilaian 0 adalah sah.
- GET memaparkan borang yang diisi dengan nilai semasa; POST mengesahkan dan menyimpan.
- `db.get_or_404` menjawab filem yang tidak dikenali dengan halaman 404.
- Alih semula selepas POST, supaya muat semula halaman tidak menghantar dua kali.

## Cuba

`/edit?id=1`

## Tangkapan skrin

![Borang sunting untuk Phone Booth](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/064-top-movies/raw/branch/main/docs/screenshots/r2-edit.png)

## Langkah seterusnya

[Langkah 3: Padam filem](Step-3-Delete-movies-ms)
