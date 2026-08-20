print("SMART E-COMMERCE")

total_belanja = int(input("Total belanja: Rp "))
status_member = input("Member (ya/tidak): ")
jarak_kirim = float(input("Jarak pengiriman (km): "))

if status_member == "ya" and total_belanja >= 500000:
    potongan_harga = total_belanja * 20 / 100
elif status_member == "ya" or total_belanja >= 300000:
    potongan_harga = total_belanja * 10 / 100
else:
    potongan_harga = 0

harga_setelah_diskon = total_belanja - potongan_harga

if harga_setelah_diskon >= 200000 and jarak_kirim <= 10:
    biaya_ongkir = 0
else:
    biaya_ongkir = jarak_kirim * 3000
total_pembayaran = harga_setelah_diskon + biaya_ongkir

print()
print("=== HASIL ===")

print("Belanja        : Rp", int(total_belanja))
print("Diskon         : Rp", int(potongan_harga))
print("Setelah diskon : Rp", int(harga_setelah_diskon))
print("Ongkir         : Rp", int(biaya_ongkir))
print("Total bayar    : Rp", int(total_pembayaran))
