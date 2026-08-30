# 01 — Pengenalan Program dan Algoritma

## 📚 Algoritma dan Pemrograman untuk Pemula

Modul ini merupakan tahap pertama dalam mempelajari **Algoritma dan Pemrograman**.

Materi ini ditujukan untuk mahasiswa atau pelajar yang:

* Belum pernah belajar pemrograman.
* Belum mengenal bahasa pemrograman.
* Belum mengetahui apa itu algoritma.
* Belum mengetahui bagaimana komputer menjalankan sebuah program.
* Belum pernah menulis kode program.
* Ingin memahami konsep pemrograman dari dasar.

Pada tahap ini **belum diperlukan coding**.

Fokus utama pembelajaran adalah memahami:

> **Apa itu komputer, program, pemrograman, programmer, dan algoritma.**

---

# 1. Tujuan Pembelajaran

Setelah menyelesaikan materi ini, mahasiswa diharapkan mampu:

1. Menjelaskan apa itu komputer.
2. Menjelaskan apa itu program.
3. Menjelaskan apa itu pemrograman.
4. Menjelaskan apa itu programmer.
5. Menjelaskan apa itu bahasa pemrograman.
6. Menjelaskan apa itu algoritma.
7. Memahami hubungan antara algoritma dan program.
8. Membuat algoritma sederhana dari aktivitas sehari-hari.
9. Memahami bahwa komputer bekerja berdasarkan instruksi.
10. Membiasakan diri berpikir secara terstruktur dan berurutan.

---

# 2. Apa Itu Komputer?

Komputer adalah perangkat elektronik yang dapat menerima data, memproses data, menyimpan data, dan menghasilkan informasi berdasarkan instruksi yang diberikan.

Secara sederhana:

```text
Komputer tidak berpikir seperti manusia.

Komputer hanya menjalankan instruksi yang diberikan.
```

Contohnya:

Jika manusia diberikan perintah:

```text
Buatkan saya secangkir kopi.
```

Manusia biasanya langsung memahami apa yang harus dilakukan.

Namun komputer tidak dapat memahami perintah tersebut secara langsung.

Komputer membutuhkan instruksi yang jauh lebih detail.

Contohnya:

```text
1. Ambil gelas.
2. Ambil kopi.
3. Masukkan kopi ke dalam gelas.
4. Panaskan air.
5. Tunggu hingga air panas.
6. Tuangkan air ke dalam gelas.
7. Tambahkan gula.
8. Aduk kopi.
9. Sajikan.
```

Konsep inilah yang menjadi dasar dari pemrograman.

---

# 3. Bagaimana Komputer Bekerja?

Secara sederhana komputer bekerja menggunakan konsep:

```text
INPUT
  ↓
PROCESS
  ↓
OUTPUT
```

atau:

```text
Masukan
  ↓
Proses
  ↓
Keluaran
```

Konsep ini sering disebut:

# IPO

```text
Input – Process – Output
```

---

# 4. Apa Itu Input?

**Input** adalah data atau informasi yang dimasukkan ke dalam sistem.

Contoh input:

```text
Nama
Umur
Nilai
Harga barang
Jumlah barang
Username
Password
Tanggal lahir
Nomor mahasiswa
```

Contoh:

```text
Nama  : Budi
Nilai : 80
```

Data tersebut merupakan **input**.

---

# 5. Apa Itu Process?

**Process** adalah tindakan atau operasi yang dilakukan terhadap input.

Contohnya:

Jika diberikan:

```text
Nilai = 80
```

Kemudian sistem melakukan pemeriksaan:

```text
Jika nilai >= 75
maka mahasiswa dinyatakan LULUS.
```

Pemeriksaan tersebut disebut sebagai **proses**.

---

# 6. Apa Itu Output?

**Output** adalah hasil dari proses yang dilakukan.

Contoh:

```text
Input:

Nilai = 80
```

Kemudian diproses:

```text
Apakah nilai >= 75?
```

Karena:

```text
80 >= 75
```

maka output:

```text
LULUS
```

Sehingga keseluruhan prosesnya adalah:

```text
INPUT
Nilai = 80

        ↓

PROCESS
Apakah nilai >= 75?

        ↓

OUTPUT
LULUS
```

---

# 7. Contoh Input, Process, dan Output

## Contoh 1 — Menghitung Luas Persegi Panjang

