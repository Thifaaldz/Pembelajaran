# Tahap 4 — Input dan Output

## Algoritma dan Pemrograman untuk Pemula

Tahap ini merupakan kelanjutan dari:

```text
Tahap 1 — Dasar Logika Pemrograman
        ↓
Tahap 2 — Pseudocode dan Flowchart
        ↓
Tahap 3 — Variabel, Tipe Data, dan Operator
        ↓
Tahap 4 — Input dan Output
```

Pada tahap sebelumnya, kita sudah dapat membuat program seperti:

```python
nama = "Budi"
umur = 20
nilai = 85
```

Masalahnya, data tersebut masih ditulis langsung oleh programmer.

Pada Tahap 4, kita akan membuat program menjadi lebih interaktif.

Pengguna dapat memasukkan sendiri:

```text
Nama
Umur
Nilai
Harga
Jumlah Barang
```

Program kemudian:

```text
MENERIMA DATA
      ↓
MEMPROSES DATA
      ↓
MENAMPILKAN HASIL
```

Konsep tersebut disebut:

# Input dan Output

---

# 1. Tujuan Pembelajaran

Setelah menyelesaikan Tahap 4, mahasiswa diharapkan mampu:

1. Memahami apa itu input.
2. Memahami apa itu output.
3. Memahami hubungan Input–Process–Output.
4. Menggunakan `print()`.
5. Menampilkan teks menggunakan `print()`.
6. Menampilkan variabel.
7. Menampilkan beberapa data sekaligus.
8. Menggunakan `input()`.
9. Menerima data dari pengguna.
10. Memahami bahwa hasil `input()` berupa String.
11. Menggunakan `int(input())`.
12. Menggunakan `float(input())`.
13. Melakukan type conversion pada input.
14. Menggabungkan input dengan variabel.
15. Menggabungkan input dengan operator.
16. Membuat kalkulator sederhana.
17. Membuat program biodata.
18. Membuat program perhitungan luas.
19. Membuat program nilai mahasiswa.
20. Membuat program kasir sederhana.
21. Mengenal format output.
22. Menggunakan f-string sederhana.
23. Mengenali error input umum.
24. Melakukan dry run program interaktif.
25. Membuat program sederhana dari IPO sampai hasil.

---

# 2. Apa Itu Input?

Input adalah data yang diberikan kepada program.

Contoh:

```text
Nama pengguna
Umur
Nilai
Harga barang
Jumlah barang
Username
Password
```

Misalnya:

```text
Masukkan nama: Budi
```

Data:

```text
Budi
```

merupakan input.

---

# 3. Apa Itu Output?

Output adalah hasil yang ditampilkan oleh program.

Contoh:

```text
Halo Budi
```

atau:

```text
Total Pembayaran = Rp30.000
```

atau:

```text
Nilai Akhir = 85
```

Output adalah hasil dari proses yang dilakukan program.

---

# 4. Hubungan Input – Process – Output

Ingat kembali konsep:

# IPO

```text
INPUT
  ↓
PROCESS
  ↓
OUTPUT
```

Contoh:

```text
INPUT
Panjang = 10
Lebar = 5

      ↓

PROCESS
Luas = Panjang × Lebar

      ↓

OUTPUT
Luas = 50
```

Dalam Python:

```python
panjang = 10
lebar = 5

luas = panjang * lebar

print(luas)
```

---

# 5. Program Statis dan Program Interaktif

Program sebelumnya:

```python
nama = "Budi"

print(nama)
```

Data:

```text
Budi
```

ditulis langsung di dalam kode.

Ini disebut secara sederhana sebagai data yang ditentukan oleh programmer.

Jika ingin mengganti nama:

```python
nama = "Siti"
```

kita harus mengubah kode.

Dengan `input()`, pengguna dapat menentukan sendiri.

```python
nama = input("Masukkan nama: ")
```

---

# 6. Mengenal print()

Fungsi:

```python
print()
```

digunakan untuk menampilkan output.

Contoh:

```python
print("Hello World")
```

Hasil:

```text
Hello World
```

---

# 7. Program Pertama

```python
print("Hello World")
```

Program tersebut memiliki satu tugas:

```text
Menampilkan tulisan:
Hello World
```

