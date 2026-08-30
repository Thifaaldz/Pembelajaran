# Mini Task — Step 5

## Percabangan / Conditional

Gunakan materi:

- `if`
- `elif`
- `else`
- Operator perbandingan
- `and`
- `%`
- `input()`
- `print()`

---

# Task 1 — Cek Umur

Buat program yang meminta:

```text
Nama
Umur
```

Ketentuan:

```text
Umur >= 17
→ Sudah Dewasa

Umur < 17
→ Belum Dewasa
```

Contoh:

```text
Nama: Budi
Umur: 20
```

Output:

```text
Nama   : Budi
Status : Sudah Dewasa
```

---

# Task 2 — Positif, Negatif, atau Nol

Input:

```text
Sebuah angka
```

Ketentuan:

```text
> 0
→ Positif

< 0
→ Negatif

= 0
→ Nol
```

Contoh:

```text
Masukkan angka: -5
```

Output:

```text
-5 adalah bilangan Negatif
```

---

# Task 3 — Cek Kelulusan

Input:

```text
Nama Mahasiswa
Nilai
```

Ketentuan:

```text
Nilai >= 75
→ Lulus

Nilai < 75
→ Tidak Lulus
```

Target output:

```text
=== HASIL ===
Nama   : Budi
Nilai  : 80
Status : Lulus
```

---

# Task 4 — Grade Mahasiswa

Input nilai mahasiswa.

Ketentuan:

```text
>= 85 → A
>= 75 → B
>= 65 → C
>= 55 → D
< 55  → E
```

Contoh:

```text
Masukkan nilai: 78
```

Output:

```text
Grade: B
```

---

# Task 5 — Ganjil atau Genap

Input:

```text
Sebuah angka
```

Gunakan:

```python
%
```

Ketentuan:

```text
angka % 2 == 0
→ Genap

Selain itu
→ Ganjil
```

---

# Task 6 — Diskon Belanja

Input:

```text
Total Belanja
```

Ketentuan:

```text
>= 500000 → Diskon 20%
>= 250000 → Diskon 10%
>= 100000 → Diskon 5%
< 100000  → Tidak Ada Diskon
```

Hitung:

```text
Potongan
Total Bayar
```

Contoh:

```text
Total Belanja: 500000
```

Output:

```text
Diskon      : 20%
Potongan    : 100000
Total Bayar : 400000
```

---

# Task 7 — Login Sederhana

Data login yang benar:

```text
Username = admin
Password = python123
```

Input:

```text
Username
Password
```

Jika keduanya benar:

```text
Login berhasil
```

Jika salah:

```text
Username atau password salah
```

Gunakan:

```python
and
```

---

# Challenge — Sistem Nilai Mahasiswa

Buat program yang meminta:

```text
Nama Mahasiswa
Nilai Tugas
Nilai UTS
Nilai UAS
```

Hitung nilai akhir:

```text
Nilai Akhir =
(Tugas × 30%)
+
(UTS × 30%)
+
(UAS × 40%)
```

Tentukan grade:

```text
>= 85 → A
>= 75 → B
>= 65 → C
>= 55 → D
< 55  → E
```

Tentukan status:

```text
Nilai Akhir >= 65
→ Lulus

Nilai Akhir < 65
→ Tidak Lulus
```

Contoh output:

```text
=========================
      HASIL NILAI
=========================
Nama        : Budi
Nilai Akhir : 81.0
Grade       : B
Status      : Lulus
=========================
```

---

# Ketentuan

1. Gunakan `input()` untuk menerima data.
2. Gunakan `int()` atau `float()` untuk angka.
3. Gunakan `if`, `elif`, dan `else`.
4. Gunakan operator perbandingan.
5. Gunakan variabel untuk menyimpan hasil.
6. Gunakan `print()` untuk output.
7. Jangan menggunakan looping karena looping baru digunakan pada Step 6.

Simpan setiap tugas dalam file berbeda:

```text
task1_umur.py
task2_angka.py
task3_kelulusan.py
task4_grade.py
task5_genap_ganjil.py
task6_diskon.py
task7_login.py
challenge_nilai.py
```

---

# Target Step 5

Setelah menyelesaikan Mini Task ini, pastikan sudah memahami:

```text
INPUT
  ↓
CONDITION
  ↓
IF / ELIF / ELSE
  ↓
KEPUTUSAN
  ↓
OUTPUT
```