Input:

```text
Panjang = 10
Lebar   = 5
```

Process:

```text
Luas = Panjang × Lebar
```

Maka:

```text
Luas = 10 × 5
Luas = 50
```

Output:

```text
Luas Persegi Panjang = 50
```

---

## Contoh 2 — Menentukan Kelulusan

Input:

```text
Nilai = 85
```

Process:

```text
Jika nilai >= 75
    Lulus
Jika nilai < 75
    Tidak Lulus
```

Output:

```text
Lulus
```

---

## Contoh 3 — Menghitung Umur

Input:

```text
Tahun Sekarang = 2026
Tahun Lahir    = 2005
```

Process:

```text
Umur = Tahun Sekarang - Tahun Lahir
```

Maka:

```text
Umur = 2026 - 2005
Umur = 21
```

Output:

```text
Umur = 21 Tahun
```

---

# 8. Apa Itu Program?

Program adalah kumpulan instruksi yang diberikan kepada komputer agar komputer melakukan tugas tertentu.

Contohnya:

```text
Aplikasi kalkulator
Aplikasi WhatsApp
Aplikasi Instagram
Website
Game
Sistem akademik
Sistem pembayaran
Sistem perpustakaan
Sistem kasir
```

Semua aplikasi tersebut dibuat menggunakan program.

---

# 9. Contoh Program Sederhana

Bayangkan kita ingin membuat program untuk menghitung total harga barang.

Input:

```text
Harga Barang  = 10.000
Jumlah Barang = 3
```

Program harus melakukan:

```text
Total Harga = Harga Barang × Jumlah Barang
```

Sehingga:

```text
10.000 × 3 = 30.000
```

Output:

```text
Total Harga = Rp30.000
```

Secara konsep:

```text
INPUT
Harga Barang
Jumlah Barang

        ↓

PROCESS
Harga Barang × Jumlah Barang

        ↓

OUTPUT
Total Harga
```

---

# 10. Apa Itu Pemrograman?

Pemrograman adalah proses membuat instruksi agar komputer dapat melakukan suatu pekerjaan.

Dalam pemrograman kita akan:

```text
Memahami masalah
        ↓
Mencari solusi
        ↓
Membuat algoritma
        ↓
Menulis kode program
        ↓
Menjalankan program
        ↓
Mengecek hasil
        ↓
Memperbaiki kesalahan
```

Jadi pemrograman bukan hanya tentang menulis kode.

Hal yang paling penting adalah:

> **Kemampuan memecahkan masalah.**

---

# 11. Apa Itu Programmer?

Programmer adalah seseorang yang membuat program menggunakan bahasa pemrograman.

Seorang programmer tidak hanya bertugas menulis kode.

Programmer harus mampu:

```text
Memahami masalah
        ↓
Menganalisis masalah
        ↓
Menentukan solusi
        ↓
Membuat algoritma
        ↓
Menulis program
        ↓
Menguji program
        ↓
Memperbaiki kesalahan
```

---

# 12. Apa Itu Bahasa Pemrograman?

Manusia menggunakan bahasa seperti:

```text
Bahasa Indonesia
Bahasa Inggris
Bahasa Jepang
Bahasa Mandarin
```

Komputer juga membutuhkan bahasa tertentu agar dapat diberikan instruksi.

Bahasa tersebut disebut:

# Bahasa Pemrograman

Contoh bahasa pemrograman:

```text
Python
Java
JavaScript
C
C++
C#
PHP
Go
Kotlin
Swift
Dart
```

---

# 13. Mengapa Ada Banyak Bahasa Pemrograman?

Karena setiap bahasa pemrograman dapat memiliki tujuan dan karakteristik yang berbeda.

Contohnya:

| Bahasa     | Penggunaan Umum                   |
| ---------- | --------------------------------- |
| Python     | Pemula, Data Science, AI, Backend |
| JavaScript | Website                           |
| PHP        | Backend Website                   |
| Java       | Backend dan Android               |
| Kotlin     | Android                           |
| Swift      | iOS                               |
| Dart       | Flutter                           |
| C          | Sistem dan Embedded               |
| C++        | Game dan sistem                   |
| C#         | .NET dan Game                     |

Namun sebagai pemula, tidak perlu mempelajari semuanya sekaligus.

Yang paling penting adalah memahami:

