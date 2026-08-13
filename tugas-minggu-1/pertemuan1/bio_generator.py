print("=" * 30)
print("FORM PENDAFTARAN BIODATA SISWA")
print("=" * 30)

nama = input("Nama Lengkap : ")
jurusan = input("Jurusan : ")
kelas = input("Kelas ( X / XI / XII) : ")
hobi = input("Hobi : ")
cita_cita = input("Cita-cita : ")
lahir = int(input("Tahun Lahir :"))
umur = (2026 - lahir)

print("=" * 30)
print("KARTU PROFILE BIODATA SISWA")
print("=" * 30)

print(f"Nama        : {nama}")
print(f"Kelas       : {kelas}")
print(f"Umur        : {umur}")
print(f"Hobi        : {hobi}")
print(f"Cita - Cita : {cita_cita}")

print("=" * 30)