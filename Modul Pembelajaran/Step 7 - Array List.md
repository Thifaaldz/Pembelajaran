# Tahap 7 — Array / List

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
```

Pada tahap sebelumnya, kita sudah dapat melakukan pengulangan.

Contoh:

```python
for i in range(5):
    print(i)
```

Sekarang kita akan belajar bagaimana menyimpan **banyak data sekaligus** dalam satu variabel.

Contoh:

Tanpa List:

```python
nilai1 = 80
nilai2 = 75
nilai3 = 90
nilai4 = 60
nilai5 = 85
```

Dengan List:

```python
nilai = [80, 75, 90, 60, 85]
```

Semua nilai dapat disimpan dalam satu variabel.

Konsep ini sangat penting karena hampir semua program nyata bekerja dengan kumpulan data.

---

# 1. Tujuan Pembelajaran

Setelah menyelesaikan Tahap 7, mahasiswa diharapkan mampu:

1. Memahami apa itu List.
2. Memahami mengapa List digunakan.
3. Membuat List.
4. Memahami index.
5. Mengakses elemen List.
6. Memahami index dimulai dari 0.
7. Mengakses elemen menggunakan index negatif.
8. Mengubah data dalam List.
9. Menambah data dengan `append()`.
10. Menambah data dengan `insert()`.
11. Menghapus data dengan `remove()`.
12. Menghapus data dengan `pop()`.
13. Menggunakan `del`.
14. Menggunakan `len()`.
15. Menggunakan `in`.
16. Menggunakan `not in`.
17. Melakukan looping pada List.
18. Menggunakan `range()` bersama List.
19. Menggunakan `enumerate()`.
20. Menghitung jumlah data.
21. Menggunakan `sum()`.
22. Menggunakan `min()`.
23. Menggunakan `max()`.
24. Menghitung rata-rata.
25. Mencari data sederhana.
26. Menghitung jumlah data tertentu.
27. Mengurutkan List dengan `sort()`.
28. Membalik List dengan `reverse()`.
29. Memahami slicing.
30. Menggabungkan dua List.
31. Menyalin List.
32. Menggunakan List String.
33. Menggunakan List Integer.
34. Menggunakan List campuran.
35. Membuat List dari input pengguna.
36. Membuat program daftar mahasiswa.
37. Membuat program daftar nilai.
38. Membuat program daftar barang.
39. Melakukan dry run List.
40. Membuat mini project menggunakan List.

---

# 2. Masalah Tanpa List

Bayangkan kita mempunyai lima nilai mahasiswa.

Tanpa List:

```python
nilai1 = 80
nilai2 = 75
nilai3 = 90
nilai4 = 60
nilai5 = 85
```

Jika ada:

```text
100 mahasiswa
```

maka kita mungkin harus membuat:

```text
nilai1
nilai2
nilai3
...
nilai100
```

Ini tidak efisien.

Karena itu kita membutuhkan struktur untuk menyimpan banyak data.

---

# 3. Apa Itu List?

List adalah struktur data Python yang digunakan untuk menyimpan banyak nilai dalam satu variabel.

Contoh:

```python
nilai = [80, 75, 90, 60, 85]
```

Variabel:

```text
nilai
```

menyimpan:

```text
80
75
90
60
85
```

---

# 4. Visualisasi List

```python
nilai = [80, 75, 90, 60, 85]
```

Secara konsep:

```text
nilai
┌────┬────┬────┬────┬────┐
│ 80 │ 75 │ 90 │ 60 │ 85 │
└────┴────┴────┴────┴────┘
```

Semua data berada dalam satu variabel.

---

# 5. Membuat List

Struktur:

```python
nama_list = [data1, data2, data3]
```

Contoh:

```python
buah = ["Apel", "Mangga", "Jeruk"]
```

Contoh angka:

```python
nilai = [80, 90, 70]
```

Contoh nama:

```python
mahasiswa = ["Budi", "Siti", "Andi"]
```

---

# 6. List Kosong

Kita juga bisa membuat List kosong.

```python
data = []
```

List ini belum memiliki data.

Nantinya data dapat ditambahkan.

Contoh:

```python
nilai = []

