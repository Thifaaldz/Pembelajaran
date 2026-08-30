# Tahap 8 — Function / Fungsi

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
        ↓
Tahap 6 — Perulangan / Looping
        ↓
Tahap 7 — Array / List
        ↓
Tahap 8 — Function / Fungsi
```

Pada tahap sebelumnya, kita sudah dapat:

```text
Menyimpan banyak data
Menggunakan List
Melakukan looping
Membuat percabangan
Mencari data
Menghitung statistik
```

Namun ketika program mulai besar, kode dapat menjadi panjang dan berulang.

Contoh:

```python
nilai = 80

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")
```

Jika proses pengecekan nilai tersebut digunakan berkali-kali, kita mungkin akan menulis kode yang sama terus-menerus.

Dengan Function, kita dapat membuat:

```python
def cek_kelulusan(nilai):
    if nilai >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"
```

Kemudian cukup menggunakan:

```python
status = cek_kelulusan(80)

print(status)
```

Konsep ini disebut:

# Function

atau:

# Fungsi

---

# 1. Tujuan Pembelajaran

Setelah menyelesaikan Tahap 8, mahasiswa diharapkan mampu:

1. Memahami apa itu Function.
2. Memahami mengapa Function digunakan.
3. Membuat Function dengan `def`.
4. Memanggil Function.
5. Memahami function call.
6. Membuat Function tanpa parameter.
7. Membuat Function dengan parameter.
8. Memahami argument.
9. Memahami perbedaan parameter dan argument.
10. Menggunakan `return`.
11. Memahami perbedaan `print()` dan `return`.
12. Membuat Function yang mengembalikan nilai.
13. Membuat Function dengan lebih dari satu parameter.
14. Menggunakan default parameter.
15. Menggunakan keyword argument.
16. Menggunakan Function dengan `if`.
17. Menggunakan Function dengan looping.
18. Menggunakan Function dengan List.
19. Membuat Function perhitungan.
20. Membuat Function validasi.
21. Membuat Function pencarian sederhana.
22. Membuat Function statistik.
23. Memahami local variable.
24. Memahami global variable.
25. Memahami scope secara sederhana.
26. Menghindari penggunaan global variable yang tidak diperlukan.
27. Memecah program panjang menjadi Function kecil.
28. Membuat menu menggunakan Function.
29. Menggunakan Function dalam mini project.
30. Melakukan dry run Function.
31. Memahami alur pemanggilan Function.
32. Menemukan kesalahan umum pada Function.

---

# 2. Masalah Tanpa Function

Bayangkan kita membuat program:

```python
nama1 = "Budi"
nilai1 = 80

if nilai1 >= 75:
    status1 = "Lulus"
else:
    status1 = "Tidak Lulus"

nama2 = "Siti"
nilai2 = 90

if nilai2 >= 75:
    status2 = "Lulus"
else:
    status2 = "Tidak Lulus"

nama3 = "Andi"
nilai3 = 60

if nilai3 >= 75:
    status3 = "Lulus"
else:
    status3 = "Tidak Lulus"
```

Perhatikan bagian:

```python
if nilai >= 75:
    ...
else:
    ...
```

ditulis berkali-kali.

Ini disebut:

```text
Code Duplication
```

atau:

```text
Pengulangan kode
```

---

# 3. Solusi Menggunakan Function

Kita dapat membuat satu Function:

```python
def cek_kelulusan(nilai):

    if nilai >= 75:
        return "Lulus"

    else:
        return "Tidak Lulus"
