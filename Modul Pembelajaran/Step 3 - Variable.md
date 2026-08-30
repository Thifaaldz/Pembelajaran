# Tahap 3 — Variabel, Tipe Data, dan Operator

## Algoritma dan Pemrograman untuk Pemula

Tahap ini merupakan kelanjutan dari:

```text
Tahap 1 — Dasar Logika Pemrograman
        ↓
Tahap 2 — Pseudocode dan Flowchart
        ↓
Tahap 3 — Variabel, Tipe Data, dan Operator
```

Pada Tahap 1 dan 2, kita sudah memahami:

* logika pemrograman,
* algoritma,
* pseudocode,
* flowchart,
* sequence,
* kondisi,
* pengulangan secara konsep,
* serta bagaimana menyusun langkah penyelesaian.

Pada Tahap 3 ini, kita mulai mengenal bagaimana sebuah program **menyimpan dan mengolah data**.

Bahasa pemrograman yang akan digunakan sebagai contoh adalah:

# Python

Python dipilih karena memiliki penulisan yang relatif sederhana dan mudah dibaca oleh pemula.

---

# 1. Tujuan Pembelajaran

Setelah menyelesaikan Tahap 3, mahasiswa diharapkan mampu:

1. Memahami apa itu variabel.
2. Memahami fungsi variabel.
3. Membuat variabel sederhana.
4. Memahami aturan penamaan variabel.
5. Memahami konsep nilai atau value.
6. Memahami tipe data.
7. Mengenal tipe data Integer.
8. Mengenal tipe data Float.
9. Mengenal tipe data String.
10. Mengenal tipe data Boolean.
11. Menggunakan fungsi `type()`.
12. Memahami perubahan nilai variabel.
13. Memahami operator aritmatika.
14. Memahami operator perbandingan.
15. Memahami operator logika.
16. Memahami operator assignment.
17. Memahami prioritas operasi.
18. Melakukan operasi sederhana menggunakan variabel.
19. Membaca kode Python sederhana.
20. Membuat program perhitungan sederhana.

---

# 2. Sebelum Mengenal Variabel

Bayangkan kita mempunyai data:

```text
Nama mahasiswa = Budi
Umur mahasiswa = 20
Nilai mahasiswa = 85
```

Jika program ingin menggunakan data tersebut, program membutuhkan tempat untuk menyimpannya.

Secara konsep:

```text
Nama
┌──────────────┐
│ Budi         │
└──────────────┘

Umur
┌──────────────┐
│ 20           │
└──────────────┘

Nilai
┌──────────────┐
│ 85           │
└──────────────┘
```

Tempat penyimpanan tersebut disebut:

# Variabel

---

# 3. Apa Itu Variabel?

Variabel adalah tempat untuk menyimpan suatu nilai atau data di dalam program.

Secara sederhana:

> Variabel dapat dianggap seperti sebuah kotak yang mempunyai nama dan dapat menyimpan data.

Contoh:

```text
nama = "Budi"
```

Artinya:

```text
Variabel:
nama

Menyimpan:
Budi
```

Visual:

```text
┌────────────────┐
│ nama           │
│                │
│ "Budi"         │
└────────────────┘
```

---

# 4. Contoh Variabel Lain

```python
nama = "Budi"
umur = 20
nilai = 85
```

Artinya:

```text
nama
↓
"Budi"

umur
↓
20

nilai
↓
85
```

Program dapat menggunakan nilai tersebut kapan pun dibutuhkan.

---

# 5. Mengapa Variabel Dibutuhkan?

Bayangkan kita ingin menghitung:

```text
10 × 5
```

Kita dapat langsung menulis:

```python
10 * 5
```

Tetapi bagaimana jika angka tersebut sebenarnya adalah:

```text
panjang = 10
lebar = 5
```

Lebih mudah dipahami jika kita menulis:

```python
panjang = 10
lebar = 5

luas = panjang * lebar
```

Daripada:

```python
luas = 10 * 5
```

Variabel membuat program menjadi:

* lebih mudah dibaca,
* lebih mudah dipahami,
* lebih mudah diubah,
* lebih mudah digunakan kembali.

---

# 6. Variabel sebagai Kotak Penyimpanan

Misalnya:

```python
umur = 20
```

Bayangkan:

```text
┌─────────────┐
│ umur        │
│             │
│ 20          │
└─────────────┘
```

Kemudian:

```python
nama = "Andi"
```