nilai.append(80)
nilai.append(90)
```

Sekarang:

```text
[80, 90]
```

---

# 7. List Dapat Menyimpan Banyak Tipe Data

Contoh:

```python
data = ["Budi", 20, 3.75, True]
```

Isi:

```text
"Budi"
→ String

20
→ Integer

3.75
→ Float

True
→ Boolean
```

Python mengizinkan List berisi tipe data berbeda.

Namun untuk program yang rapi, biasanya satu List berisi data yang sejenis.

---

# 8. Apa Itu Index?

Setiap data dalam List mempunyai posisi.

Posisi tersebut disebut:

# Index

Perhatikan:

```python
buah = ["Apel", "Mangga", "Jeruk"]
```

Index:

```text
Apel    → 0
Mangga  → 1
Jeruk   → 2
```

Visual:

```text
Index     0         1         2
        ┌───────┬────────┬───────┐
Data    │ Apel  │ Mangga │ Jeruk │
        └───────┴────────┴───────┘
```

---

# 9. Index Dimulai dari 0

Ini sangat penting.

Dalam Python:

```text
Data pertama
```

memiliki index:

```text
0
```

Bukan:

```text
1
```

Jadi:

```python
buah = ["Apel", "Mangga", "Jeruk"]
```

Maka:

```text
buah[0]
→ Apel
```

```text
buah[1]
→ Mangga
```

```text
buah[2]
→ Jeruk
```

---

# 10. Mengakses Data List

Gunakan:

```python
nama_list[index]
```

Contoh:

```python
buah = ["Apel", "Mangga", "Jeruk"]

print(buah[0])
```

Output:

```text
Apel
```

---

# 11. Mengakses Data Kedua

```python
buah = ["Apel", "Mangga", "Jeruk"]

print(buah[1])
```

Output:

```text
Mangga
```

---

# 12. Mengakses Data Terakhir

```python
buah = ["Apel", "Mangga", "Jeruk"]

print(buah[2])
```

Output:

```text
Jeruk
```

---

# 13. Index Negatif

Python juga memiliki index negatif.

Contoh:

```python
buah = ["Apel", "Mangga", "Jeruk"]
```

Index positif:

```text
0      1        2
```

Index negatif:

```text
-3     -2       -1
```

Visual:

```text
          0        1         2
        ┌──────┬────────┬───────┐
        │ Apel │ Mangga │ Jeruk │
        └──────┴────────┴───────┘
         -3       -2       -1
```

---

# 14. Mengakses Data Terakhir dengan -1

```python
buah = ["Apel", "Mangga", "Jeruk"]

print(buah[-1])
```

Output:

```text
Jeruk
```

`-1` berarti:

```text
elemen terakhir
```

---

# 15. Mengakses Elemen Kedua dari Belakang

```python
print(buah[-2])
```

Output:

```text
Mangga
```

---

# 16. Kesalahan Index

Perhatikan:

```python
buah = ["Apel", "Mangga", "Jeruk"]

print(buah[5])
```

List hanya memiliki index:

```text
0
1
2
```

Index:

```text
5
```

tidak tersedia.

Python akan menghasilkan:

```text
IndexError
```

---

# 17. Mengubah Isi List

List dapat diubah.

Contoh:

```python
buah = ["Apel", "Mangga", "Jeruk"]

buah[1] = "Pisang"
```

Sebelum:

```text
["Apel", "Mangga", "Jeruk"]
```

Sesudah:

```text
["Apel", "Pisang", "Jeruk"]
```

---

# 18. Mengubah Nilai Mahasiswa

```python
nilai = [80, 70, 90]

nilai[1] = 85