```

Kemudian digunakan:

```python
print(cek_kelulusan(80))
print(cek_kelulusan(90))
print(cek_kelulusan(60))
```

Output:

```text
Lulus
Lulus
Tidak Lulus
```

Kode menjadi lebih ringkas.

---

# 4. Apa Itu Function?

Function adalah sekumpulan instruksi yang dibuat untuk melakukan suatu tugas tertentu dan dapat digunakan kembali.

Sederhananya:

> Function adalah blok kode yang diberi nama agar dapat dipanggil kembali kapan pun dibutuhkan.

Contoh analogi:

```text
Function membuat kopi
```

Isinya:

```text
1. Ambil gelas
2. Masukkan kopi
3. Tambahkan air
4. Aduk
5. Sajikan
```

Daripada menjelaskan semua langkah setiap kali, kita cukup mengatakan:

```text
buat_kopi()
```

---

# 5. Mengapa Function Digunakan?

Function membantu membuat program:

```text
Lebih rapi
Lebih pendek
Lebih mudah dibaca
Lebih mudah diuji
Lebih mudah diperbaiki
Lebih mudah digunakan kembali
```

Prinsip penting:

```text
Jangan menulis kode yang sama berkali-kali
jika bisa dibuat menjadi Function.
```

---

# 6. Struktur Dasar Function

Dalam Python gunakan:

```python
def nama_function():
    perintah
```

Contoh:

```python
def salam():
    print("Halo")
```

Bagian:

```text
def
```

digunakan untuk mendefinisikan Function.

---

# 7. Mengenal `def`

`def` berasal dari:

```text
define
```

yang berarti:

```text
mendefinisikan
```

Contoh:

```python
def salam():
    print("Halo")
```

Artinya:

```text
Buat Function bernama salam
yang ketika dijalankan
akan menampilkan Halo.
```

---

# 8. Membuat Function Tidak Otomatis Menjalankannya

Perhatikan:

```python
def salam():
    print("Halo")
```

Jika program hanya seperti itu, belum ada output.

Mengapa?

Karena kita baru:

```text
MENDEFINISIKAN FUNCTION
```

Belum:

```text
MEMANGGIL FUNCTION
```

---

# 9. Memanggil Function

Untuk menjalankan Function:

```python
salam()
```

Program lengkap:

```python
def salam():
    print("Halo")


salam()
```

Output:

```text
Halo
```

---

# 10. Function Call

Proses:

```python
salam()
```

disebut:

# Function Call

atau:

```text
Pemanggilan Function
```

Alurnya:

```text
Program berjalan
      ↓
Menemukan salam()
      ↓
Masuk ke Function salam
      ↓
Menjalankan isi Function
      ↓
Kembali ke program utama
```

---

# 11. Function Bisa Dipanggil Berkali-kali

```python
def salam():
    print("Halo")


salam()
salam()
salam()
```

Output:

```text
Halo
Halo
Halo
```

Tidak perlu menulis:

```python
print("Halo")
print("Halo")
print("Halo")
```

---

# 12. Nama Function

Nama Function sebaiknya menjelaskan tugasnya.

Baik:

```python
def hitung_luas():
    ...
```

```python
def cek_kelulusan():
    ...
```

```python
def tampilkan_menu():
    ...
```

Kurang baik:

```python
def x():
    ...
```

```python
def abc():
    ...
```

---

# 13. Aturan Nama Function

Aturannya mirip variabel.

Benar:

```python
def hitung_luas():
    pass
```

```python
def cek_nilai():
    pass
```

Salah:

```python
def hitung luas():
    pass
```

Salah:

```python
def 1hitung():
    pass
```

---

# 14. Mengenal `pass`

Kadang kita ingin membuat Function tetapi belum menulis isinya.

Gunakan:

```python
def hitung_luas():
    pass
```

`pass` berarti:

```text
Untuk sementara tidak melakukan apa-apa.
```

---

# 15. Function Tanpa Parameter

Contoh:

```python
def tampilkan_menu():

    print("=== MENU ===")
    print("1. Tambah")
    print("2. Hapus")
    print("3. Keluar")
```

Pemanggilan:

```python
tampilkan_menu()
```

Output:

```text
=== MENU ===
1. Tambah
2. Hapus
3. Keluar
```

---

# 16. Function dengan Beberapa Perintah

```python
def biodata():

    print("Nama: Budi")
    print("Umur: 20")
    print("Jurusan: Sistem Informasi")
```

Panggil:

```python
biodata()
```

---

# 17. Masalah Function Tanpa Parameter

Perhatikan:

```python
def salam():
    print("Halo Budi")
