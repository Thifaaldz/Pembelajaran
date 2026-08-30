# Mini Task — Step 7

## Array / List

Gunakan materi:

- List
- Index
- `append()`
- `remove()`
- `len()`
- `sum()`
- `max()`
- `min()`
- `for`
- `enumerate()`
- `in`

---

# Task 1 — Daftar Nama

Buat List:

```python
nama = ["Budi", "Siti", "Andi", "Rina"]
```

Tampilkan:

```text
Semua Data
Data Pertama
Data Kedua
Data Terakhir
```

---

# Task 2 — Tambah Mahasiswa

Buat:

```python
mahasiswa = ["Budi", "Siti"]
```

Tambahkan:

```text
Andi
Rina
```

menggunakan:

```python
append()
```

Target:

```text
["Budi", "Siti", "Andi", "Rina"]
```

---

# Task 3 — Ubah Data

Diberikan:

```python
mahasiswa = ["Budi", "Siti", "Andi"]
```

Ubah:

```text
Siti
```

menjadi:

```text
Sinta
```

menggunakan index.

Target:

```text
["Budi", "Sinta", "Andi"]
```

---

# Task 4 — Hapus Data

Diberikan:

```python
mahasiswa = ["Budi", "Siti", "Andi"]
```

Hapus:

```text
Siti
```

menggunakan:

```python
remove()
```

---

# Task 5 — Tampilkan Semua Mahasiswa

Gunakan List:

```python
mahasiswa = ["Budi", "Siti", "Andi", "Rina"]
```

Tampilkan menggunakan:

```python
enumerate()
```

Target output:

```text
1. Budi
2. Siti
3. Andi
4. Rina
```

---

# Task 6 — Input 5 Nilai

Buat List kosong:

```python
nilai = []
```

Minta pengguna memasukkan 5 nilai.

Setiap nilai harus dimasukkan ke List menggunakan:

```python
append()
```

Setelah selesai, tampilkan seluruh List.

---

# Task 7 — Statistik Nilai

Gunakan List:

```python
nilai = [80, 75, 90, 60, 85]
```

Hitung:

```text
Jumlah Data
Total Nilai
Rata-rata
Nilai Tertinggi
Nilai Terendah
```

Gunakan:

```python
len()
sum()
max()
min()
```

Target output:

```text
Jumlah Data     : 5
Total Nilai     : 390
Rata-rata       : 78.0
Nilai Tertinggi : 90
Nilai Terendah  : 60
```

---

# Task 8 — Status Kelulusan

Gunakan:

```python
nilai = [80, 60, 90, 70, 85]
```

Ketentuan:

```text
Nilai >= 75
→ Lulus

Nilai < 75
→ Tidak Lulus
```

Tampilkan:

```text
80 → Lulus
60 → Tidak Lulus
90 → Lulus
70 → Tidak Lulus
85 → Lulus
```

Kemudian hitung:

```text
Jumlah Lulus
Jumlah Tidak Lulus
```

---

# Task 9 — Cari Mahasiswa

Gunakan List:

```python
mahasiswa = ["Budi", "Siti", "Andi", "Rina"]
```

Minta pengguna memasukkan:

```text
Nama yang dicari
```

Contoh:

```text
Cari nama: Andi
```

Jika ada:

```text
Data ditemukan
```

Jika tidak ada:

```text
Data tidak ditemukan
```

Gunakan:

```python
in
```

---

# Task 10 — Daftar Belanja

Buat List kosong:

```python
daftar_belanja = []
```

Minta pengguna memasukkan:

```text
Jumlah barang
```

Kemudian input nama barang sebanyak jumlah tersebut.

Contoh:

```text
Jumlah barang: 3

Barang ke-1: Buku
Barang ke-2: Pensil
Barang ke-3: Penghapus
```

Target output:

```text
=== DAFTAR BELANJA ===
1. Buku
2. Pensil
3. Penghapus
```

---

# Challenge — Sistem Nilai Mahasiswa

Buat dua List:

```python
nama_mahasiswa = []
nilai_mahasiswa = []
```

Minta:

```text
Jumlah Mahasiswa
```

Kemudian input:

```text
Nama
Nilai
```

untuk setiap mahasiswa.

Contoh:

```text
Jumlah mahasiswa: 3

Mahasiswa ke-1
Nama : Budi
Nilai: 80

Mahasiswa ke-2
Nama : Andi
Nilai: 60

Mahasiswa ke-3
Nama : Siti
Nilai: 90
```

Tampilkan:

```text
============================
      DATA MAHASISWA
============================
1. Budi - 80 - Lulus
2. Andi - 60 - Tidak Lulus
3. Siti - 90 - Lulus
============================
```

Kemudian tampilkan statistik:

```text
Jumlah Mahasiswa
Jumlah Lulus
Jumlah Tidak Lulus
Rata-rata
Nilai Tertinggi
Nilai Terendah
```

Target:

```text
============================
       STATISTIK KELAS
============================
Jumlah Mahasiswa   : 3
Jumlah Lulus       : 2
Jumlah Tidak Lulus : 1
Rata-rata          : 76.67
Nilai Tertinggi    : 90
Nilai Terendah     : 60
============================
```

---

# Ketentuan

1. Gunakan List untuk menyimpan data.
2. Gunakan `append()` untuk menambahkan data.
3. Gunakan `for` untuk membaca isi List.
4. Gunakan `enumerate()` jika membutuhkan nomor urut.
5. Gunakan `if` dan `else` untuk status.
6. Gunakan `len()` untuk jumlah data.
7. Gunakan `sum()` untuk total.
8. Gunakan `max()` untuk nilai tertinggi.
9. Gunakan `min()` untuk nilai terendah.
10. Gunakan `in` untuk pencarian data.
11. Belum perlu membuat Function sendiri karena Function digunakan pada Step 8.

Simpan setiap tugas dalam file berbeda:

```text
task1_daftar.py
task2_tambah.py
task3_ubah.py
task4_hapus.py
task5_tampilkan.py
task6_input_nilai.py
task7_statistik.py
task8_kelulusan.py
task9_pencarian.py
task10_belanja.py
challenge_mahasiswa.py
```

---

# Target Step 7

Setelah menyelesaikan Mini Task, pastikan sudah memahami:

```text
BANYAK DATA
    ↓
LIST
    ↓
INDEX
    ↓
TAMBAH / UBAH / HAPUS
    ↓
LOOPING
    ↓
STATISTIK
    ↓
PENCARIAN
```