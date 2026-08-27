print("SMART E-COMMERCE")

belanja = int(input("Total belanja: Rp "))
member = input("Member (ya/tidak): ")
jarak = float(input("Jarak pengiriman (km): "))

if member == "ya" and belanja >= 500000:
    diskon = belanja * 20 / 100
elif member == "ya" or belanja >= 300000:
    diskon = belanja * 10 / 100
else:
    diskon = 0

setelah_diskon = belanja - diskon

if setelah_diskon >= 200000 and jarak <= 10:
    ongkir = 0
else:
    ongkir = jarak * 3000

total = setelah_diskon + ongkir

print()
print("=== HASIL ===")
print("Belanja       : Rp", int(belanja))
print("Diskon        : Rp", int(diskon))
print("Setelah diskon: Rp", int(setelah_diskon))
print("Ongkir        : Rp", int(ongkir))
print("Total bayar   : Rp", int(total))