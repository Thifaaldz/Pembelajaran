# Step 4 - Input dan Output

print("=== PROGRAM BIODATA MAHASISWA ===")

# INPUT
nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))
jurusan = input("Masukkan jurusan: ")

print()

# OUTPUT
print("=== BIODATA ===")
print("Nama    :", nama)
print("Umur    :", umur)
print("Jurusan :", jurusan)

print()

# =========================
# PROGRAM PERHITUNGAN
# =========================

print("=== PERHITUNGAN NILAI ===")

nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

# PROCESS
total_nilai = nilai_tugas + nilai_uts + nilai_uas
rata_rata = total_nilai / 3

print()

# OUTPUT
print("=== HASIL NILAI ===")
print("Nilai Tugas :", nilai_tugas)
print("Nilai UTS   :", nilai_uts)
print("Nilai UAS   :", nilai_uas)
print("Total Nilai :", total_nilai)
print("Rata-rata   :", round(rata_rata, 2))

print()

# =========================
# PROGRAM KASIR SEDERHANA
# =========================

print("=== KASIR SEDERHANA ===")

nama_barang = input("Nama barang: ")
harga = float(input("Harga barang: "))
jumlah = int(input("Jumlah barang: "))

# PROCESS
subtotal = harga * jumlah

print()

# OUTPUT
print("=== DETAIL PEMBELIAN ===")
print("Barang   :", nama_barang)
print("Harga    :", harga)
print("Jumlah   :", jumlah)
print("Subtotal :", subtotal)  