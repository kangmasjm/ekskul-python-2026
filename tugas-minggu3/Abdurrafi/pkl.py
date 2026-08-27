print("=" * 50)
print("SISTEM SELEKSI KELAYAKAN MAGANG / PKL")
print("=" * 50)

kehadiran = float(input("Masukkan Nilai Kehadiran (%) : "))
sikap = input("Masukkan Nilai Sikap (A/B/C/D) : ").upper()
project = int(input("Masukkan Jumlah Project Selesai : "))

if kehadiran >= 85 and (sikap == "A" or sikap == "B") and project >= 3:
    if project >= 5:
        hasil = "Magang di Perusahaan Tier-1 (BUMN/Unicorn)"
    else:
        hasil = "Magang di Perusahaan Tier-2 (Startup/Local Industry)"
else:
    hasil = "Belum Layak Magang (Wajib Remedial)"

print("=" * 50)
print("HASIL SELEKSI MAGANG / PKL")
print("=" * 50)

print(f"Kehadiran       : {kehadiran}%")
print(f"Nilai Sikap     : {sikap}")
print(f"Jumlah Project  : {project}")
print("-" * 50)
print(f"Hasil           : {hasil}")
print("=" * 50)