print(nilai)
```

Output:

```text
[80, 85, 90]
```

---

# 19. Menambahkan Data dengan append()

Gunakan:

```python
append()
```

untuk menambahkan data ke bagian akhir List.

Contoh:

```python
buah = ["Apel", "Mangga"]

buah.append("Jeruk")

print(buah)
```

Output:

```text
["Apel", "Mangga", "Jeruk"]
```

---

# 20. append() pada List Kosong

```python
nama = []

nama.append("Budi")
nama.append("Siti")
nama.append("Andi")

print(nama)
```

Output:

```text
["Budi", "Siti", "Andi"]
```

---

# 21. Membuat List dari Input

```python
nama_mahasiswa = []

nama = input("Masukkan nama: ")

nama_mahasiswa.append(nama)

print(nama_mahasiswa)
```

Jika:

```text
Budi
```

maka:

```text
["Budi"]
```

---

# 22. Input Banyak Data dengan Loop

```python
nama_mahasiswa = []

for i in range(3):

    nama = input(f"Nama mahasiswa ke-{i + 1}: ")

    nama_mahasiswa.append(nama)

print(nama_mahasiswa)
```

Contoh input:

```text
Budi
Siti
Andi
```

Hasil:

```text
["Budi", "Siti", "Andi"]
```

---

# 23. Menambah Data dengan insert()

`insert()` digunakan untuk menambahkan data pada posisi tertentu.

Struktur:

```python
list.insert(index, data)
```

Contoh:

```python
buah = ["Apel", "Jeruk"]

buah.insert(1, "Mangga")

print(buah)
```

Output:

```text
["Apel", "Mangga", "Jeruk"]
```

---

# 24. Perbedaan append() dan insert()

`append()`:

```python
buah.append("Jeruk")
```

menambahkan data di:

```text
akhir List
```

Sedangkan:

```python
buah.insert(1, "Mangga")
```

menambahkan data pada:

```text
index tertentu
```

---

# 25. Menghapus Data dengan remove()

`remove()` digunakan untuk menghapus berdasarkan nilai.

Contoh:

```python
buah = ["Apel", "Mangga", "Jeruk"]

buah.remove("Mangga")

print(buah)
```

Output:

```text
["Apel", "Jeruk"]
```

---

# 26. remove() Mencari Berdasarkan Data

Contoh:

```python
angka = [10, 20, 30]

angka.remove(20)
```

Hasil:

```text
[10, 30]
```

---

# 27. Hati-Hati remove()

Jika data tidak ada:

```python
buah.remove("Durian")
```

padahal:

```text
Durian
```

tidak terdapat dalam List, maka program dapat menghasilkan error.

Lebih aman:

```python
if "Durian" in buah:
    buah.remove("Durian")
```

---

# 28. Menghapus Data dengan pop()

`pop()` digunakan untuk menghapus berdasarkan index.

Contoh:

```python
buah = ["Apel", "Mangga", "Jeruk"]

buah.pop(1)

print(buah)
```

Output:

```text
["Apel", "Jeruk"]
```

---

# 29. pop() Tanpa Index

Jika:

```python
buah.pop()
```

maka elemen terakhir akan dihapus.

Contoh:

```python
buah = ["Apel", "Mangga", "Jeruk"]

buah.pop()
```

Hasil:

```text
["Apel", "Mangga"]
```

---

# 30. pop() Bisa Mengembalikan Data

```python
buah = ["Apel", "Mangga", "Jeruk"]

dihapus = buah.pop()

print(dihapus)
```

Output:

```text
Jeruk
```

Karena `pop()` bukan hanya menghapus, tetapi juga mengembalikan nilai yang dihapus.

---

# 31. Menghapus dengan del

Contoh:

```python
buah = ["Apel", "Mangga", "Jeruk"]

del buah[1]

