print("============================================")
print("=== Sistem Seleksi Magang / PKL Industri ===")
print("============================================")

nilai_kehadiran = int(input("nilai kehadiran (%) : "))
nilai_sikap = input("nilai sikap (A/B/C/D) : ").upper()
jumlah_projek_selesai = int(input("jumlah projek selesai : "))

if nilai_kehadiran >= 85 and (nilai_sikap == "A" or nilai_sikap == "B") and jumlah_projek_selesai >= 3:
    status = "lolos"
else:
    status = "tidak lolos"

if status == "lolos" and jumlah_projek_selesai >= 5:
    kategori = "Magang di Perusahaan Tier-1 (BUMN/Unicorn)"
elif status == "lolos" and jumlah_projek_selesai >= 3:
    kategori = "Magang di Perusahaan Tier-2 (Startup/Local Industry)"
else:
    kategori = "Belum Layak Magang (Wajib Remedial)"

print("\n=== Hasil Seleksi ===")
print(f"status : {status}")
print(f"kategori : {kategori}")