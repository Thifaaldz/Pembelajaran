# Instalasi Python dan Visual Studio Code di macOS

Panduan ini digunakan untuk melakukan instalasi:

* Python
* Visual Studio Code
* Python Extension di VS Code

sampai program Python berhasil dijalankan melalui Visual Studio Code.

Program pertama:

```python
print("Hello World")
```

---

# 1. Buka Website Python

Buka browser seperti:

```text
Safari
Google Chrome
Firefox
```

Kemudian buka website resmi Python:

```text
https://www.python.org
```

---

# 2. Buka Menu Downloads

Pada halaman utama Python, pilih menu:

```text
Downloads
```

Kemudian pilih:

```text
macOS
```

---

# 3. Download Python

Download versi:

```text
Python 3
```

terbaru yang tersedia untuk macOS.

File installer biasanya memiliki ekstensi:

```text
.pkg
```

Contoh:

```text
python-3.x.x-macos11.pkg
```

Tunggu sampai proses download selesai.

---

# 4. Buka File Installer Python

Setelah proses download selesai, buka folder:

```text
Downloads
```

Kemudian klik dua kali file:

```text
python-3.x.x-macos11.pkg
```

Installer Python akan terbuka.

---

# 5. Mulai Proses Instalasi

Pada halaman installer, klik:

```text
Continue
```

---

# 6. Lanjutkan Instalasi

Klik kembali:

```text
Continue
```

jika muncul informasi mengenai Python.

---

# 7. Setujui Lisensi

Pada halaman lisensi klik:

```text
Continue
```

Kemudian pilih:

```text
Agree
```

---

# 8. Pilih Lokasi Instalasi

Gunakan lokasi instalasi default.

Tidak perlu mengubah lokasi instalasi untuk pembelajaran dasar.

Klik:

```text
Install
```

---

# 9. Masukkan Password macOS

Jika macOS meminta autentikasi, masukkan:

```text
Password perangkat Mac
```

atau gunakan:

```text
Touch ID
```

jika tersedia.

---

# 10. Tunggu Instalasi Python

Tunggu sampai proses instalasi selesai.

Jika berhasil, klik:

```text
Close
```

Python sekarang sudah terpasang.

---

# 11. Buka Terminal

Tekan:

```text
Command + Space
```

Kemudian ketik:

```text
Terminal
```

Tekan:

```text
Enter
```

---

# 12. Cek Versi Python

Pada Terminal ketik:

```bash
python3 --version
```

Kemudian tekan Enter.

Jika instalasi berhasil akan muncul:

```text
Python 3.x.x
```

Contoh:

```text
Python 3.14.x
```

Jika versi Python muncul, berarti Python sudah berhasil terpasang.

---

# 13. Tes Python dari Terminal

Ketik:

```bash
python3
```

Jika berhasil akan muncul:

```text
Python 3.x.x
>>>
```

Tanda:

```text
>>>
```

menunjukkan Python Interactive Shell sudah berjalan.

---

# 14. Tes Hello World

Pada:

```text
>>>
```

ketik:

```python
print("Hello World")
```

Output:

```text
Hello World
```

Jika berhasil, Python sudah dapat digunakan.

---

# 15. Keluar dari Python

Ketik:

```python
exit()
```

Kemudian tekan Enter.

Terminal akan kembali seperti:

```text
namauser@MacBook ~ %
```

---

# Instalasi Visual Studio Code

Setelah Python berhasil terpasang, berikutnya install Visual Studio Code sebagai editor untuk menulis program Python.

---

# 16. Buka Website Visual Studio Code

Buka browser.

Kemudian buka:

```text
https://code.visualstudio.com
```

---

# 17. Download VS Code

Pilih:

```text
Download for macOS
```

Download versi yang sesuai dengan perangkat Mac.

Mac modern umumnya menggunakan:

```text
Apple Silicon
```

seperti:

```text
M1
M2
M3
M4
```

Jika menggunakan Mac Intel, pilih versi:

```text
Intel
```

---

# 18. Buka File VS Code

Setelah download selesai, buka folder:

```text
Downloads
```

Buka file Visual Studio Code yang sudah didownload.

Biasanya berbentuk:

```text
.zip
```

atau aplikasi Visual Studio Studio Code hasil ekstraksi.

---

# 19. Pindahkan VS Code ke Applications

Setelah file berhasil dibuka atau diekstrak, pindahkan:

```text
Visual Studio Code.app
```

ke folder:

```text
Applications
```

Contoh:

```text
Applications
└── Visual Studio Code.app
```

---

# 20. Buka Visual Studio Code

Buka:

```text
Applications
```

Kemudian klik:

```text
Visual Studio Code
```

Jika macOS meminta konfirmasi keamanan, pilih:

```text
Open
```

---

# 21. Install Python Extension

Setelah VS Code terbuka, pilih menu:

```text
Extensions
```

atau gunakan shortcut:

```text
Command + Shift + X
```

---

# 22. Cari Python Extension

Pada kolom pencarian ketik:

```text
Python
```

Pilih extension:

```text
Python
```

Publisher:

```text
Microsoft
```

Kemudian klik:

```text
Install
```

---

# 23. Pastikan Python Extension Terpasang

Setelah selesai, status extension akan menjadi:

```text
Installed
```

Python Extension digunakan agar VS Code dapat:

```text
Menjalankan Python
Mendeteksi syntax Python
Memberikan autocomplete
Mendeteksi error
Memilih Python Interpreter
```

---

