# Instalasi Python dan Visual Studio Code di Windows

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
Google Chrome
Microsoft Edge
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
Windows
```

---

# 3. Download Python

Download versi:

```text
Python 3
```

terbaru yang tersedia untuk Windows.

Untuk kebanyakan laptop Windows modern, gunakan versi:

```text
64-bit
```

Tunggu sampai proses download selesai.

---

# 4. Buka File Installer

Setelah proses download selesai, buka folder:

```text
Downloads
```

Kemudian klik dua kali file installer Python.

Nama file biasanya seperti:

```text
python-3.x.x-amd64.exe
```

atau installer Python terbaru yang tersedia dari website resmi.

---

# 5. Aktifkan PATH

Pada halaman awal installer, jika tersedia pilihan:

```text
Add Python to PATH
```

aktifkan atau centang pilihan tersebut.

Contoh:

```text
☑ Add Python to PATH
```

Bagian ini penting agar Python dapat dijalankan melalui:

```text
Command Prompt
PowerShell
Terminal
```

---

# 6. Mulai Instalasi

Klik:

```text
Install Now
```

untuk menggunakan konfigurasi instalasi standar.

Untuk pembelajaran dasar, tidak perlu mengubah pengaturan lanjutan.

---

# 7. Tunggu Proses Instalasi

Tunggu sampai proses instalasi selesai.

Jika berhasil, akan muncul informasi bahwa Python berhasil dipasang.

Kemudian klik:

```text
Close
```

---

# 8. Buka Command Prompt

Setelah Python berhasil di-install, buka:

```text
Command Prompt
```

Caranya:

Tekan:

```text
Windows Key
```

Kemudian ketik:

```text
cmd
```

Pilih:

```text
Command Prompt
```

---

# 9. Cek Versi Python

Pada Command Prompt ketik:

```bash
py --version
```

Kemudian tekan:

```text
Enter
```

Jika instalasi berhasil, akan muncul seperti:

```text
Python 3.x.x
```

Contoh:

```text
Python 3.14.x
```

Jika versi Python sudah muncul, berarti instalasi berhasil.

---

# 10. Alternatif Pengecekan

Selain:

```bash
py --version
```

Anda juga dapat mencoba:

```bash
python --version
```

Jika berhasil, hasilnya juga seperti:

```text
Python 3.x.x
```

Untuk panduan ini, kita akan menggunakan:

```text
py
```

sebagai command utama di Windows.

---

# 11. Jalankan Python

Pada Command Prompt ketik:

```bash
py
```

Kemudian tekan:

```text
Enter
```

Jika berhasil, akan muncul tampilan seperti:

```text
Python 3.x.x
>>>
```

Tanda:

```text
>>>
```

menandakan Python sudah berjalan.

---

# 12. Jalankan Hello World

Setelah muncul:

```text
>>>
```

ketik:

```python
print("Hello World")
```

Kemudian tekan:

```text
Enter
```

Output:

```text
Hello World
```

Jika output tersebut muncul, Python sudah berhasil dijalankan.

---

# 13. Percobaan Kedua

Coba:

```python
print("Saya sedang belajar Python")
```

Output:

```text
Saya sedang belajar Python
```

---

# 14. Percobaan Perhitungan

Coba:

```python
print(10 + 5)
```

Output:

```text
15
```

---

# 15. Keluar dari Python

Untuk keluar dari Python Interactive Shell, ketik:

```python
exit()
```

Kemudian tekan:

```text
Enter
```

Setelah itu tampilan akan kembali ke Command Prompt.

Contoh:

```text
C:\Users\NamaUser>
```

---

# 16. Jika `py` Tidak Ditemukan

Jika ketika menjalankan:

```bash
py --version
```

muncul pesan seperti:

```text
'py' is not recognized
```

lakukan langkah berikut:

```text
1. Tutup Command Prompt.
2. Buka kembali Command Prompt.
3. Jalankan lagi:

   py --version