print(buah)
```

Output:

```text
["Apel", "Jeruk"]
```

---

# 32. Menghapus Semua Data

Gunakan:

```python
clear()
```

Contoh:

```python
buah = ["Apel", "Mangga", "Jeruk"]

buah.clear()

print(buah)
```

Output:

```text
[]
```

---

# 33. Menghitung Jumlah Data dengan len()

Gunakan:

```python
len()
```

Contoh:

```python
buah = ["Apel", "Mangga", "Jeruk"]

print(len(buah))
```

Output:

```text
3
```

---

# 34. len() Sangat Penting

Contoh:

```python
nilai = [80, 75, 90, 60, 85]

jumlah_data = len(nilai)

print(jumlah_data)
```

Output:

```text
5
```

---

# 35. Mengecek Data dengan in

Gunakan:

```python
in
```

untuk mengecek apakah suatu data ada dalam List.

Contoh:

```python
buah = ["Apel", "Mangga", "Jeruk"]

if "Mangga" in buah:
    print("Mangga ditemukan")
```

Output:

```text
Mangga ditemukan
```

---

# 36. Menggunakan not in

```python
if "Durian" not in buah:
    print("Durian tidak ditemukan")
```

---

# 37. Looping pada List

Salah satu kegunaan paling penting List adalah dapat diproses dengan looping.

Contoh:

```python
buah = ["Apel", "Mangga", "Jeruk"]

for item in buah:
    print(item)
```

Output:

```text
Apel
Mangga
Jeruk
```

---

# 38. Cara Membaca Loop List

```python
for item in buah:
```

berarti:

```text
Untuk setiap item dalam buah
```

Kemudian:

```python
print(item)
```

berarti:

```text
tampilkan item tersebut
```

---

# 39. Loop Nilai

```python
nilai = [80, 75, 90, 60, 85]

for n in nilai:
    print(n)
```

Output:

```text
80
75
90
60
85
```

---

# 40. Loop dengan range() dan len()

Kita juga dapat menggunakan:

```python
range(len(list))
```

Contoh:

```python
buah = ["Apel", "Mangga", "Jeruk"]

for i in range(len(buah)):
    print(i, buah[i])
```

Output:

```text
0 Apel
1 Mangga
2 Jeruk
```

---

# 41. Kapan Menggunakan Loop Langsung?

Jika hanya butuh datanya:

```python
for buah_item in buah:
    print(buah_item)
```

Lebih sederhana.

Jika butuh index:

```python
for i in range(len(buah)):
    print(i, buah[i])
```

---

# 42. Mengenal enumerate()

Python menyediakan:

```python
enumerate()
```

untuk mendapatkan index dan data sekaligus.

Contoh:

```python
buah = ["Apel", "Mangga", "Jeruk"]

for index, item in enumerate(buah):
    print(index, item)
```

Output:

```text
0 Apel
1 Mangga
2 Jeruk
```

---

# 43. enumerate() Mulai dari 1

Untuk tampilan manusia, biasanya kita ingin nomor mulai dari 1.

```python
for nomor, item in enumerate(buah, start=1):
    print(nomor, item)
```

Output:

```text
1 Apel
2 Mangga
3 Jeruk
```

---

# 44. Menghitung Total dengan sum()

Contoh:

```python
nilai = [80, 75, 90, 60, 85]

total = sum(nilai)

print(total)
```

Perhitungan:

```text
80 + 75 + 90 + 60 + 85
= 390
```

Output:

```text
390
```

---

# 45. Menghitung Rata-Rata List

Rumus:

```text
Rata-rata =
Total / Jumlah Data
```

Program:

```python
nilai = [80, 75, 90, 60, 85]

total = sum(nilai)

jumlah = len(nilai)

rata_rata = total / jumlah

print(rata_rata)
```

Hasil:

```text
78.0
```

---

# 46. Menggunakan max()

Untuk mencari nilai terbesar:

```python
nilai = [80, 75, 90, 60, 85]