```text
LOGIKA PEMROGRAMAN
```

Karena logika dasarnya hampir sama.

---

# 14. Bahasa Pemrograman yang Akan Digunakan

Untuk tahap awal, bahasa yang direkomendasikan adalah:

# Python

Alasannya karena Python memiliki sintaks yang relatif sederhana.

Contoh:

```python
print("Hello World")
```

Kode tersebut digunakan untuk menampilkan:

```text
Hello World
```

Namun pada materi pertama ini kita **belum fokus pada coding**.

Kita akan fokus memahami algoritma terlebih dahulu.

---

# 15. Apa Itu Algoritma?

Algoritma adalah urutan langkah-langkah yang logis, sistematis, dan terstruktur untuk menyelesaikan suatu masalah.

Sederhananya:

> **Algoritma adalah langkah-langkah untuk menyelesaikan masalah.**

---

# 16. Algoritma dalam Kehidupan Sehari-hari

Tanpa kita sadari, sebenarnya manusia sering menggunakan algoritma.

Contohnya:

## Algoritma Membuat Kopi

```text
1. Siapkan gelas.
2. Masukkan kopi.
3. Masukkan gula.
4. Panaskan air.
5. Tunggu hingga air panas.
6. Tuangkan air ke gelas.
7. Aduk kopi.
8. Sajikan.
```

Ini merupakan algoritma karena terdapat langkah-langkah yang berurutan.

---

# 17. Contoh Algoritma Membuat Mie Instan

```text
MULAI

1. Siapkan panci.
2. Masukkan air.
3. Nyalakan kompor.
4. Tunggu air mendidih.
5. Masukkan mie.
6. Tunggu beberapa menit.
7. Matikan kompor.
8. Siapkan mangkuk.
9. Masukkan bumbu.
10. Masukkan mie.
11. Aduk.
12. Sajikan.

SELESAI
```

---

# 18. Mengapa Urutan Algoritma Penting?

Perhatikan algoritma berikut:

```text
1. Masukkan mie.
2. Nyalakan kompor.
3. Ambil panci.
4. Masukkan air.
```

Secara logika urutan tersebut salah.

Kita tidak dapat memasukkan mie sebelum panci tersedia.

Urutan seharusnya:

```text
1. Ambil panci.
2. Masukkan air.
3. Nyalakan kompor.
4. Tunggu air mendidih.
5. Masukkan mie.
```

Dalam pemrograman:

> **Urutan instruksi sangat penting.**

Komputer menjalankan instruksi berdasarkan urutan yang diberikan.

---

# 19. Komputer Tidak Bisa Menebak

Misalnya kita memberikan instruksi kepada manusia:

```text
Pergi ke kampus.
```

Manusia mungkin langsung mengetahui:

```text
Bangun
Mandi
Berpakaian
Menyiapkan tas
Keluar rumah
Menggunakan kendaraan
Pergi ke kampus
```

Namun komputer membutuhkan instruksi yang lebih detail.

Komputer:

```text
Tidak memiliki intuisi.
Tidak dapat menebak maksud programmer.
Tidak mengetahui konteks jika tidak diberikan.
```

Oleh karena itu programmer harus membuat instruksi dengan jelas.

---

# 20. Ciri-Ciri Algoritma yang Baik

Algoritma yang baik harus memiliki beberapa karakteristik.

## 20.1 Memiliki Awal

Setiap algoritma harus memiliki titik awal.

Contoh:

```text
MULAI
```

---

## 20.2 Memiliki Akhir

Algoritma juga harus memiliki titik akhir.

Contoh:

```text
SELESAI
```

---

## 20.3 Langkahnya Jelas

Instruksi harus mudah dipahami.

Kurang baik:

```text
Lakukan sesuatu dengan nilai.
```

Lebih baik:

```text
Tambahkan nilai tugas dengan nilai ujian.
```

---

## 20.4 Langkahnya Berurutan

Contoh:

```text
1. Masukkan nilai.
2. Hitung nilai.
3. Tampilkan hasil.
```

Bukan:

```text
1. Tampilkan hasil.
2. Masukkan nilai.
3. Hitung nilai.
```

---

## 20.5 Dapat Menyelesaikan Masalah

Algoritma harus menghasilkan solusi.

Jika diberikan:

```text
Panjang = 10
Lebar   = 5
```