```

Jika masih tidak berhasil, coba:

```bash
python --version
```

Jika keduanya tidak berhasil, kemungkinan Python belum terpasang dengan benar.

---

# 17. Jika Python Tidak Terdeteksi

Jika Python belum terdeteksi:

1. Buka kembali installer Python.
2. Pastikan Python benar-benar sudah terinstall.
3. Jika tersedia, aktifkan:

```text
Add Python to PATH
```

4. Selesaikan instalasi.
5. Tutup Command Prompt.
6. Buka Command Prompt kembali.
7. Jalankan:

```bash
py --version
```

---

# Instalasi Visual Studio Code

Setelah Python berhasil terpasang, berikutnya install Visual Studio Code sebagai editor untuk menulis dan menjalankan program Python.

---

# 18. Buka Website Visual Studio Code

Buka browser.

Kemudian buka:

```text
https://code.visualstudio.com
```

---

# 19. Download Visual Studio Code

Pada halaman utama pilih:

```text
Download for Windows
```

Tunggu sampai proses download selesai.

File installer biasanya memiliki nama seperti:

```text
VSCodeUserSetup-x64-x.x.x.exe
```

---

# 20. Buka Installer VS Code

Buka folder:

```text
Downloads
```

Kemudian klik dua kali file installer Visual Studio Code.

---

# 21. Setujui License Agreement

Pilih:

```text
I accept the agreement
```

Kemudian klik:

```text
Next
```

---

# 22. Pilih Lokasi Instalasi

Gunakan lokasi instalasi default.

Kemudian klik:

```text
Next
```

---

# 23. Pilih Start Menu Folder

Gunakan pengaturan default.

Klik:

```text
Next
```

---

# 24. Pilih Additional Tasks

Pada bagian:

```text
Select Additional Tasks
```

disarankan mengaktifkan:

```text
☑ Add "Open with Code" action to Windows Explorer file context menu

☑ Add "Open with Code" action to Windows Explorer directory context menu

☑ Register Code as an editor for supported file types

☑ Add to PATH
```

Bagian yang paling penting adalah:

```text
☑ Add to PATH
```

Kemudian klik:

```text
Next
```

---

# 25. Install Visual Studio Code

Klik:

```text
Install
```

Tunggu sampai proses instalasi selesai.

---

# 26. Jalankan Visual Studio Code

Setelah proses instalasi selesai, aktifkan:

```text
☑ Launch Visual Studio Code
```

Kemudian klik:

```text
Finish
```

Visual Studio Code akan terbuka.

---

# 27. Install Python Extension

Setelah VS Code terbuka, pilih menu:

```text
Extensions
```

atau tekan:

```text
Ctrl + Shift + X
```

---

# 28. Cari Python Extension

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

# 29. Pastikan Python Extension Terpasang

Setelah selesai, status extension akan menjadi:

```text
Installed
```

Python Extension digunakan agar VS Code dapat:

```text
Menjalankan Python
Mendeteksi syntax Python
Memberikan autocomplete
Menampilkan error
Memilih Python Interpreter
```

---

# 30. Buat Folder Belajar Python

Buat folder baru.

Contoh:

```text
Documents
└── belajar-python
```

---

# 31. Buka Folder di VS Code

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
Select Folder
```

Jika muncul pertanyaan mengenai Workspace Trust, pilih:

```text
Yes, I trust the authors
```

untuk folder belajar yang dibuat sendiri.

---

# 32. Buat File Python

Pada bagian Explorer klik:

```text
New File
```

Buat file:

```text
hello.py
```

Pastikan menggunakan ekstensi:

```text
.py
```

---

# 33. Isi File Python

Masukkan:

```python
print("Hello World")
```

Kemudian simpan dengan:

```text
Ctrl + S
```

---

# 34. Pilih Python Interpreter

Tekan:

```text
Ctrl + Shift + P
```

Kemudian cari:

```text
Python: Select Interpreter
```

Klik menu:

```text
Python: Select Interpreter
```

---

# 35. Pilih Python 3

Pilih interpreter Python yang sebelumnya sudah di-install.

Contoh:

```text
Python 3.x.x
```

Pastikan menggunakan:

```text
Python 3
```