terbesar = max(nilai)

print(terbesar)
```

Output:

```text
90
```

---

# 47. Menggunakan min()

```python
terkecil = min(nilai)

print(terkecil)
```

Output:

```text
60
```

---

# 48. Statistik Sederhana

```python
nilai = [80, 75, 90, 60, 85]

print("Jumlah data :", len(nilai))
print("Total       :", sum(nilai))
print("Tertinggi   :", max(nilai))
print("Terendah    :", min(nilai))
print("Rata-rata   :", sum(nilai) / len(nilai))
```

---

# 49. Menghitung Nilai Lulus

Aturan:

```text
Nilai >= 75
→ Lulus
```

Program:

```python
nilai = [80, 75, 90, 60, 85]

jumlah_lulus = 0

for n in nilai:

    if n >= 75:
        jumlah_lulus += 1

print("Jumlah lulus:", jumlah_lulus)
```

---

# 50. Menghitung Tidak Lulus

```python
jumlah_tidak_lulus = 0

for n in nilai:

    if n < 75:
        jumlah_tidak_lulus += 1
```

---

# 51. Menampilkan Status Setiap Nilai

```python
nilai = [80, 75, 90, 60, 85]

for n in nilai:

    if n >= 75:
        print(f"{n} → Lulus")
    else:
        print(f"{n} → Tidak Lulus")
```

---

# 52. Searching Sederhana dengan in

```python
nama = ["Budi", "Siti", "Andi"]

cari = input("Cari nama: ")

if cari in nama:
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")
```

---

# 53. Searching dengan Loop

```python
nama = ["Budi", "Siti", "Andi"]

cari = input("Cari nama: ")

ditemukan = False

for item in nama:

    if item == cari:
        ditemukan = True
        break

if ditemukan:
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")
```

Konsep searching akan dipelajari lebih detail pada Tahap 10.

---

# 54. Mengetahui Posisi Data

Gunakan:

```python
index()
```

Contoh:

```python
buah = ["Apel", "Mangga", "Jeruk"]

posisi = buah.index("Mangga")

print(posisi)
```

Output:

```text
1
```

---

# 55. Menghitung Kemunculan Data

Gunakan:

```python
count()
```

Contoh:

```python
angka = [1, 2, 2, 3, 2, 4]

jumlah = angka.count(2)

print(jumlah)
```

Output:

```text
3
```

Karena angka 2 muncul tiga kali.

---

# 56. Mengurutkan Data dengan sort()

```python
nilai = [80, 60, 90, 70]

nilai.sort()

print(nilai)
```

Output:

```text
[60, 70, 80, 90]
```

---

# 57. Mengurutkan Menurun

```python
nilai.sort(reverse=True)

print(nilai)
```

Output:

```text
[90, 80, 70, 60]
```

---

# 58. sort() Mengubah List Asli

Perhatikan:

```python
nilai = [80, 60, 90, 70]

nilai.sort()
```

List `nilai` sekarang berubah menjadi:

```text
[60, 70, 80, 90]
```

---

# 59. sorted()

Jika tidak ingin mengubah List asli, gunakan:

```python
sorted()
```

Contoh:

```python
nilai = [80, 60, 90, 70]

nilai_urut = sorted(nilai)

print(nilai)
print(nilai_urut)
```

Output:

```text
[80, 60, 90, 70]

[60, 70, 80, 90]
```

---

# 60. Membalik Urutan List

Gunakan:

```python
reverse()
```

Contoh:

```python
buah = ["Apel", "Mangga", "Jeruk"]

buah.reverse()

