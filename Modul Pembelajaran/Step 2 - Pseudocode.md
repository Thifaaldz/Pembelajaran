# Tahap 2 — Pseudocode dan Flowchart

## Algoritma dan Pemrograman untuk Pemula

Tahap ini merupakan kelanjutan dari:

> **Tahap 1 — Dasar Logika Pemrograman**

Pada Tahap 1, kita sudah memahami bahwa programming tidak dimulai dari coding, tetapi dari:

```text
MASALAH
   ↓
ANALISIS
   ↓
LOGIKA
   ↓
LANGKAH PENYELESAIAN
```

Pada Tahap 2, kita akan belajar bagaimana menuliskan logika tersebut dalam bentuk yang lebih terstruktur menggunakan:

```text
PSEUDOCODE
dan
FLOWCHART
```

Pada tahap ini, kita juga masih belum perlu fokus pada Python, Java, JavaScript, atau bahasa pemrograman lainnya.

---

# 1. Tujuan Pembelajaran

Setelah menyelesaikan Tahap 2, mahasiswa diharapkan mampu:

1. Memahami apa itu algoritma.
2. Memahami apa itu pseudocode.
3. Memahami apa itu flowchart.
4. Mengetahui perbedaan algoritma, pseudocode, dan flowchart.
5. Menulis pseudocode sederhana.
6. Membaca pseudocode.
7. Mengenali simbol-simbol flowchart.
8. Membuat flowchart sederhana.
9. Mengubah permasalahan menjadi pseudocode.
10. Mengubah pseudocode menjadi flowchart.
11. Membuat alur sequence.
12. Membuat alur percabangan sederhana.
13. Membuat alur pengulangan sederhana.
14. Melakukan dry run sederhana.
15. Menemukan kesalahan logika sebelum coding.

---

# 2. Apa Itu Algoritma?

Algoritma adalah urutan langkah-langkah logis dan terstruktur untuk menyelesaikan suatu masalah.

Contoh:

## Masalah

Menghitung luas persegi panjang.

Rumus:

```text
Luas = Panjang × Lebar
```

Algoritmanya:

```text
1. Mulai.
2. Masukkan panjang.
3. Masukkan lebar.
4. Hitung panjang × lebar.
5. Simpan hasil sebagai luas.
6. Tampilkan luas.
7. Selesai.
```

Algoritma tersebut belum menggunakan bahasa pemrograman.

---

# 3. Mengapa Algoritma Dibutuhkan?

Misalnya kita ingin membuat program:

```text
Menghitung nilai akhir mahasiswa.
```

Jika langsung coding, kita mungkin bertanya:

```text
Variabelnya apa?
Rumusnya bagaimana?
Kondisinya bagaimana?
Outputnya bagaimana?
```

Karena itu, lebih baik kita susun terlebih dahulu langkah penyelesaiannya.

```text
Masukkan nilai tugas
        ↓
Masukkan nilai UTS
        ↓
Masukkan nilai UAS
        ↓
Hitung nilai akhir
        ↓
Tentukan lulus/tidak
        ↓
Tampilkan hasil
```

Setelah alurnya jelas, barulah nanti kode dibuat.

---

# 4. Apa Itu Pseudocode?

Pseudocode adalah cara menuliskan algoritma dengan bentuk yang menyerupai kode program, tetapi tidak terikat pada aturan bahasa pemrograman tertentu.

Kata:

```text
Pseudo
```

dapat diartikan sebagai:

```text
semu
```

Sehingga secara sederhana:

```text
Pseudocode = kode semu
```

Pseudocode bukan bahasa pemrograman.

Pseudocode digunakan untuk membantu manusia memahami alur program.

---

# 5. Contoh Pseudocode

Masalah:

```text
Menghitung luas persegi panjang.
```

Pseudocode:

```text
MULAI

INPUT panjang
INPUT lebar

luas = panjang × lebar

OUTPUT luas

SELESAI
```