```

Jika ingin menyapa:

```text
Siti
Andi
Rina
```

kita harus membuat Function berbeda atau mengubah kode.

Lebih baik menggunakan:

# Parameter

---

# 18. Apa Itu Parameter?

Parameter adalah variabel yang digunakan Function untuk menerima data.

Contoh:

```python
def salam(nama):

    print(f"Halo {nama}")
```

Bagian:

```text
nama
```

adalah parameter.

---

# 19. Memanggil Function dengan Data

```python
def salam(nama):
    print(f"Halo {nama}")


salam("Budi")
```

Output:

```text
Halo Budi
```

---

# 20. Apa Itu Argument?

Perhatikan:

```python
def salam(nama):
```

`nama` adalah:

```text
Parameter
```

Sedangkan:

```python
salam("Budi")
```

`"Budi"` adalah:

```text
Argument
```

---

# 21. Parameter vs Argument

Sederhananya:

```text
PARAMETER
→ nama variabel yang diterima Function

ARGUMENT
→ nilai yang dikirim saat Function dipanggil
```

Contoh:

```python
def salam(nama):
    print(nama)
```

Parameter:

```text
nama
```

Pemanggilan:

```python
salam("Budi")
```

Argument:

```text
"Budi"
```

---

# 22. Function Bisa Digunakan dengan Argument Berbeda

```python
def salam(nama):
    print(f"Halo {nama}")


salam("Budi")
salam("Siti")
salam("Andi")
```

Output:

```text
Halo Budi
Halo Siti
Halo Andi
```

Function yang sama dapat digunakan untuk data berbeda.

---

# 23. Function dengan Dua Parameter

```python
def perkenalan(nama, umur):

    print(f"Nama saya {nama}")
    print(f"Umur saya {umur} tahun")
```

Pemanggilan:

```python
perkenalan("Budi", 20)
```

Output:

```text
Nama saya Budi
Umur saya 20 tahun
```

---

# 24. Urutan Argument Penting

Function:

```python
def perkenalan(nama, umur):
    print(nama)
    print(umur)
```

Jika:

```python
perkenalan("Budi", 20)
```

maka:

```text
nama = "Budi"
umur = 20
```

Tetapi jika:

```python
perkenalan(20, "Budi")
```

maka:

```text
nama = 20
umur = "Budi"
```

Urutan argument harus sesuai.

---

# 25. Function Penjumlahan

```python
def tambah(angka1, angka2):

    hasil = angka1 + angka2

    print(hasil)
```

Panggil:

```python
tambah(10, 5)
```

Output:

```text
15
```

---

# 26. Function Perhitungan Luas

```python
def hitung_luas(panjang, lebar):

    luas = panjang * lebar

    print(luas)
```

Panggil:

```python
hitung_luas(10, 5)
```

Output:

```text
50
```

---

# 27. Masalah Menggunakan print() Saja

Perhatikan:

```python
def hitung_luas(panjang, lebar):

    luas = panjang * lebar

    print(luas)
```

Function hanya menampilkan hasil.

Bagaimana jika hasilnya ingin digunakan untuk perhitungan lain?

Contoh:

```text
Luas × Harga per meter
```

Untuk itu kita membutuhkan:

# return

---

# 28. Apa Itu return?

`return` digunakan untuk mengirim hasil dari Function kembali ke tempat Function dipanggil.

Contoh:

```python
def tambah(a, b):

    hasil = a + b

    return hasil
```

Kemudian:

```python
nilai = tambah(10, 5)

print(nilai)
```

Output:

```text
15
```

---

# 29. Alur return

```text
tambah(10, 5)
      ↓
Masuk ke Function
      ↓
a = 10
b = 5
      ↓
hasil = 15
      ↓
return 15
      ↓
nilai = 15
```

---

# 30. Return Langsung

Daripada:

```python
def tambah(a, b):

    hasil = a + b

    return hasil
```

bisa juga:

```python
def tambah(a, b):

    return a + b
```

---

# 31. Perbedaan print() dan return

Ini sangat penting.

`print()`:

```text
Menampilkan hasil ke layar.
```

`return`:

```text
Mengirim nilai keluar dari Function.
```

---

# 32. Contoh print()

```python
def tambah(a, b):

    print(a + b)
