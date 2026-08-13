import datetime

print("=" * 40)
print("     FORM PENDAFTARAN BIODATA SISWA")
print("=" * 40)

nama = input("Nama Lengkap     : ")
jurusan = input("Jurusan          : ")
kelas = input("Kelas (X/XI/XII) : ")
hobi = input("Hobi Utama       : ")
cita2 = input("Cita-cita        : ")
lahir = input("Tahun Lahir      : ")

tahun = datetime.datetime.now().year
umur = tahun - int(lahir)

print("=" * 40)
print("     FORM PENDAFTARAN BIODATA SISWA")
print("=" * 40)
print(f"Nama         : {nama}")
print(f"Kelas/Rombel : {kelas}")
print(f"Usia         : {umur} Tahun")
print(f"Hobi         : {hobi}")
print(f"Cita-cita    : {cita2}")
print("-" * 40)
print(f"Pesan Motivasi: 'Semangat belajar Python, {nama}! Masa depanmu di {cita2} dimulai hari ini.'")
print("=" * 40)