Jika hanya terdapat satu Python, pilih Python tersebut.

---

# 36. Menjalankan Python dari VS Code

Buka file:

```text
hello.py
```

Kemudian klik tombol:

```text
▶
```

di bagian kanan atas VS Code.

Pilih:

```text
Run Python File
```

---

# 37. Melihat Output

Terminal VS Code akan terbuka di bagian bawah.

Program:

```python
print("Hello World")
```

akan menghasilkan:

```text
Hello World
```

Jika hasil tersebut muncul, Python sudah berhasil dijalankan melalui VS Code.

---

# 38. Menjalankan dari Terminal VS Code

Selain menggunakan tombol Run, program juga dapat dijalankan melalui Terminal VS Code.

Pilih:

```text
Terminal
↓
New Terminal
```

atau gunakan shortcut:

```text
Ctrl + `
```

Kemudian jalankan:

```bash
py hello.py
```

Output:

```text
Hello World
```

Jika `py` tidak tersedia, coba:

```bash
python hello.py
```

---

# 39. Percobaan Kedua di VS Code

Ubah isi file:

```text
hello.py
```

menjadi:

```python
print("Hello World")
print("Saya sedang belajar Python")
```

Jalankan kembali.

Output:

```text
Hello World
Saya sedang belajar Python
```

---

# 40. Percobaan Perhitungan

Tambahkan:

```python
print(10 + 5)
```

Sehingga:

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

# 41. Struktur Folder Awal

Untuk pembelajaran dapat menggunakan struktur:

```text
belajar-python/
│
├── hello.py
├── latihan1.py
├── latihan2.py
└── latihan3.py
```

Setiap program Python dapat dibuat dalam file:

```text
.py
```

---

# 42. Ringkasan Command Windows

## Mengecek Python

```bash
py --version
```

---

## Alternatif Mengecek Python

```bash
python --version
```

---

## Menjalankan Python Interactive Shell

```bash
py
```

---

## Keluar dari Python

```python
exit()
```

---

## Menjalankan File Python

```bash
py hello.py
```

Alternatif:

```bash
python hello.py
```

---

# 43. Alur Instalasi Lengkap

```text
Buka python.org
        ↓
Downloads
        ↓
Pilih Windows
        ↓
Download Python 3
        ↓
Buka Installer
        ↓
Aktifkan Add Python to PATH
        ↓
Install Now
        ↓
Python Terpasang
        ↓
Buka Command Prompt
        ↓
py --version
        ↓
py
        ↓
>>>
        ↓
print("Hello World")
        ↓
Hello World
        ↓
Download Visual Studio Code
        ↓
Install VS Code
        ↓
Aktifkan Add to PATH
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

# 44. Checklist Instalasi Python

Pastikan:

* [ ] Python sudah didownload dari website resmi.
* [ ] Installer Python berhasil dibuka.
* [ ] `Add Python to PATH` sudah diaktifkan jika tersedia.
* [ ] Python berhasil di-install.
* [ ] Command Prompt berhasil dibuka.
* [ ] `py --version` berhasil dijalankan.
* [ ] Versi Python muncul.
* [ ] `py` berhasil dijalankan.
* [ ] Tanda `>>>` muncul.
* [ ] `print("Hello World")` berhasil dijalankan.
* [ ] Output `Hello World` muncul.
* [ ] `exit()` berhasil digunakan.

---

# 45. Checklist Visual Studio Code

Pastikan:

* [ ] Visual Studio Code sudah didownload.
* [ ] VS Code berhasil di-install.
* [ ] `Add to PATH` sudah diaktifkan saat instalasi VS Code.
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

# 46. Hasil Akhir

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

atau melalui Terminal:

```bash
py hello.py
```

dengan output:

```text
Hello World
```

maka seluruh proses instalasi sudah berhasil.

```text
Python Installed
      ↓
Python Detected
      ↓
VS Code Installed
      ↓
Python Extension Installed
      ↓
Python Interpreter Selected
      ↓
hello.py
      ↓
Run Python File
      ↓
Hello World
      ↓
READY TO CODE
```
