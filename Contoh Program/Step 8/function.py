# Step 8 - Function / Fungsi

# =========================
# FUNCTION SEDERHANA
# =========================

def salam():
    print("Halo, selamat belajar Python!")


print("=== FUNCTION SEDERHANA ===")

salam()

print()


# =========================
# FUNCTION DENGAN PARAMETER
# =========================

def sapa(nama):
    print("Halo", nama)


print("=== FUNCTION DENGAN PARAMETER ===")

nama = input("Masukkan nama: ")

sapa(nama)

print()


# =========================
# FUNCTION DENGAN RETURN
# =========================

def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas


print("=== HITUNG LUAS ===")

panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

hasil_luas = hitung_luas(panjang, lebar)

print("Luas:", hasil_luas)

print()


# =========================
# FUNCTION CEK KELULUSAN
# =========================

def cek_kelulusan(nilai):

    if nilai >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"


print("=== CEK KELULUSAN ===")

nama_mahasiswa = input("Nama mahasiswa: ")
nilai_mahasiswa = float(input("Nilai mahasiswa: "))

status = cek_kelulusan(nilai_mahasiswa)

print()
print("Nama   :", nama_mahasiswa)
print("Nilai  :", nilai_mahasiswa)
print("Status :", status)

print()


# =========================
# FUNCTION PENENTUAN GRADE
# =========================

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


print("=== PENENTUAN GRADE ===")

nilai = float(input("Masukkan nilai: "))

grade = tentukan_grade(nilai)

print("Grade:", grade)

print()


# =========================
# FUNCTION DENGAN LIST
# =========================

def hitung_rata_rata(data):

    total = sum(data)

    rata_rata = total / len(data)

    return rata_rata


print("=== RATA-RATA NILAI ===")

nilai_kelas = [80, 75, 90, 60, 85]

hasil_rata_rata = hitung_rata_rata(nilai_kelas)

print("Data Nilai :", nilai_kelas)
print("Rata-rata  :", round(hasil_rata_rata, 2))

print()


# =========================
# FUNCTION HITUNG LULUS
# =========================

def hitung_lulus(data):

    jumlah_lulus = 0

    for nilai in data:

        if nilai >= 75:
            jumlah_lulus += 1

    return jumlah_lulus


print("=== JUMLAH MAHASISWA LULUS ===")

jumlah_lulus = hitung_lulus(nilai_kelas)

print("Jumlah Lulus:", jumlah_lulus)

print()


# =========================
# FUNCTION TAMPILKAN DATA
# =========================

def tampilkan_data(data):

    for nomor, item in enumerate(data, start=1):
        print(nomor, ".", item)


print("=== DAFTAR MAHASISWA ===")

mahasiswa = ["Budi", "Siti", "Andi", "Rina"]

tampilkan_data(mahasiswa)

print()


# =========================
# FUNCTION TAMBAH DATA
# =========================

def tambah_data(data, nama):
    data.append(nama)


print("=== TAMBAH MAHASISWA ===")

nama_baru = input("Masukkan nama mahasiswa baru: ")

tambah_data(mahasiswa, nama_baru)

print()

tampilkan_data(mahasiswa)