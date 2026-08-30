# Step 6 — Perulangan / Looping

Program ini berisi contoh:

1. `for`
2. `range()`
3. Bilangan genap
4. Counter
5. Accumulator
6. Input data berulang
7. `while`
8. Validasi input
9. `break`
10. `continue`

---

# 1. Perulangan

Perulangan digunakan untuk menjalankan perintah secara berulang.

Contoh:

```python
for i in range(1, 6):
    print(i)
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

# 2. for

`for` digunakan ketika jumlah perulangan sudah diketahui.

Contoh:

```python
for i in range(1, 6):
    print("Perulangan ke-", i)
```

Artinya program melakukan perulangan sebanyak 5 kali.

---

# 3. range()

Pada program digunakan:

```python
range(1, 6)
```

Artinya:

```text
Mulai dari 1
Berhenti sebelum 6
```

Sehingga menghasilkan:

```text
1
2
3
4
5
```

Contoh lain:

```python
range(1, 11)
```

menghasilkan:

```text
1 sampai 10
```

---

# 4. Looping dengan if

Pada program bilangan genap digunakan:

```python
for angka in range(1, 11):

    if angka % 2 == 0:
        print(angka)
```

Operator:

```python
%
```

digunakan untuk mencari sisa pembagian.

Jika:

```text
angka % 2 == 0
```

berarti angka tersebut genap.

---

# 5. Accumulator

Accumulator digunakan untuk mengumpulkan nilai.

Pada program:

```python
total = 0
```

Kemudian:

```python
total = total + angka
```

Contoh proses:

```text
total = 0

0 + 1 = 1
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
...
```

Digunakan untuk menghitung total.

---

# 6. Counter

Counter digunakan untuk menghitung jumlah kejadian.

Contoh:

```python
jumlah_lulus = 0
```

Jika mahasiswa lulus:

```python
jumlah_lulus = jumlah_lulus + 1
```

Artinya jumlah mahasiswa lulus bertambah satu.

---

# 7. Input Data Berulang

Program meminta jumlah mahasiswa:

```python
jumlah_mahasiswa = int(input("Jumlah mahasiswa: "))
```

Kemudian melakukan looping:

```python
for i in range(1, jumlah_mahasiswa + 1):
```

Sehingga input nama dan nilai dilakukan sebanyak jumlah mahasiswa.

---

# 8. Menghitung Total Nilai

Pada setiap perulangan:

```python
total_nilai = total_nilai + nilai
```

Nilai mahasiswa akan terus ditambahkan ke:

```python
total_nilai
```

---

# 9. Menghitung Rata-Rata

Setelah looping selesai:

```python
rata_rata = total_nilai / jumlah_mahasiswa
```

Rumus:

```text
Rata-rata =
Total Nilai / Jumlah Mahasiswa
```

---

# 10. while

`while` menjalankan perulangan selama kondisi masih benar.

Contoh:

```python
angka = 1

while angka <= 5:
    print(angka)
    angka = angka + 1
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

# 11. Cara Kerja while

Awalnya:

```python
angka = 1
```

Kondisi:

```python
angka <= 5
```

Selama kondisi benar, program terus berjalan.

Setiap perulangan:

```python
angka = angka + 1
```

Nilai angka bertambah.

Saat angka menjadi:

```text
6
```

kondisi:

```text
6 <= 5
```

menjadi salah dan looping berhenti.

---

# 12. Validasi Input dengan while

Pada program digunakan:

```python
while nilai < 0 or nilai > 100:
```

Artinya selama nilai:

```text
Kurang dari 0
ATAU
Lebih dari 100
```

program akan meminta input ulang.

Contoh:

```text
Masukkan nilai 0-100: 150
Nilai tidak valid.

Masukkan nilai 0-100: 80
Nilai diterima: 80
```

---

# 13. break

`break` digunakan untuk menghentikan looping.

Contoh:

```python
for angka in range(1, 11):

    if angka == 6:
        break

    print(angka)
```

Output:

```text
1
2
3
4
5
```

Ketika angka menjadi 6, looping langsung berhenti.

---

# 14. continue

`continue` digunakan untuk melewati satu perulangan.

Contoh:

```python
for angka in range(1, 11):

    if angka == 5:
        continue

    print(angka)
```

Output:

```text
1
2
3
4
6
7
8
9
10
```

Angka 5 dilewati.

---

# 15. Perbedaan break dan continue

```text
break
→ menghentikan seluruh looping

continue
→ melewati satu iterasi saja
```

---

# 16. Fungsi yang Digunakan

| Syntax | Kegunaan |
|---|---|
| `for` | Melakukan perulangan |
| `range()` | Menentukan rentang perulangan |
| `while` | Mengulang berdasarkan kondisi |
| `break` | Menghentikan looping |
| `continue` | Melewati satu iterasi |
| `%` | Mencari sisa pembagian |
| `round()` | Membatasi angka desimal |

---

# 17. Menjalankan Program

## Windows

```bash
py looping.py
```

## macOS / Linux

```bash
python3 looping.py
```

Atau gunakan:

```text
Run Python File
```

di VS Code.

---

# Kesimpulan

Pada Step 6 digunakan:

```text
for
→ perulangan dengan jumlah tertentu

range()
→ menentukan rentang angka

while
→ perulangan berdasarkan kondisi

counter
→ menghitung jumlah kejadian

accumulator
→ mengumpulkan nilai

break
→ menghentikan looping

continue
→ melewati satu iterasi
```

Alur dasarnya:

```text
MULAI
  ↓
PERIKSA / TENTUKAN PERULANGAN
  ↓
JALANKAN PROSES
  ↓
ULANGI
  ↓
SELESAI
```