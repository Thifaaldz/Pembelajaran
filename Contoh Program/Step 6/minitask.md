# Mini Task — Step 6

## Perulangan / Looping

Gunakan materi:

- `for`
- `range()`
- `while`
- `if`
- Counter
- Accumulator
- `break`
- `continue`

---

# Task 1 — Angka 1 sampai 20

Buat program menggunakan `for` untuk menampilkan:

```text
1
2
3
...
20
```

Gunakan:

```python
range()
```

---

# Task 2 — Angka 20 sampai 1

Buat program untuk menampilkan:

```text
20
19
18
...
1
```

Gunakan perulangan menurun.

---

# Task 3 — Bilangan Genap

Tampilkan bilangan genap dari:

```text
1 sampai 20
```

Target output:

```text
2
4
6
8
10
12
14
16
18
20
```

Gunakan:

```python
%
```

---

# Task 4 — Bilangan Ganjil

Tampilkan bilangan ganjil dari:

```text
1 sampai 20
```

Target:

```text
1
3
5
7
9
11
13
15
17
19
```

---

# Task 5 — Menghitung Total

Hitung jumlah angka:

```text
1 + 2 + 3 + ... + 10
```

Gunakan variabel:

```python
total = 0
```

Target output:

```text
Total: 55
```

---

# Task 6 — Tabel Perkalian

Minta pengguna memasukkan sebuah angka.

Contoh:

```text
Masukkan angka: 5
```

Tampilkan:

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

---

# Task 7 — Input Nilai Mahasiswa

Minta:

```text
Jumlah Mahasiswa
```

Kemudian input nilai sebanyak jumlah mahasiswa.

Contoh:

```text
Jumlah mahasiswa: 3

Nilai mahasiswa ke-1: 80
Nilai mahasiswa ke-2: 70
Nilai mahasiswa ke-3: 90
```

Hitung:

```text
Total Nilai
Rata-rata
```

---

# Task 8 — Lulus dan Tidak Lulus

Lanjutkan Task 7.

Ketentuan:

```text
Nilai >= 75
→ Lulus

Nilai < 75
→ Tidak Lulus
```

Hitung:

```text
Jumlah Lulus
Jumlah Tidak Lulus
```

Contoh output:

```text
=== STATISTIK ===
Jumlah Mahasiswa   : 5
Jumlah Lulus       : 3
Jumlah Tidak Lulus : 2
Rata-rata          : 78.50
```

---

# Task 9 — Validasi Nilai

Gunakan `while`.

Minta pengguna memasukkan nilai:

```text
0 sampai 100
```

Jika pengguna memasukkan:

```text
150
```

tampilkan:

```text
Nilai tidak valid
```

Kemudian minta input kembali.

Loop berhenti ketika nilai valid.

---

# Task 10 — Password

Password benar:

```text
python123
```

Gunakan `while` untuk meminta password sampai benar.

Contoh:

```text
Masukkan password: abc
Password salah

Masukkan password: 123
Password salah

Masukkan password: python123
Login berhasil
```

---

# Task 11 — break

Tampilkan angka:

```text
1 sampai 20
```

Tetapi hentikan looping ketika angka mencapai:

```text
10
```

Gunakan:

```python
break
```

---

# Task 12 — continue

Tampilkan angka:

```text
1 sampai 10
```

Tetapi jangan tampilkan angka:

```text
5
```

Gunakan:

```python
continue
```

---

# Challenge — Sistem Nilai Kelas

Buat program yang meminta:

```text
Jumlah Mahasiswa
```

Kemudian untuk setiap mahasiswa input:

```text
Nama
Nilai
```

Ketentuan:

```text
Nilai >= 75
→ Lulus

Nilai < 75
→ Tidak Lulus
```

Program harus menghitung:

```text
Jumlah Mahasiswa
Jumlah Lulus
Jumlah Tidak Lulus
Total Nilai
Rata-rata Nilai
```

Contoh:

```text
Jumlah mahasiswa: 3

=== MAHASISWA KE-1 ===
Nama: Budi
Nilai: 80
Status: Lulus

=== MAHASISWA KE-2 ===
Nama: Andi
Nilai: 60
Status: Tidak Lulus

=== MAHASISWA KE-3 ===
Nama: Siti
Nilai: 90
Status: Lulus
```

Target output:

```text
========================
     STATISTIK KELAS
========================
Jumlah Mahasiswa   : 3
Jumlah Lulus       : 2
Jumlah Tidak Lulus : 1
Total Nilai        : 230
Rata-rata          : 76.67
========================
```

---

# Ketentuan

1. Gunakan `for` atau `while`.
2. Gunakan `range()` jika menggunakan `for`.
3. Gunakan `if` dan `else` jika diperlukan.
4. Gunakan counter untuk menghitung jumlah data.
5. Gunakan accumulator untuk menghitung total.
6. Gunakan `round()` untuk rata-rata.
7. Gunakan `break` atau `continue` pada task yang memintanya.
8. Belum perlu menggunakan List karena List akan digunakan pada Step 7.

Simpan setiap tugas dalam file berbeda:

```text
task1_angka.py
task2_mundur.py
task3_genap.py
task4_ganjil.py
task5_total.py
task6_perkalian.py
task7_nilai.py
task8_kelulusan.py
task9_validasi.py
task10_password.py
task11_break.py
task12_continue.py
challenge_kelas.py
```

---

# Target Step 6

Setelah menyelesaikan Mini Task, pastikan sudah memahami:

```text
FOR
  ↓
RANGE
  ↓
LOOPING
  ↓
COUNTER / ACCUMULATOR
  ↓
WHILE
  ↓
BREAK / CONTINUE
```

dan sudah dapat menentukan:

```text
Jumlah perulangan diketahui
→ gunakan FOR

Perulangan bergantung kondisi
→ gunakan WHILE
```