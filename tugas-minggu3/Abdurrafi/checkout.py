print("=" * 50)
print("SMART E-COMMERCE CHECKOUT")
print("=" * 50)

total_belanja = int(input("Masukkan Total Belanja (Rp) : "))
member = input("Apakah Anda Member? (Ya/Tidak) : ").lower()
jarak = float(input("Masukkan Jarak Pengiriman (km) : "))

if member == "ya" and total_belanja >= 500000:
    diskon = 20
elif member == "ya" or total_belanja >= 300000:
    diskon = 10
else:
    diskon = 0

jumlah_diskon = total_belanja * diskon / 100
belanja_setelah_diskon = total_belanja - jumlah_diskon

if belanja_setelah_diskon >= 200000 and jarak <= 10:
    ongkir = 0
else:
    ongkir = jarak * 3000

total_bayar = belanja_setelah_diskon + ongkir

print("=" * 50)
print("STRUK CHECKOUT")
print("=" * 50)

print(f"Total Belanja          : Rp{total_belanja:,.0f}")
print(f"Status Member          : {member}")
print(f"Diskon                 : {diskon}%")
print(f"Jumlah Diskon          : Rp{jumlah_diskon:,.0f}")
print(f"Belanja Setelah Diskon : Rp{belanja_setelah_diskon:,.0f}")
print(f"Jarak Pengiriman       : {jarak} km")
print(f"Ongkir                 : Rp{ongkir:,.0f}")
print("-" * 50)
print(f"Total Bayar            : Rp{total_bayar:,.0f}")
print("=" * 50)