print(buah)
```

Output:

```text
["Jeruk", "Mangga", "Apel"]
```

---

# 61. Mengenal Slicing

Slicing digunakan untuk mengambil sebagian data dalam List.

Contoh:

```python
angka = [10, 20, 30, 40, 50]
```

Jika:

```python
print(angka[1:4])
```

Output:

```text
[20, 30, 40]
```

---

# 62. Cara Membaca Slicing

```python
angka[1:4]
```

berarti:

```text
mulai index 1
sampai sebelum index 4
```

Index 4 tidak ikut.

---

# 63. Slicing dari Awal

```python
print(angka[:3])
```

Output:

```text
[10, 20, 30]
```

---

# 64. Slicing Sampai Akhir

```python
print(angka[2:])
```

Output:

```text
[30, 40, 50]
```

---

# 65. Slicing dengan Step

```python
angka = [1, 2, 3, 4, 5, 6, 7, 8]

print(angka[::2])
```

Output:

```text
[1, 3, 5, 7]
```

---

# 66. Membalik List dengan Slicing

```python
angka = [1, 2, 3, 4, 5]

print(angka[::-1])
```

Output:

```text
[5, 4, 3, 2, 1]
```

---

# 67. Menggabungkan Dua List

Gunakan:

```text
+
```

Contoh:

```python
buah1 = ["Apel", "Mangga"]
buah2 = ["Jeruk", "Pisang"]

semua_buah = buah1 + buah2

print(semua_buah)
```

Output:

```text
["Apel", "Mangga", "Jeruk", "Pisang"]
```

---

# 68. Menambahkan Banyak Data dengan extend()

```python
buah = ["Apel", "Mangga"]

buah.extend(["Jeruk", "Pisang"])

print(buah)
```

Output:

```text
["Apel", "Mangga", "Jeruk", "Pisang"]
```

---

# 69. Perbedaan append() dan extend()

Perhatikan:

```python
buah = ["Apel"]

buah.append(["Mangga", "Jeruk"])
```

Hasil:

```text
["Apel", ["Mangga", "Jeruk"]]
```

Sedangkan:

```python
buah = ["Apel"]

buah.extend(["Mangga", "Jeruk"])
```

Hasil:

```text
["Apel", "Mangga", "Jeruk"]
```

---

# 70. Menyalin List

Perhatikan:

```python
data1 = [10, 20, 30]

data2 = data1
```

Kedua variabel dapat menunjuk List yang sama.

Untuk membuat salinan:

```python
data2 = data1.copy()
```

---

# 71. Contoh copy()

```python
data1 = [10, 20, 30]

data2 = data1.copy()

data2.append(40)

print(data1)
print(data2)
```

Output:

```text
[10, 20, 30]

[10, 20, 30, 40]
```

---

# 72. List String

```python
nama = ["Budi", "Siti", "Andi"]

for item in nama:
    print(item)
```

---

# 73. List Integer

```python
angka = [10, 20, 30, 40]

for item in angka:
    print(item)
```

---

# 74. List Float

```python
ipk = [3.5, 3.75, 3.2, 3.9]
```

---

# 75. List Boolean

```python
status = [True, False, True]
```

---

# 76. Membuat Daftar Nilai dari Input

```python
nilai = []

jumlah_data = int(input("Jumlah nilai: "))

for i in range(jumlah_data):

    n = float(input(f"Nilai ke-{i + 1}: "))

    nilai.append(n)

print(nilai)
```

---

# 77. Menampilkan Daftar Nilai

```python
for nomor, n in enumerate(nilai, start=1):

    print(f"Nilai ke-{nomor}: {n}")
```

---

# 78. Statistik dari Input

```python
nilai = []

jumlah_data = int(input("Jumlah nilai: "))

for i in range(jumlah_data):

    n = float(input(f"Nilai ke-{i + 1}: "))

    nilai.append(n)

print("\n=== STATISTIK ===")
print(f"Jumlah Data : {len(nilai)}")
print(f"Total       : {sum(nilai)}")
print(f"Tertinggi   : {max(nilai)}")
print(f"Terendah    : {min(nilai)}")
print(f"Rata-rata   : {sum(nilai) / len(nilai):.2f}")
```

---

# 79. Program Daftar Belanja

```python
daftar_belanja = []

