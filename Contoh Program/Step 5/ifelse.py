# Step 5 - Percabangan / Conditional

# =========================
# PROGRAM CEK KELULUSAN
# =========================

print("=== CEK KELULUSAN ===")

nama = input("Masukkan nama mahasiswa: ")
nilai = float(input("Masukkan nilai: "))

if nilai >= 75:
    status = "Lulus"
else:
    status = "Tidak Lulus"

print()
print("=== HASIL ===")
print("Nama   :", nama)
print("Nilai  :", nilai)
print("Status :", status)

print()


# =========================
# PROGRAM PENENTUAN GRADE
# =========================

print("=== PENENTUAN GRADE ===")

nilai_grade = float(input("Masukkan nilai: "))

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

print("Grade:", grade)

print()


# =========================
# PROGRAM GANJIL / GENAP
# =========================

print("=== CEK GANJIL / GENAP ===")

angka = int(input("Masukkan angka: "))

if angka % 2 == 0:
    print(angka, "adalah bilangan Genap")
else:
    print(angka, "adalah bilangan Ganjil")

print()


# =========================
# PROGRAM DISKON
# =========================

print("=== PROGRAM DISKON ===")

total_belanja = float(input("Masukkan total belanja: "))

if total_belanja >= 500000:
    persen_diskon = 20
elif total_belanja >= 250000:
    persen_diskon = 10
elif total_belanja >= 100000:
    persen_diskon = 5
else:
    persen_diskon = 0

diskon = total_belanja * persen_diskon / 100
total_bayar = total_belanja - diskon

print()
print("=== HASIL PEMBAYARAN ===")
print("Total Belanja :", total_belanja)
print("Diskon        :", persen_diskon, "%")
print("Potongan      :", diskon)
print("Total Bayar   :", total_bayar)

print()


# =========================
# PROGRAM LOGIN SEDERHANA
# =========================

print("=== LOGIN SEDERHANA ===")

username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "python123":
    print("Login berhasil")
else:
    print("Username atau password salah")