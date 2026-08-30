# Tahap 6 — Perulangan / Looping

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
```

Pada Tahap 5, kita sudah belajar membuat program mengambil keputusan menggunakan:

```python
if
elif
else
```

Sekarang kita akan belajar bagaimana membuat program melakukan suatu pekerjaan secara berulang.

Contoh:

Daripada menulis:

```python
print("Halo")
print("Halo")
print("Halo")
print("Halo")
print("Halo")
```

kita dapat menulis:

```python
for i in range(5):
    print("Halo")
```

Hasilnya tetap:

```text
Halo
Halo
Halo
Halo
Halo
```

Konsep ini disebut:

# Looping

atau:

# Perulangan

---

# 1. Tujuan Pembelajaran

Setelah menyelesaikan Tahap 6, mahasiswa diharapkan mampu:

1. Memahami apa itu perulangan.
2. Memahami mengapa perulangan diperlukan.
3. Memahami konsep iterasi.
4. Menggunakan `for`.
5. Menggunakan `range()`.
6. Memahami `range(start, stop, step)`.
7. Membuat perulangan naik.
8. Membuat perulangan turun.
9. Menggunakan variabel counter.
10. Menggunakan accumulator.
11. Menghitung total menggunakan loop.
12. Menghitung rata-rata menggunakan loop.
13. Menggunakan `while`.
14. Memahami kondisi pada `while`.
15. Menghindari infinite loop.
16. Menggunakan `break`.
17. Menggunakan `continue`.
18. Menggunakan nested loop.
19. Membuat pola sederhana.
20. Melakukan input berulang.
21. Membuat validasi input dengan `while`.
22. Menggabungkan looping dengan `if`.
23. Menggunakan looping untuk menghitung bilangan ganjil dan genap.
24. Membuat program tabel perkalian.
25. Membuat program faktorial sederhana.
26. Melakukan dry run perulangan.
27. Membuat trace table.
28. Memahami kapan menggunakan `for` dan `while`.
29. Menemukan kesalahan umum pada looping.
30. Membuat mini project menggunakan perulangan.

---

# 2. Apa Itu Perulangan?

Perulangan adalah proses menjalankan suatu perintah lebih dari satu kali.

Contoh dalam kehidupan sehari-hari:

```text
Push-up sebanyak 10 kali.
```

Artinya:

```text
Push-up
Push-up
Push-up
Push-up
...
sampai 10 kali.
```

Contoh lain:

```text
Bagikan soal kepada 30 mahasiswa.
```

Kita melakukan proses:

```text
Ambil soal
↓
Berikan kepada mahasiswa
↓
Ulangi
```

hingga seluruh mahasiswa mendapat soal.

Dalam programming konsep ini disebut:

```text
Loop
Looping
Iteration
Repetition
Perulangan
```

---

# 3. Mengapa Perulangan Dibutuhkan?

Bayangkan kita ingin menampilkan:

```text
Saya belajar Python
```

sebanyak 100 kali.

Tanpa looping:

```python
print("Saya belajar Python")
print("Saya belajar Python")
print("Saya belajar Python")
...
```

kita harus menulis hingga 100 baris.

Dengan looping:

```python
for i in range(100):
    print("Saya belajar Python")
```

Jauh lebih sederhana.

---

# 4. Apa Itu Iterasi?

Iterasi adalah satu kali proses di dalam sebuah perulangan.

Misalnya:

```python
for i in range(3):
    print("Halo")
```

Perulangan dilakukan 3 kali.

```text
Iterasi 1 → Halo
Iterasi 2 → Halo
Iterasi 3 → Halo
```

Jadi:

```text
1 Iterasi
=
1 kali proses loop
```

---

# 5. Jenis Perulangan di Python

Untuk pemula, kita fokus pada dua jenis utama:

```text
for
```

dan:

```text
while
```

Secara sederhana:

```text
FOR
digunakan jika jumlah pengulangan relatif diketahui.

WHILE
digunakan selama sebuah kondisi masih benar.
```

---

# 6. Mengenal `for`

Struktur dasar:

```python
for variabel in range(jumlah):
    perintah