```text
┌─────────────┐
│ nama        │
│             │
│ "Andi"      │
└─────────────┘
```

Setiap variabel mempunyai:

```text
NAMA
+
NILAI
```

---

# 7. Mengenal Assignment

Perhatikan:

```python
umur = 20
```

Tanda:

```text
=
```

di sini bukan berarti "sama dengan" seperti dalam matematika.

Dalam pemrograman, tanda tersebut digunakan untuk:

> memberikan nilai kepada variabel.

Artinya:

```text
Simpan nilai 20
ke dalam variabel umur
```

Konsep ini disebut:

# Assignment

---

# 8. Arah Assignment

Perhatikan:

```python
umur = 20
```

Cara membacanya:

```text
20
↓
disimpan ke
↓
umur
```

Bukan:

```text
umur sama dengan 20 secara matematis
```

Untuk sementara, biasakan membaca:

```text
umur diberi nilai 20
```

---

# 9. Contoh Assignment

```python
nama = "Siti"
umur = 19
tinggi = 160.5
aktif = True
```

Artinya:

```text
nama
→ "Siti"

umur
→ 19

tinggi
→ 160.5

aktif
→ True
```

---

# 10. Nilai Variabel Dapat Berubah

Variabel disebut variabel karena nilainya dapat berubah.

Contoh:

```python
nilai = 70
```

Kemudian:

```python
nilai = 90
```

Nilai terakhir dari variabel `nilai` adalah:

```text
90
```

Nilai sebelumnya:

```text
70
```

digantikan.

---

# 11. Contoh Perubahan Nilai

```python
saldo = 100000
saldo = 75000
```

Awalnya:

```text
saldo = 100000
```

Kemudian berubah menjadi:

```text
saldo = 75000
```

Sehingga nilai terakhir adalah:

```text
75000
```

---

# 12. Variabel Bisa Menggunakan Nilai Sebelumnya

Contoh:

```python
saldo = 100000
saldo = saldo - 25000
```

Cara membaca:

```text
Saldo awal = 100000

Saldo baru =
Saldo lama - 25000
```

Maka:

```text
100000 - 25000
= 75000
```

Sehingga:

```text
saldo = 75000
```

---

# 13. Ini Bukan Persamaan Matematika

Dalam matematika:

```text
x = x + 1
```

terlihat tidak masuk akal.

Tetapi dalam pemrograman:

```python
x = x + 1
```

artinya:

```text
Ambil nilai x sekarang
        ↓
Tambahkan 1
        ↓
Simpan kembali ke x
```

Jika:

```text
x = 5
```

maka:

```text
x = x + 1

x = 5 + 1

x = 6
```

---

# 14. Aturan Penamaan Variabel

Nama variabel sebaiknya menggambarkan data yang disimpan.

Baik:

```python
nama_mahasiswa = "Budi"
umur = 20
nilai_akhir = 85
harga_barang = 10000
```

Kurang baik:

```python
a = "Budi"
b = 20
c = 85
d = 10000
```

Nama yang jelas membuat program lebih mudah dibaca.

---

# 15. Nama Variabel Tidak Boleh Menggunakan Spasi

Salah:

```python
nama mahasiswa = "Budi"
```

Python akan menganggapnya salah.

Gunakan:

```python
nama_mahasiswa = "Budi"
```

Tanda:

```text
_
```

disebut:

# underscore

---

# 16. Nama Variabel Tidak Boleh Diawali Angka

Salah:

```python
1nama = "Budi"
```

Benar:

```python
nama1 = "Budi"
```

atau:

```python
nama_mahasiswa1 = "Budi"
```

---

# 17. Nama Variabel Boleh Mengandung Angka

Contoh:

```python
nilai1 = 80
nilai2 = 90
nilai3 = 70
```

Tetapi:

```python
1nilai = 80
```

tidak diperbolehkan.

---

# 18. Hindari Karakter Khusus

Sebaiknya jangan menggunakan:

```text
@
#
$
%
&
*
-
```

dalam nama variabel.

Contoh salah:

```python
nilai-akhir = 90
harga@barang = 10000
```

Gunakan:

```python
nilai_akhir = 90
harga_barang = 10000
```

---

# 19. Python Case Sensitive

Python membedakan huruf besar dan kecil.

Contoh:

```python
nama = "Budi"
Nama = "Siti"
NAMA = "Andi"
```

