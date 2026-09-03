# input
nilaikehadiran = float(input("Masukkan nilai kehadiran: "))
nilaisikap = input("Masukkan nilai sikap (A/B/C/D): ")
projek = int(input("Masukkan projek yang sudah dikerjakan: "))

# konversi
persen = (nilaikehadiran / 100) * 100

# validasi
if (nilaikehadiran >= 85 and (nilaisikap == "A" or nilaisikap == "B") and projek >= 5):
    print("Anda magang di BUMN")

elif (nilaikehadiran >= 85 and (nilaisikap == "A" or nilaisikap == "B") and projek in (3, 4)):
    print("Anda magang di toko kelontong")

else: 
    pesan_error = "ga layak magang."
    if nilaikehadiran < 85:
        pesan_error += " kehadiran wajib 85"
    if nilaisikap not in ("A", "B"):
        pesan_error += " dan nilai sikap A/B" if nilaikehadiran < 85 else " nilai sikap A/B"
    print(pesan_error)

# output
print(f"Nilai kehadiran anda : {nilaikehadiran}")
print(f"Nilai sikap anda     : {nilaisikap}")
print(f"Jumlah projek anda   : {projek}")
print(f"Persentase kehadiran anda : {persen}%")