```

Contoh:

```python
for i in range(5):
    print("Halo")
```

Output:

```text
Halo
Halo
Halo
Halo
Halo
```

---

# 7. Apa Itu Variabel `i`?

Perhatikan:

```python
for i in range(5):
```

Variabel:

```text
i
```

biasanya digunakan sebagai penghitung atau iterator.

Sebenarnya nama variabel tidak harus `i`.

Contoh:

```python
for angka in range(5):
    print("Halo")
```

juga valid.

Tetapi `i` sering digunakan karena berasal dari kata:

```text
index
atau
iteration
```

---

# 8. Bagaimana `range(5)` Bekerja?

Perhatikan:

```python
range(5)
```

menghasilkan angka:

```text
0
1
2
3
4
```

Bukan:

```text
1
2
3
4
5
```

Jadi:

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

---

# 9. Mengapa Mulai dari 0?

Dalam banyak bahasa pemrograman, termasuk Python, proses indeks sering dimulai dari:

```text
0
```

Karena itu:

```python
range(5)
```

berarti:

```text
mulai 0
berhenti sebelum 5
```

Hasil:

```text
0 1 2 3 4
```

---

# 10. Menampilkan Angka 1 sampai 5

Jika ingin:

```text
1
2
3
4
5
```

gunakan:

```python
for i in range(1, 6):
    print(i)
```

Perhatikan:

```text
Mulai = 1
Berhenti sebelum = 6
```

---

# 11. Mengenal `range(start, stop)`

Struktur:

```python
range(start, stop)
```

Contoh:

```python
range(1, 6)
```

menghasilkan:

```text
1
2
3
4
5
```

Karena nilai `stop` tidak ikut.

---

# 12. Contoh `range(5, 10)`

```python
for i in range(5, 10):
    print(i)
```

Output:

```text
5
6
7
8
9
```

Nilai:

```text
10
```

tidak ikut.

---

# 13. Mengenal `range(start, stop, step)`

Struktur lengkap:

```python
range(start, stop, step)
```

`step` digunakan untuk menentukan kenaikan.

Contoh:

```python
for i in range(1, 11, 2):
    print(i)
```

Output:

```text
1
3
5
7
9
```

Karena naik:

```text
+2
```

---

# 14. Menampilkan Bilangan Genap

```python
for i in range(2, 11, 2):
    print(i)
```

Output:

```text
2
4
6
8
10
```

---

# 15. Menampilkan Bilangan Ganjil

```python
for i in range(1, 11, 2):
    print(i)
```

Output:

```text
1
3
5
7
9
```

---

# 16. Perulangan Menurun

Kita dapat menggunakan step negatif.

Contoh:

```python
for i in range(5, 0, -1):
    print(i)
```

Output:

```text
5
4
3
2
1
```

---

# 17. Countdown

```python
for i in range(10, 0, -1):
    print(i)

print("Mulai!")
```

Output:

```text
10
9
8
7
6
5
4
3
2
1
Mulai!
```

---

# 18. Menampilkan Nomor Urut

```python
for i in range(1, 6):
    print(f"Mahasiswa ke-{i}")
```

Output:

```text
Mahasiswa ke-1
Mahasiswa ke-2
Mahasiswa ke-3
Mahasiswa ke-4
Mahasiswa ke-5
```

---

# 19. Menggunakan Nilai `i`

Variabel loop dapat digunakan untuk perhitungan.

```python
for i in range(1, 6):
    hasil = i * 2

    print(hasil)
```

Output:

```text
2
4
6
8
10
```

---

# 20. Tabel Perkalian Sederhana

```python
angka = 5

for i in range(1, 11):
    hasil = angka * i

    print(f"{angka} x {i} = {hasil}")
```

Output:

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

---

# 21. Tabel Perkalian dengan Input

```python
angka = int(input("Masukkan angka: "))

for i in range(1, 11):
    hasil = angka * i

    print(f"{angka} x {i} = {hasil}")
```

Jika pengguna:

```text
7
```

maka program menampilkan tabel perkalian 7.

---

# 22. Menggabungkan `for` dengan `if`

Contoh:

```python
for i in range(1, 11):

    if i % 2 == 0:
        print(f"{i} adalah genap")