```

Pemanggilan:

```python
hasil = tambah(10, 5)
```

Function menampilkan:

```text
15
```

Tetapi variabel `hasil` sebenarnya:

```text
None
```

karena Function tidak melakukan `return`.

---

# 33. Contoh return

```python
def tambah(a, b):

    return a + b


hasil = tambah(10, 5)

print(hasil)
```

Sekarang:

```text
hasil = 15
```

---

# 34. Hasil Function Bisa Digunakan Kembali

```python
def tambah(a, b):

    return a + b


hasil = tambah(10, 5)

hasil_akhir = hasil * 2

print(hasil_akhir)
```

Output:

```text
30
```

---

# 35. Function Luas dengan return

```python
def hitung_luas(panjang, lebar):

    return panjang * lebar
```

Gunakan:

```python
luas = hitung_luas(10, 5)

print(f"Luas = {luas}")
```

---

# 36. Menggunakan Function di Dalam Perhitungan

```python
def hitung_luas(panjang, lebar):

    return panjang * lebar


harga_per_meter = 50000

luas = hitung_luas(10, 5)

total_harga = luas * harga_per_meter

print(total_harga)
```

---

# 37. Function Cek Kelulusan

```python
def cek_kelulusan(nilai):

    if nilai >= 75:
        return "Lulus"

    else:
        return "Tidak Lulus"
```

Pemanggilan:

```python
status = cek_kelulusan(80)

print(status)
```

Output:

```text
Lulus
```

---

# 38. Return Bisa Langsung di Dalam if

```python
def cek_kelulusan(nilai):

    if nilai >= 75:
        return "Lulus"

    return "Tidak Lulus"
```

Mengapa tidak perlu `else`?

Karena jika kondisi pertama benar, Function langsung berhenti ketika mencapai `return`.

---

# 39. return Mengakhiri Function

Perhatikan:

```python
def contoh():

    print("A")

    return

    print("B")
```

Jika dipanggil:

```python
contoh()
```

Output:

```text
A
```

Bagian:

```python
print("B")
```

tidak pernah dijalankan.

---

# 40. Function Grade

```python
def tentukan_grade(nilai):

    if nilai >= 85:
        return "A"

    elif nilai >= 75:
        return "B"

    elif nilai >= 65:
        return "C"

    elif nilai >= 55:
        return "D"

    else:
        return "E"
```

Gunakan:

```python
grade = tentukan_grade(82)

print(grade)
```

Output:

```text
B
```

---

# 41. Function dengan Validasi

```python
def tentukan_grade(nilai):

    if nilai < 0 or nilai > 100:
        return "Nilai tidak valid"

    elif nilai >= 85:
        return "A"

    elif nilai >= 75:
        return "B"

    elif nilai >= 65:
        return "C"

    else:
        return "D"
```

---

# 42. Default Parameter

Kita dapat memberikan nilai default kepada parameter.

Contoh:

```python
def salam(nama="Pengguna"):

    print(f"Halo {nama}")
```

Jika:

```python
salam()
```

Output:

```text
Halo Pengguna
```

Jika:

```python
salam("Budi")
```

Output:

```text
Halo Budi
```

---

# 43. Default Parameter untuk Diskon

```python
def hitung_diskon(total, diskon=10):

    potongan = total * diskon / 100

    return potongan
```

Panggil:

```python
print(hitung_diskon(100000))
```

Diskon default:

```text
10%
```

Atau:

```python
print(hitung_diskon(100000, 20))
```

Diskon:

```text
20%
```

---

# 44. Keyword Argument

Kita dapat memanggil Function menggunakan nama parameter.

Contoh:

```python
def perkenalan(nama, umur):

    print(nama)
    print(umur)
```

Pemanggilan:

```python
perkenalan(nama="Budi", umur=20)
```

---

# 45. Keyword Argument Bisa Mengubah Urutan

```python
perkenalan(umur=20, nama="Budi")
```

Tetap benar karena kita menyebutkan nama parameternya.

---

# 46. Function dengan Banyak Parameter

```python
def hitung_nilai_akhir(tugas, uts, uas):

    nilai_akhir = (
        tugas * 0.30
        + uts * 0.30
        + uas * 0.40
    )

    return nilai_akhir
