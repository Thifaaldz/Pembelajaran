# Mini Task — Step 8

## Function / Fungsi

Gunakan materi:

- `def`
- Parameter
- Argument
- `return`
- `if`
- `for`
- List
- `append()`
- `sum()`
- `len()`

---

# Task 1 — Function Salam

Buat Function:

```python
def salam():
```

Ketika dipanggil:

```python
salam()
```

Target output:

```text
Halo, selamat belajar Python!
```

---

# Task 2 — Function Sapa

Buat Function:

```python
def sapa(nama):
```

Contoh pemanggilan:

```python
sapa("Budi")
```

Target:

```text
Halo Budi
```

---

# Task 3 — Function Penjumlahan

Buat Function:

```python
def tambah(angka1, angka2):
```

Gunakan:

```python
return
```

Contoh:

```python
hasil = tambah(10, 5)
```

Target:

```text
15
```

---

# Task 4 — Luas Persegi Panjang

Buat Function:

```python
def hitung_luas(panjang, lebar):
```

Rumus:

```text
Luas = Panjang × Lebar
```

Gunakan `return`.

Contoh:

```text
Panjang: 10
Lebar: 5
```

Output:

```text
Luas: 50
```

---

# Task 5 — Cek Ganjil Genap

Buat:

```python
def cek_angka(angka):
```

Ketentuan:

```text
angka % 2 == 0
→ Genap

Selain itu
→ Ganjil
```

Gunakan `return`.

---

# Task 6 — Cek Kelulusan

Buat:

```python
def cek_kelulusan(nilai):
```

Ketentuan:

```text
Nilai >= 75
→ Lulus

Nilai < 75
→ Tidak Lulus
```

Contoh:

```python
status = cek_kelulusan(80)
```

Output:

```text
Lulus
```

---

# Task 7 — Penentuan Grade

Buat:

```python
def tentukan_grade(nilai):
```

Ketentuan:

```text
>= 85 → A
>= 75 → B
>= 65 → C
>= 55 → D
< 55  → E
```

Return grade.

---

# Task 8 — Menghitung Rata-Rata

Gunakan List:

```python
nilai = [80, 75, 90, 60, 85]
```

Buat Function:

```python
def hitung_rata_rata(data):
```

Gunakan:

```python
sum()
len()
```

Return rata-rata.

---

# Task 9 — Menghitung Mahasiswa Lulus

Gunakan:

```python
nilai = [80, 60, 90, 70, 85]
```

Buat:

```python
def hitung_lulus(data):
```

Ketentuan:

```text
Nilai >= 75
→ Lulus
```

Return jumlah mahasiswa yang lulus.

---

# Task 10 — Tampilkan Data

Gunakan:

```python
mahasiswa = ["Budi", "Siti", "Andi", "Rina"]
```

Buat:

```python
def tampilkan_data(data):
```

Gunakan:

```python
enumerate()
```

Target:

```text
1. Budi
2. Siti
3. Andi
4. Rina
```

---

# Task 11 — Tambah Mahasiswa

Buat:

```python
def tambah_data(data, nama):
```

Gunakan:

```python
append()
```

Contoh:

```python
mahasiswa = ["Budi", "Siti"]

tambah_data(mahasiswa, "Andi")
```

Target:

```text
["Budi", "Siti", "Andi"]
```

---

# Task 12 — Cari Mahasiswa

Buat:

```python
def cari_mahasiswa(data, nama):
```

Jika nama ada dalam List:

```text
return True
```

Jika tidak ada:

```text
return False
```

Gunakan:

```python
in
```

---

# Challenge — Sistem Nilai Modular

Buat program sistem nilai mahasiswa menggunakan Function.

Gunakan List:

```python
nama_mahasiswa = []
nilai_mahasiswa = []
```

Buat Function:

```text
tambah_mahasiswa()
tampilkan_data()
cek_kelulusan()
tentukan_grade()
hitung_rata_rata()
hitung_lulus()
```

---

## Function Tambah Mahasiswa

Buat:

```python
def tambah_mahasiswa(nama_list, nilai_list):
```

Function meminta:

```text
Nama
Nilai
```

Kemudian memasukkan data ke List.

---

## Function Cek Kelulusan

```python
def cek_kelulusan(nilai):
```

Ketentuan:

```text
>= 75 → Lulus
< 75  → Tidak Lulus
```

---

## Function Grade

```python
def tentukan_grade(nilai):
```

Ketentuan:

```text
>= 85 → A
>= 75 → B
>= 65 → C
>= 55 → D
< 55  → E
```

---

## Function Tampilkan Data

Tampilkan:

```text
1. Budi - 80 - B - Lulus
2. Andi - 60 - D - Tidak Lulus
3. Siti - 90 - A - Lulus
```

---

## Function Statistik

Hitung:

```text
Jumlah Mahasiswa
Jumlah Lulus
Jumlah Tidak Lulus
Rata-rata
Nilai Tertinggi
Nilai Terendah
```

Contoh:

```text
=========================
      STATISTIK KELAS
=========================
Jumlah Mahasiswa   : 3
Jumlah Lulus       : 2
Jumlah Tidak Lulus : 1
Rata-rata          : 76.67
Nilai Tertinggi    : 90
Nilai Terendah     : 60
=========================
```

---

# Ketentuan

1. Gunakan `def` untuk membuat Function.
2. Gunakan parameter jika Function membutuhkan data.
3. Gunakan `return` jika Function menghasilkan nilai.
4. Gunakan List untuk menyimpan banyak data.
5. Gunakan `for` jika perlu memproses List.
6. Gunakan `if`, `elif`, dan `else` untuk keputusan.
7. Hindari menulis kode yang sama berulang kali.
8. Pecah program menjadi beberapa Function.

Simpan setiap tugas dalam file berbeda:

```text
task1_salam.py
task2_sapa.py
task3_tambah.py
task4_luas.py
task5_genap.py
task6_kelulusan.py
task7_grade.py
task8_rata_rata.py
task9_lulus.py
task10_tampilkan.py
task11_tambah_data.py
task12_cari.py
challenge_nilai.py
```

---

# Target Step 8

Setelah menyelesaikan Step 8, pastikan memahami:

```text
PROGRAM
   ↓
DIPECAH MENJADI FUNCTION
   ↓
PARAMETER
   ↓
PROCESS
   ↓
RETURN
   ↓
FUNCTION DIPANGGIL
```

dan mampu menggabungkan:

```text
FUNCTION
+
CONDITIONAL
+
LOOPING
+
LIST
```