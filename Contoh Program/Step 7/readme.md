# Step 7 — Array / List

Program ini berisi contoh:

1. Membuat List
2. Mengakses data List
3. Menambah data
4. Mengubah data
5. Menghapus data
6. Looping List
7. Input data ke List
8. Statistik List
9. Status kelulusan
10. Pencarian sederhana

---

# 1. Membuat List

List digunakan untuk menyimpan banyak data dalam satu variabel.

Contoh:

```python
mahasiswa = ["Budi", "Siti", "Andi"]
```

Satu variabel `mahasiswa` menyimpan tiga data.

---

# 2. Index List

Setiap data dalam List memiliki index.

```python
mahasiswa = ["Budi", "Siti", "Andi"]
```

Index:

```text
0 → Budi
1 → Siti
2 → Andi
```

Contoh:

```python
print(mahasiswa[0])
```

Output:

```text
Budi
```

---

# 3. Index Terakhir

Gunakan:

```python
mahasiswa[-1]
```

untuk mengambil data terakhir.

Contoh:

```python
print(mahasiswa[-1])
```

Output:

```text
Andi
```

---

# 4. Menambahkan Data

Gunakan:

```python
append()
```

Contoh:

```python
mahasiswa.append("Rina")
```

List menjadi:

```text
["Budi", "Siti", "Andi", "Rina"]
```

---

# 5. Mengubah Data

Data dapat diubah menggunakan index.

Contoh:

```python
mahasiswa[1] = "Sinta"
```

Artinya data pada index `1` diganti menjadi:

```text
Sinta
```

---

# 6. Menghapus Data

Gunakan:

```python
remove()
```

Contoh:

```python
mahasiswa.remove("Andi")
```

Data `Andi` akan dihapus dari List.

---

# 7. Menampilkan Semua Data

List dapat digabung dengan looping.

Contoh:

```python
for nama in mahasiswa:
    print(nama)
```

---

# 8. enumerate()

Pada program digunakan:

```python
enumerate()
```

Contoh:

```python
for nomor, nama in enumerate(mahasiswa, start=1):
    print(nomor, ".", nama)
```

Output:

```text
1 . Budi
2 . Sinta
3 . Rina
```

`start=1` membuat nomor dimulai dari 1.

---

# 9. Membuat List Kosong

Pada program nilai digunakan:

```python
nilai_mahasiswa = []
```

Artinya List dibuat dalam keadaan kosong.

Data akan dimasukkan kemudian.

---

# 10. Input Data ke List

Program meminta jumlah data:

```python
jumlah_data = int(input("Jumlah nilai yang ingin dimasukkan: "))
```

Kemudian input dilakukan menggunakan looping:

```python
for i in range(jumlah_data):

    nilai = float(input(f"Masukkan nilai ke-{i + 1}: "))

    nilai_mahasiswa.append(nilai)
```

Setiap nilai dimasukkan ke List menggunakan:

```python
append()
```

---

# 11. len()

Gunakan:

```python
len()
```

untuk mengetahui jumlah data.

Contoh:

```python
jumlah_nilai = len(nilai_mahasiswa)
```

---

# 12. sum()

Gunakan:

```python
sum()
```

untuk menjumlahkan seluruh data angka.

Contoh:

```python
total_nilai = sum(nilai_mahasiswa)
```

---

# 13. Rata-Rata

Rumus:

```text
Rata-rata =
Total Nilai / Jumlah Data
```

Kode:

```python
rata_rata = total_nilai / jumlah_nilai
```

---

# 14. max()

Gunakan:

```python
max()
```

untuk mencari nilai terbesar.

Contoh:

```python
nilai_tertinggi = max(nilai_mahasiswa)
```

---

# 15. min()

Gunakan:

```python
min()
```

untuk mencari nilai terkecil.

Contoh:

```python
nilai_terendah = min(nilai_mahasiswa)
```

---

# 16. Status Kelulusan

Setiap nilai diperiksa menggunakan looping dan percabangan.

```python
for nilai in nilai_mahasiswa:

    if nilai >= 75:
        print(nilai, "-> Lulus")

    else:
        print(nilai, "-> Tidak Lulus")
```

Ketentuan:

```text
Nilai >= 75
→ Lulus

Nilai < 75
→ Tidak Lulus
```

---

# 17. Menghitung Jumlah Lulus

Pada program digunakan counter:

```python
jumlah_lulus = 0
jumlah_tidak_lulus = 0
```

Jika lulus:

```python
jumlah_lulus += 1
```

Jika tidak lulus:

```python
jumlah_tidak_lulus += 1
```

---

# 18. Mencari Data

Gunakan:

```python
in
```

untuk memeriksa apakah data terdapat dalam List.

Contoh:

```python
if cari in mahasiswa:
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")
```

---

# 19. Fungsi yang Digunakan

| Fungsi / Syntax | Kegunaan |
|---|---|
| `[]` | Membuat List |
| `[index]` | Mengakses data |
| `append()` | Menambahkan data |
| `remove()` | Menghapus data |
| `len()` | Menghitung jumlah data |
| `sum()` | Menghitung total |
| `max()` | Mencari nilai terbesar |
| `min()` | Mencari nilai terkecil |
| `enumerate()` | Mendapatkan nomor dan data |
| `in` | Mengecek keberadaan data |

---

# 20. Menjalankan Program

## Windows

```bash
py list.py
```

## macOS / Linux

```bash
python3 list.py
```

Atau klik:

```text
Run Python File
```

di VS Code.

---

# Kesimpulan

Pada Step 7 digunakan:

```text
List
→ menyimpan banyak data

Index
→ mengakses data

append()
→ menambahkan data

remove()
→ menghapus data

for
→ memproses semua data

len()
→ jumlah data

sum()
→ total data

max()
→ nilai terbesar

min()
→ nilai terkecil

in
→ mencari data
```

Alur program:

```text
INPUT
  ↓
SIMPAN KE LIST
  ↓
LOOPING DATA
  ↓
PROCESS
  ↓
STATISTIK / PENCARIAN
  ↓
OUTPUT
```