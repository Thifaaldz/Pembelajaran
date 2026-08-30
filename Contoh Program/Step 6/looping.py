# Step 6 - Perulangan / Looping

# =========================
# PROGRAM FOR LOOP
# =========================

print("=== FOR LOOP ===")

for i in range(1, 6):
    print("Perulangan ke-", i)

print()


# =========================
# PROGRAM BILANGAN GENAP
# =========================

print("=== BILANGAN GENAP 1-10 ===")

for angka in range(1, 11):
    if angka % 2 == 0:
        print(angka)

print()


# =========================
# PROGRAM TOTAL ANGKA
# =========================

print("=== TOTAL ANGKA 1-10 ===")

total = 0

for angka in range(1, 11):
    total = total + angka

print("Total :", total)

print()


# =========================
# PROGRAM INPUT NILAI
# =========================

print("=== INPUT NILAI MAHASISWA ===")

jumlah_mahasiswa = int(input("Jumlah mahasiswa: "))

total_nilai = 0
jumlah_lulus = 0
jumlah_tidak_lulus = 0

for i in range(1, jumlah_mahasiswa + 1):

    print()
    print("Mahasiswa ke-", i)

    nama = input("Nama  : ")
    nilai = float(input("Nilai : "))

    total_nilai = total_nilai + nilai

    if nilai >= 75:
        status = "Lulus"
        jumlah_lulus = jumlah_lulus + 1
    else:
        status = "Tidak Lulus"
        jumlah_tidak_lulus = jumlah_tidak_lulus + 1

    print("Status:", status)

rata_rata = total_nilai / jumlah_mahasiswa

print()
print("=== STATISTIK KELAS ===")
print("Jumlah Mahasiswa   :", jumlah_mahasiswa)
print("Jumlah Lulus       :", jumlah_lulus)
print("Jumlah Tidak Lulus :", jumlah_tidak_lulus)
print("Total Nilai        :", total_nilai)
print("Rata-rata          :", round(rata_rata, 2))

print()


# =========================
# PROGRAM WHILE
# =========================

print("=== WHILE LOOP ===")

angka = 1

while angka <= 5:
    print("Angka:", angka)
    angka = angka + 1

print()


# =========================
# PROGRAM VALIDASI NILAI
# =========================

print("=== VALIDASI NILAI ===")

nilai = float(input("Masukkan nilai 0-100: "))

while nilai < 0 or nilai > 100:

    print("Nilai tidak valid.")

    nilai = float(input("Masukkan nilai 0-100: "))

print("Nilai diterima:", nilai)

print()


# =========================
# PROGRAM BREAK
# =========================

print("=== CONTOH BREAK ===")

for angka in range(1, 11):

    if angka == 6:
        break

    print(angka)

print()


# =========================
# PROGRAM CONTINUE
# =========================

print("=== CONTOH CONTINUE ===")

for angka in range(1, 11):

    if angka == 5:
        continue

    print(angka)