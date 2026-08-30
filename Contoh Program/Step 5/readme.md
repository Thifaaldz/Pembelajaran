# Step 5 — Percabangan / Conditional

Program ini berisi contoh:

1. Cek Kelulusan
2. Penentuan Grade
3. Ganjil / Genap
4. Program Diskon
5. Login Sederhana

---

# 1. Percabangan

Percabangan digunakan ketika program harus mengambil keputusan berdasarkan kondisi tertentu.

Struktur dasar:

```python
if kondisi:
    perintah
else:
    perintah
```

---

# 2. if

`if` digunakan untuk memeriksa kondisi.

Contoh pada program:

```python
if nilai >= 75:
    status = "Lulus"
```

Artinya:

```text
Jika nilai lebih besar atau sama dengan 75
maka status = Lulus
```

---

# 3. else

`else` dijalankan jika kondisi `if` tidak terpenuhi.

```python
if nilai >= 75:
    status = "Lulus"
else:
    status = "Tidak Lulus"
```

Alurnya:

```text
nilai >= 75?
   ↓
 YA        TIDAK
 ↓           ↓
Lulus    Tidak Lulus
```

---

# 4. elif

`elif` digunakan jika terdapat lebih dari dua kondisi.

Contoh:

```python
if nilai_grade >= 85:
    grade = "A"
elif nilai_grade >= 75:
    grade = "B"
elif nilai_grade >= 65:
    grade = "C"
elif nilai_grade >= 55:
    grade = "D"
else:
    grade = "E"
```

Program akan memeriksa kondisi dari atas ke bawah.

---

# 5. Operator Perbandingan

Operator yang digunakan:

| Operator | Arti |
|---|---|
| `==` | Sama dengan |
| `!=` | Tidak sama dengan |
| `>` | Lebih besar |
| `<` | Lebih kecil |
| `>=` | Lebih besar atau sama dengan |
| `<=` | Lebih kecil atau sama dengan |

Contoh:

```python
nilai >= 75
```

---

# 6. Ganjil dan Genap

Program menggunakan operator:

```python
%
```

untuk mendapatkan sisa pembagian.

```python
if angka % 2 == 0:
    print("Genap")
else:
    print("Ganjil")
```

Contoh:

```text
10 % 2 = 0
→ Genap

7 % 2 = 1
→ Ganjil
```

---

# 7. Program Diskon

Program menentukan diskon berdasarkan total belanja.

```python
if total_belanja >= 500000:
    persen_diskon = 20
elif total_belanja >= 250000:
    persen_diskon = 10
elif total_belanja >= 100000:
    persen_diskon = 5
else:
    persen_diskon = 0
```

Kemudian menghitung:

```python
diskon = total_belanja * persen_diskon / 100
total_bayar = total_belanja - diskon
```

Alurnya:

```text
Input Total Belanja
        ↓
Periksa Kondisi
        ↓
Tentukan Diskon
        ↓
Hitung Potongan
        ↓
Hitung Total Bayar
```

---

# 8. Operator and

Pada program login digunakan:

```python
and
```

Contoh:

```python
if username == "admin" and password == "python123":
```

Artinya kedua kondisi harus benar:

```text
Username benar
      DAN
Password benar
      ↓
Login Berhasil
```

---

# 9. Perbedaan = dan ==

`=` digunakan untuk memberikan nilai:

```python
nama = "Budi"
```

Sedangkan `==` digunakan untuk membandingkan:

```python
username == "admin"
```

---

# 10. Indentasi

Kode di dalam `if`, `elif`, dan `else` harus memiliki indentasi.

Benar:

```python
if nilai >= 75:
    print("Lulus")
```

Salah:

```python
if nilai >= 75:
print("Lulus")
```

Biasanya Python menggunakan 4 spasi.

---

# 11. Program yang Digunakan

### Cek Kelulusan

```text
Nilai >= 75
→ Lulus

Nilai < 75
→ Tidak Lulus
```

### Grade

```text
>= 85 → A
>= 75 → B
>= 65 → C
>= 55 → D
< 55  → E
```

### Ganjil / Genap

```text
Sisa bagi 2 = 0
→ Genap

Selain itu
→ Ganjil
```

### Diskon

```text
>= 500000 → 20%
>= 250000 → 10%
>= 100000 → 5%
< 100000  → 0%
```

### Login

```text
Username = admin
Password = python123
```

Keduanya harus benar.

---

# 12. Menjalankan Program

## Windows

```bash
py ifelse.py
```

## macOS / Linux

```bash
python3 ifelse.py
```

Atau gunakan:

```text
Run Python File
```

di VS Code.

---

# Kesimpulan

Pada program ini digunakan:

```text
if
→ memeriksa kondisi

elif
→ memeriksa kondisi tambahan

else
→ dijalankan jika kondisi sebelumnya salah

==
→ membandingkan nilai

>=
→ lebih besar atau sama dengan

%
→ mencari sisa pembagian

and
→ kedua kondisi harus benar
```

Konsep utama:

```text
INPUT
  ↓
PERIKSA KONDISI
  ↓
KEPUTUSAN
  ↓
OUTPUT
```