# Step 4 — Input dan Output

## Tujuan

Pada step ini kita akan belajar:

- `input()`
- `print()`
- Menerima data dari pengguna
- Mengubah tipe data input
- Menggunakan `int()`
- Menggunakan `float()`
- Konsep Input → Process → Output

---

# 1. Apa Itu Input?

Input adalah data yang diberikan oleh pengguna kepada program.

Di Python, input dapat menggunakan:

```python
input()
```

Contoh:

```python
nama = input("Masukkan nama: ")
```

Ketika program dijalankan:

```text
Masukkan nama: Budi
```

Data:

```text
Budi
```

akan disimpan ke variabel:

```python
nama
```

---

# 2. Contoh Input Sederhana

```python
nama = input("Masukkan nama: ")

print("Nama Anda:", nama)
```

Contoh output:

```text
Masukkan nama: Budi
Nama Anda: Budi
```

---

# 3. Apa Itu Output?

Output adalah hasil yang ditampilkan oleh program.

Untuk menampilkan output kita menggunakan:

```python
print()
```

Contoh:

```python
print("Hello World")
```

Output:

```text
Hello World
```

---

# 4. Menampilkan Variabel

Contoh:

```python
nama = "Budi"

print("Nama:", nama)
```

Output:

```text
Nama: Budi
```

---

# 5. Input Secara Default Adalah String

Perhatikan:

```python
umur = input("Masukkan umur: ")
```

Walaupun pengguna memasukkan:

```text
20
```

Python tetap membaca data tersebut sebagai:

```text
string
```

Kita dapat mengeceknya menggunakan:

```python
print(type(umur))
```

Hasil:

```text
<class 'str'>
```

---

# 6. Mengubah Input Menjadi Integer

Jika data akan digunakan untuk perhitungan bilangan bulat, gunakan:

```python
int()
```

Contoh:

```python
umur = int(input("Masukkan umur: "))
```

Sekarang `umur` memiliki tipe:

```text
integer
```

atau:

```python
int
```

---

# 7. Mengubah Input Menjadi Float

Jika data dapat memiliki angka desimal, gunakan:

```python
float()
```

Contoh:

```python
nilai = float(input("Masukkan nilai: "))
```

Contoh input:

```text
85.5
```

---

# 8. Perbedaan int() dan float()

| Fungsi | Digunakan untuk | Contoh |
|---|---|---|
| `int()` | Bilangan bulat | `20` |
| `float()` | Bilangan desimal | `85.5` |
| `input()` | Menerima teks | `"Budi"` |

Contoh:

```python
nama = input("Nama: ")
umur = int(input("Umur: "))
ipk = float(input("IPK: "))
```

---

# 9. Input → Process → Output

Konsep dasar sebuah program:

```text
INPUT
  ↓
PROCESS
  ↓
OUTPUT
```

Contoh program menghitung subtotal barang:

```python
harga = float(input("Harga barang: "))
jumlah = int(input("Jumlah barang: "))

subtotal = harga * jumlah

print("Subtotal:", subtotal)
```

Alurnya:

```text
INPUT
Harga
Jumlah
   ↓
PROCESS
Harga × Jumlah
   ↓
OUTPUT
Subtotal
```

---

# 10. Contoh Biodata

```python
nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))
jurusan = input("Masukkan jurusan: ")

print()
print("=== BIODATA ===")
print("Nama    :", nama)
print("Umur    :", umur)
print("Jurusan :", jurusan)
```

Contoh:

```text
Masukkan nama: Budi
Masukkan umur: 20
Masukkan jurusan: Sistem Informasi

=== BIODATA ===
Nama    : Budi
Umur    : 20
Jurusan : Sistem Informasi
```

---

# 11. Contoh Perhitungan Nilai

```python
nilai_tugas = float(input("Nilai tugas: "))
nilai_uts = float(input("Nilai UTS: "))
nilai_uas = float(input("Nilai UAS: "))

total = nilai_tugas + nilai_uts + nilai_uas
rata_rata = total / 3

print("Total      :", total)
print("Rata-rata :", rata_rata)
```

---

# 12. Membatasi Angka Desimal

Gunakan:

```python
round()
```

Contoh:

```python
rata_rata = 81.666666

print(round(rata_rata, 2))
```

Output:

```text
81.67
```

Angka:

```text
2
```

berarti menampilkan maksimal 2 angka di belakang koma.

---

# 13. Contoh Program Kasir

```python
nama_barang = input("Nama barang: ")
harga = float(input("Harga barang: "))
jumlah = int(input("Jumlah barang: "))

subtotal = harga * jumlah

print()
print("=== DETAIL PEMBELIAN ===")
print("Barang   :", nama_barang)
print("Harga    :", harga)
print("Jumlah   :", jumlah)
print("Subtotal :", subtotal)
```

---

# 14. Menjalankan Program

File contoh:

```text
inputoutput.py
```

## Windows

Jalankan melalui terminal:

```bash
py inputoutput.py
```

atau klik:

```text
Run Python File
```

di VS Code.

---

## macOS / Linux

Jalankan:

```bash
python3 inputoutput.py
```

atau klik:

```text
Run Python File
```

di VS Code.

---

# 15. Kesalahan yang Sering Terjadi

## Tidak Menggunakan int()

Contoh:

```python
angka1 = input("Angka 1: ")
angka2 = input("Angka 2: ")

print(angka1 + angka2)
```

Jika input:

```text
10
20
```

hasilnya:

```text
1020
```

Bukan:

```text
30
```

Karena input masih berupa string.

Perbaikan:

```python
angka1 = int(input("Angka 1: "))
angka2 = int(input("Angka 2: "))

print(angka1 + angka2)
```

Output:

```text
30
```

---

# 16. Kesimpulan

Fungsi utama pada Step 4:

```text
input()
→ menerima data dari pengguna

print()
→ menampilkan data

int()
→ mengubah data menjadi bilangan bulat

float()
→ mengubah data menjadi bilangan desimal

round()
→ membatasi angka desimal
```

Alur dasar program:

```text
INPUT
  ↓
VARIABEL
  ↓
PROCESS
  ↓
OUTPUT
```

Contoh:

```python
harga = float(input("Harga: "))
jumlah = int(input("Jumlah: "))

subtotal = harga * jumlah

print("Subtotal:", subtotal)
```

Setelah memahami Step 4, materi berikutnya adalah:

# Step 5 — Percabangan / Conditional

Pada Step 5 kita akan mulai menggunakan:

```python
if
elif
else
```

untuk membuat program dapat mengambil keputusan.