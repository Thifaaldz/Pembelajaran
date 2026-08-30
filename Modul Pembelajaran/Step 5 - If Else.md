# Tahap 5 — Percabangan / Conditional

## Algoritma dan Pemrograman Python untuk Pemula

Tahap ini merupakan kelanjutan dari:

```text
Tahap 1 — Dasar Logika Pemrograman
        ↓
Tahap 2 — Pseudocode dan Flowchart
        ↓
Tahap 3 — Variabel, Tipe Data, dan Operator
        ↓
Tahap 4 — Input dan Output
        ↓
Tahap 5 — Percabangan / Conditional
```

Pada tahap sebelumnya kita sudah bisa membuat program seperti:

```python
nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))

print(f"Nama: {nama}")
print(f"Umur: {umur}")
```

Namun program tersebut belum dapat **mengambil keputusan**.

Misalnya:

```text
Jika umur >= 17
    Boleh membuat SIM

Jika umur < 17
    Belum boleh membuat SIM
```

Pada tahap ini kita akan membuat program mampu memilih tindakan berdasarkan kondisi.

---

# 1. Tujuan Pembelajaran

Setelah menyelesaikan Tahap 5, mahasiswa diharapkan mampu:

1. Memahami apa itu percabangan.
2. Memahami apa itu kondisi.
3. Memahami nilai Boolean.
4. Menggunakan operator perbandingan.
5. Menggunakan `if`.
6. Menggunakan `if-else`.
7. Menggunakan `if-elif-else`.
8. Membuat lebih dari dua kondisi.
9. Memahami urutan kondisi.
10. Menggunakan `and`.
11. Menggunakan `or`.
12. Menggunakan `not`.
13. Menggunakan nested `if`.
14. Membuat validasi input sederhana.
15. Menentukan ganjil atau genap.
16. Menentukan positif, negatif, atau nol.
17. Menentukan kelulusan mahasiswa.
18. Menentukan grade.
19. Membuat sistem diskon.
20. Membuat login sederhana.
21. Membuat validasi pembayaran.
22. Membuat program menu sederhana.
23. Melakukan dry run percabangan.
24. Menemukan kesalahan logika.
25. Membuat mini project berbasis kondisi.

---

# 2. Apa Itu Percabangan?

Percabangan adalah proses untuk memilih tindakan berdasarkan suatu kondisi.

Contoh kehidupan sehari-hari:

```text
Jika hujan
    Bawa payung
```

Contoh lain:

```text
Jika lapar
    Makan
```

Contoh:

```text
Jika nilai >= 75
    Lulus
```

Dalam programming konsep ini disebut:

```text
Conditional
Decision
Selection
Percabangan
```

---

# 3. Mengapa Percabangan Dibutuhkan?

Bayangkan kita membuat program nilai mahasiswa.

Program sebelumnya hanya dapat:

```text
Masukkan nilai
        ↓
Tampilkan nilai
```

Tetapi kita ingin program dapat menentukan:

```text
Nilai 80
    ↓
Apakah >= 75?
    ↓
Ya
    ↓
Lulus
```

Atau:

```text
Nilai 60
    ↓
Apakah >= 75?
    ↓
Tidak
    ↓
Tidak Lulus
```

Untuk itu kita membutuhkan percabangan.

---

# 4. Bentuk Dasar Kondisi

Secara konsep:

```text
JIKA kondisi benar
    lakukan sesuatu
```

Dalam Python:

```python
if kondisi:
    lakukan_sesuatu
```

Contoh:

```python
nilai = 80

if nilai >= 75:
    print("Lulus")
```

Output:

```text
Lulus
```

---

# 5. Mengenal `if`

`if` berarti:

```text
JIKA
```

Contoh:

```python
umur = 20

if umur >= 17:
    print("Boleh membuat SIM")
```

Cara membacanya:

```text
Jika umur lebih besar atau sama dengan 17
maka tampilkan:
"Boleh membuat SIM"
```

---

# 6. Struktur Dasar `if`

```python
if kondisi:
    perintah
```

Perhatikan:

```text
if
```

diikuti kondisi.

Kemudian:

```text
:
```

dan baris berikutnya harus memiliki indentasi.

---

# 7. Apa Itu Indentasi?

Indentasi adalah jarak atau spasi di awal baris kode.

Contoh benar:

```python
if umur >= 17:
    print("Boleh membuat SIM")
```