```

Penggunaan:

```python
nilai = hitung_nilai_akhir(80, 70, 90)

print(nilai)
```

Hasil:

```text
81.0
```

---

# 47. Function Bisa Memanggil Function Lain

Contoh:

```python
def hitung_nilai_akhir(tugas, uts, uas):

    return tugas * 0.30 + uts * 0.30 + uas * 0.40


def cek_kelulusan(nilai):

    if nilai >= 75:
        return "Lulus"

    return "Tidak Lulus"
```

Penggunaan:

```python
nilai_akhir = hitung_nilai_akhir(80, 70, 90)

status = cek_kelulusan(nilai_akhir)

print(nilai_akhir)
print(status)
```

---

# 48. Alur Antar Function

```text
INPUT NILAI
    ↓
hitung_nilai_akhir()
    ↓
Nilai Akhir
    ↓
cek_kelulusan()
    ↓
Status
```

Ini membuat program lebih terstruktur.

---

# 49. Function dengan List

Contoh:

```python
def hitung_rata_rata(data):

    total = sum(data)

    jumlah = len(data)

    return total / jumlah
```

Penggunaan:

```python
nilai = [80, 75, 90, 60, 85]

rata_rata = hitung_rata_rata(nilai)

print(rata_rata)
```

Output:

```text
78.0
```

---

# 50. Function Mencari Nilai Terbesar

```python
def nilai_terbesar(data):

    return max(data)
```

Penggunaan:

```python
nilai = [80, 75, 90, 60]

print(nilai_terbesar(nilai))
```

Output:

```text
90
```

---

# 51. Function Mencari Nilai Terkecil

```python
def nilai_terkecil(data):

    return min(data)
```

---

# 52. Function Menghitung Jumlah Lulus

```python
def hitung_lulus(data):

    jumlah = 0

    for nilai in data:

        if nilai >= 75:
            jumlah += 1

    return jumlah
```

---

# 53. Menggunakan Function dengan List Nilai

```python
nilai = [80, 75, 90, 60, 85]

jumlah_lulus = hitung_lulus(nilai)

print(jumlah_lulus)
```

Output:

```text
4
```

---

# 54. Function Searching Sederhana

```python
def cari_data(data, keyword):

    if keyword in data:
        return True

    return False
```

Penggunaan:

```python
nama = ["Budi", "Siti", "Andi"]

hasil = cari_data(nama, "Siti")

print(hasil)
```

Output:

```text
True
```

---

# 55. Searching yang Mengembalikan Pesan

```python
def cari_mahasiswa(data, nama):

    if nama in data:
        return "Data ditemukan"

    return "Data tidak ditemukan"
```

---

# 56. Function Menambahkan Data

```python
def tambah_data(data, nilai):

    data.append(nilai)
```

Penggunaan:

```python
nama = []

tambah_data(nama, "Budi")
tambah_data(nama, "Siti")

print(nama)
```

Output:

```text
["Budi", "Siti"]
```

---

# 57. Function Menghapus Data

```python
def hapus_data(data, nilai):

    if nilai in data:

        data.remove(nilai)

        return True

    return False
```

---

# 58. Penggunaan Function Hapus

```python
mahasiswa = ["Budi", "Siti", "Andi"]

hasil = hapus_data(mahasiswa, "Siti")

if hasil:
    print("Data berhasil dihapus")
else:
    print("Data tidak ditemukan")
```

---

# 59. Function dengan Looping

```python
def tampilkan_data(data):

    for item in data:
        print(item)
```

Penggunaan:

```python
buah = ["Apel", "Mangga", "Jeruk"]

tampilkan_data(buah)
```

---

# 60. Function dengan enumerate()

```python
def tampilkan_data(data):

    for nomor, item in enumerate(data, start=1):

        print(f"{nomor}. {item}")