```

Output:

```text
2 adalah genap
4 adalah genap
6 adalah genap
8 adalah genap
10 adalah genap
```

---

# 23. Menampilkan Ganjil dan Genap

```python
for i in range(1, 11):

    if i % 2 == 0:
        print(f"{i} = Genap")
    else:
        print(f"{i} = Ganjil")
```

---

# 24. Apa Itu Counter?

Counter adalah variabel yang digunakan untuk menghitung jumlah kejadian.

Contoh:

```python
jumlah_genap = 0
```

Setiap menemukan angka genap:

```python
jumlah_genap += 1
```

---

# 25. Contoh Counter

```python
jumlah_genap = 0

for i in range(1, 11):

    if i % 2 == 0:
        jumlah_genap += 1

print("Jumlah bilangan genap:", jumlah_genap)
```

Bilangan genap dari 1–10:

```text
2
4
6
8
10
```

Jumlah:

```text
5
```

---

# 26. Dry Run Counter

Awal:

```text
jumlah_genap = 0
```

Ketemu 2:

```text
jumlah_genap = 1
```

Ketemu 4:

```text
jumlah_genap = 2
```

Ketemu 6:

```text
jumlah_genap = 3
```

Ketemu 8:

```text
jumlah_genap = 4
```

Ketemu 10:

```text
jumlah_genap = 5
```

---

# 27. Apa Itu Accumulator?

Accumulator adalah variabel yang digunakan untuk mengumpulkan atau menjumlahkan nilai secara bertahap.

Contoh:

```python
total = 0
```

Kemudian:

```python
total = total + angka
```

atau:

```python
total += angka
```

---

# 28. Menjumlahkan Angka 1 sampai 5

```python
total = 0

for i in range(1, 6):
    total += i

print("Total:", total)
```

Proses:

```text
0 + 1 = 1
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15
```

Output:

```text
Total: 15
```

---

# 29. Trace Table Accumulator

| Iterasi |  i | total sebelum | total sesudah |
| ------- | -: | ------------: | ------------: |
| 1       |  1 |             0 |             1 |
| 2       |  2 |             1 |             3 |
| 3       |  3 |             3 |             6 |
| 4       |  4 |             6 |            10 |
| 5       |  5 |            10 |            15 |

---

# 30. Input Nilai Berulang

Misalnya kita ingin memasukkan 3 nilai.

Tanpa looping:

```python
nilai1 = float(input("Nilai 1: "))
nilai2 = float(input("Nilai 2: "))
nilai3 = float(input("Nilai 3: "))
```

Dengan looping:

```python
for i in range(1, 4):
    nilai = float(input(f"Masukkan nilai ke-{i}: "))
```

---

# 31. Menjumlahkan Input Berulang

```python
total = 0

for i in range(1, 4):

    nilai = float(input(f"Nilai ke-{i}: "))

    total += nilai

print("Total nilai:", total)
```

---

# 32. Menghitung Rata-Rata

Rumus:

```text
Rata-rata =
Total Nilai / Jumlah Data
```

Program:

```python
total = 0
jumlah_data = 3

for i in range(1, jumlah_data + 1):

    nilai = float(input(f"Nilai ke-{i}: "))

    total += nilai

rata_rata = total / jumlah_data

print(f"Rata-rata: {rata_rata:.2f}")
```

---

# 33. Contoh Dry Run Rata-Rata

Input:

```text
80
70
90
```

Proses:

```text
total = 0

total = 0 + 80
= 80

total = 80 + 70
= 150

total = 150 + 90
= 240
```

Rata-rata:

```text
240 / 3
= 80
```

---

# 34. Jumlah Data dari Pengguna

Kita dapat meminta jumlah data terlebih dahulu.

```python
jumlah_data = int(input("Berapa jumlah nilai? "))

total = 0

for i in range(1, jumlah_data + 1):

    nilai = float(input(f"Nilai ke-{i}: "))

    total += nilai

rata_rata = total / jumlah_data