Perhatikan:

```python
    print(...)
```

memiliki beberapa spasi di depan.

Biasanya Python menggunakan:

```text
4 spasi
```

---

# 8. Mengapa Indentasi Penting?

Dalam Python, indentasi menentukan blok program.

Benar:

```python
if nilai >= 75:
    print("Lulus")
```

Salah:

```python
if nilai >= 75:
print("Lulus")
```

Python dapat menghasilkan error.

---

# 9. Contoh `if`

```python
nilai = 90

if nilai >= 75:
    print("Anda lulus")
```

Karena:

```text
90 >= 75
```

hasil:

```text
True
```

maka:

```text
Anda lulus
```

ditampilkan.

---

# 10. Bagaimana Jika Kondisi Salah?

Contoh:

```python
nilai = 60

if nilai >= 75:
    print("Anda lulus")
```

Karena:

```text
60 >= 75
```

hasil:

```text
False
```

maka:

```text
print("Anda lulus")
```

tidak dijalankan.

Program tidak menampilkan apa-apa.

---

# 11. Mengenal Boolean

Hasil sebuah kondisi biasanya berupa:

```text
True
```

atau:

```text
False
```

Contoh:

```python
print(80 >= 75)
```

Output:

```text
True
```

Contoh:

```python
print(60 >= 75)
```

Output:

```text
False
```

---

# 12. Operator Perbandingan

Operator perbandingan sangat penting pada percabangan.

| Operator | Arti                         |
| -------- | ---------------------------- |
| `==`     | Sama dengan                  |
| `!=`     | Tidak sama dengan            |
| `>`      | Lebih besar                  |
| `<`      | Lebih kecil                  |
| `>=`     | Lebih besar atau sama dengan |
| `<=`     | Lebih kecil atau sama dengan |

---

# 13. Contoh `==`

```python
nama = "Budi"

if nama == "Budi":
    print("Nama benar")
```

Artinya:

```text
Apakah nama sama dengan "Budi"?
```

---

# 14. Jangan Salah antara `=` dan `==`

Ini sangat penting.

```python
nilai = 80
```

berarti:

```text
Simpan 80 ke variabel nilai.
```

Sedangkan:

```python
nilai == 80
```

berarti:

```text
Apakah nilai sama dengan 80?
```

Jadi:

```text
=
Assignment
```

sedangkan:

```text
==
Comparison
```

---

# 15. Operator `!=`

Contoh:

```python
password = "12345"

if password != "admin":
    print("Password bukan admin")
```

`!=` berarti:

```text
tidak sama dengan
```

---

# 16. Operator `>`

```python
saldo = 100000

if saldo > 50000:
    print("Saldo lebih dari Rp50.000")
```

---

# 17. Operator `<`

```python
umur = 15

if umur < 17:
    print("Belum cukup umur")
```

---

# 18. Operator `>=`

```python
nilai = 75

if nilai >= 75:
    print("Lulus")
```

Nilai `75` tetap lulus karena:

```text
>=
```

berarti:

```text
lebih besar
ATAU
sama dengan
```

---

# 19. Operator `<=`

```python
stok = 5

if stok <= 5:
    print("Stok hampir habis")
```

---

# 20. Mengenal `else`

`else` digunakan ketika kondisi `if` salah.

Struktur:

```python
if kondisi:
    perintah_jika_benar
else:
    perintah_jika_salah
```

---

# 21. Contoh `if-else`

```python
nilai = 80

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")
```

Karena:

```text
80 >= 75
```

hasil:

```text
Lulus
```

---

# 22. Contoh Nilai Tidak Lulus

```python
nilai = 60

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")
```

Output:

```text
Tidak Lulus
```

---

# 23. Alur `if-else`

```text
         Kondisi
        /       \
      True      False
       ↓          ↓
   Perintah A  Perintah B
```

Contoh:

```text
       Nilai >= 75?
       /          \
     YA           TIDAK
     ↓              ↓
   Lulus       Tidak Lulus
```

---

# 24. Percabangan dengan Input

Sekarang kita gabungkan dengan materi sebelumnya.

```python
nilai = float(input("Masukkan nilai: "))

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")
```

Contoh:

```text
Masukkan nilai: 85

Lulus
```

---

# 25. Program Umur SIM

```python
umur = int(input("Masukkan umur: "))

if umur >= 17:
    print("Boleh membuat SIM")
else:
    print("Belum boleh membuat SIM")
```