Algoritma:

```text
Luas = Panjang × Lebar
```

menghasilkan:

```text
50
```

Artinya algoritma berhasil menyelesaikan masalah.

---

# 21. Hubungan Masalah, Algoritma, dan Program

Dalam pemrograman biasanya prosesnya adalah:

```text
MASALAH
    ↓
ANALISIS
    ↓
ALGORITMA
    ↓
PROGRAM
    ↓
OUTPUT
```

Contoh:

## Masalah

```text
Bagaimana menentukan mahasiswa lulus atau tidak?
```

## Analisis

Aturan:

```text
Nilai >= 75 → Lulus
Nilai < 75  → Tidak Lulus
```

## Algoritma

```text
1. Masukkan nilai.
2. Periksa nilai.
3. Jika nilai >= 75, tampilkan "Lulus".
4. Jika tidak, tampilkan "Tidak Lulus".
```

## Program

Nantinya dapat diterjemahkan ke Python:

```python
nilai = 80

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")
```

## Output

```text
Lulus
```

---

# 22. Algoritma Sebelum Coding

Kesalahan yang sering dilakukan pemula adalah langsung membuat kode.

Contohnya:

```text
Diberikan tugas membuat program kasir.
```

Kemudian mahasiswa langsung membuka editor dan mulai menulis kode.

Padahal sebaiknya:

```text
PAHAMI MASALAH
      ↓
TENTUKAN INPUT
      ↓
TENTUKAN PROSES
      ↓
TENTUKAN OUTPUT
      ↓
BUAT ALGORITMA
      ↓
BARU CODING
```

---

# 23. Contoh Kasus — Program Kasir

## Permasalahan

Seorang pembeli membeli:

```text
Barang = Buku
Harga  = Rp10.000
Jumlah = 3
```

Kita ingin mengetahui total pembayaran.

---

## Input

```text
Harga Barang
Jumlah Barang
```

---

## Process

```text
Total = Harga Barang × Jumlah Barang
```

---

## Output

```text
Total Pembayaran
```

---

## Algoritma

```text
MULAI

1. Masukkan harga barang.
2. Masukkan jumlah barang.
3. Hitung:

   Total = Harga Barang × Jumlah Barang

4. Tampilkan Total.

SELESAI
```

Jika:

```text
Harga  = 10.000
Jumlah = 3
```

Maka:

```text
Total = 10.000 × 3
Total = 30.000
```

Output:

```text
Total Pembayaran = Rp30.000
```

---

# 24. Contoh Kasus — Menentukan Bilangan Ganjil atau Genap

Misalnya:

```text
Angka = 10
```

Kita ingin mengetahui apakah angka tersebut ganjil atau genap.

Algoritma:

```text
MULAI

1. Masukkan angka.

2. Bagi angka dengan 2.

3. Periksa sisa pembagian.

4. Jika sisa pembagian = 0
      Tampilkan "GENAP"

5. Jika tidak
      Tampilkan "GANJIL"

SELESAI
```

Karena:

```text
10 ÷ 2
```

tidak memiliki sisa, maka:

```text
10 = GENAP
```

---

# 25. Contoh Kasus — Menentukan Nilai Mahasiswa

Misalnya aturan:

```text
Nilai >= 75 = LULUS
Nilai < 75  = TIDAK LULUS
```

Algoritma:

```text
MULAI

1. Masukkan nilai mahasiswa.

2. Jika nilai >= 75
      tampilkan "LULUS".

3. Jika nilai < 75
      tampilkan "TIDAK LULUS".

SELESAI
```

---

# 26. Belajar Berpikir Seperti Programmer

Programmer biasanya tidak langsung berpikir:

```text
Kode apa yang harus saya tulis?
```

Tetapi:

```text
Masalahnya apa?
        ↓
Inputnya apa?
        ↓
Prosesnya apa?
        ↓
Outputnya apa?
        ↓
Kondisinya apa?
        ↓
Langkah penyelesaiannya bagaimana?
```

Inilah yang disebut:

# Computational Thinking

atau:

```text
Berpikir Komputasional
```

---

# 27. Memecah Masalah Menjadi Masalah Kecil

Misalnya kita ingin membuat:

# Sistem Login

Jangan langsung berpikir:

```text
Bagaimana membuat aplikasi login?
```

Pecah menjadi:

```text
1. Pengguna memasukkan username.
2. Pengguna memasukkan password.
3. Sistem membaca username.
4. Sistem membaca password.
5. Sistem membandingkan username.
6. Sistem membandingkan password.
7. Jika benar → Login berhasil.
8. Jika salah → Login gagal.
```

Masalah besar menjadi lebih mudah ketika dipecah menjadi bagian kecil.

Konsep ini disebut:

# Decomposition

---

# 28. Contoh Decomposition

Masalah:

```text
Membuat Sistem Nilai Mahasiswa
```

Dapat dipecah menjadi:

```text
Sistem Nilai Mahasiswa

├── Input Nama
├── Input NIM
├── Input Nilai Tugas
├── Input Nilai UTS
├── Input Nilai UAS
├── Hitung Nilai Akhir
├── Tentukan Grade
├── Tentukan Kelulusan
└── Tampilkan Hasil
```

Dengan cara tersebut masalah menjadi lebih mudah dipahami.

---

# 29. Kesalahan Umum Pemula

## 29.1 Langsung Menghafal Coding

Kesalahan:

```text
Menghafal if
Menghafal for
Menghafal while
Menghafal syntax
```

tanpa memahami kegunaannya.

Yang seharusnya dipahami adalah:

```text
IF digunakan ketika ada kondisi.

LOOP digunakan ketika pekerjaan perlu dilakukan berulang kali.
```

---

## 29.2 Takut Melihat Error

Dalam pemrograman error adalah hal yang normal.

Contoh:

```text
Syntax Error
Logic Error
Runtime Error
```

Programmer juga sering mengalami error.

Yang perlu dipelajari adalah:

```text
Membaca error
        ↓
Mencari penyebab
        ↓
Memperbaiki kode
        ↓
Menguji kembali
```

---

## 29.3 Menganggap Coding Harus Hafal

Programmer tidak perlu menghafal semua kode.

Yang penting adalah memahami:

```text
Konsep
Logika
Struktur
Cara mencari solusi
```

---

# 30. Mindset Belajar Pemrograman

Ketika belajar programming, jangan berpikir:

```text
"Saya harus hafal semua kode."
```

Tetapi:

```text
"Saya harus memahami bagaimana menyelesaikan masalah."
```

Karena syntax dapat dicari.

Namun logika harus dipahami.

---

# 31. Analogi Programmer dan Resep Masakan

Pemrograman dapat dianalogikan seperti memasak.

## Masalah

```text
Saya ingin membuat nasi goreng.
```

## Algoritma

```text
Resep nasi goreng.
```

## Bahasa Pemrograman

Seperti bahasa yang digunakan untuk menulis resep.

Misalnya:

```text
Bahasa Indonesia
Bahasa Inggris
```

## Programmer

```text
Orang yang membuat resep.
```

## Komputer

```text
Orang yang menjalankan resep secara tepat.
```

Jika resep salah:

```text
Hasil makanan bisa salah.
```

Jika algoritma salah:

```text
Hasil program juga bisa salah.
```

---

# 32. Algoritma yang Sama Bisa Menggunakan Bahasa Berbeda

Misalnya algoritma:

```text
1. Masukkan dua angka.
2. Tambahkan kedua angka.
3. Tampilkan hasil.
```

Algoritmanya tetap sama.

Namun programnya dapat dibuat menggunakan:

```text
Python
Java
JavaScript
C++
PHP
```

Ini membuktikan bahwa:

> **Algoritma lebih penting daripada bahasa pemrograman tertentu.**

---

# 33. Studi Kasus Sederhana

## Kasus

Sebuah toko memberikan diskon apabila total belanja minimal Rp100.000.

Aturan:

```text
Jika belanja >= 100.000
Diskon = 10%

Jika belanja < 100.000
Tidak mendapatkan diskon
```

Misalnya:

```text
Total Belanja = 200.000
```

Diskon:

```text
10% × 200.000
= 20.000
```

Total Bayar:

```text
200.000 - 20.000
= 180.000
```

Algoritma:

```text
MULAI

1. Masukkan total belanja.

2. Jika total belanja >= 100.000

       Diskon = total belanja × 10%

       Total Bayar =
       total belanja - diskon

3. Jika total belanja < 100.000

       Total Bayar = total belanja

4. Tampilkan total bayar.

SELESAI
```