print(f"Rata-rata: {rata_rata:.2f}")
```

---

# 35. Menghitung Banyak Nilai Lulus

Aturan:

```text
Nilai >= 75
→ Lulus
```

Program:

```python
jumlah_data = int(input("Jumlah mahasiswa: "))

jumlah_lulus = 0

for i in range(1, jumlah_data + 1):

    nilai = float(input(f"Nilai mahasiswa ke-{i}: "))

    if nilai >= 75:
        jumlah_lulus += 1

print("Jumlah mahasiswa lulus:", jumlah_lulus)
```

---

# 36. Menghitung Lulus dan Tidak Lulus

```python
jumlah_data = int(input("Jumlah mahasiswa: "))

lulus = 0
tidak_lulus = 0

for i in range(1, jumlah_data + 1):

    nilai = float(input(f"Nilai mahasiswa ke-{i}: "))

    if nilai >= 75:
        lulus += 1
    else:
        tidak_lulus += 1

print("Lulus:", lulus)
print("Tidak Lulus:", tidak_lulus)
```

---

# 37. Mengenal `while`

Selain `for`, Python memiliki:

```python
while
```

`while` berarti:

```text
SELAMA
```

Struktur:

```python
while kondisi:
    perintah
```

Artinya:

```text
Selama kondisi bernilai True,
jalankan perintah.
```

---

# 38. Contoh `while`

```python
angka = 1

while angka <= 5:
    print(angka)

    angka += 1
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

# 39. Cara Kerja `while`

Awal:

```text
angka = 1
```

Periksa:

```text
1 <= 5?
True
```

Tampilkan:

```text
1
```

Kemudian:

```text
angka = 2
```

Periksa lagi:

```text
2 <= 5?
True
```

Berlanjut sampai:

```text
angka = 6
```

Periksa:

```text
6 <= 5?
False
```

Loop berhenti.

---

# 40. Flow Sederhana `while`

```text
angka = 1
   ↓
angka <= 5?
 /        \
YA        TIDAK
↓            ↓
print angka   SELESAI
↓
angka += 1
↓
kembali cek kondisi
```

---

# 41. Infinite Loop

Perhatikan:

```python
angka = 1

while angka <= 5:
    print(angka)
```

Apa masalahnya?

Nilai:

```text
angka
```

selalu:

```text
1
```

Kondisi:

```text
1 <= 5
```

selalu:

```text
True
```

Akibatnya loop berjalan terus.

Ini disebut:

# Infinite Loop

---

# 42. Cara Menghindari Infinite Loop

Pastikan ada sesuatu yang membuat kondisi menjadi:

```text
False
```

Contoh:

```python
angka = 1

while angka <= 5:
    print(angka)

    angka += 1
```

Nilai berubah:

```text
1
2
3
4
5
6
```

Saat menjadi 6, loop berhenti.

---

# 43. Countdown dengan `while`

```python
angka = 5

while angka >= 1:
    print(angka)

    angka -= 1

print("Mulai!")
```

Output:

```text
5
4
3
2
1
Mulai!
```

---

# 44. Input Berulang dengan `while`

```python
jawaban = "ya"

while jawaban == "ya":

    nama = input("Masukkan nama: ")

    print(f"Halo {nama}")

    jawaban = input("Input lagi? ya/tidak: ").lower()
```

Program akan terus berjalan selama pengguna mengetik:

```text
ya
```

---

# 45. Validasi Input dengan `while`

Misalnya nilai harus:

```text
0 sampai 100
```

Program:

```python
nilai = float(input("Masukkan nilai: "))

while nilai < 0 or nilai > 100:

    print("Nilai tidak valid.")

    nilai = float(input("Masukkan nilai 0-100: "))

print("Nilai diterima:", nilai)
```

---

# 46. Cara Kerja Validasi

Jika pengguna:

```text
150
```

maka:

```text
150 > 100
```

True.

Program meminta ulang.

Jika:

```text
-10
```

juga tidak valid.

Jika:

```text
80
```

kondisi:

```text
80 < 0 or 80 > 100
```

False.

Loop berhenti.

---

# 47. Validasi Password Sederhana