---

# 26. Program Ganjil atau Genap

Untuk menentukan ganjil atau genap gunakan:

```text
%
```

Jika:

```text
angka % 2 == 0
```

maka:

```text
GENAP
```

Jika tidak:

```text
GANJIL
```

Program:

```python
angka = int(input("Masukkan angka: "))

if angka % 2 == 0:
    print("Genap")
else:
    print("Ganjil")
```

---

# 27. Mengapa `% 2 == 0`?

Misalnya:

```text
10 % 2 = 0
```

Karena 10 dibagi 2 tidak memiliki sisa.

Maka:

```text
10 = Genap
```

Contoh:

```text
7 % 2 = 1
```

Maka:

```text
7 = Ganjil
```

---

# 28. Menentukan Positif atau Negatif

```python
angka = int(input("Masukkan angka: "))

if angka > 0:
    print("Positif")
else:
    print("Negatif atau Nol")
```

Namun terdapat masalah.

Jika:

```text
angka = 0
```

program menampilkan:

```text
Negatif atau Nol
```

Padahal kita mungkin ingin membedakan nol.

Untuk itu kita membutuhkan kondisi lebih dari dua.

---

# 29. Mengenal `elif`

`elif` berarti:

```text
else if
```

atau:

```text
jika kondisi sebelumnya salah,
periksa kondisi berikutnya
```

Struktur:

```python
if kondisi1:
    ...
elif kondisi2:
    ...
else:
    ...
```

---

# 30. Positif, Negatif, dan Nol

```python
angka = int(input("Masukkan angka: "))

if angka > 0:
    print("Positif")
elif angka < 0:
    print("Negatif")
else:
    print("Nol")
```

---

# 31. Cara Kerja `if-elif-else`

Program membaca dari atas.

Contoh:

```python
if kondisi1:
    ...
elif kondisi2:
    ...
else:
    ...
```

Urutan:

```text
Periksa kondisi 1
        ↓
Jika benar → jalankan
        ↓
Jika salah → cek kondisi 2
        ↓
Jika kondisi 2 benar → jalankan
        ↓
Jika semua salah → jalankan else
```

---

# 32. Menentukan Grade

Misalnya aturan:

```text
Nilai >= 85 → A
Nilai >= 75 → B
Nilai >= 65 → C
Nilai >= 55 → D
Selain itu → E
```

Program:

```python
nilai = float(input("Masukkan nilai: "))

if nilai >= 85:
    print("Grade A")
elif nilai >= 75:
    print("Grade B")
elif nilai >= 65:
    print("Grade C")
elif nilai >= 55:
    print("Grade D")
else:
    print("Grade E")
```

---

# 33. Mengapa Tidak Menulis Batas Atas?

Perhatikan:

```python
if nilai >= 85:
    print("A")
elif nilai >= 75:
    print("B")
```

Untuk nilai:

```text
80
```

Kondisi pertama:

```text
80 >= 85
→ False
```

Kemudian:

```text
80 >= 75
→ True
```

Maka:

```text
B
```

Karena kondisi dibaca berurutan.

---

# 34. Urutan Kondisi Sangat Penting

Salah:

```python
if nilai >= 60:
    print("C")
elif nilai >= 75:
    print("B")
elif nilai >= 85:
    print("A")
```

Jika nilai:

```text
90
```

maka kondisi:

```text
90 >= 60
```

sudah benar.

Program langsung:

```text
C
```

Padahal seharusnya:

```text
A
```

---

# 35. Urutan yang Benar

Mulai dari nilai terbesar.

```python
if nilai >= 85:
    print("A")
elif nilai >= 75:
    print("B")
elif nilai >= 60:
    print("C")
else:
    print("D")
```

---

# 36. Validasi Nilai 0 Sampai 100

Kita juga dapat memeriksa input.

```python
nilai = float(input("Masukkan nilai: "))

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid")
elif nilai >= 85:
    print("A")
elif nilai >= 75:
    print("B")
elif nilai >= 65:
    print("C")
else:
    print("D")
```

---

# 37. Mengenal `and`

`and` digunakan jika **semua kondisi harus benar**.

Contoh aturan:

```text
Mahasiswa lulus jika:

Nilai >= 75
DAN
Kehadiran >= 80
```

Python:

```python
nilai = 80
kehadiran = 90

if nilai >= 75 and kehadiran >= 80:
    print("Lulus")
else:
    print("Tidak Lulus")
```

---

# 38. Tabel `and`

| Kondisi 1 | Kondisi 2 | Hasil |
| --------- | --------- | ----- |
| True      | True      | True  |
| True      | False     | False |
| False     | True      | False |
| False     | False     | False |

Jadi:

> `and` membutuhkan semua kondisi benar.

---

# 39. Contoh Login dengan `and`

```python
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "12345":
    print("Login berhasil")
else:
    print("Login gagal")
```

Untuk login berhasil:

```text
Username harus benar
DAN
Password harus benar
```

---

# 40. Mengenal `or`

`or` berarti:

```text
cukup salah satu kondisi benar
```

Contoh:

```text
Boleh masuk jika:

punya kartu mahasiswa
ATAU
punya surat izin
```

Program:

```python
punya_kartu = input("Punya kartu? ")

if punya_kartu == "ya" or punya_kartu == "iya":
    print("Boleh masuk")
else:
    print("Tidak boleh masuk")
```

---

# 41. Tabel `or`

| Kondisi 1 | Kondisi 2 | Hasil |
| --------- | --------- | ----- |
| True      | True      | True  |
| True      | False     | True  |
| False     | True      | True  |
| False     | False     | False |

---

# 42. Contoh `or`

```python
hari = input("Masukkan hari: ")

if hari == "Sabtu" or hari == "Minggu":
    print("Hari libur")
else:
    print("Hari kerja")
```

---

# 43. Mengenal `not`

`not` digunakan untuk membalik kondisi.

Contoh:

```python
aktif = True

if not aktif:
    print("Akun tidak aktif")
```

Karena:

```text
aktif = True
```

maka:

```text
not aktif
```

menjadi:

```text
False
```

---

# 44. Contoh `not`

```python
sudah_bayar = False

if not sudah_bayar:
    print("Silakan lakukan pembayaran")
```

Karena:

```text
sudah_bayar = False
```

maka:

```text
not False
```

menjadi:

```text
True
```

---

# 45. Menggabungkan Kondisi

Contoh:

```python
umur = 20
punya_ktp = True

if umur >= 17 and punya_ktp:
    print("Memenuhi syarat")
else:
    print("Belum memenuhi syarat")
```

Tidak harus menulis:

```python
punya_ktp == True
```

Cukup:

```python
punya_ktp
```

karena variabel sudah bertipe Boolean.

---

# 46. Nested If

Nested `if` berarti:

```text
if di dalam if
```

Contoh:

```python
umur = 20
punya_ktp = True

if umur >= 17:
    if punya_ktp:
        print("Boleh mendaftar")
    else:
        print("Harus memiliki KTP")
else:
    print("Umur belum cukup")
```

---

# 47. Cara Membaca Nested If

```text
Apakah umur >= 17?
        ↓
       Ya
        ↓
Apakah punya KTP?
    /         \
   Ya         Tidak
   ↓            ↓
Boleh        Harus KTP
```

Jika umur belum cukup, pengecekan KTP tidak perlu dilakukan.

---

# 48. Kapan Menggunakan Nested If?

Gunakan nested `if` jika kondisi kedua hanya perlu diperiksa setelah kondisi pertama terpenuhi.

Contoh:

```text
Login
 ↓
Username benar?
 ↓
Password benar?
```

Namun jika kondisi sederhana, kadang `and` lebih ringkas.

Contoh:

```python
if username == "admin" and password == "12345":
    print("Login berhasil")
```

---

# 49. Program Login dengan Nested If

```python
username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "12345":
        print("Login berhasil")
    else:
        print("Password salah")
else:
    print("Username salah")
```

Keuntungan nested `if`:

Program dapat memberikan pesan kesalahan lebih spesifik.

---

# 50. Sistem Diskon Sederhana

Aturan:

```text
Jika total belanja >= 100000
    Diskon 10%

Jika tidak
    Tidak ada diskon
```

Program:

```python
total_belanja = float(input("Total belanja: "))

if total_belanja >= 100000:
    diskon = total_belanja * 0.10
else:
    diskon = 0

total_bayar = total_belanja - diskon

print(f"Diskon: Rp{diskon}")
print(f"Total Bayar: Rp{total_bayar}")
```

---

# 51. Sistem Diskon Bertingkat

