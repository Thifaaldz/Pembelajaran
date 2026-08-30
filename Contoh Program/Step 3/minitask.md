# Mini Task — Step 3

## Variabel, Tipe Data, dan Operator

Gunakan materi:

- Variabel
- `str`
- `int`
- `float`
- `bool`
- Operator matematika
- `print()`
- `type()`
- `round()`

> Pada Step 3 belum menggunakan `input()`.

Semua nilai langsung ditentukan di dalam program.

---

# Task 1 — Biodata Mahasiswa

Buat variabel:

```text
nama
umur
jurusan
semester
ipk
mahasiswa_aktif
```

Contoh nilai:

```python
nama = "Budi"
umur = 20
jurusan = "Sistem Informasi"
semester = 4
ipk = 3.75
mahasiswa_aktif = True
```

Tampilkan:

```text
=== BIODATA MAHASISWA ===
Nama       : Budi
Umur       : 20
Jurusan    : Sistem Informasi
Semester   : 4
IPK        : 3.75
Aktif      : True
```

---

# Task 2 — Cek Tipe Data

Gunakan:

```python
nama = "Andi"
umur = 21
tinggi = 172.5
aktif = True
```

Tampilkan tipe data setiap variabel menggunakan:

```python
type()
```

Target:

```text
Nama   : <class 'str'>
Umur   : <class 'int'>
Tinggi : <class 'float'>
Aktif  : <class 'bool'>
```

---

# Task 3 — Operasi Matematika

Buat:

```python
angka1 = 20
angka2 = 5
```

Hitung:

```text
Penjumlahan
Pengurangan
Perkalian
Pembagian
Sisa Bagi
```

Gunakan:

```text
+
-
*
/
%
```

Target output:

```text
=== OPERASI MATEMATIKA ===
Penjumlahan : 25
Pengurangan : 15
Perkalian   : 100
Pembagian   : 4.0
Sisa Bagi   : 0
```

---

# Task 4 — Persegi Panjang

Buat variabel:

```python
panjang = 10
lebar = 5
```

Hitung:

```text
Luas
Keliling
```

Rumus:

```text
Luas = Panjang × Lebar
```

```text
Keliling = 2 × (Panjang + Lebar)
```

Target:

```text
=== PERSEGI PANJANG ===
Panjang  : 10
Lebar    : 5
Luas     : 50
Keliling : 30
```

---

# Task 5 — Nilai Mahasiswa

Buat:

```python
nama = "Budi"

nilai_tugas = 80
nilai_uts = 75
nilai_uas = 90
```

Hitung:

```text
Total Nilai
Rata-rata
```

Rumus:

```text
Total =
Tugas + UTS + UAS
```

```text
Rata-rata =
Total / 3
```

Gunakan:

```python
round(rata_rata, 2)
```

Target:

```text
=== NILAI MAHASISWA ===
Nama        : Budi
Nilai Tugas : 80
Nilai UTS   : 75
Nilai UAS   : 90
Total       : 245
Rata-rata   : 81.67
```

---

# Task 6 — Data Barang

Buat variabel:

```python
nama_barang = "Keyboard"
harga = 250000
jumlah = 2
```

Hitung:

```text
Subtotal = Harga × Jumlah
```

Target:

```text
=== DATA BARANG ===
Barang   : Keyboard
Harga    : 250000
Jumlah   : 2
Subtotal : 500000
```

---

# Task 7 — Gaji Karyawan

Buat:

```python
nama = "Andi"
gaji_pokok = 5000000
tunjangan = 1000000
potongan = 500000
```

Hitung:

```text
Gaji Bersih =
Gaji Pokok + Tunjangan - Potongan
```

Target:

```text
=== DATA GAJI ===
Nama        : Andi
Gaji Pokok  : 5000000
Tunjangan   : 1000000
Potongan    : 500000
Gaji Bersih : 5500000
```

---

# Challenge — Data Transaksi

Buat program transaksi sederhana.

Gunakan variabel:

```text
nama_barang
harga_barang
jumlah_barang
diskon
```

Contoh:

```python
nama_barang = "Laptop"
harga_barang = 8000000
jumlah_barang = 2
diskon = 500000
```

Hitung:

```text
Subtotal =
Harga Barang × Jumlah Barang
```

Kemudian:

```text
Total Bayar =
Subtotal - Diskon
```

Target:

```text
========================
       TRANSAKSI
========================
Barang      : Laptop
Harga       : 8000000
Jumlah      : 2
Subtotal    : 16000000
Diskon      : 500000
Total Bayar : 15500000
========================
```

---

# Ketentuan

1. Gunakan variabel untuk menyimpan data.
2. Gunakan tipe data yang sesuai.
3. Gunakan operator matematika untuk perhitungan.
4. Gunakan `print()` untuk menampilkan hasil.
5. Gunakan `type()` pada tugas pengecekan tipe data.
6. Gunakan `round()` jika terdapat angka desimal panjang.
7. Jangan menggunakan `input()`.
8. Jangan menggunakan `if`, `for`, atau Function karena belum dipelajari pada Step 3.

Simpan setiap tugas dalam file berbeda:

```text
task1_biodata.py
task2_tipedata.py
task3_operator.py
task4_persegi_panjang.py
task5_nilai.py
task6_barang.py
task7_gaji.py
challenge_transaksi.py
```

---

# Target Step 3

Setelah menyelesaikan Mini Task, pastikan sudah memahami:

```text
DATA
 ↓
VARIABEL
 ↓
TIPE DATA
 ↓
OPERATOR
 ↓
PERHITUNGAN
 ↓
OUTPUT
```

dan dapat membedakan:

```text
"Budi"
→ str

20
→ int

170.5
→ float

True
→ bool
```