```python
password = input("Masukkan password: ")

while password != "python123":

    print("Password salah.")

    password = input("Masukkan password lagi: ")

print("Login berhasil")
```

Program terus meminta sampai password benar.

---

# 48. Membatasi Percobaan Login

Kita dapat menggunakan counter.

```python
password_benar = "python123"

percobaan = 0
maksimal = 3

while percobaan < maksimal:

    password = input("Password: ")

    if password == password_benar:
        print("Login berhasil")
        break

    else:
        print("Password salah")

    percobaan += 1
```

---

# 49. Mengenal `break`

`break` digunakan untuk:

```text
menghentikan perulangan
```

meskipun kondisi loop sebenarnya masih bisa berjalan.

Contoh:

```python
for i in range(1, 11):

    if i == 5:
        break

    print(i)
```

Output:

```text
1
2
3
4
```

Saat:

```text
i == 5
```

loop dihentikan.

---

# 50. Contoh `break`

```python
while True:

    angka = int(input("Masukkan angka 0 untuk keluar: "))

    if angka == 0:
        break

    print(f"Anda memasukkan {angka}")
```

Loop:

```text
while True
```

sebenarnya berjalan terus.

Tetapi:

```python
break
```

menghentikannya.

---

# 51. Apa Itu `while True`?

```python
while True:
```

berarti:

```text
Selama True
```

Karena `True` selalu benar, loop berjalan terus.

Karena itu harus memiliki mekanisme keluar seperti:

```python
break
```

---

# 52. Program Menu dengan `while True`

```python
while True:

    print("\n=== MENU ===")
    print("1. Halo")
    print("2. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("Halo!")

    elif pilihan == "2":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak tersedia")
```

---

# 53. Mengenal `continue`

`continue` digunakan untuk:

```text
melewati iterasi saat ini
dan lanjut ke iterasi berikutnya
```

Contoh:

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

Angka:

```text
3
```

dilewati.

---

# 54. Perbedaan `break` dan `continue`

```text
break
→ menghentikan loop seluruhnya
```

```text
continue
→ hanya melewati iterasi saat ini
```

Contoh:

```python
for i in range(1, 6):

    if i == 3:
        break

    print(i)
```

Output:

```text
1
2
```

Sedangkan:

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

---

# 55. Menggunakan `continue` untuk Melewati Angka Genap

```python
for i in range(1, 11):

    if i % 2 == 0:
        continue

    print(i)
```

Output:

```text
1
3
5
7
9
```

---

# 56. Nested Loop

Nested loop berarti:

```text
loop di dalam loop
```

Contoh:

```python
for i in range(1, 4):

    for j in range(1, 4):

        print(i, j)
```

Output:

```text
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

---

# 57. Cara Membaca Nested Loop

Loop luar:

```text
i = 1
```

Loop dalam:

```text
j = 1
j = 2
j = 3
```

Setelah selesai:

```text
i = 2
```

Loop dalam kembali:

```text
j = 1
j = 2
j = 3
```

Begitu seterusnya.

---

# 58. Nested Loop dalam Kehidupan

Bayangkan:

```text
3 kelas
```

dan setiap kelas memiliki:

```text
5 mahasiswa
```

Maka:

```text
Untuk setiap kelas
    Untuk setiap mahasiswa
        lakukan proses
```

Ini merupakan nested loop.

---

# 59. Membuat Pola Bintang

```python
for i in range(5):

    print("*")
```

Output:

```text
*
*
*
*
*
```

---

# 60. Bintang Mendatar

```python
for i in range(5):

    print("*", end="")
```

Output:

```text
*****
```

---

# 61. Mengenal `end=""`

Secara default:

```python
print()
```

membuat baris baru.

Contoh:

```python
print("A")
print("B")
```

Output:

```text
A
B
```

Jika:

```python
print("A", end="")
print("B")
```

Output:

```text
AB
```

---

# 62. Pola Bintang Segitiga

```python
for i in range(1, 6):

    print("*" * i)
```

Output:

```text
*
**
***
****
*****
```

---

# 63. Pola Bintang Menurun

```python
for i in range(5, 0, -1):

    print("*" * i)