Perhatikan bahwa pseudocode tersebut mudah dibaca meskipun kita belum mengetahui bahasa pemrograman.

---

# 6. Pseudocode Tidak Harus Memiliki Syntax yang Sangat Ketat

Dalam pseudocode, kita tidak terlalu mempermasalahkan syntax.

Misalnya:

```text
INPUT nilai
```

atau:

```text
MASUKKAN nilai
```

atau:

```text
BACA nilai
```

Semuanya bisa digunakan selama maknanya jelas.

Yang paling penting adalah:

```text
LOGIKANYA BENAR
```

---

# 7. Struktur Dasar Pseudocode

Pseudocode sederhana biasanya mempunyai pola:

```text
MULAI

INPUT

PROCESS

OUTPUT

SELESAI
```

Secara umum:

```text
MULAI
   ↓
Masukkan data
   ↓
Proses data
   ↓
Tampilkan hasil
   ↓
SELESAI
```

---

# 8. Kata-Kata yang Sering Digunakan dalam Pseudocode

Beberapa kata yang umum digunakan:

```text
MULAI
SELESAI

INPUT
OUTPUT

IF
ELSE

JIKA
JIKA TIDAK

FOR
WHILE

ULANGI

TAMPILKAN

HITUNG
```

Untuk pemula, boleh menggunakan Bahasa Indonesia.

Contoh:

```text
MULAI

MASUKKAN nilai

JIKA nilai >= 75
    TAMPILKAN "Lulus"
JIKA TIDAK
    TAMPILKAN "Tidak Lulus"

SELESAI
```

---

# 9. Contoh Pseudocode Sequence

Sequence adalah proses yang berjalan secara berurutan.

Contoh:

## Menghitung Luas Segitiga

Rumus:

```text
Luas = 1/2 × Alas × Tinggi
```

Pseudocode:

```text
MULAI

INPUT alas
INPUT tinggi

luas = 0.5 × alas × tinggi

OUTPUT luas

SELESAI
```

Alurnya:

```text
INPUT ALAS
    ↓
INPUT TINGGI
    ↓
HITUNG LUAS
    ↓
OUTPUT
```

---

# 10. Contoh Pseudocode Penjumlahan

Masalah:

```text
Menjumlahkan dua angka.
```

Pseudocode:

```text
MULAI

INPUT angka1
INPUT angka2

hasil = angka1 + angka2

OUTPUT hasil

SELESAI
```

Jika:

```text
angka1 = 10
angka2 = 20
```

maka:

```text
hasil = 10 + 20
hasil = 30
```

---

# 11. Mengenal Assignment

Perhatikan:

```text
hasil = angka1 + angka2
```

Artinya:

```text
Hitung angka1 + angka2
kemudian simpan hasilnya ke dalam "hasil"
```

Tanda:

```text
=
```

dalam pseudocode dapat digunakan sebagai tanda pemberian nilai.

Contoh:

```text
umur = 20
```

artinya:

```text
variabel umur menyimpan nilai 20
```

---

# 12. Pseudocode Percabangan

Percabangan digunakan ketika terdapat kondisi.

Contoh:

```text
Jika nilai >= 75
    mahasiswa lulus

Jika tidak
    mahasiswa tidak lulus
```

Pseudocode:

```text
MULAI

INPUT nilai

IF nilai >= 75 THEN
    OUTPUT "Lulus"
ELSE
    OUTPUT "Tidak Lulus"

SELESAI
```

Atau menggunakan Bahasa Indonesia:

```text
MULAI

MASUKKAN nilai

JIKA nilai >= 75
    TAMPILKAN "Lulus"
JIKA TIDAK
    TAMPILKAN "Tidak Lulus"

SELESAI
```

---

# 13. Cara Membaca Pseudocode Percabangan

Perhatikan:

```text
JIKA nilai >= 75
```

Artinya sistem bertanya:

```text
Apakah nilai lebih besar atau sama dengan 75?
```

Jika:

```text
YA
```

maka:

```text
Lulus
```

Jika:

```text
TIDAK
```

maka:

```text
Tidak Lulus
```

---

# 14. Contoh Percabangan Umur

Permasalahan:

```text
Menentukan apakah seseorang boleh membuat SIM.
```

Aturan:

```text
Umur >= 17 → Boleh
Umur < 17 → Belum Boleh
```

Pseudocode:

```text
MULAI

INPUT umur

IF umur >= 17 THEN
    OUTPUT "Boleh membuat SIM"
ELSE
    OUTPUT "Belum boleh membuat SIM"

SELESAI
```

---

# 15. Percabangan Lebih dari Dua Kondisi

Misalnya menentukan grade.

Aturan:

```text
Nilai >= 85 → A
Nilai >= 75 → B
Nilai >= 65 → C
Nilai < 65  → D
```

Pseudocode:

```text
MULAI

INPUT nilai

IF nilai >= 85 THEN
    OUTPUT "A"
ELSE IF nilai >= 75 THEN
    OUTPUT "B"
ELSE IF nilai >= 65 THEN
    OUTPUT "C"
ELSE
    OUTPUT "D"

SELESAI
```

Urutannya penting.

---

# 16. Mengapa Urutan Kondisi Penting?

Jika kita menulis:

```text
IF nilai >= 65
    Grade C
ELSE IF nilai >= 75
    Grade B
ELSE IF nilai >= 85
    Grade A
```

maka nilai:

```text
90
```

sudah memenuhi:

```text
90 >= 65
```

Akibatnya sistem bisa langsung memberikan:

```text
C
```

Padahal seharusnya:

```text
A
```

Karena itu kondisi harus disusun secara logis.

---

# 17. Pseudocode Pengulangan

Misalnya kita ingin menampilkan:

```text
Halo
```

sebanyak 5 kali.

Daripada menulis:

```text
OUTPUT "Halo"
OUTPUT "Halo"
OUTPUT "Halo"
OUTPUT "Halo"
OUTPUT "Halo"
```

kita dapat menulis:

```text
ULANGI 5 KALI
    OUTPUT "Halo"
```

atau:

```text
FOR i = 1 TO 5
    OUTPUT "Halo"
END FOR
```

---

# 18. Contoh Pengulangan Angka

Masalah:

```text
Menampilkan angka 1 sampai 5.
```

Pseudocode:

```text
MULAI

FOR i = 1 TO 5
    OUTPUT i
END FOR

SELESAI
```

Output:

```text
1
2
3
4
5
```

---

# 19. Contoh WHILE

Selain perulangan dengan jumlah tertentu, kita bisa mengulang selama kondisi masih benar.

Pseudocode:

```text
MULAI

angka = 1

WHILE angka <= 5
    OUTPUT angka
    angka = angka + 1

SELESAI
```

Output:

```text
1
2
3
4
5
```

---

# 20. Hati-Hati Infinite Loop

Perhatikan:

```text
angka = 1

WHILE angka <= 5
    OUTPUT angka
```

Apa masalahnya?

Nilai:

```text
angka
```

tidak pernah berubah.

Sehingga:

```text
angka <= 5
```

akan terus benar.

Program akan terus mengulang.

Hal ini disebut:

# Infinite Loop

atau:

# Perulangan Tak Berujung

Seharusnya:

```text
angka = angka + 1
```

ditambahkan.

---

# 21. Apa Itu Flowchart?

Flowchart adalah diagram yang digunakan untuk menggambarkan alur sebuah algoritma.

Jika pseudocode menggunakan tulisan, flowchart menggunakan:

```text
SIMBOL
+
GARIS
+
ARAH
```

Flowchart membantu kita melihat alur program secara visual.

---

# 22. Mengapa Flowchart Digunakan?

Flowchart membantu:

1. Memahami urutan proses.
2. Melihat kondisi.
3. Melihat percabangan.
4. Melihat pengulangan.
5. Memeriksa logika.
6. Menjelaskan algoritma kepada orang lain.
7. Merancang program sebelum coding.

---

# 23. Simbol Flowchart — Terminator

Simbol terminator digunakan untuk:

```text
MULAI
```

dan:

```text
SELESAI
```

Bentuk:

```text
╭──────────────╮
│    MULAI     │
╰──────────────╯
```

Biasanya berbentuk oval atau rounded rectangle.

---

# 24. Simbol Flowchart — Input / Output

Digunakan untuk:

```text
INPUT
```

atau:

```text
OUTPUT
```

Contoh:

```text
Masukkan nilai
```

atau:

```text
Tampilkan hasil
```

Secara umum digambarkan dengan bentuk jajar genjang.

Contoh:

```text
   /----------------/
  / INPUT NILAI   /
 /----------------/
```

---

# 25. Simbol Flowchart — Process

Digunakan untuk proses atau perhitungan.

Contoh:

```text
luas = panjang × lebar
```

Biasanya berbentuk persegi panjang.

```text
┌──────────────────────┐
│ luas = panjang*lebar │
└──────────────────────┘
```

---

# 26. Simbol Flowchart — Decision

Decision digunakan untuk kondisi atau keputusan.

Biasanya berbentuk belah ketupat.

Contoh:

```text
       ◇
    nilai >= 75?
```

Memiliki cabang:

```text
YA
```

dan:

```text
TIDAK
```

---

# 27. Simbol Flowchart — Flowline

Flowline adalah garis atau panah yang menunjukkan arah proses.

Contoh:

```text
MULAI
  ↓
INPUT
  ↓
PROCESS
  ↓
OUTPUT
  ↓
SELESAI
```

Panah menunjukkan urutan eksekusi.

---

# 28. Simbol Flowchart Dasar yang Harus Dihafal

Untuk tahap awal, cukup ingat:

| Simbol          | Fungsi          |
| --------------- | --------------- |
| Oval            | Mulai / Selesai |
| Jajar Genjang   | Input / Output  |
| Persegi Panjang | Proses          |
| Belah Ketupat   | Kondisi         |
| Panah           | Arah proses     |

Tidak perlu menghafal seluruh simbol flowchart sekaligus.

---

# 29. Flowchart Sequence

Masalah:

```text
Menghitung luas persegi panjang.
```

Flowchart sederhana:

```text
        ┌─────────┐
        │  MULAI  │
        └────┬────┘
             ↓
     /---------------/
    / Input Panjang /
   /---------------/
             ↓
      /-------------/
     / Input Lebar /
    /-------------/
             ↓
   ┌────────────────────┐
   │ Luas = Panjang ×   │
   │        Lebar       │
   └─────────┬──────────┘
             ↓
       /------------/
      / Output Luas/
     /------------/
             ↓
        ┌─────────┐
        │ SELESAI │
        └─────────┘
```

---

# 30. Flowchart Percabangan

Masalah:

```text
Menentukan kelulusan.
```

Flowchart:

```text
       ┌─────────┐
       │  MULAI  │
       └────┬────┘
            ↓
       /-----------/
      / Input Nilai/
     /-----------/
            ↓
       ◇──────────◇
      / Nilai >=75?\
      ◇──────────◇
       /          \
     YA            TIDAK
     ↓               ↓
/-----------/    /----------------/
/ "Lulus"  /    / "Tidak Lulus" /
/-----------/   /----------------/
     \               /
      \             /
            ↓
       ┌─────────┐
       │ SELESAI │
       └─────────┘
```

---

# 31. Cara Membaca Flowchart Percabangan

Flowchart tersebut dibaca:

```text
Mulai
↓
Masukkan nilai
↓
Periksa apakah nilai >= 75
↓
Jika Ya → Lulus
Jika Tidak → Tidak Lulus
↓
Selesai
```