Aturan:

```text
>= 500000 → 20%
>= 250000 → 10%
>= 100000 → 5%
< 100000  → 0%
```

Program:

```python
belanja = float(input("Total belanja: "))

if belanja >= 500000:
    diskon_persen = 20
elif belanja >= 250000:
    diskon_persen = 10
elif belanja >= 100000:
    diskon_persen = 5
else:
    diskon_persen = 0

diskon = belanja * diskon_persen / 100
total_bayar = belanja - diskon

print(f"Diskon: {diskon_persen}%")
print(f"Potongan: Rp{diskon}")
print(f"Total bayar: Rp{total_bayar}")
```

---

# 52. Dry Run Diskon

Input:

```text
Belanja = 300000
```

Pemeriksaan:

```text
300000 >= 500000?
False
```

Kemudian:

```text
300000 >= 250000?
True
```

Maka:

```text
Diskon = 10%
```

Perhitungan:

```text
300000 × 10%
= 30000
```

Total:

```text
300000 - 30000
= 270000
```

---

# 53. Sistem Pembayaran

Input:

```text
Total Bayar
Uang Pembeli
```

Jika uang cukup:

```text
Pembayaran berhasil
```

Jika tidak:

```text
Uang tidak cukup
```

Program:

```python
total_bayar = float(input("Total bayar: "))
uang = float(input("Uang pembayaran: "))

if uang >= total_bayar:
    kembalian = uang - total_bayar

    print("Pembayaran berhasil")
    print(f"Kembalian: Rp{kembalian}")
else:
    kekurangan = total_bayar - uang

    print("Uang tidak cukup")
    print(f"Kekurangan: Rp{kekurangan}")
```

---

# 54. Menentukan Nilai Terbesar dari Dua Angka

```python
angka1 = float(input("Angka 1: "))
angka2 = float(input("Angka 2: "))

if angka1 > angka2:
    print(f"{angka1} lebih besar")
elif angka2 > angka1:
    print(f"{angka2} lebih besar")
else:
    print("Kedua angka sama")
```

---

# 55. Menentukan Nilai Terbesar dari Tiga Angka

```python
a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

if a >= b and a >= c:
    print(f"Terbesar: {a}")
elif b >= a and b >= c:
    print(f"Terbesar: {b}")
else:
    print(f"Terbesar: {c}")
```

---

# 56. Menentukan Bilangan Kelipatan

Misalnya ingin mengetahui apakah angka merupakan kelipatan 5.

```python
angka = int(input("Masukkan angka: "))

if angka % 5 == 0:
    print("Kelipatan 5")
else:
    print("Bukan kelipatan 5")
```

---

# 57. Menentukan Bilangan Habis Dibagi 3 dan 5

```python
angka = int(input("Masukkan angka: "))

if angka % 3 == 0 and angka % 5 == 0:
    print("Habis dibagi 3 dan 5")
else:
    print("Tidak habis dibagi keduanya")
```

---

# 58. Menentukan Tahun Kabisat Sederhana

Versi sederhana:

```python
tahun = int(input("Masukkan tahun: "))

if tahun % 4 == 0:
    print("Kemungkinan tahun kabisat")
else:
    print("Bukan tahun kabisat")
```

Untuk aturan tahun kabisat yang lengkap:

```python
tahun = int(input("Masukkan tahun: "))

if tahun % 400 == 0:
    print("Tahun kabisat")
elif tahun % 100 == 0:
    print("Bukan tahun kabisat")
elif tahun % 4 == 0:
    print("Tahun kabisat")
else:
    print("Bukan tahun kabisat")
```

---

# 59. Validasi Username

```python
username = input("Username: ")

if username == "":
    print("Username tidak boleh kosong")
else:
    print("Username diterima")
```

---

# 60. Validasi Nilai

```python
nilai = float(input("Masukkan nilai: "))

if nilai < 0 or nilai > 100:
    print("Nilai harus antara 0 sampai 100")
else:
    print("Nilai valid")
```

---

# 61. Validasi Umur

```python
umur = int(input("Masukkan umur: "))

if umur < 0:
    print("Umur tidak valid")
elif umur < 17:
    print("Belum cukup umur")
else:
    print("Sudah cukup umur")
```

---

# 62. Program Grade Lengkap