```

Output:

```text
*****
****
***
**
*
```

---

# 64. Pola Menggunakan Nested Loop

```python
for baris in range(1, 6):

    for kolom in range(baris):

        print("*", end="")

    print()
```

Output:

```text
*
**
***
****
*****
```

---

# 65. Pola Angka

```python
for i in range(1, 6):

    print(str(i) * i)
```

Output:

```text
1
22
333
4444
55555
```

---

# 66. Tabel Perkalian 1 sampai 5

```python
for angka in range(1, 6):

    print(f"\nPerkalian {angka}")

    for i in range(1, 11):

        print(f"{angka} x {i} = {angka * i}")
```

---

# 67. Faktorial

Faktorial ditulis:

```text
5!
```

Artinya:

```text
5 × 4 × 3 × 2 × 1
```

Hasil:

```text
120
```

---

# 68. Faktorial dengan `for`

```python
angka = int(input("Masukkan angka: "))

hasil = 1

for i in range(1, angka + 1):

    hasil *= i

print(f"{angka}! = {hasil}")
```

Jika:

```text
angka = 5
```

proses:

```text
1 × 1 = 1
1 × 2 = 2
2 × 3 = 6
6 × 4 = 24
24 × 5 = 120
```

---

# 69. Menghitung Jumlah Bilangan 1 sampai N

```python
n = int(input("Masukkan N: "))

total = 0

for i in range(1, n + 1):

    total += i

print("Total:", total)
```

Jika:

```text
N = 5
```

hasil:

```text
1 + 2 + 3 + 4 + 5
= 15
```

---

# 70. Menghitung Jumlah Bilangan Genap

```python
n = int(input("Masukkan batas: "))

total = 0

for i in range(1, n + 1):

    if i % 2 == 0:
        total += i

print("Total bilangan genap:", total)
```

---

# 71. Mencari Nilai Terbesar Secara Bertahap

Misalnya pengguna memasukkan 5 nilai.

```python
jumlah_data = 5

nilai_terbesar = None

for i in range(1, jumlah_data + 1):

    nilai = float(input(f"Nilai ke-{i}: "))

    if nilai_terbesar is None or nilai > nilai_terbesar:
        nilai_terbesar = nilai

print("Nilai terbesar:", nilai_terbesar)
```

Konsep mencari nilai terbesar ini akan lebih sering digunakan saat mempelajari List.

---

# 72. Mencari Nilai Terkecil

```python
jumlah_data = 5

nilai_terkecil = None

for i in range(1, jumlah_data + 1):

    nilai = float(input(f"Nilai ke-{i}: "))

    if nilai_terkecil is None or nilai < nilai_terkecil:
        nilai_terkecil = nilai

print("Nilai terkecil:", nilai_terkecil)
```

---

# 73. Program Nilai Mahasiswa Berulang

```python
jumlah_mahasiswa = int(input("Jumlah mahasiswa: "))

for i in range(1, jumlah_mahasiswa + 1):

    print(f"\nMahasiswa ke-{i}")

    nama = input("Nama: ")
    nilai = float(input("Nilai: "))

    if nilai >= 75:
        status = "Lulus"
    else:
        status = "Tidak Lulus"

    print(f"{nama} → {status}")
```

---

# 74. Menghitung Statistik Kelulusan

```python
jumlah_mahasiswa = int(input("Jumlah mahasiswa: "))

lulus = 0
tidak_lulus = 0
total_nilai = 0

for i in range(1, jumlah_mahasiswa + 1):

    nilai = float(input(f"Nilai mahasiswa ke-{i}: "))

    total_nilai += nilai

    if nilai >= 75:
        lulus += 1
    else:
        tidak_lulus += 1

rata_rata = total_nilai / jumlah_mahasiswa

print("\n=== HASIL ===")
print(f"Lulus       : {lulus}")
print(f"Tidak Lulus : {tidak_lulus}")
print(f"Rata-rata   : {rata_rata:.2f}")
```

---

# 75. Kapan Menggunakan `for`?

Gunakan `for` ketika jumlah perulangan relatif diketahui.

Contoh:

```text
Ulangi 10 kali.
```

```text
Tampilkan angka 1–100.
```

```text
Input 5 nilai.
```

```text
Proses 30 mahasiswa.
```

Contoh:

```python
for i in range(10):
    ...
