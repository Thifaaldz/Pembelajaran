# Mini Task — Step 4

## Input dan Output

Kerjakan menggunakan materi yang sudah dipelajari pada `inputoutput.py`.

Gunakan:

- `input()`
- `print()`
- `int()`
- `float()`
- `round()`
- Variabel
- Operator `+`
- Operator `-`
- Operator `*`
- Operator `/`

> Pada Step 4 belum perlu menggunakan `if`, `elif`, atau `else`.

---

# Task 1 — Biodata Mahasiswa

Buat program yang meminta pengguna memasukkan:

```text
Nama
Umur
Jurusan
Semester
```

Contoh input:

```text
Masukkan nama: Budi
Masukkan umur: 20
Masukkan jurusan: Sistem Informasi
Masukkan semester: 4
```

Target output:

```text
=== BIODATA MAHASISWA ===
Nama     : Budi
Umur     : 20
Jurusan  : Sistem Informasi
Semester : 4
```

### Ketentuan

Gunakan:

```python
input()
int()
print()
```

---

# Task 2 — Menghitung Nilai Mahasiswa

Buat program yang meminta:

```text
Nama Mahasiswa
Nilai Tugas
Nilai UTS
Nilai UAS
```

Hitung:

```text
Total Nilai
Rata-rata Nilai
```

Rumus:

```text
Total Nilai =
Nilai Tugas + Nilai UTS + Nilai UAS
```

```text
Rata-rata =
Total Nilai / 3
```

Gunakan:

```python
round(rata_rata, 2)
```

untuk membatasi rata-rata menjadi 2 angka di belakang koma.

Contoh input:

```text
Nama mahasiswa: Budi
Nilai tugas: 80
Nilai UTS: 75
Nilai UAS: 90
```

Target output:

```text
=== HASIL NILAI ===
Nama        : Budi
Nilai Tugas : 80.0
Nilai UTS   : 75.0
Nilai UAS   : 90.0
Total Nilai : 245.0
Rata-rata   : 81.67
```

---

# Task 3 — Kasir Sederhana

Buat program yang meminta:

```text
Nama Barang
Harga Barang
Jumlah Barang
```

Hitung:

```text
Subtotal
```

Rumus:

```text
Subtotal = Harga Barang × Jumlah Barang
```

Contoh input:

```text
Nama barang: Buku
Harga barang: 25000
Jumlah barang: 3
```

Target output:

```text
=== DETAIL PEMBELIAN ===
Barang   : Buku
Harga    : 25000.0
Jumlah   : 3
Subtotal : 75000.0
```

---

# Task 4 — Menghitung Luas Persegi Panjang

Buat program yang meminta:

```text
Panjang
Lebar
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

Contoh input:

```text
Panjang: 10
Lebar: 5
```

Target output:

```text
=== HASIL PERHITUNGAN ===
Panjang  : 10.0
Lebar    : 5.0
Luas     : 50.0
Keliling : 30.0
```

---

# Task 5 — Kalkulator Sederhana

Buat program yang meminta:

```text
Angka Pertama
Angka Kedua
```

Kemudian hitung:

```text
Penjumlahan
Pengurangan
Perkalian
Pembagian
```

Contoh input:

```text
Angka pertama: 20
Angka kedua: 5
```

Target output:

```text
=== HASIL KALKULATOR ===
Penjumlahan : 25.0
Pengurangan : 15.0
Perkalian   : 100.0
Pembagian   : 4.0
```

---

# Challenge — Kasir dengan Pembayaran

Buat program kasir yang meminta:

```text
Nama Barang
Harga Barang
Jumlah Barang
Uang Pembayaran
```

Hitung:

```text
Subtotal
Kembalian
```

Rumus:

```text
Subtotal =
Harga × Jumlah
```

```text
Kembalian =
Uang Pembayaran - Subtotal
```

Contoh input:

```text
Nama barang: Keyboard
Harga barang: 250000
Jumlah barang: 2
Uang pembayaran: 600000
```

Target output:

```text
========================
      STRUK BELANJA
========================
Barang     : Keyboard
Harga      : 250000.0
Jumlah     : 2
Subtotal   : 500000.0
Bayar      : 600000.0
Kembalian  : 100000.0
========================
```

---

# Ketentuan

1. Semua data harus dimasukkan menggunakan `input()`.
2. Gunakan `int()` untuk data bilangan bulat jika diperlukan.
3. Gunakan `float()` untuk data angka yang dapat memiliki desimal.
4. Gunakan variabel untuk menyimpan hasil perhitungan.
5. Gunakan `print()` untuk menampilkan hasil.
6. Gunakan `round()` jika hasil memiliki terlalu banyak angka desimal.
7. Jangan menggunakan `if`, `elif`, atau `else`.
8. Simpan setiap tugas dalam file `.py` yang berbeda.

Contoh:

```text
task1_biodata.py
task2_nilai.py
task3_kasir.py
task4_persegi_panjang.py
task5_kalkulator.py
challenge_kasir.py
```

---

# Target Step 4

Setelah menyelesaikan Mini Task ini, pastikan sudah memahami:

```text
INPUT
  ↓
SIMPAN KE VARIABEL
  ↓
PROCESS
  ↓
OUTPUT
```

dan sudah dapat menggunakan:

```python
input()
print()
int()
float()
round()
```