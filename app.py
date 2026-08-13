#print("Hello, World!")
'''
nama = input("Masukkan nama kamu: ")
jurusan = input("Masukkan jurusan kamu: ")
#print("Selamat datang di ekstrakulikuler Python, " + nama + " dari jurusan " + jurusan + "!")

print(f"Selamat datang di ekstrakulikuler python, {nama} dari jurusan {jurusan}!")
'''
print("=" * 40)
print("FORM PENDAFTARAN BIODATA SISWA")
print("=" * 40)
nama = input("Nama Lengkap: ")
jurusan = input("Jurusan: ")
kelas = input("Kelas(X/XI/XII): ")
hobi = input("Hobi Utama: ")
cita = input("Cita-cita: ")
tahun = input("Tahun Lahir: ")

umur = 2026 - int(tahun)

print("=" * 40)
print("KARTU PROFIL DIGITAL SISWA")
print("=" * 40)
print(f"Nama Lengkap: {nama}")
print(f"Jurusan: {jurusan}")
print(f"Kelas(X/XI/XII): {kelas}")
print(f"Hobi Utama: {hobi}")
print(f"Cita-cita: {cita}")
print(f"Umur: {umur} tahun")