Ketiganya dianggap sebagai variabel yang berbeda.

```text
nama ≠ Nama ≠ NAMA
```

Karena itu disarankan menggunakan format yang konsisten.

---

# 20. Snake Case

Dalam Python, nama variabel biasanya menggunakan:

# snake_case

Contoh:

```python
nama_mahasiswa = "Budi"
nilai_akhir = 90
harga_barang = 15000
jumlah_barang = 3
```

Kata dipisahkan menggunakan underscore.

---

# 21. Hindari Nama Variabel yang Tidak Jelas

Kurang baik:

```python
x = 10000
y = 3
z = x * y
```

Lebih baik:

```python
harga_barang = 10000
jumlah_barang = 3
total_harga = harga_barang * jumlah_barang
```

Kode kedua jauh lebih mudah dipahami.

---

# 22. Apa Itu Data?

Data adalah informasi yang digunakan atau disimpan oleh program.

Contoh:

```text
Budi
20
85.5
True
```

Semua merupakan data.

Namun data tersebut memiliki jenis yang berbeda.

Jenis data disebut:

# Tipe Data

---

# 23. Apa Itu Tipe Data?

Tipe data adalah jenis dari suatu nilai yang disimpan di dalam program.

Misalnya:

```text
20
```

adalah angka bulat.

```text
20.5
```

adalah angka desimal.

```text
"Budi"
```

adalah teks.

```text
True
```

adalah nilai logika.

Python mempunyai beberapa tipe data.

Pada tahap awal kita fokus pada:

```text
Integer
Float
String
Boolean
```

---

# 24. Integer

Integer adalah tipe data untuk bilangan bulat.

Contoh:

```text
1
10
20
100
-5
-100
0
```

Dalam Python:

```python
umur = 20
jumlah_barang = 5
tahun = 2026
```

Semua merupakan:

# Integer

Disingkat:

```text
int
```

---

# 25. Contoh Integer

```python
umur = 20
jumlah_mahasiswa = 30
stok = 100
```

Tidak mempunyai bagian desimal.

---

# 26. Integer Bisa Negatif

Contoh:

```python
suhu = -5
saldo = -10000
```

Keduanya tetap bertipe:

```text
Integer
```

---

# 27. Float

Float digunakan untuk angka yang mempunyai bagian desimal.

Contoh:

```text
10.5
20.75
3.14
85.5
```

Dalam Python:

```python
tinggi = 170.5
berat = 60.7
ipk = 3.75
```

Tipe datanya:

# Float

---

# 28. Perbedaan Integer dan Float

Integer:

```python
umur = 20
```

Float:

```python
tinggi = 170.5
```

Perbedaan:

```text
20
→ Integer

20.0
→ Float
```

Walaupun nilainya secara matematis sama, Python melihat tipe datanya berbeda.

---

# 29. String

String digunakan untuk menyimpan teks.

Contoh:

```python
nama = "Budi"
alamat = "Jakarta"
jurusan = "Sistem Informasi"
```

String biasanya ditulis menggunakan:

```text
" "
```

atau:

```text
' '
```

Contoh:

```python
nama = "Budi"
```

atau:

```python
nama = 'Budi'
```

Keduanya valid.

---

# 30. Angka Bisa Menjadi String

Perhatikan:

```python
umur = 20
```

Ini:

```text
Integer
```

Tetapi:

```python
umur = "20"
```

Ini:

```text
String
```

Mengapa?

Karena `"20"` berada di dalam tanda kutip.

---

# 31. Contoh String

```python
nama = "Siti"
nim = "202601234"
kelas = "SI-01"
nomor_telepon = "08123456789"
```

Perhatikan `nomor_telepon`.

Walaupun berisi angka, sering kali lebih cocok disimpan sebagai String karena:

```text
Nomor telepon tidak digunakan untuk perhitungan matematika.
```

---

# 32. Boolean

Boolean adalah tipe data yang hanya memiliki dua nilai:

```text
True
False
```

Artinya:

```text
Benar
Salah
```

Contoh:

```python
sudah_login = True
sudah_bayar = False
aktif = True
```

---

# 33. Boolean Sangat Penting

Boolean banyak digunakan untuk kondisi.

Contoh:

```text
Apakah pengguna sudah login?
```

Jawabannya hanya:

```text
True
atau
False
```

Contoh:

```python
sudah_login = True
```

Artinya:

```text
Pengguna sudah login.
```

