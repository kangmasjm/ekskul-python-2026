#sistem kelayakan pkl

print("=== SISTEM SELEKSI KELAYAKAN MAGANG ===")

kehadiran = int(input("Masukkan nilai kehadiran: "))
sikap = input("Masukkan nilai sikap (A/B/C/D): ").upper()
projek = int(input("Masukkan jumlah project selesai: "))

if kehadiran >= 85 and (sikap == "A" or sikap == "B") and projek >= 3:
    status = "LOLOS"

    if projek >= 5:
        kategori = "Magang Tier 1 (BUMN/Unicorn)"
    else:
        kategori = "Magang Tier 2 (Startup/Industri Lokal)"
        pesan = "Semua persyaratan magang sudah terpenuhi."
else:
    status = "BELUM LAYAK MAGANG"
    kategori = "Wajib remedial"

    if kehadiran < 85:
        pesan = "Perbaiki nilai kehadiran."
    elif sikap == "C" or sikap == "D":
        pesan = "Perbaiki nilai sikap."
    elif projek < 3:
        pesan = "Kumpulkan projek."

print("=== HASIL SELEKSI ===")
print("Status   :", status)
print("Kategori :", kategori)
print("Pesan    :", pesan)
