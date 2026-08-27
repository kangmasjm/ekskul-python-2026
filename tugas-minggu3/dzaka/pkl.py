print("=== Sistem Seleksi Kelayakan Magang / PKL ===")

kehadiran = float(input("Masukkan Nilai Kehadiran (%) [Contoh: 90]: "))
sikap = input("Masukkan Nilai Sikap (A/B/C/D): ").upper() # .upper() memastikan huruf besar
project = int(input("Masukkan Jumlah Project Selesai (Angka): "))

syarat_kehadiran = kehadiran >= 85
syarat_sikap = (sikap == 'A' or sikap == 'B')
syarat_project = project >= 3

print("\n--- Status Kelayakan ---")
if syarat_kehadiran and syarat_sikap and syarat_project:
    if project >= 5:
        print("Selamat! Anda lolos ke: Magang di Perusahaan Tier-1 (BUMN/Unicorn)")
    else:
        print("Selamat! Anda lolos ke: Magang di Perusahaan Tier-2 (Startup/Local Industry)")
else:
    print("Mohon maaf, Anda: Belum Layak Magang (Wajib Remedial)")