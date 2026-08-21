print("=" * 50)
print ("        SISTEM SELEKSI KELAYAKAN MAGANG PKL")
print("=" * 50)


kehadiran = int(input("Masukan Persentase kehadiran minimal 85 : "))
nilai_sikap = input("a/b : ").strip().lower()
project = int(input("Masukan jumlah project :"))


if kehadiran > 85:
    print("Kehadiran terpenuhi")
else:
    print("Kehadiran Kurang!")

if project < 3:
    print (f"project hanya {project} Minimal 3!")
else:
    print("Ketentuan terpenuhi")

if kehadiran > 85 and (nilai_sikap == "a" or nilai_sikap == "b") and project >= 5:
    print(f"SELAMAT! Kamu magang di {tier_1}")
elif kehadiran >85 and (nilai_sikap == "a" or nilai_sikap == "b" and project == 3 or project == 4) :
    print(f"SELAMAT! kamu magang di {tier_2}")
else:
    print("Belum layak magang (Wajib Remedial)")
