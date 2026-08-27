print("=== SISTEM SELEKSI KELAYAKAN MAGANG ===")

kehadiran = float(input("Masukkan nilai kehadiran (%): "))
sikap = input("Masukkan nilai sikap (A/B/C/D): ").upper()
project = int(input("Masukkan jumlah project selesai: "))

if kehadiran >= 85 and sikap in ["A", "B"] and project >= 3:
    status = "LOLOS"

    if project >= 5:
        kategori = "Magang Tier 1 (BUMN/Unicorn)"
    else:
        kategori = "Magang Tier 2 (Startup/Industri Lokal)"

    evaluasi = "Seluruh persyaratan magang telah terpenuhi."

else:
    status = "BELUM LAYAK MAGANG"
    kategori = "Wajib remedial"

    if kehadiran < 85:
        evaluasi = "Kehadiran belum memenuhi minimal 85%."
    elif sikap not in ["A", "B"]:
        evaluasi = "Nilai sikap belum memenuhi standar minimal B."
    elif project < 3:
        evaluasi = "Jumlah project belum mencapai minimal 3."

print("\n=== HASIL SELEKSI ===")
print("Status    :", status)
print("Kategori  :", kategori)
print("Evaluasi  :", evaluasi)