---

# 32. Flowchart Ganjil atau Genap

Aturan:

```text
Jika angka habis dibagi 2
→ Genap

Jika tidak
→ Ganjil
```

Flowchart:

```text
        MULAI
          ↓
     INPUT ANGKA
          ↓
   ANGKA MOD 2 = 0?
       /        \
      YA        TIDAK
      ↓           ↓
   "GENAP"     "GANJIL"
       \         /
          ↓
        SELESAI
```

---

# 33. Apa Itu MOD?

MOD adalah sisa hasil pembagian.

Contoh:

```text
10 MOD 2 = 0
```

Karena:

```text
10 ÷ 2 = 5
```

tidak memiliki sisa.

Maka:

```text
10 = GENAP
```

Contoh:

```text
7 MOD 2 = 1
```

Karena:

```text
7 ÷ 2 = 3 sisa 1
```

Maka:

```text
7 = GANJIL
```

---

# 34. Flowchart Lebih dari Dua Kondisi

Contoh grade:

```text
Nilai >= 85 → A
Nilai >= 75 → B
Nilai >= 65 → C
Selain itu → D
```

Alur:

```text
INPUT NILAI
    ↓
Nilai >= 85?
 /        \
YA        TIDAK
↓           ↓
A       Nilai >=75?
         /      \
       YA       TIDAK
       ↓          ↓
       B       Nilai >=65?
                /     \
              YA      TIDAK
              ↓         ↓
              C         D
```

---

# 35. Flowchart Pengulangan

Masalah:

```text
Menampilkan angka 1 sampai 5.
```

Flowchart konsep:

```text
MULAI
  ↓
i = 1
  ↓
i <= 5?
 /    \
YA    TIDAK
↓       ↓
OUTPUT i  SELESAI
↓
i = i + 1
↓
KEMBALI KE
i <= 5?
```

---

# 36. Hubungan Pseudocode dan Flowchart

Pseudocode:

```text
MULAI

INPUT nilai

IF nilai >= 75
    OUTPUT "Lulus"
ELSE
    OUTPUT "Tidak Lulus"

SELESAI
```

Flowchart:

```text
Input nilai
    ↓
nilai >= 75?
 /         \
Ya         Tidak
↓            ↓
Lulus    Tidak Lulus
```

Keduanya menjelaskan logika yang sama.

Perbedaannya hanya bentuk penyajiannya.

---

# 37. Perbedaan Algoritma, Pseudocode, Flowchart, dan Program

## Algoritma

Menjelaskan langkah secara umum.

```text
1. Masukkan dua angka.
2. Jumlahkan.
3. Tampilkan hasil.
```

## Pseudocode

```text
INPUT angka1
INPUT angka2
hasil = angka1 + angka2
OUTPUT hasil
```

## Flowchart

```text
INPUT
 ↓
PROSES
 ↓
OUTPUT
```

## Program

Nantinya dalam Python:

```python
angka1 = int(input("Angka 1: "))
angka2 = int(input("Angka 2: "))

hasil = angka1 + angka2

print(hasil)
```

Urutan belajarnya:

```text
MASALAH
   ↓
ALGORITMA
   ↓
PSEUDOCODE
   ↓
FLOWCHART
   ↓
PROGRAM
```

---

# 38. Apa Itu Dry Run?

Dry Run adalah proses menjalankan algoritma secara manual menggunakan contoh data.

Tujuannya adalah memastikan logika kita benar sebelum membuat kode.

Contoh pseudocode:

```text
INPUT angka1
INPUT angka2

hasil = angka1 + angka2

OUTPUT hasil
```

Gunakan data:

```text
angka1 = 5
angka2 = 10
```

Dry Run:

```text
hasil = angka1 + angka2

hasil = 5 + 10

hasil = 15
```

Output:

```text
15
```

---

# 39. Dry Run Percabangan

Pseudocode:

```text
INPUT umur

IF umur >= 17
    OUTPUT "Boleh SIM"
ELSE
    OUTPUT "Belum Boleh SIM"
```

Data:

```text
umur = 20
```

Periksa:

```text
20 >= 17
```

Hasil:

```text
BENAR
```

Maka output:

```text
Boleh SIM
```

---

# 40. Trace Table

Untuk program yang lebih kompleks, kita bisa menggunakan tabel penelusuran.

Pseudocode:

```text
i = 1

WHILE i <= 3
    OUTPUT i
    i = i + 1
```

Trace Table:

| Langkah | Nilai i | Kondisi i <= 3 |  Output |
| ------- | ------: | -------------- | ------: |
| 1       |       1 | Benar          |       1 |
| 2       |       2 | Benar          |       2 |
| 3       |       3 | Benar          |       3 |
| 4       |       4 | Salah          | Selesai |

Dengan tabel ini kita dapat melihat bagaimana nilai berubah.

---

# 41. Kesalahan Umum dalam Pseudocode

## Kesalahan 1 — Tidak Memiliki Urutan

Salah:

```text
OUTPUT luas
INPUT panjang
INPUT lebar
HITUNG luas
```

Benar:

```text
INPUT panjang
INPUT lebar
HITUNG luas
OUTPUT luas
```

---

# 42. Kesalahan 2 — Menggunakan Data yang Belum Ada

Salah:

```text
total = harga × jumlah

INPUT harga
INPUT jumlah
```

Kita melakukan perhitungan sebelum mendapatkan nilai.

Benar:

```text
INPUT harga
INPUT jumlah

total = harga × jumlah
```

---

# 43. Kesalahan 3 — Kondisi Tidak Lengkap

Contoh:

```text
IF nilai >= 75
    OUTPUT "Lulus"
```

Bagaimana jika:

```text
nilai = 50?
```

Jika sistem membutuhkan hasil untuk kondisi tersebut, tambahkan:

```text
ELSE
    OUTPUT "Tidak Lulus"
```

---

# 44. Kesalahan 4 — Kondisi Bertabrakan

Contoh:

```text
Jika nilai >= 60 → C
Jika nilai >= 75 → B
Jika nilai >= 85 → A
```

Urutan kurang tepat.

Lebih baik:

```text
Jika nilai >= 85 → A
Jika tidak dan nilai >= 75 → B
Jika tidak dan nilai >= 60 → C
Selain itu → D
```

---

# 45. Kesalahan 5 — Perulangan Tidak Memiliki Akhir

Contoh:

```text
i = 1

WHILE i <= 10
    OUTPUT i
```

Nilai `i` tidak berubah.

Akibatnya program terus mengulang.

Benar:

```text
i = 1

WHILE i <= 10
    OUTPUT i
    i = i + 1
```

---

# 46. Cara Membuat Pseudocode dari Soal

Gunakan langkah berikut.

## Langkah 1 — Baca Soal

Contoh:

```text
Hitung luas lingkaran.
```

Rumus:

```text
L = π × r × r
```

## Langkah 2 — Tentukan Input

```text
r
```

## Langkah 3 — Tentukan Proses

```text
L = 3.14 × r × r
```

## Langkah 4 — Tentukan Output

```text
Luas
```

## Langkah 5 — Buat Pseudocode

```text
MULAI

INPUT r

luas = 3.14 × r × r

OUTPUT luas

SELESAI
```

---

# 47. Cara Membuat Flowchart dari Pseudocode

Pseudocode:

```text
MULAI

INPUT panjang
INPUT lebar

luas = panjang × lebar

OUTPUT luas

SELESAI
```

Identifikasi:

```text
MULAI
→ Terminator

INPUT panjang
→ Input

INPUT lebar
→ Input

luas = panjang × lebar
→ Process

OUTPUT luas
→ Output

SELESAI
→ Terminator
```

Kemudian hubungkan menggunakan panah.

---