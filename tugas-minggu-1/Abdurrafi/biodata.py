# nama = input("Masukkan Nama Kamu :")
# jurusan = input("Masukkan Jurusan Kamu :")
# print("Selamat datang " + nama + ". Dari jurusan " + jurusan)
# print(f"Selamat datang {nama}. Dari jurusan {jurusan}")

print("=" * 30)
print("FORM PENDAFTARAN BIODATA SISWA")
print("=" * 30)

nama = input("Masukkan Nama Kamu : ")
jurusan = input("Masukkan Jurusan Kamu : ")
kelas = input("Masukkan Kelas ( X / XI / XII) : ")

if kelas == "X":
    rombel = "X - " + jurusan
elif kelas == "XI":
    rombel = "XI - " + jurusan
elif kelas == "XII":
    rombel = "XII - " + jurusan
else:
    rombel = "Kelas tidak valid"

hobi = input("Masukkan Hobi Kamu : ")
citaCita = input("Masukkan Cita - Cita Kamu : ")
lahir = int(input("Masukkan Tahun Lahir :"))
usia = (2026 - lahir)

print("=" * 30)
print("KARTU PROFILE BIODATA SISWA")
print("=" * 30)

print(f"Nama : {nama}")
print(f"Rombel : {rombel}")
print(f"Usia : {usia}")
print(f"Hobi : {hobi}")
print(f"Cita - Cita : {citaCita}")

print("=" * 30)