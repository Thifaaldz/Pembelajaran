# Step 7 - Array / List

# =========================
# LIST SEDERHANA
# =========================

print("=== LIST NAMA MAHASISWA ===")

mahasiswa = ["Budi", "Siti", "Andi"]

print("Semua Data :", mahasiswa)
print("Data Pertama :", mahasiswa[0])
print("Data Kedua   :", mahasiswa[1])
print("Data Terakhir:", mahasiswa[-1])

print()


# =========================
# MENAMBAH DATA
# =========================

print("=== TAMBAH DATA ===")

mahasiswa.append("Rina")

print("Setelah Ditambah:", mahasiswa)

print()


# =========================
# MENGUBAH DATA
# =========================

print("=== UBAH DATA ===")

mahasiswa[1] = "Sinta"

print("Setelah Diubah:", mahasiswa)

print()


# =========================
# MENGHAPUS DATA
# =========================

print("=== HAPUS DATA ===")

mahasiswa.remove("Andi")

print("Setelah Dihapus:", mahasiswa)

print()


# =========================
# MENAMPILKAN LIST DENGAN LOOP
# =========================

print("=== DAFTAR MAHASISWA ===")

for nomor, nama in enumerate(mahasiswa, start=1):
    print(nomor, ".", nama)

print()


# =========================
# PROGRAM INPUT NILAI
# =========================

print("=== INPUT NILAI MAHASISWA ===")

nilai_mahasiswa = []

jumlah_data = int(input("Jumlah nilai yang ingin dimasukkan: "))

for i in range(jumlah_data):

    nilai = float(input(f"Masukkan nilai ke-{i + 1}: "))

    nilai_mahasiswa.append(nilai)

print()

print("=== DATA NILAI ===")

for nomor, nilai in enumerate(nilai_mahasiswa, start=1):
    print("Nilai ke-", nomor, ":", nilai)

print()


# =========================
# STATISTIK NILAI
# =========================

total_nilai = sum(nilai_mahasiswa)
jumlah_nilai = len(nilai_mahasiswa)
rata_rata = total_nilai / jumlah_nilai
nilai_tertinggi = max(nilai_mahasiswa)
nilai_terendah = min(nilai_mahasiswa)

print("=== STATISTIK NILAI ===")
print("Jumlah Data    :", jumlah_nilai)
print("Total Nilai    :", total_nilai)
print("Rata-rata      :", round(rata_rata, 2))
print("Nilai Tertinggi:", nilai_tertinggi)
print("Nilai Terendah :", nilai_terendah)

print()


# =========================
# CEK KELULUSAN
# =========================

print("=== STATUS NILAI ===")

jumlah_lulus = 0
jumlah_tidak_lulus = 0

for nilai in nilai_mahasiswa:

    if nilai >= 75:
        print(nilai, "-> Lulus")
        jumlah_lulus += 1

    else:
        print(nilai, "-> Tidak Lulus")
        jumlah_tidak_lulus += 1

print()

print("Jumlah Lulus       :", jumlah_lulus)
print("Jumlah Tidak Lulus :", jumlah_tidak_lulus)

print()


# =========================
# PENCARIAN DATA SEDERHANA
# =========================

print("=== CARI MAHASISWA ===")

cari = input("Masukkan nama yang dicari: ")

if cari in mahasiswa:
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")