Walaupun sangat sederhana, ini biasanya menjadi program pertama ketika belajar bahasa pemrograman.

---

# 8. Menampilkan Teks

Contoh:

```python
print("Saya sedang belajar Python")
```

Output:

```text
Saya sedang belajar Python
```

---

# 9. Teks Harus Menggunakan Tanda Kutip

Benar:

```python
print("Halo")
```

Benar:

```python
print('Halo')
```

Salah:

```python
print(Halo)
```

Mengapa?

Karena tanpa tanda kutip, Python akan menganggap:

```text
Halo
```

sebagai nama variabel.

---

# 10. Menampilkan Beberapa Baris

```python
print("Nama: Budi")
print("Umur: 20")
print("Jurusan: Sistem Informasi")
```

Output:

```text
Nama: Budi
Umur: 20
Jurusan: Sistem Informasi
```

Setiap `print()` biasanya menghasilkan baris baru.

---

# 11. Menampilkan Angka

```python
print(10)
print(20)
print(3.14)
```

Output:

```text
10
20
3.14
```

Angka tidak harus menggunakan tanda kutip.

---

# 12. Menampilkan Variabel

```python
nama = "Budi"

print(nama)
```

Output:

```text
Budi
```

Perhatikan:

```python
print(nama)
```

berarti tampilkan isi variabel `nama`.

Sedangkan:

```python
print("nama")
```

akan menghasilkan:

```text
nama
```

---

# 13. Perbedaan print(nama) dan print("nama")

Contoh:

```python
nama = "Budi"

print(nama)
print("nama")
```

Output:

```text
Budi
nama
```

Karena:

```text
nama
→ variabel
```

sedangkan:

```text
"nama"
→ String
```

---

# 14. Menampilkan Teks dan Variabel

```python
nama = "Budi"

print("Nama saya:", nama)
```

Output:

```text
Nama saya: Budi
```

Python dapat menampilkan beberapa nilai dalam satu `print()`.

---

# 15. Contoh Biodata

```python
nama = "Budi"
umur = 20
jurusan = "Sistem Informasi"

print("Nama:", nama)
print("Umur:", umur)
print("Jurusan:", jurusan)
```

Output:

```text
Nama: Budi
Umur: 20
Jurusan: Sistem Informasi
```

---

# 16. Menampilkan Hasil Perhitungan

```python
angka1 = 10
angka2 = 5

hasil = angka1 + angka2

print("Hasil:", hasil)
```

Output:

```text
Hasil: 15
```

---

# 17. print() Bisa Langsung Menghitung

Kita juga dapat menulis:

```python
print(10 + 5)
```

Output:

```text
15
```

Tetapi untuk program yang lebih jelas, sebaiknya gunakan variabel.

```python
angka1 = 10
angka2 = 5

hasil = angka1 + angka2

print(hasil)
```

---

# 18. Mengenal input()

Fungsi:

```python
input()
```

digunakan untuk menerima data dari pengguna.

Contoh:

```python
input("Masukkan nama: ")
```

Ketika program dijalankan:

```text
Masukkan nama:
```

Program akan menunggu pengguna mengetik sesuatu.

---

# 19. Menyimpan Hasil input()

Biasanya hasil input disimpan ke variabel.

```python
nama = input("Masukkan nama: ")
```

Jika pengguna mengetik:

```text
Budi
```

maka:

```text
nama = "Budi"
```

---

# 20. Program Input Pertama

```python
nama = input("Masukkan nama: ")

print(nama)
```

Ketika dijalankan:

```text
Masukkan nama: Budi
Budi
```

---

# 21. Membuat Sapaan

```python
nama = input("Masukkan nama: ")

print("Halo", nama)
```

Contoh:

```text
Masukkan nama: Siti
Halo Siti
```

Program sekarang menjadi interaktif.

---

# 22. Input – Process – Output Pertama

```python
nama = input("Masukkan nama: ")

pesan = "Selamat datang"

print(pesan, nama)
```

Analisis:

```text
INPUT
nama

PROCESS
membuat pesan

OUTPUT
pesan + nama
```

---

# 23. Hal Penting tentang input()

Semua data yang masuk melalui:

```python
input()
```

secara default dianggap sebagai:

# String

Contoh:

```python
umur = input("Masukkan umur: ")
```

Jika pengguna mengetik:

```text
20
```

Python menyimpan sebagai:

```text
"20"
```

bukan:

```text
20
```

---

# 24. Membuktikan Tipe input()

```python
umur = input("Masukkan umur: ")

print(type(umur))
```

Jika pengguna memasukkan:

```text
20
```

hasil tetap:

```text
<class 'str'>
```

Artinya:

```text
String
```

---

# 25. Mengapa Ini Penting?

Perhatikan:

```python
umur = input("Masukkan umur: ")

umur_baru = umur + 1
```

Jika pengguna memasukkan:

```text
20
```

program akan error.

Mengapa?

Karena:

```text
umur = "20"
```

sehingga program mencoba:

```text
"20" + 1
```

yaitu:

```text
String + Integer
```

---

# 26. Solusi: int()

Jika input berupa bilangan bulat dan ingin dihitung, gunakan:

```python
int()
```

Contoh:

```python
umur = int(input("Masukkan umur: "))
```

Urutannya:

```text
Pengguna mengetik:
20

      ↓

input()
menghasilkan:
"20"

      ↓

int("20")

      ↓

menjadi:
20
```

---

# 27. Contoh int(input())

```python
umur = int(input("Masukkan umur: "))

umur_tahun_depan = umur + 1

print(umur_tahun_depan)
```

Jika:

```text
Masukkan umur: 20
```

Output:

```text
21
```

---

# 28. Cara Membaca int(input())

Perhatikan:

```python
umur = int(input("Masukkan umur: "))
```

Bacanya dari dalam ke luar:

```text
1. input()
   menerima data pengguna

2. int()
   mengubah data menjadi Integer

3. =
   menyimpan ke variabel umur
```

---

# 29. Bisa Ditulis Terpisah

Kode:

```python
umur = int(input("Masukkan umur: "))
```

sebenarnya dapat ditulis:

```python
umur = input("Masukkan umur: ")

umur = int(umur)
```

Keduanya menghasilkan hal yang sama.

Untuk pemula, cara kedua kadang lebih mudah dipahami.

---

# 30. Mengenal float(input())

Jika pengguna memasukkan angka desimal, gunakan:

```python
float()
```

Contoh:

```python
tinggi = float(input("Masukkan tinggi badan: "))
```

Jika pengguna:

```text
170.5
```

maka:

```text
tinggi = 170.5
```

bertipe Float.

---

# 31. Contoh Float

```python
ipk = float(input("Masukkan IPK: "))

print("IPK:", ipk)
```

Contoh:

```text
Masukkan IPK: 3.75
IPK: 3.75
```

---

# 32. Kapan Menggunakan input(), int(), dan float()?

Gunakan:

```python
input()
```

untuk data teks.

Contoh:

```text
Nama
Alamat
Jurusan
Username
```

Gunakan:

```python
int(input())
```

untuk angka bulat.

Contoh:

```text
Umur
Jumlah Barang
Jumlah Mahasiswa
Tahun
```

Gunakan:

```python
float(input())
```

untuk angka desimal.

Contoh:

```text
Berat
Tinggi
IPK
Harga desimal
```

---

# 33. Contoh Biodata Interaktif

```python
nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))
jurusan = input("Masukkan jurusan: ")

print("Nama:", nama)
print("Umur:", umur)
print("Jurusan:", jurusan)
```

Contoh:

```text
Masukkan nama: Budi
Masukkan umur: 20
Masukkan jurusan: Sistem Informasi

Nama: Budi
Umur: 20
Jurusan: Sistem Informasi
```

---

# 34. Dari Program Statis ke Interaktif

Sebelumnya:

```python
nama = "Budi"
umur = 20
```

Sekarang:

```python
nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))
```

Perbedaannya:

```text
STATIS
Data ditentukan programmer

INTERAKTIF
Data ditentukan pengguna
```

---

# 35. Program Penjumlahan Dua Angka

Pseudocode:

```text
MULAI

INPUT angka1
INPUT angka2

hasil = angka1 + angka2

OUTPUT hasil

SELESAI
```

Python:

```python
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

hasil = angka1 + angka2

print("Hasil:", hasil)
```