```

Output:

```text
1. Apel
2. Mangga
3. Jeruk
```

---

# 61. Function yang Mengembalikan Beberapa Nilai

Python dapat mengembalikan lebih dari satu nilai.

Contoh:

```python
def statistik(data):

    total = sum(data)
    rata_rata = total / len(data)
    terbesar = max(data)
    terkecil = min(data)

    return total, rata_rata, terbesar, terkecil
```

Penggunaan:

```python
nilai = [80, 75, 90]

total, rata, terbesar, terkecil = statistik(nilai)

print(total)
print(rata)
print(terbesar)
print(terkecil)
```

---

# 62. Memahami Multiple Return

Function:

```python
return total, rata, terbesar
```

mengembalikan beberapa nilai sekaligus.

Kemudian:

```python
a, b, c = statistik(data)
```

Python membagi nilainya ke beberapa variabel.

Konsep ini bagus dipahami, tetapi belum perlu digunakan berlebihan oleh pemula.

---

# 63. Apa Itu Scope?

Scope berarti:

```text
Wilayah di mana sebuah variabel dapat digunakan.
```

Secara sederhana kita akan mengenal:

```text
Local Variable
Global Variable
```

---

# 64. Local Variable

Variabel yang dibuat di dalam Function disebut local variable.

Contoh:

```python
def hitung():

    hasil = 10 + 5

    print(hasil)
```

Variabel:

```text
hasil
```

dibuat di dalam Function.

---

# 65. Local Variable Hanya Digunakan dalam Function

Perhatikan:

```python
def hitung():

    hasil = 15


hitung()

print(hasil)
```

Ini akan bermasalah.

Karena:

```text
hasil
```

hanya dikenal di dalam Function `hitung()`.

---

# 66. Visualisasi Local Variable

```text
PROGRAM UTAMA
│
│
└── Function hitung()
      │
      └── hasil = 15
```

Variabel:

```text
hasil
```

berada di dalam Function.

---

# 67. Global Variable

Global variable adalah variabel yang dibuat di luar Function.

Contoh:

```python
nama = "Budi"


def tampilkan_nama():

    print(nama)
```

Panggil:

```python
tampilkan_nama()
```

Output:

```text
Budi
```

Function dapat membaca variabel global.

---

# 68. Jangan Terlalu Banyak Menggunakan Global Variable

Walaupun bisa digunakan, terlalu banyak variabel global dapat membuat program:

```text
Sulit dipahami
Sulit diuji
Sulit diperbaiki
```

Untuk pemula, lebih baik gunakan:

```text
PARAMETER
+
RETURN
```

sebanyak mungkin.

---

# 69. Contoh Kurang Baik

```python
nilai = 80


def cek():

    if nilai >= 75:
        print("Lulus")
```

Function bergantung pada variabel global.

---

# 70. Contoh Lebih Baik

```python
def cek(nilai):

    if nilai >= 75:
        return "Lulus"

    return "Tidak Lulus"
```

Function dapat digunakan untuk nilai apa pun.

---

# 71. Keyword global

Python memiliki:

```python
global
```

Contoh:

```python
jumlah = 0


def tambah():

    global jumlah

    jumlah += 1
```

Namun:

> Untuk pemula, `global` sebaiknya tidak terlalu sering digunakan.

Lebih baik belajar menggunakan parameter dan `return`.

---

# 72. Function yang Terlalu Besar

Contoh kurang baik:

```python
def program():

    # input
    # perhitungan
    # login
    # menu
    # data mahasiswa
    # statistik
    # pencarian
    # penghapusan
    # output
```

Function terlalu banyak tugas.

---

# 73. Prinsip Satu Function Satu Tugas

Lebih baik:

```python
def tampilkan_menu():
    ...

def tambah_mahasiswa():
    ...

def hapus_mahasiswa():
    ...

def cari_mahasiswa():
    ...

def hitung_statistik():
    ...
```

Setiap Function memiliki tujuan yang jelas.

---

# 74. Function untuk Input Nilai

```python
def input_nilai():

    nilai = float(input("Masukkan nilai: "))

    return nilai
```

Panggil:

```python
nilai = input_nilai()
```

---

# 75. Function Validasi Nilai

```python
def input_nilai_valid():

    while True:

        nilai = float(input("Masukkan nilai 0-100: "))

        if 0 <= nilai <= 100:
            return nilai

        print("Nilai tidak valid")
