input = "masukkan nama karyawan     :"
input = "masukkan golongan (A/B/C): "
input = "total jam kerja/minggu : "
input = "rating performa (1-5)"
lembur = jamkerja * 1.5
jamkerja = 40
bonus = 200000

golonganA = 50000
golonganB = 35000
golonganC = 25000

if jamkerja > 40:
    gaji_pokok = golonganA * jamkerja
    gaji_lembur = lembur * (jamkerja - 40)
    gaji_bonus = bonus * rating
    total_gaji = gaji_pokok + gaji_lembur + gaji_bonus

if golongan == "B":
    gaji_pokok = golonganB * jamkerja
    gaji_lembur = lembur * (jamkerja - 40)
    gaji_bonus = bonus * rating
    total_gaji = gaji_pokok + gaji_lembur + gaji_bonus

if golongan == "C":
    gaji_pokok = golonganC * jamkerja
    gaji_lembur = lembur * (jamkerja - 40)
    gaji_bonus = bonus * rating
    total_gaji = gaji_pokok + gaji_lembur + gaji_bonus





print(f"gaji pokok : {gaji_pokok}, {jamkerja} jam : ")
print(f"gaji lembur : {gaji_lembur}")
print(f"gaji bonus : {gaji_bonus}")
print(f"total gaji : {total_gaji}")