---

# 36. Contoh Eksekusi

```text
Masukkan angka pertama: 10
Masukkan angka kedua: 20

Hasil: 30
```

---

# 37. Program Pengurangan

```python
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

hasil = angka1 - angka2

print("Hasil pengurangan:", hasil)
```

---

# 38. Program Perkalian

```python
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

hasil = angka1 * angka2

print("Hasil perkalian:", hasil)
```

---

# 39. Program Pembagian

```python
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

hasil = angka1 / angka2

print("Hasil pembagian:", hasil)
```

---

# 40. Program Kalkulator Sederhana

```python
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

tambah = angka1 + angka2
kurang = angka1 - angka2
kali = angka1 * angka2
bagi = angka1 / angka2

print("Penjumlahan:", tambah)
print("Pengurangan:", kurang)
print("Perkalian:", kali)
print("Pembagian:", bagi)
```

---

# 41. Program Luas Persegi

Rumus:

```text
Luas = sisi × sisi
```

Program:

```python
sisi = float(input("Masukkan panjang sisi: "))

luas = sisi * sisi

print("Luas persegi:", luas)
```

---

# 42. Program Luas Persegi Panjang

Rumus:

```text
Luas = Panjang × Lebar
```

Python:

```python
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

luas = panjang * lebar

print("Luas persegi panjang:", luas)
```

---

# 43. Analisis IPO Luas Persegi Panjang

```text
INPUT
Panjang
Lebar

PROCESS
Luas = Panjang × Lebar

OUTPUT
Luas
```

Kode:

```python
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

luas = panjang * lebar

print("Luas:", luas)
```

---

# 44. Program Luas Segitiga

Rumus:

```text
Luas = 1/2 × Alas × Tinggi
```

Python:

```python
alas = float(input("Masukkan alas: "))
tinggi = float(input("Masukkan tinggi: "))

luas = 0.5 * alas * tinggi

print("Luas segitiga:", luas)
```

---

# 45. Program Luas Lingkaran

Rumus:

```text
Luas = π × r²
```

Gunakan:

```text
π = 3.14
```

Program:

```python
jari_jari = float(input("Masukkan jari-jari: "))

pi = 3.14

luas = pi * jari_jari ** 2

print("Luas lingkaran:", luas)
```

---

# 46. Program Menghitung Umur Sederhana

```python
tahun_sekarang = int(input("Masukkan tahun sekarang: "))
tahun_lahir = int(input("Masukkan tahun lahir: "))

umur = tahun_sekarang - tahun_lahir

print("Umur Anda:", umur)
```

Contoh:

```text
Tahun sekarang: 2026
Tahun lahir: 2005

Umur Anda: 21
```

---

# 47. Program Menghitung Rata-Rata

```python
nilai1 = float(input("Masukkan nilai 1: "))
nilai2 = float(input("Masukkan nilai 2: "))
nilai3 = float(input("Masukkan nilai 3: "))

rata_rata = (nilai1 + nilai2 + nilai3) / 3

print("Rata-rata:", rata_rata)
```

---

# 48. Mengapa Menggunakan Kurung?

Perhatikan:

```python
rata_rata = (nilai1 + nilai2 + nilai3) / 3
```

Bagian:

```text
nilai1 + nilai2 + nilai3
```

harus dijumlahkan terlebih dahulu.

Karena itu digunakan:

```text
()
```

---

# 49. Program Nilai Mahasiswa

Gunakan bobot:

```text
Tugas = 30%
UTS = 30%
UAS = 40%
```

Program:

```python
nama = input("Masukkan nama mahasiswa: ")

nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

nilai_akhir = (
    nilai_tugas * 0.30
    + nilai_uts * 0.30
    + nilai_uas * 0.40
)

print("Nama:", nama)
print("Nilai Akhir:", nilai_akhir)
```

---

# 50. Dry Run Nilai Mahasiswa

Input:

```text
Nama = Budi

Nilai Tugas = 80
Nilai UTS = 70
Nilai UAS = 90
```

Proses:

```text
80 × 0.30 = 24

70 × 0.30 = 21

90 × 0.40 = 36
```

Nilai akhir:

```text
24 + 21 + 36 = 81
```

Output:

```text
Nama: Budi
Nilai Akhir: 81
```

---

# 51. Program Kasir Sederhana

Input:

```text
Nama Barang
Harga Barang
Jumlah Barang
```

Process:

```text
Subtotal = Harga × Jumlah
```

Output:

```text
Subtotal
```

Program:

```python
nama_barang = input("Masukkan nama barang: ")
harga_barang = float(input("Masukkan harga barang: "))
jumlah_barang = int(input("Masukkan jumlah barang: "))

subtotal = harga_barang * jumlah_barang

print("Nama Barang:", nama_barang)
print("Subtotal:", subtotal)
```

---

# 52. Contoh Program Kasir

Input:

```text
Nama Barang: Buku
Harga Barang: 10000
Jumlah Barang: 3
```

Process:

```text
10000 × 3
= 30000
```

Output:

```text
Nama Barang: Buku
Subtotal: 30000
```

---

# 53. Program Kasir dengan Diskon Tetap

Misalnya:

```text
Diskon = 10%
```

Program:

```python
nama_barang = input("Masukkan nama barang: ")
harga_barang = float(input("Masukkan harga barang: "))
jumlah_barang = int(input("Masukkan jumlah barang: "))

subtotal = harga_barang * jumlah_barang

diskon = subtotal * 10 / 100

total_bayar = subtotal - diskon

print("Nama Barang:", nama_barang)
print("Subtotal:", subtotal)
print("Diskon:", diskon)
print("Total Bayar:", total_bayar)
```

---

# 54. Mengenal Format Output

Output seperti:

```text
Total Bayar: 30000
```

sudah benar.

Tetapi kita dapat membuatnya lebih jelas:

```text
Total Bayar: Rp30000
```

Contoh:

```python
print("Total Bayar: Rp", total_bayar)
```

---

# 55. Mengenal f-string

Python mempunyai cara yang nyaman untuk menggabungkan teks dan variabel:

# f-string

Contoh:

```python
nama = "Budi"
umur = 20

print(f"Nama saya {nama}")
print(f"Umur saya {umur} tahun")
```

Output:

```text
Nama saya Budi
Umur saya 20 tahun
```

---

# 56. Cara Membaca f-string

Perhatikan:

```python
print(f"Nama saya {nama}")
```

Huruf:

```text
f
```

sebelum tanda kutip memberitahu Python bahwa String tersebut memiliki variabel.

Variabel ditulis di:

```text
{}
```

---

# 57. Contoh f-string

```python
nama = "Siti"
jurusan = "Sistem Informasi"

print(f"Nama: {nama}")
print(f"Jurusan: {jurusan}")
```

Output:

```text
Nama: Siti
Jurusan: Sistem Informasi
```

---

# 58. f-string dengan Perhitungan

```python
angka1 = 10
angka2 = 20

print(f"Hasil = {angka1 + angka2}")
```

Output:

```text
Hasil = 30
```

---

# 59. f-string dalam Program Kasir

```python
nama_barang = input("Nama barang: ")
harga = float(input("Harga: "))
jumlah = int(input("Jumlah: "))

total = harga * jumlah

print(f"Barang: {nama_barang}")
print(f"Total: Rp{total}")
```

---

# 60. Membatasi Angka Desimal

Misalnya:

```python
nilai = 81.333333333
```

Kita dapat menampilkan dua angka di belakang koma:

```python
print(f"Nilai: {nilai:.2f}")
```

Output:

```text
Nilai: 81.33
```

Bagian:

```text
:.2f
```

artinya tampilkan dua angka desimal.

---

# 61. Contoh Rata-Rata Lebih Rapi

```python
nilai1 = float(input("Nilai 1: "))
nilai2 = float(input("Nilai 2: "))
nilai3 = float(input("Nilai 3: "))

rata_rata = (nilai1 + nilai2 + nilai3) / 3

print(f"Rata-rata: {rata_rata:.2f}")
```

---

# 62. Escape Character Sederhana

Kita dapat membuat baris baru menggunakan:

```text
\n
```

Contoh:

```python
print("Nama: Budi\nUmur: 20")
```

Output:

```text
Nama: Budi
Umur: 20
```

---

# 63. Tab

Gunakan:

```text
\t
```

