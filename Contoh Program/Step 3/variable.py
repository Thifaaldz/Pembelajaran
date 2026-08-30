# Step 3 - Variabel, Tipe Data, dan Operator

# =========================
# VARIABEL
# =========================

nama = "Budi"
umur = 20
tinggi = 170.5
mahasiswa_aktif = True

# =========================
# NILAI
# =========================

nilai_tugas = 80
nilai_uts = 75
nilai_uas = 90

# =========================
# OPERATOR
# =========================

total_nilai = nilai_tugas + nilai_uts + nilai_uas
rata_rata = total_nilai / 3

# =========================
# OUTPUT
# =========================

print("=== BIODATA MAHASISWA ===")
print("Nama            :", nama)
print("Umur            :", umur)
print("Tinggi          :", tinggi)
print("Mahasiswa Aktif :", mahasiswa_aktif)

print()

print("=== NILAI MAHASISWA ===")
print("Nilai Tugas     :", nilai_tugas)
print("Nilai UTS       :", nilai_uts)
print("Nilai UAS       :", nilai_uas)
print("Total Nilai     :", total_nilai)
print("Rata-rata       :", round(rata_rata, 2))

print()

print("=== TIPE DATA ===")
print("Nama            :", type(nama))
print("Umur            :", type(umur))
print("Tinggi          :", type(tinggi))
print("Mahasiswa Aktif :", type(mahasiswa_aktif))