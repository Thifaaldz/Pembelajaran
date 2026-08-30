# Step 3 — Variabel, Tipe Data, dan Operator

Program ini mempelajari:

1. Variabel
2. Tipe Data
3. Operator Matematika
4. Menghitung Total Nilai
5. Menghitung Rata-rata
6. Mengecek Tipe Data dengan `type()`
7. Menampilkan Data dengan `print()`

---

# 1. Variabel

Variabel digunakan untuk menyimpan data.

Contoh:

```python
nama = "Budi"
umur = 20
tinggi = 170.5
mahasiswa_aktif = True
```

Artinya:

```text
nama
→ menyimpan "Budi"

umur
→ menyimpan 20

tinggi
→ menyimpan 170.5

mahasiswa_aktif
→ menyimpan True
```

---

# 2. Tipe Data String

String digunakan untuk menyimpan teks.

Contoh:

```python
nama = "Budi"
```

Tipe datanya:

```text
str
```

String menggunakan tanda kutip:

```python
"Budi"
```

---

# 3. Tipe Data Integer

Integer digunakan untuk menyimpan bilangan bulat.

Contoh:

```python
umur = 20
```

Tipe datanya:

```text
int
```

Contoh integer:

```text
10
20
100
500
```

---

# 4. Tipe Data Float

Float digunakan untuk menyimpan angka desimal.

Contoh:

```python
tinggi = 170.5
```

Tipe datanya:

```text
float
```

Contoh:

```text
170.5
80.5
3.75
```

---

# 5. Tipe Data Boolean

Boolean hanya memiliki dua nilai:

```python
True
False
```

Pada program digunakan:

```python
mahasiswa_aktif = True
```

Tipe datanya:

```text
bool
```

---

# 6. Variabel Nilai Mahasiswa

Program menyimpan tiga nilai:

```python
nilai_tugas = 80
nilai_uts = 75
nilai_uas = 90
```

Masing-masing nilai disimpan dalam variabel berbeda.

---

# 7. Menghitung Total Nilai

Program menggunakan operator:

```python
+
```

Kode:

```python
total_nilai = nilai_tugas + nilai_uts + nilai_uas
```

Contoh:

```text
80 + 75 + 90
= 245
```

Sehingga:

```text
total_nilai = 245
```

---

# 8. Menghitung Rata-Rata

Rumus:

```text
Rata-rata =
Total Nilai / Jumlah Nilai
```

Kode:

```python
rata_rata = total_nilai / 3
```

Contoh:

```text
245 / 3
= 81.666666...
```

---

# 9. Operator yang Digunakan

Pada program digunakan:

| Operator | Fungsi |
|---|---|
| `=` | Memberikan nilai ke variabel |
| `+` | Penjumlahan |
| `/` | Pembagian |

Contoh:

```python
nama = "Budi"
```

`=` digunakan untuk menyimpan nilai.

Contoh:

```python
total_nilai = nilai_tugas + nilai_uts + nilai_uas
```

`+` digunakan untuk penjumlahan.

Contoh:

```python
rata_rata = total_nilai / 3
```

`/` digunakan untuk pembagian.

---

# 10. Menampilkan Data

Untuk menampilkan data digunakan:

```python
print()
```

Contoh:

```python
print("Nama :", nama)
```

Output:

```text
Nama : Budi
```

---

# 11. Membatasi Angka Desimal

Pada program digunakan:

```python
round()
```

Contoh:

```python
print("Rata-rata :", round(rata_rata, 2))
```

Jika hasil:

```text
81.666666
```

maka menjadi:

```text
81.67
```

Angka:

```text
2
```

berarti maksimal 2 angka di belakang koma.

---

# 12. Mengecek Tipe Data

Untuk mengetahui tipe data sebuah variabel digunakan:

```python
type()
```

Contoh:

```python
print(type(nama))
```

Output:

```text
<class 'str'>
```

Contoh lainnya:

```python
print(type(umur))
print(type(tinggi))
print(type(mahasiswa_aktif))
```

Hasil:

```text
<class 'int'>
<class 'float'>
<class 'bool'>
```

---

# 13. Tipe Data yang Digunakan

| Variabel | Contoh Nilai | Tipe |
|---|---:|---|
| `nama` | `"Budi"` | `str` |
| `umur` | `20` | `int` |
| `tinggi` | `170.5` | `float` |
| `mahasiswa_aktif` | `True` | `bool` |
| `nilai_tugas` | `80` | `int` |
| `nilai_uts` | `75` | `int` |
| `nilai_uas` | `90` | `int` |

---

# 14. Alur Program

```text
BUAT VARIABEL
      ↓
SIMPAN DATA
      ↓
LAKUKAN PERHITUNGAN
      ↓
TOTAL NILAI
      ↓
RATA-RATA
      ↓
TAMPILKAN DATA
      ↓
CEK TIPE DATA
```

---

# 15. Menjalankan Program

File:

```text
variable.py
```

## Windows

```bash
py variable.py
```

## macOS / Linux

```bash
python3 variable.py
```

Atau klik:

```text
Run Python File
```

di VS Code.

---

# Kesimpulan

Pada Step 3 kita menggunakan:

```text
Variabel
→ menyimpan data

str
→ teks

int
→ bilangan bulat

float
→ bilangan desimal

bool
→ True atau False

=
→ memberikan nilai

+
→ penjumlahan

/
→ pembagian

print()
→ menampilkan data

type()
→ mengecek tipe data

round()
→ membatasi angka desimal
```

Konsep utama:

```text
DATA
 ↓
VARIABEL
 ↓
TIPE DATA
 ↓
OPERATOR
 ↓
HASIL
```