Contoh:

```python
print("Nama\tNilai")
print("Budi\t80")
```

Output kira-kira:

```text
Nama    Nilai
Budi    80
```

---

# 64. Membuat Output Biodata Lebih Rapi

```python
nama = input("Nama: ")
umur = int(input("Umur: "))
jurusan = input("Jurusan: ")

print("\n=== BIODATA ===")
print(f"Nama    : {nama}")
print(f"Umur    : {umur}")
print(f"Jurusan : {jurusan}")
```

Contoh:

```text
=== BIODATA ===
Nama    : Budi
Umur    : 20
Jurusan : Sistem Informasi
```

---

# 65. Input String Tidak Perlu Casting

Contoh:

```python
nama = input("Nama: ")
alamat = input("Alamat: ")
```

Karena keduanya berupa teks.

Tidak perlu:

```python
str(input())
```

karena `input()` sendiri sudah menghasilkan String.

---

# 66. Input Integer Harus Dikonversi Jika Akan Dihitung

Misalnya:

```python
jumlah = input("Jumlah: ")
```

Jika ingin:

```python
total = jumlah * 10000
```

ini bermasalah karena `jumlah` merupakan String.

Gunakan:

```python
jumlah = int(input("Jumlah: "))
```

---

# 67. Contoh Kesalahan String Multiplication

Perhatikan:

```python
jumlah = input("Jumlah: ")

print(jumlah * 3)
```

Jika pengguna:

```text
5
```

maka output bisa menjadi:

```text
555
```

Mengapa?

Karena:

```text
"5" * 3
```

berarti mengulang String `"5"` tiga kali.

Jika ingin:

```text
15
```

gunakan:

```python
jumlah = int(input("Jumlah: "))

print(jumlah * 3)
```

---

# 68. Kesalahan Umum — Lupa int()

Salah:

```python
angka1 = input("Angka 1: ")
angka2 = input("Angka 2: ")

hasil = angka1 + angka2

print(hasil)
```

Jika pengguna memasukkan:

```text
10
20
```

output:

```text
1020
```

bukan:

```text
30
```

---

# 69. Mengapa 10 + 20 Menjadi 1020?

Karena:

```text
angka1 = "10"
angka2 = "20"
```

Kemudian:

```text
"10" + "20"
```

untuk String berarti menggabungkan.

Hasil:

```text
"1020"
```

---

# 70. Perbaikan

```python
angka1 = int(input("Angka 1: "))
angka2 = int(input("Angka 2: "))

hasil = angka1 + angka2

print(hasil)
```

Output:

```text
30
```

---

# 71. Kesalahan Input Non-Angka

Perhatikan:

```python
umur = int(input("Masukkan umur: "))
```

Jika pengguna memasukkan:

```text
dua puluh
```

Python tidak dapat mengubah:

```text
"dua puluh"
```

menjadi Integer.

Akan terjadi error.

Untuk tahap ini, pastikan pengguna memasukkan data sesuai tipe yang diminta.

Validasi input akan dipelajari lebih lanjut setelah materi kondisi.

---

# 72. Kesalahan Pembagian dengan Nol

Program:

```python
angka1 = float(input("Angka 1: "))
angka2 = float(input("Angka 2: "))

hasil = angka1 / angka2
```

Jika:

```text
angka2 = 0
```

program akan error karena pembagian dengan nol tidak diperbolehkan.

Nantinya masalah seperti ini akan ditangani menggunakan percabangan.

---

# 73. Menghubungkan Flowchart ke Input dan Output

Flowchart:

```text
MULAI
  ↓
INPUT panjang
  ↓
INPUT lebar
  ↓
luas = panjang × lebar
  ↓
OUTPUT luas
  ↓
SELESAI
```

Python:

```python
panjang = float(input("Panjang: "))
lebar = float(input("Lebar: "))

luas = panjang * lebar

print("Luas:", luas)
```

---

# 74. Menghubungkan Pseudocode ke Python

Pseudocode:

```text
MULAI

INPUT nama
INPUT umur

OUTPUT nama
OUTPUT umur

SELESAI
```

Python:

```python
nama = input("Nama: ")
umur = int(input("Umur: "))

print(nama)
print(umur)
```

---

