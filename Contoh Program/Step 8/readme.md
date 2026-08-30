# Step 8 — Function / Fungsi

Program ini berisi contoh:

1. Function sederhana
2. Function dengan parameter
3. Function dengan `return`
4. Function dengan percabangan
5. Function dengan List
6. Function dengan looping
7. Function untuk menambahkan data

---

# 1. Membuat Function

Function dibuat menggunakan:

```python
def
```

Contoh:

```python
def salam():
    print("Halo, selamat belajar Python!")
```

Untuk menjalankannya:

```python
salam()
```

---

# 2. Function dengan Parameter

Parameter digunakan untuk menerima data.

Contoh:

```python
def sapa(nama):
    print("Halo", nama)
```

Kemudian:

```python
sapa("Budi")
```

Output:

```text
Halo Budi
```

Pada program:

```python
nama = input("Masukkan nama: ")

sapa(nama)
```

---

# 3. Function dengan Return

`return` digunakan untuk mengembalikan hasil dari Function.

Contoh:

```python
def hitung_luas(panjang, lebar):

    luas = panjang * lebar

    return luas
```

Kemudian:

```python
hasil_luas = hitung_luas(10, 5)
```

Nilai:

```text
hasil_luas = 50
```

---

# 4. Parameter

Pada:

```python
def hitung_luas(panjang, lebar):
```

Parameter yang digunakan adalah:

```text
panjang
lebar
```

Function menerima dua data untuk melakukan perhitungan.

---

# 5. Argument

Ketika Function dipanggil:

```python
hitung_luas(10, 5)
```

nilai:

```text
10
5
```

disebut argument.

Sederhananya:

```text
Parameter
→ variabel yang menerima data

Argument
→ data yang dikirim ke Function
```

---

# 6. Function Cek Kelulusan

Program menggunakan:

```python
def cek_kelulusan(nilai):

    if nilai >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"
```

Ketentuan:

```text
Nilai >= 75
→ Lulus

Nilai < 75
→ Tidak Lulus
```

Pemanggilan:

```python
status = cek_kelulusan(nilai_mahasiswa)
```

---

# 7. Function Penentuan Grade

Program menggunakan:

```python
def tentukan_grade(nilai):

    if nilai >= 85:
        return "A"

    elif nilai >= 75:
        return "B"

    elif nilai >= 65:
        return "C"

    elif nilai >= 55:
        return "D"

    else:
        return "E"
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

# 8. Function dengan List

Function juga dapat menerima List.

Contoh:

```python
def hitung_rata_rata(data):

    total = sum(data)

    rata_rata = total / len(data)

    return rata_rata
```

Data:

```python
nilai_kelas = [80, 75, 90, 60, 85]
```

Pemanggilan:

```python
hasil_rata_rata = hitung_rata_rata(nilai_kelas)
```

---

# 9. Function dengan Looping

Pada Function:

```python
def hitung_lulus(data):

    jumlah_lulus = 0

    for nilai in data:

        if nilai >= 75:
            jumlah_lulus += 1

    return jumlah_lulus
```

Function melakukan looping terhadap seluruh data dalam List.

---

# 10. Function Menampilkan Data

Program menggunakan:

```python
def tampilkan_data(data):

    for nomor, item in enumerate(data, start=1):
        print(nomor, ".", item)
```

Contoh data:

```python
mahasiswa = ["Budi", "Siti", "Andi", "Rina"]
```

Output:

```text
1 . Budi
2 . Siti
3 . Andi
4 . Rina
```

---

# 11. Function Menambahkan Data

Program menggunakan:

```python
def tambah_data(data, nama):
    data.append(nama)
```

Pemanggilan:

```python
tambah_data(mahasiswa, nama_baru)
```

Data baru akan ditambahkan ke List mahasiswa.

---

# 12. Perbedaan print() dan return

`print()` digunakan untuk menampilkan hasil.

Contoh:

```python
print("Halo")
```

Sedangkan:

```python
return
```

digunakan untuk mengembalikan nilai dari Function.

Contoh:

```python
def tambah(a, b):
    return a + b
```

Kemudian:

```python
hasil = tambah(10, 5)
```

Nilai:

```text
hasil = 15
```

---

# 13. Alur Function

Contoh:

```python
hasil_luas = hitung_luas(10, 5)
```

Alurnya:

```text
hitung_luas(10, 5)
        ↓
panjang = 10
lebar = 5
        ↓
10 × 5
        ↓
return 50
        ↓
hasil_luas = 50
```

---

# 14. Function yang Digunakan

| Function | Kegunaan |
|---|---|
| `salam()` | Menampilkan salam |
| `sapa()` | Menampilkan salam berdasarkan nama |
| `hitung_luas()` | Menghitung luas |
| `cek_kelulusan()` | Menentukan status kelulusan |
| `tentukan_grade()` | Menentukan grade |
| `hitung_rata_rata()` | Menghitung rata-rata List |
| `hitung_lulus()` | Menghitung jumlah mahasiswa lulus |
| `tampilkan_data()` | Menampilkan isi List |
| `tambah_data()` | Menambahkan data ke List |

---

# 15. Syntax yang Digunakan

```text
def
→ membuat Function

()
→ parameter dan pemanggilan Function

return
→ mengembalikan hasil

if / elif / else
→ membuat keputusan

for
→ melakukan looping

List
→ menyimpan banyak data
```

---

# 16. Menjalankan Program

## Windows

```bash
py function.py
```

## macOS / Linux

```bash
python3 function.py
```

Atau gunakan:

```text
Run Python File
```

di VS Code.

---

# Kesimpulan

Function digunakan untuk membuat bagian program yang dapat digunakan kembali.

Contoh:

```python
def cek_kelulusan(nilai):

    if nilai >= 75:
        return "Lulus"

    return "Tidak Lulus"
```

Kemudian cukup digunakan dengan:

```python
status = cek_kelulusan(80)
```

Konsep utama:

```text
BUAT FUNCTION
      ↓
PARAMETER
      ↓
PROCESS
      ↓
RETURN
      ↓
PANGGIL FUNCTION
      ↓
HASIL
```

Dengan Function, program menjadi:

```text
Lebih rapi
Lebih mudah dibaca
Lebih mudah digunakan kembali
```