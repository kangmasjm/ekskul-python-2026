kehadiran = int(input(f"input nilai kehadiran :" "%"))
sikap = input(f"input nilai sikap A/B/C/D :".upper())
projek = int(input(f"jumlah project selesai :"))

if kehadiran >= 85 and sikap == "A" or sikap == "B" and projek > 4:
    print("magang tier 1 Masuk BUMN")
elif kehadiran >= 85 and sikap == "A" or sikap == "B" and projek <= 4 and projek > 2:
    print("magang tier 2 Masuk Starup/Local")
elif kehadiran <= 85:
    print("tidak lulus nilai kehadiran kurang dari 85%")
elif sikap == "C" or sikap == "D":
    print("tidak lulus perbaiki nilai sikap")
elif projek <= 2:
    print("tidak lulus perbaiki nilai projek")
else:
    print("tidak lulus")

print("=")
        