# 75. Pola Dasar Program yang Harus Dibiasakan

Gunakan pola:

```text
INPUT
   ↓
PROCESS
   ↓
OUTPUT
```

Dalam Python:

```python
# INPUT
...

# PROCESS
...

# OUTPUT
...
```

---

# 76. Contoh Struktur yang Rapi

```python
# INPUT
harga_barang = float(input("Harga barang: "))
jumlah_barang = int(input("Jumlah barang: "))

# PROCESS
total = harga_barang * jumlah_barang

# OUTPUT
print(f"Total: Rp{total}")
```

Dengan cara ini mahasiswa dapat melihat dengan jelas bagian program.

---

# 77. Studi Kasus — Konversi Celsius ke Fahrenheit

Rumus:

```text
Fahrenheit = (Celsius × 9/5) + 32
```

Program:

```python
celsius = float(input("Masukkan suhu Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"Fahrenheit: {fahrenheit:.2f}")
```

---

# 78. Studi Kasus — Menghitung Kecepatan

Rumus:

```text
Kecepatan = Jarak / Waktu
```

Program:

```python
jarak = float(input("Masukkan jarak: "))
waktu = float(input("Masukkan waktu: "))

kecepatan = jarak / waktu

print(f"Kecepatan: {kecepatan:.2f}")
```

---

# 79. Studi Kasus — BMI Sederhana

Rumus:

```text
BMI = Berat / Tinggi²
```

Tinggi harus dalam meter.

Program:

```python
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (meter): "))

bmi = berat / (tinggi ** 2)

print(f"BMI: {bmi:.2f}")
```

Pada tahap ini kita hanya menghitung nilai BMI.

Belum menentukan kategorinya karena membutuhkan percabangan.

---

# 80. Studi Kasus — Gaji Sederhana

Input:

```text
Nama Pegawai
Gaji Pokok
Tunjangan
```

Rumus:

```text
Total Gaji = Gaji Pokok + Tunjangan
```

Program:

```python
nama = input("Nama pegawai: ")
gaji_pokok = float(input("Gaji pokok: "))
tunjangan = float(input("Tunjangan: "))

total_gaji = gaji_pokok + tunjangan

print(f"Nama: {nama}")
print(f"Total Gaji: Rp{total_gaji}")
```

---

# 81. Studi Kasus — Kembalian

Input:

```text
Total Belanja
Uang Bayar
```

Rumus:

```text
Kembalian = Uang Bayar - Total Belanja
```

Program:

```python
total_belanja = float(input("Total belanja: "))
uang_bayar = float(input("Uang bayar: "))

kembalian = uang_bayar - total_belanja

print(f"Kembalian: Rp{kembalian}")
```

Untuk sementara diasumsikan uang bayar cukup.

Nantinya akan diperiksa menggunakan `if`.

---

# 82. Studi Kasus — Total Belanja Beberapa Barang

Misalnya ada 3 barang.

```python
harga1 = float(input("Harga barang 1: "))
harga2 = float(input("Harga barang 2: "))
harga3 = float(input("Harga barang 3: "))

total = harga1 + harga2 + harga3

print(f"Total belanja: Rp{total}")
```

---

# 83. Program dengan Nama dan Harga Barang

```python
barang1 = input("Nama barang 1: ")
harga1 = float(input("Harga barang 1: "))

barang2 = input("Nama barang 2: ")
harga2 = float(input("Harga barang 2: "))

total = harga1 + harga2

print("\n=== BELANJA ===")
print(f"{barang1}: Rp{harga1}")
print(f"{barang2}: Rp{harga2}")
print(f"Total: Rp{total}")
```

---

# 84. Dry Run Program Kasir

Kode:

```python
harga = float(input("Harga: "))
jumlah = int(input("Jumlah: "))

subtotal = harga * jumlah

print(subtotal)
```

Input:

```text
Harga = 15000
Jumlah = 4
```

Trace:

```text
harga = 15000
jumlah = 4

subtotal =
15000 × 4

subtotal = 60000
```

Output:

```text
60000
```

---

# 85. Trace Table

| Variabel | Nilai |
| -------- | ----: |
| harga    | 15000 |
| jumlah   |     4 |
| subtotal | 60000 |

---