# 24. Buat Folder Belajar Python

Buat folder baru.

Contoh:

```text
Documents
└── belajar-python
```

---

# 25. Buka Folder di VS Code

Pada VS Code pilih:

```text
File
↓
Open Folder
```

Pilih:

```text
belajar-python
```

Kemudian klik:

```text
Open
```

Jika muncul pertanyaan mengenai workspace trust, pilih:

```text
Yes, I trust the authors
```

untuk folder belajar yang dibuat sendiri.

---

# 26. Buat File Python

Pada bagian Explorer klik:

```text
New File
```

Buat file:

```text
hello.py
```

Pastikan file memiliki ekstensi:

```text
.py
```

---

# 27. Isi File Python

Masukkan:

```python
print("Hello World")
```

Kemudian simpan dengan:

```text
Command + S
```

---

# 28. Pilih Python Interpreter

Tekan:

```text
Command + Shift + P
```

Kemudian cari:

```text
Python: Select Interpreter
```

Klik menu tersebut.

---

# 29. Pilih Python 3

Pilih interpreter Python yang sudah di-install.

Contoh:

```text
Python 3.x.x
```

Pastikan menggunakan:

```text
Python 3
```

---

# 30. Menjalankan Python dari VS Code

Buka file:

```text
hello.py
```

Kemudian klik tombol:

```text
▶
```

di kanan atas.

Pilih:

```text
Run Python File
```

---

# 31. Melihat Output

Terminal VS Code akan terbuka di bagian bawah.

Program:

```python
print("Hello World")
```

akan menghasilkan:

```text
Hello World
```

Jika hasil tersebut muncul, VS Code sudah berhasil menjalankan Python.

---

# 32. Menjalankan dari Terminal VS Code

Program juga dapat dijalankan melalui Terminal VS Code.

Buka:

```text
Terminal
↓
New Terminal
```

Kemudian jalankan:

```bash
python3 hello.py
```

Output:

```text
Hello World
```

---

# 33. Percobaan Kedua

Ubah file `hello.py` menjadi:

```python
print("Hello World")
print("Saya sedang belajar Python")
```

Output:

```text
Hello World
Saya sedang belajar Python
```

---

# 34. Percobaan Perhitungan

Tambahkan:

```python
print(10 + 5)
```

Program:

```python
print("Hello World")
print("Saya sedang belajar Python")
print(10 + 5)
```

Output:

```text
Hello World
Saya sedang belajar Python
15
```

---

# 35. Struktur Folder Awal

Untuk pembelajaran dapat menggunakan struktur:

```text
belajar-python/
│
├── hello.py
├── latihan1.py
├── latihan2.py
└── latihan3.py
```

Nantinya setiap latihan Python dapat dibuat dalam file:

```text
.py
```

---

# 36. Ringkasan Command macOS

## Mengecek Python

```bash
python3 --version
```

---

## Menjalankan Python Interactive Shell

```bash
python3
```

---

## Keluar dari Python

```python
exit()
```

---

## Menjalankan File Python

```bash
python3 hello.py
```

---

# 37. Alur Instalasi Lengkap

```text
Buka python.org
        ↓
Download Python untuk macOS
        ↓
Buka file .pkg
        ↓
Continue
        ↓
Agree
        ↓
Install
        ↓
Python Terpasang
        ↓
Buka Terminal
        ↓
python3 --version
        ↓
Tes Hello World
        ↓
Download Visual Studio Code
        ↓
Pindahkan ke Applications
        ↓
Buka VS Code
        ↓
Install Python Extension
        ↓
Buat Folder belajar-python
        ↓
Buat hello.py
        ↓
Select Python Interpreter
        ↓
Run Python File
        ↓
Hello World
        ↓
READY TO CODE
```

---

# 38. Checklist Instalasi Python

Pastikan:

* [ ] Python sudah didownload.
* [ ] File `.pkg` berhasil dibuka.
* [ ] Python berhasil di-install.
* [ ] Terminal berhasil dibuka.
* [ ] `python3 --version` berhasil.
* [ ] Versi Python muncul.
* [ ] `python3` berhasil dijalankan.
* [ ] `>>>` muncul.
* [ ] `print("Hello World")` berhasil.
* [ ] `exit()` berhasil digunakan.

---

# 39. Checklist Visual Studio Code

Pastikan:

* [ ] VS Code sudah didownload.
* [ ] VS Code sudah dipindahkan ke `Applications`.
* [ ] VS Code berhasil dibuka.
* [ ] Python Extension dari Microsoft sudah di-install.
* [ ] Folder `belajar-python` sudah dibuat.
* [ ] Folder berhasil dibuka di VS Code.
* [ ] File `hello.py` sudah dibuat.
* [ ] Python Interpreter sudah dipilih.
* [ ] Tombol `Run Python File` dapat digunakan.
* [ ] Terminal VS Code terbuka.
* [ ] Output `Hello World` muncul.

---

# 40. Hasil Akhir

Jika file:

```text
hello.py
```

berisi:

```python
print("Hello World")
```

dan dapat dijalankan melalui:

```text
VS Code
↓
Run Python File
```

atau:

```bash
python3 hello.py
```

dengan output:

```text
Hello World
```

maka seluruh instalasi sudah berhasil.

```text
Python Installed
      ↓
VS Code Installed
      ↓
Python Extension Installed
      ↓
Interpreter Selected
      ↓
hello.py
      ↓
Run Python File
      ↓
Hello World
      ↓
READY TO CODE
```
