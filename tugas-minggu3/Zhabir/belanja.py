print("=" * 50)
print("         SMART E-COMMERCE CHECKOUT")
print("=" * 50)

Total_belanja = int(input("Total Belanja (Rp) : "))
Status_member = input("Status Member (ya/tidak) : ").strip().lower()
jarak_pengiriman = int(input("Jarak Pengiriman (km) : "))

if Status_member == "ya" and Total_belanja >= 500000:
    diskon_persen = 20
elif Status_member == "ya" or Total_belanja >= 300000:
    diskon_persen = 10
else:
    diskon_persen = 0

nominal_diskon = Total_belanja * (diskon_persen / 100)
belanja_setelah_diskon = Total_belanja - nominal_diskon

if belanja_setelah_diskon >= 200000 and jarak_pengiriman <= 10:
    ongkir = 0
else:
    ongkir = jarak_pengiriman * 3000
    total_bayar = belanja_setelah_diskon + ongkir

print("\n" + "=" * 50)
print("HASIL CHECKOUT")
print("=" * 50)
print(f"Total Belanja       : Rp{Total_belanja:,.0f}")
print(f"Diskon              : {diskon_persen}%")
print(f"Nominal Diskon      : Rp{nominal_diskon:,.0f}")
print(f"Setelah Diskon      : Rp{belanja_setelah_diskon:,.0f}")
print(f"Ongkir              : Rp{ongkir:,.0f}")
print(f"Total Bayar         : Rp{total_bayar:,.0f}")
print("=" * 50)