```

Perhatikan:

```python
return nilai
```

sekaligus menghentikan `while True` ketika nilai valid.

---

# 76. Function Menghitung Diskon

```python
def hitung_diskon(subtotal):

    if subtotal >= 500000:
        persen = 20

    elif subtotal >= 250000:
        persen = 10

    elif subtotal >= 100000:
        persen = 5

    else:
        persen = 0

    diskon = subtotal * persen / 100

    return diskon
```

---

# 77. Function Menghitung Total Belanja

```python
def hitung_subtotal(harga, jumlah):

    return harga * jumlah
```

Gunakan:

```python
subtotal = hitung_subtotal(10000, 3)

print(subtotal)
```

---

# 78. Memecah Program Kasir

Daripada satu kode panjang, kita dapat membuat:

```python
def hitung_subtotal(harga, jumlah):
    return harga * jumlah


def hitung_diskon(subtotal):

    if subtotal >= 100000:
        return subtotal * 0.10

    return 0


def hitung_total(subtotal, diskon):
    return subtotal - diskon
```

---

# 79. Menggunakan Function Kasir

```python
harga = float(input("Harga: "))
jumlah = int(input("Jumlah: "))

subtotal = hitung_subtotal(harga, jumlah)

diskon = hitung_diskon(subtotal)

total = hitung_total(subtotal, diskon)

print(f"Subtotal: {subtotal}")
print(f"Diskon: {diskon}")
print(f"Total: {total}")
```

---

# 80. Program Lebih Mudah Dibaca

Alur utama sekarang:

```text
INPUT
  ↓
hitung_subtotal()
  ↓
hitung_diskon()
  ↓
hitung_total()
  ↓
OUTPUT
```

Function menyembunyikan detail perhitungan agar program utama lebih bersih.

---

# 81. Function untuk Menu

```python
def tampilkan_menu():

    print("\n=== MENU ===")
    print("1. Tambah")
    print("2. Lihat")
    print("3. Hapus")
    print("4. Keluar")
```

Dalam program utama:

```python
while True:

    tampilkan_menu()

    pilihan = input("Pilih: ")
```

---

# 82. Function untuk Menampilkan List

```python
def tampilkan_data(data):

    if len(data) == 0:

        print("Belum ada data")

        return

    for nomor, item in enumerate(data, start=1):

        print(f"{nomor}. {item}")
```

---

# 83. Function untuk Tambah Mahasiswa

```python
def tambah_mahasiswa(data):

    nama = input("Nama mahasiswa: ")

    data.append(nama)

    print("Data berhasil ditambahkan")
```

---

# 84. Function untuk Cari Mahasiswa

```python
def cari_mahasiswa(data):

    nama = input("Cari mahasiswa: ")

    if nama in data:
        print("Data ditemukan")

    else:
        print("Data tidak ditemukan")
```

---

# 85. Function untuk Hapus Mahasiswa

```python
def hapus_mahasiswa(data):

    nama = input("Nama yang dihapus: ")

    if nama in data:

        data.remove(nama)

        print("Data berhasil dihapus")

    else:

        print("Data tidak ditemukan")
```

---

# 86. Program Modular Sederhana

```python
def tampilkan_menu():

    print("\n=== MENU ===")
    print("1. Lihat")
    print("2. Tambah")
    print("3. Cari")
    print("4. Hapus")
    print("5. Keluar")


def tampilkan_data(data):

    if len(data) == 0:

        print("Belum ada data")

    else:

        for nomor, item in enumerate(data, start=1):

            print(f"{nomor}. {item}")


def tambah_data(data):

    nama = input("Nama: ")

    data.append(nama)


def cari_data(data):

    nama = input("Cari: ")

    if nama in data:
        print("Ditemukan")
    else:
        print("Tidak ditemukan")


def hapus_data(data):

    nama = input("Hapus: ")

    if nama in data:
        data.remove(nama)
        print("Berhasil dihapus")
    else:
        print("Tidak ditemukan")