---

# 34. Ringkasan Tipe Data Dasar

| Tipe Data | Fungsi           | Contoh   |
| --------- | ---------------- | -------- |
| Integer   | Bilangan bulat   | `20`     |
| Float     | Bilangan desimal | `20.5`   |
| String    | Teks             | `"Budi"` |
| Boolean   | Benar / Salah    | `True`   |

---

# 35. Contoh Gabungan

```python
nama = "Budi"
umur = 20
ipk = 3.75
aktif = True
```

Maka:

```text
nama
→ String

umur
→ Integer

ipk
→ Float

aktif
→ Boolean
```

---

# 36. Mengenal Fungsi type()

Python mempunyai fungsi:

```python
type()
```

untuk mengetahui tipe suatu data.

Contoh:

```python
umur = 20

print(type(umur))
```

Hasil:

```text
<class 'int'>
```

Artinya:

```text
umur bertipe Integer
```

---

# 37. Contoh type() Lain

```python
nama = "Budi"
tinggi = 170.5
aktif = True

print(type(nama))
print(type(tinggi))
print(type(aktif))
```

Hasil kurang lebih:

```text
<class 'str'>
<class 'float'>
<class 'bool'>
```

---

# 38. Singkatan Tipe Data dalam Python

```text
Integer
→ int

Float
→ float

String
→ str

Boolean
→ bool
```

---

# 39. Apa Itu Operator?

Operator adalah simbol yang digunakan untuk melakukan operasi terhadap nilai atau variabel.

Contoh:

```python
hasil = 10 + 5
```

Tanda:

```text
+
```

adalah operator.

---

# 40. Jenis Operator yang Akan Dipelajari

Pada tahap ini kita akan mengenal:

```text
1. Operator Aritmatika
2. Operator Assignment
3. Operator Perbandingan
4. Operator Logika
```

---

# 41. Operator Aritmatika

Operator aritmatika digunakan untuk operasi matematika.

Operator dasar:

| Operator | Fungsi          |
| -------- | --------------- |
| `+`      | Penjumlahan     |
| `-`      | Pengurangan     |
| `*`      | Perkalian       |
| `/`      | Pembagian       |
| `%`      | Modulus         |
| `//`     | Pembagian bulat |
| `**`     | Pangkat         |

---

# 42. Penjumlahan

```python
angka1 = 10
angka2 = 5

hasil = angka1 + angka2
```

Hasil:

```text
15
```

---

# 43. Pengurangan

```python
angka1 = 10
angka2 = 5

hasil = angka1 - angka2
```

Hasil:

```text
5
```

---

# 44. Perkalian

```python
angka1 = 10
angka2 = 5

hasil = angka1 * angka2
```

Hasil:

```text
50
```

---

# 45. Pembagian

```python
angka1 = 10
angka2 = 5

hasil = angka1 / angka2
```

Hasil:

```text
2.0
```

Perhatikan hasilnya:

```text
2.0
```

bukan:

```text
2
```

Pada Python, operator `/` menghasilkan Float.

---

# 46. Modulus

Operator:

```text
%
```

digunakan untuk mencari sisa pembagian.

Contoh:

```python
hasil = 10 % 3
```

Karena:

```text
10 ÷ 3
= 3
sisa 1
```

maka:

```text
hasil = 1
```

---

# 47. Modulus untuk Menentukan Genap

Contoh:

```python
angka = 10

sisa = angka % 2
```

Hasil:

```text
0
```

Jika:

```text
angka % 2 = 0
```

maka angka tersebut genap.

---

# 48. Pembagian Bulat

Operator:

```text
//
```

menghasilkan hasil pembagian tanpa bagian desimal.

Contoh:

```python
hasil = 10 // 3
```

Hasil:

```text
3
```

Sedangkan:

```python
hasil = 10 / 3
```

menghasilkan sekitar:

```text
3.333333
```

---

# 49. Pangkat

Operator:

```text
**
```

digunakan untuk pangkat.

Contoh:

```python
hasil = 2 ** 3
```

Artinya:

```text
2³
```

atau:

```text
2 × 2 × 2
```

Hasil:

```text
8
```

---

# 50. Contoh Luas Persegi

Rumus:

```text
Luas = sisi × sisi
```

Python:

```python
sisi = 5

luas = sisi * sisi

print(luas)
```

Hasil:

```text
25
```

Bisa juga:

```python
luas = sisi ** 2
```