jumlah = int(input("Berapa barang? "))

for i in range(jumlah):

    barang = input(f"Barang ke-{i + 1}: ")

    daftar_belanja.append(barang)

print("\n=== DAFTAR BELANJA ===")

for nomor, barang in enumerate(daftar_belanja, start=1):

    print(f"{nomor}. {barang}")
```

---

# 80. Menambah Barang

```python
barang_baru = input("Tambah barang: ")

daftar_belanja.append(barang_baru)
```

---

# 81. Menghapus Barang

```python
hapus = input("Barang yang dihapus: ")

if hapus in daftar_belanja:

    daftar_belanja.remove(hapus)

    print("Barang berhasil dihapus")

else:

    print("Barang tidak ditemukan")
```

---

# 82. Program Menu List Sederhana

```python
data = []

while True:

    print("\n=== MENU ===")
    print("1. Lihat Data")
    print("2. Tambah Data")
    print("3. Hapus Data")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":

        print(data)

    elif pilihan == "2":

        nilai = input("Masukkan data: ")

        data.append(nilai)

    elif pilihan == "3":

        nilai = input("Data yang dihapus: ")

        if nilai in data:
            data.remove(nilai)
        else:
            print("Data tidak ditemukan")

    elif pilihan == "4":

        break

    else:

        print("Menu tidak tersedia")
```

---

# 83. Parallel List

Untuk pemula, kita dapat menggunakan dua List yang saling berkaitan.

Contoh:

```python
nama = ["Budi", "Siti", "Andi"]
nilai = [80, 90, 70]
```

Artinya:

```text
nama[0]
→ Budi

nilai[0]
→ 80
```

Sehingga:

```text
Budi → 80
```

---

# 84. Menampilkan Parallel List

```python
nama = ["Budi", "Siti", "Andi"]
nilai = [80, 90, 70]

for i in range(len(nama)):

    print(f"{nama[i]} = {nilai[i]}")
```

Output:

```text
Budi = 80
Siti = 90
Andi = 70
```

---

# 85. Hati-Hati Parallel List

Jumlah datanya harus sinkron.

Misalnya:

```python
nama = ["Budi", "Siti", "Andi"]

nilai = [80, 90]
```

Jumlahnya berbeda.

Hal ini dapat menimbulkan masalah.

Nantinya pada materi lanjutan kita dapat menggunakan struktur seperti Dictionary atau Object.

---

# 86. Mencari Nilai Mahasiswa

```python
nama = ["Budi", "Siti", "Andi"]
nilai = [80, 90, 70]

cari = input("Cari nama: ")

if cari in nama:

    posisi = nama.index(cari)

    print(f"Nilai {cari}: {nilai[posisi]}")

else:

    print("Mahasiswa tidak ditemukan")
```

---

# 87. Mengubah Nilai Mahasiswa

```python
cari = input("Nama mahasiswa: ")

if cari in nama:

    posisi = nama.index(cari)

    nilai_baru = float(input("Nilai baru: "))

    nilai[posisi] = nilai_baru

    print("Nilai berhasil diperbarui")
```

---

# 88. Menghapus Mahasiswa dan Nilai

Karena List saling terkait:

```python
posisi = nama.index(cari)

nama.pop(posisi)
nilai.pop(posisi)
```

Keduanya harus dihapus pada index yang sama.

---

# 89. Dry Run List

```python
nilai = [80, 70, 90]

nilai.append(85)

nilai[1] = 75

nilai.remove(90)
```

Langkah 1:

```text
[80, 70, 90]
```

Setelah:

```python
append(85)
```

menjadi:

```text
[80, 70, 90, 85]
```

Setelah:

```python
nilai[1] = 75
```

menjadi:

```text
[80, 75, 90, 85]
```

Setelah:

```python
remove(90)
```

menjadi:

```text
[80, 75, 85]
```

---