```

---

# 87. Program Utama

```python
mahasiswa = []

while True:

    tampilkan_menu()

    pilihan = input("Pilih menu: ")

    if pilihan == "1":

        tampilkan_data(mahasiswa)

    elif pilihan == "2":

        tambah_data(mahasiswa)

    elif pilihan == "3":

        cari_data(mahasiswa)

    elif pilihan == "4":

        hapus_data(mahasiswa)

    elif pilihan == "5":

        print("Program selesai")
        break

    else:

        print("Pilihan tidak tersedia")
```

Sekarang program jauh lebih terstruktur.

---

# 88. Apa Itu Modular Programming?

Konsep memecah program menjadi bagian kecil disebut:

# Modular Programming

Contoh:

```text
PROGRAM UTAMA
│
├── tampilkan_menu()
├── tambah_data()
├── hapus_data()
├── cari_data()
└── tampilkan_data()
```

Setiap bagian mempunyai tanggung jawab sendiri.

---

# 89. Keuntungan Modular Programming

Program menjadi:

```text
Lebih mudah dibaca
Lebih mudah diuji
Lebih mudah diperbaiki
Lebih mudah dikembangkan
Lebih sedikit kode berulang
```

---

# 90. Dry Run Function

Function:

```python
def tambah(a, b):

    hasil = a + b

    return hasil
```

Pemanggilan:

```python
nilai = tambah(10, 5)
```

Dry run:

```text
Masuk Function tambah

a = 10
b = 5

hasil = 10 + 5
hasil = 15

return 15

nilai = 15
```

---

# 91. Dry Run Function dengan Kondisi

```python
def cek_lulus(nilai):

    if nilai >= 75:
        return "Lulus"

    return "Tidak Lulus"
```

Input:

```text
nilai = 80
```

Trace:

```text
80 >= 75?
True

return "Lulus"
```

Function berhenti.

---

# 92. Kesalahan Umum — Lupa Memanggil Function

Kode:

```python
def salam():
    print("Halo")
```

Tidak ada output.

Mengapa?

Karena belum:

```python
salam()
```

---

# 93. Kesalahan Umum — Lupa Tanda Kurung

Salah:

```python
salam
```

Benar:

```python
salam()
```

Untuk menjalankan Function, gunakan `()`.

---

# 94. Kesalahan Umum — Jumlah Argument Tidak Sesuai

Function:

```python
def tambah(a, b):

    return a + b
```

Salah:

```python
tambah(10)
```

Karena Function membutuhkan:

```text
2 argument
```

---

# 95. Kesalahan Umum — Terlalu Banyak Argument

Salah:

```python
tambah(10, 20, 30)
```

Function hanya memiliki:

```text
a
b
```

---

# 96. Kesalahan Umum — Mengira print() Sama dengan return

Salah konsep:

```python
def tambah(a, b):

    print(a + b)


hasil = tambah(10, 5)

print(hasil)
```

Output:

```text
15
None
```

Mengapa?

Function hanya mencetak `15`, tidak mengembalikan nilai.

---

# 97. Perbaikan return

```python
def tambah(a, b):

    return a + b


hasil = tambah(10, 5)

print(hasil)
```

Output:

```text
15
```

---

# 98. Kesalahan Umum — Kode Setelah return

```python
def contoh():

    return "Selesai"

    print("Halo")
```

`print()` tidak akan pernah dijalankan.

---

# 99. Kesalahan Umum — Local Variable

```python
def hitung():

    total = 100


print(total)
```

Akan error karena `total` hanya ada di dalam Function.

---

# 100. Kesalahan Umum — Nama Function Bertabrakan

Hindari:

```python
def print():
    ...
```

atau:

```python
def sum():
    ...
```

karena dapat menimpa nama built-in Python.

Gunakan nama spesifik:

```python
def tampilkan_data():
    ...
```

---

# 101. Built-in Function Python

Sebenarnya kita sudah menggunakan banyak Function bawaan Python.

Contoh:

```text
print()
input()
len()
sum()
max()
min()
int()
float()
str()
range()
```

Semua itu adalah Function.

Sekarang kita belajar membuat Function sendiri.

---