```python
nilai = float(input("Masukkan nilai: "))

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid")
elif nilai >= 90:
    print("Grade A")
elif nilai >= 80:
    print("Grade B")
elif nilai >= 70:
    print("Grade C")
elif nilai >= 60:
    print("Grade D")
else:
    print("Grade E")
```

---

# 63. Status Kelulusan dengan Grade

```python
nilai = float(input("Masukkan nilai: "))

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid")
elif nilai >= 85:
    grade = "A"
    status = "Lulus"
elif nilai >= 75:
    grade = "B"
    status = "Lulus"
elif nilai >= 65:
    grade = "C"
    status = "Lulus"
else:
    grade = "D"
    status = "Tidak Lulus"

if nilai >= 0 and nilai <= 100:
    print(f"Grade: {grade}")
    print(f"Status: {status}")
```

---

# 64. Program Nilai Mahasiswa

Bobot:

```text
Tugas = 30%
UTS = 30%
UAS = 40%
```

Program:

```python
nama = input("Nama mahasiswa: ")

nilai_tugas = float(input("Nilai tugas: "))
nilai_uts = float(input("Nilai UTS: "))
nilai_uas = float(input("Nilai UAS: "))

nilai_akhir = (
    nilai_tugas * 0.30
    + nilai_uts * 0.30
    + nilai_uas * 0.40
)

if nilai_akhir >= 75:
    status = "Lulus"
else:
    status = "Tidak Lulus"

print("\n=== HASIL ===")
print(f"Nama        : {nama}")
print(f"Nilai Akhir : {nilai_akhir:.2f}")
print(f"Status      : {status}")
```

---

# 65. Menambahkan Grade

```python
if nilai_akhir >= 85:
    grade = "A"
elif nilai_akhir >= 75:
    grade = "B"
elif nilai_akhir >= 65:
    grade = "C"
elif nilai_akhir >= 55:
    grade = "D"
else:
    grade = "E"
```

Kemudian:

```python
print(f"Grade: {grade}")
```

---

# 66. Sistem Kasir dengan Diskon dan Pembayaran

```python
nama_barang = input("Nama barang: ")
harga = float(input("Harga barang: "))
jumlah = int(input("Jumlah barang: "))

subtotal = harga * jumlah

if subtotal >= 500000:
    diskon_persen = 20
elif subtotal >= 250000:
    diskon_persen = 10
elif subtotal >= 100000:
    diskon_persen = 5
else:
    diskon_persen = 0

diskon = subtotal * diskon_persen / 100
total_bayar = subtotal - diskon

uang_bayar = float(input("Uang bayar: "))

print("\n=== STRUK ===")
print(f"Barang      : {nama_barang}")
print(f"Subtotal    : Rp{subtotal}")
print(f"Diskon      : {diskon_persen}%")
print(f"Total Bayar : Rp{total_bayar}")

if uang_bayar >= total_bayar:
    kembalian = uang_bayar - total_bayar

    print("Pembayaran berhasil")
    print(f"Kembalian   : Rp{kembalian}")
else:
    kekurangan = total_bayar - uang_bayar

    print("Pembayaran gagal")
    print(f"Kekurangan  : Rp{kekurangan}")
```

---

# 67. Program Menu Sederhana

Misalnya:

```text
1. Penjumlahan
2. Pengurangan
```

Program:

```python
print("=== MENU ===")
print("1. Penjumlahan")
print("2. Pengurangan")

pilihan = input("Pilih menu: ")

angka1 = float(input("Angka 1: "))
angka2 = float(input("Angka 2: "))

if pilihan == "1":
    hasil = angka1 + angka2
    print(f"Hasil: {hasil}")

elif pilihan == "2":
    hasil = angka1 - angka2
    print(f"Hasil: {hasil}")

else:
    print("Menu tidak tersedia")
```

---

# 68. Kalkulator dengan Percabangan

```python
print("=== KALKULATOR ===")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

pilihan = input("Pilih operasi: ")

angka1 = float(input("Angka pertama: "))
angka2 = float(input("Angka kedua: "))

if pilihan == "1":
    hasil = angka1 + angka2
elif pilihan == "2":
    hasil = angka1 - angka2
elif pilihan == "3":
    hasil = angka1 * angka2
elif pilihan == "4":
    if angka2 == 0:
        hasil = None
        print("Tidak dapat membagi dengan nol")
    else:
        hasil = angka1 / angka2
else:
    hasil = None
    print("Pilihan tidak tersedia")

if hasil is not None:
    print(f"Hasil: {hasil}")
```