```

---

# 76. Kapan Menggunakan `while`?

Gunakan `while` ketika perulangan bergantung pada kondisi.

Contoh:

```text
Ulangi sampai password benar.
```

```text
Ulangi selama pengguna memilih lanjut.
```

```text
Ulangi selama nilai tidak valid.
```

```text
Jalankan menu sampai pengguna memilih keluar.
```

---

# 77. Perbandingan `for` dan `while`

| `for`                                   | `while`                     |
| --------------------------------------- | --------------------------- |
| Jumlah perulangan biasanya diketahui    | Bergantung pada kondisi     |
| Sering menggunakan `range()`            | Menggunakan kondisi Boolean |
| Lebih aman dari infinite loop sederhana | Lebih rawan infinite loop   |
| Cocok untuk hitungan tertentu           | Cocok untuk validasi/menu   |

---

# 78. Contoh `for`

```python
for i in range(5):
    print(i)
```

Jumlah loop sudah jelas:

```text
5 kali
```

---

# 79. Contoh `while`

```python
password = ""

while password != "123":

    password = input("Password: ")
```

Kita tidak mengetahui pasti berapa kali pengguna akan salah.

---

# 80. Dry Run `for`

Kode:

```python
total = 0

for i in range(1, 4):
    total += i
```

Trace:

| Iterasi |  i | total |
| ------- | -: | ----: |
| Awal    |  - |     0 |
| 1       |  1 |     1 |
| 2       |  2 |     3 |
| 3       |  3 |     6 |

Nilai akhir:

```text
6
```

---

# 81. Dry Run `while`

Kode:

```python
x = 1

while x <= 3:

    print(x)

    x += 1
```

Trace:

| Iterasi | x awal | Kondisi | Output | x akhir |
| ------- | -----: | ------- | -----: | ------: |
| 1       |      1 | True    |      1 |       2 |
| 2       |      2 | True    |      2 |       3 |
| 3       |      3 | True    |      3 |       4 |
| 4       |      4 | False   |      - |       - |

---

# 82. Kesalahan Umum — Salah `range()`

Jika ingin menampilkan:

```text
1 sampai 5
```

Salah:

```python
for i in range(1, 5):
    print(i)
```

Hasil:

```text
1
2
3
4
```

Benar:

```python
for i in range(1, 6):
    print(i)
```

---

# 83. Kesalahan Umum — Lupa Indentasi

Salah:

```python
for i in range(5):
print(i)
```

Benar:

```python
for i in range(5):
    print(i)
```

---

# 84. Kesalahan Umum — Infinite Loop

Salah:

```python
x = 1

while x <= 5:
    print(x)
```

Benar:

```python
x = 1

while x <= 5:
    print(x)

    x += 1
```

---

# 85. Kesalahan Umum — Counter di Tempat Salah

Perhatikan:

```python
for i in range(5):

    jumlah = 0

    jumlah += 1

print(jumlah)
```

Hasil akhir:

```text
1
```

Bukan:

```text
5
```

Mengapa?

Karena:

```python
jumlah = 0
```

dijalankan ulang setiap iterasi.

---

# 86. Counter yang Benar

```python
jumlah = 0

for i in range(5):

    jumlah += 1

print(jumlah)
```

Output:

```text
5
```

Variabel accumulator/counter biasanya dibuat:

```text
SEBELUM LOOP
```

---

# 87. Kesalahan Umum — Salah Menggunakan `break`

```python
for i in range(1, 11):

    break

    print(i)
```

Program langsung keluar pada iterasi pertama.

`print(i)` tidak pernah dijalankan.

---

# 88. Kesalahan Umum — Salah Menggunakan `continue`

```python
for i in range(1, 6):

    continue

    print(i)
```

`print()` tidak pernah dijalankan karena setiap iterasi langsung dilanjutkan.

---