---

# 51. Contoh Luas Persegi Panjang

```python
panjang = 10
lebar = 5

luas = panjang * lebar

print(luas)
```

Hasil:

```text
50
```

---

# 52. Contoh Luas Segitiga

Rumus:

```text
Luas = 1/2 × Alas × Tinggi
```

Python:

```python
alas = 10
tinggi = 8

luas = 0.5 * alas * tinggi

print(luas)
```

Hasil:

```text
40.0
```

---

# 53. Operator Assignment

Kita sudah mengenal:

```text
=
```

Contoh:

```python
nilai = 80
```

Selain itu terdapat operator assignment lain.

| Operator | Contoh   |
| -------- | -------- |
| `=`      | `x = 10` |
| `+=`     | `x += 1` |
| `-=`     | `x -= 1` |
| `*=`     | `x *= 2` |
| `/=`     | `x /= 2` |

---

# 54. Operator +=

Contoh:

```python
x = 5

x += 1
```

Sama dengan:

```python
x = x + 1
```

Hasil:

```text
6
```

---

# 55. Operator -=

```python
saldo = 100000

saldo -= 25000
```

Sama dengan:

```python
saldo = saldo - 25000
```

Hasil:

```text
75000
```

---

# 56. Operator *=

```python
angka = 5

angka *= 2
```

Sama dengan:

```python
angka = angka * 2
```

Hasil:

```text
10
```

---

# 57. Operator Perbandingan

Operator perbandingan digunakan untuk membandingkan dua nilai.

Hasil operator perbandingan selalu:

```text
True
atau
False
```

Operator:

| Operator | Arti                         |
| -------- | ---------------------------- |
| `==`     | Sama dengan                  |
| `!=`     | Tidak sama dengan            |
| `>`      | Lebih besar                  |
| `<`      | Lebih kecil                  |
| `>=`     | Lebih besar atau sama dengan |
| `<=`     | Lebih kecil atau sama dengan |

---

# 58. Perbedaan = dan ==

Ini sangat penting.

```text
=
```

digunakan untuk:

```text
Memberikan nilai
```

Contoh:

```python
umur = 20
```

Sedangkan:

```text
==
```

digunakan untuk:

```text
Membandingkan nilai
```

Contoh:

```python
umur == 20
```

Artinya:

```text
Apakah umur sama dengan 20?
```

---

# 59. Contoh ==

```python
umur = 20

hasil = umur == 20

print(hasil)
```

Hasil:

```text
True
```

---

# 60. Contoh !=

```python
umur = 20

hasil = umur != 20
```

Artinya:

```text
Apakah umur tidak sama dengan 20?
```

Jawaban:

```text
False
```

Karena umur memang 20.

---

# 61. Operator >

```python
nilai = 80

hasil = nilai > 75
```

Karena:

```text
80 > 75
```

maka:

```text
True
```

---

# 62. Operator <

```python
umur = 15

hasil = umur < 17
```

Karena:

```text
15 < 17
```

hasil:

```text
True
```

---

# 63. Operator >=

```python
nilai = 75

hasil = nilai >= 75
```

Hasil:

```text
True
```

Karena:

```text
75 sama dengan 75
```

dan operator `>=` berarti:

```text
lebih besar
ATAU
sama dengan
```

---

# 64. Operator <=

```python
umur = 17

hasil = umur <= 17
```

Hasil:

```text
True
```

---

# 65. Operator Logika

Operator logika digunakan untuk menggabungkan beberapa kondisi.

Python memiliki:

```text
and
or
not
```

---

# 66. Operator and

`and` berarti kedua kondisi harus benar.

Contoh:

```python
umur = 20
punya_ktp = True

hasil = umur >= 17 and punya_ktp == True
```

Kondisi 1:

```text
20 >= 17
→ True
```

Kondisi 2:

```text
punya_ktp = True
→ True
```

Maka:

```text
True AND True
→ True
```

---

# 67. Tabel AND

| Kondisi 1 | Kondisi 2 | Hasil |
| --------- | --------- | ----- |
| True      | True      | True  |
| True      | False     | False |
| False     | True      | False |
| False     | False     | False |

Sederhananya:

> AND membutuhkan semua kondisi benar.

---

# 68. Contoh Login dengan AND

```python
username_benar = True
password_benar = True

login = username_benar and password_benar
```

Hasil:

```text
True
```

Jika:

```python
username_benar = True
password_benar = False
```

hasil:

```text
False
```

---

# 69. Operator OR

`or` berarti cukup salah satu kondisi benar.

Contoh:

```python
punya_kartu_mahasiswa = False
punya_surat = True

boleh_masuk = punya_kartu_mahasiswa or punya_surat
```

Hasil:

```text
True
```

Karena salah satu kondisi benar.

---

# 70. Tabel OR

| Kondisi 1 | Kondisi 2 | Hasil |
| --------- | --------- | ----- |
| True      | True      | True  |
| True      | False     | True  |
| False     | True      | True  |
| False     | False     | False |

---

# 71. Operator NOT

`not` digunakan untuk membalik nilai Boolean.

Contoh:

```python
aktif = True
```

Jika:

```python
not aktif
```

hasil:

```text
False
```

Jika:

```python
aktif = False
```

maka:

```python
not aktif
```

hasil:

```text
True
```

---

# 72. Contoh Operator Logika

```python
nilai = 80
kehadiran = 90

hasil = nilai >= 75 and kehadiran >= 80
```

Periksa:

```text
80 >= 75
→ True

90 >= 80
→ True
```

Sehingga:

```text
True and True
→ True
```

Mahasiswa memenuhi kedua syarat.

---

# 73. Prioritas Operasi

Perhatikan:

```python
hasil = 2 + 3 * 4
```

Apakah:

```text
2 + 3 = 5
5 × 4 = 20
```

?

Tidak.

Perkalian dilakukan lebih dulu.

```text
3 × 4 = 12

2 + 12 = 14
```

Hasil:

```text
14
```

---

# 74. Gunakan Kurung Jika Perlu

Jika ingin penjumlahan dilakukan lebih dahulu:

```python
hasil = (2 + 3) * 4
```

Maka:

```text
2 + 3 = 5

5 × 4 = 20
```

Hasil:

```text
20
```

---

# 75. Urutan Sederhana Operasi

Secara sederhana:

```text
1. Kurung ()
2. Pangkat **
3. Perkalian / Pembagian / Modulus
4. Penjumlahan / Pengurangan
5. Perbandingan
6. Operator Logika
```

Untuk pemula, jika ragu gunakan tanda kurung agar lebih jelas.

---

# 76. String dan Operator +

Operator `+` juga dapat digunakan pada String.

Contoh:

```python
nama_depan = "Budi"
nama_belakang = "Santoso"

nama_lengkap = nama_depan + nama_belakang
```

Hasil:

```text
BudiSantoso
```

Tidak ada spasi.

Untuk menambahkan spasi:

```python
nama_lengkap = nama_depan + " " + nama_belakang
```

Hasil:

```text
Budi Santoso
```

---

# 77. String dan Operator *

Contoh:

```python
kata = "Halo "

hasil = kata * 3
```

Hasil:

```text
Halo Halo Halo
```

---

# 78. Kesalahan Tipe Data

Perhatikan:

```python
umur = "20"
```

Karena `"20"` adalah String.

Jika kita menulis:

```python
hasil = umur + 5
```

akan terjadi error.

Mengapa?

Karena program mencoba:

```text
String + Integer
```

Python tidak mengetahui apakah kita ingin:

```text
"205"
```

atau:

```text
25
```

---

# 79. Type Conversion

Kadang-kadang kita perlu mengubah tipe data.

Proses ini disebut:

# Type Conversion

atau:

# Casting

Fungsi yang umum:

```text
int()
float()
str()
bool()
```

---

# 80. Mengubah String Menjadi Integer

```python
umur = "20"

umur = int(umur)
```

Awalnya:

```text
"20"
→ String
```

Setelah:

```python
int("20")
```

menjadi:

```text
20
→ Integer
```

---

# 81. Mengubah Integer Menjadi String

```python
umur = 20

umur_teks = str(umur)
```

Hasil:

```text
"20"
```

---

# 82. Mengubah Integer Menjadi Float

```python
angka = 10

hasil = float(angka)
```

Hasil:

```text
10.0
```

---

# 83. Mengapa Casting Penting?

Nantinya ketika pengguna memasukkan data melalui:

```python
input()
```

data yang masuk secara default adalah String.

Misalnya pengguna mengetik:

```text
20
```

Python bisa membacanya sebagai:

```text
"20"
```

Karena itu, untuk melakukan perhitungan kita perlu:

```python
int()
```

atau:

```python
float()
```

Materi ini akan digunakan lebih banyak pada Tahap 4.

---

# 84. Contoh dari Pseudocode ke Python

Pseudocode:

```text
MULAI

panjang = 10
lebar = 5

luas = panjang × lebar

OUTPUT luas

SELESAI
```

Python:

```python
panjang = 10
lebar = 5

luas = panjang * lebar

print(luas)
```

Hasil:

```text
50
```

---

# 85. Contoh Nilai Mahasiswa

```python
nilai_tugas = 80
nilai_uts = 70
nilai_uas = 90

nilai_akhir = (
    nilai_tugas * 0.30
    + nilai_uts * 0.30
    + nilai_uas * 0.40
)

print(nilai_akhir)
```

Perhitungan:

```text
80 × 0.30 = 24

70 × 0.30 = 21

90 × 0.40 = 36
```

Total:

```text
24 + 21 + 36 = 81
```

---

# 86. Contoh Sistem Kasir Sederhana

```python
nama_barang = "Buku"
harga_barang = 10000
jumlah_barang = 3

subtotal = harga_barang * jumlah_barang

print(subtotal)
```

Perhitungan:

```text
10000 × 3
= 30000
```

---

# 87. Menambahkan Diskon

Misalnya diskon diketahui sebesar:

```text
10%
```

Kode:

```python
subtotal = 200000
diskon_persen = 10

diskon = subtotal * diskon_persen / 100

total_bayar = subtotal - diskon
```

Perhitungan:

```text
Diskon =
200000 × 10 / 100

= 20000
```

Total:

```text
200000 - 20000
= 180000
```

---

# 88. Contoh Biodata

```python
nama = "Budi"
umur = 20
tinggi = 170.5
mahasiswa_aktif = True
```

Tipe:

```text
nama
→ String

umur
→ Integer

tinggi
→ Float

mahasiswa_aktif
→ Boolean
```

---

# 89. Membaca Kode dari Atas ke Bawah

Perhatikan:

```python
angka1 = 10
angka2 = 20

hasil = angka1 + angka2

print(hasil)
```

Python secara sederhana menjalankan:

```text
1. Buat angka1 = 10
2. Buat angka2 = 20
3. Hitung angka1 + angka2
4. Simpan ke hasil
5. Tampilkan hasil
```

Hasil:

```text
30
```

---

# 90. Melakukan Dry Run

Kode:

```python
x = 5
y = 3

hasil = x * y + 2
```

Dry Run:

```text
x = 5
y = 3

hasil = 5 × 3 + 2

hasil = 15 + 2

hasil = 17
```

---

# 91. Trace Table Variabel

Kode:

```python
x = 5
x = x + 2
x = x * 3
```

Trace:

| Langkah     | Nilai x |
| ----------- | ------: |
| `x = 5`     |       5 |
| `x = x + 2` |       7 |
| `x = x * 3` |      21 |

Nilai akhir:

```text
21
```

---

# 92. Kesalahan Umum Pemula — String dan Integer

Salah:

```python
umur = "20"
hasil = umur + 5
```

Masalah:

```text
"20"
adalah String

5
adalah Integer
```

Keduanya tidak bisa langsung dijumlahkan secara matematis.

Perbaikan:

```python
umur = "20"
umur = int(umur)

hasil = umur + 5
```

Hasil:

```text
25
```

---

# 93. Kesalahan Umum — Salah Menggunakan =

Salah konsep:

```python
nilai = 80

nilai = 75
```

Jika ingin mengecek:

```text
Apakah nilai sama dengan 75?
```

gunakan:

```python
nilai == 75
```

---

# 94. Kesalahan Umum — Salah Penamaan Variabel

Salah:

```python
harga barang = 10000
```

Benar:

```python
harga_barang = 10000
```

---

# 95. Kesalahan Umum — Variabel Belum Dibuat

Salah:

```python
luas = panjang * lebar
```

Padahal:

```text
panjang
dan
lebar
```

belum memiliki nilai.

Benar:

```python
panjang = 10
lebar = 5

luas = panjang * lebar
```

---

# 96. Kesalahan Umum — Typo Nama Variabel

Contoh:

```python
harga_barang = 10000

total = harga_baranng * 2
```

Masalah:

```text
harga_barang
```

berbeda dengan:

```text
harga_baranng
```

Satu huruf saja berbeda dianggap sebagai variabel berbeda.

---