---

# 69. Kesalahan Umum — Menggunakan `=` di Kondisi

Salah:

```python
if nilai = 75:
    print("Lulus")
```

Benar:

```python
if nilai == 75:
    print("Nilai tepat 75")
```

Untuk kelulusan biasanya:

```python
if nilai >= 75:
    print("Lulus")
```

---

# 70. Kesalahan Umum — Lupa Titik Dua

Salah:

```python
if nilai >= 75
    print("Lulus")
```

Benar:

```python
if nilai >= 75:
    print("Lulus")
```

---

# 71. Kesalahan Umum — Indentasi

Salah:

```python
if nilai >= 75:
print("Lulus")
```

Benar:

```python
if nilai >= 75:
    print("Lulus")
```

---

# 72. Kesalahan Umum — Kondisi Salah Urutan

Salah:

```python
if nilai >= 60:
    grade = "C"
elif nilai >= 75:
    grade = "B"
elif nilai >= 85:
    grade = "A"
```

Untuk nilai:

```text
90
```

hasil:

```text
C
```

karena kondisi pertama sudah benar.

Benar:

```python
if nilai >= 85:
    grade = "A"
elif nilai >= 75:
    grade = "B"
elif nilai >= 60:
    grade = "C"
```

---

# 73. Kesalahan Umum — `if` Terpisah

Perhatikan:

```python
nilai = 90

if nilai >= 60:
    print("C")

if nilai >= 75:
    print("B")

if nilai >= 85:
    print("A")
```

Output:

```text
C
B
A
```

Mengapa?

Karena setiap `if` diperiksa sendiri.

Jika hanya ingin satu grade gunakan:

```python
if
elif
else
```

---

# 74. Perbedaan Banyak `if` dan `if-elif`

Banyak `if`:

```python
if kondisi1:
    ...

if kondisi2:
    ...

if kondisi3:
    ...
```

Semua kondisi dapat dijalankan.

Sedangkan:

```python
if kondisi1:
    ...
elif kondisi2:
    ...
elif kondisi3:
    ...
```

Setelah satu kondisi benar, kondisi berikutnya tidak diperiksa.

---

# 75. Kesalahan Umum — Membandingkan String dengan Integer

Salah:

```python
umur = input("Umur: ")

if umur >= 17:
    print("Boleh")
```

Karena:

```text
umur
```

berupa String.

Benar:

```python
umur = int(input("Umur: "))

if umur >= 17:
    print("Boleh")
```

---

# 76. Kesalahan Huruf Besar dan Kecil

Program:

```python
jawaban = input("Lanjut? ")

if jawaban == "ya":
    print("Melanjutkan")
```

Jika pengguna mengetik:

```text
YA
```

maka kondisi salah.

Solusi sederhana:

```python
jawaban = input("Lanjut? ").lower()

if jawaban == "ya":
    print("Melanjutkan")
```

---

# 77. Mengenal `.lower()`

```python
teks = "HELLO"

print(teks.lower())
```

Output:

```text
hello
```

Contoh:

```python
jawaban = input("Lanjut? ").lower()

if jawaban == "ya":
    print("Lanjut")
else:
    print("Berhenti")
```

Maka input:

```text
YA
Ya
ya
```

akan menjadi:

```text
ya
```

---

# 78. `.upper()`

```python
nama = "budi"

print(nama.upper())
```

Output:

```text
BUDI
```

---

# 79. Dry Run Percabangan

Kode:

```python
nilai = 80

if nilai >= 75:
    status = "Lulus"
else:
    status = "Tidak Lulus"
```

Trace:

```text
nilai = 80

80 >= 75?
True

status = "Lulus"
```

---

# 80. Trace Table

| Langkah    | Kondisi | Hasil |
| ---------- | ------- | ----- |
| Nilai      | `80`    |       |
| `80 >= 75` | True    |       |
| Status     |         | Lulus |

---

# 81. Dry Run `elif`

Kode:

```python
nilai = 78

if nilai >= 85:
    grade = "A"
elif nilai >= 75:
    grade = "B"
elif nilai >= 65:
    grade = "C"
else:
    grade = "D"
```

Trace:

```text
78 >= 85?
False

78 >= 75?
True

grade = B
```

Program berhenti memeriksa kondisi setelah menemukan kondisi yang benar.

---
