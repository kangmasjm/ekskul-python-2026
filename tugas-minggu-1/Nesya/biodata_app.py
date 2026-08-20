#print("Hello, World!")

'''
nama = input("Masukkan nama kamu: ")
jurusan = input("Masukkan jurusan kamu:")'''
#print("Selamat datang di ekstrakulikuler Python, " + nama + " dari jurusan " + jurusan + "!")

#print(f"Selamat datang di Ekstrakulikuler Python, (nama) dari jurusan (jurusan) !")

'''
print("=" *40)
print("FORM PENDAFTARAN BIODATA SISWA")
print("=" *40)
nama = input("Masukkan Nama Lengkap: ")
jurusan = input("Masukkan jurusan: ")
kelas = input ("Masukkan Kelas (X/XI/XII): ")
hobi = input("Masukkan Hobi utama: ")
cita = input("Masukkan Cita-Cita: ")
tahun = input("Masukkan Tahun lahir: ")

print("=" *40)
print("KARTU PROFIL DIGITAL SISWA")
print("=" *40)
print("Nama Lengkap: " + nama)
print("Jurusan: " + jurusan)
print("Kelas(X/XI/XII): " + kelas)
print("Hobi utama: " + hobi)
print("Cita-cita: " + cita)
print("Tahun lahir" + tahun)'''


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

#konversi
rupiah = int(input("Masukkan uang rupiah: "))

dollar = rupiah / 16000

print(f"Uang dalam dollar = {dollar}")
