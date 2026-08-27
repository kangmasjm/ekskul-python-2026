print("=== Smart E-Commerce Checkout & Fast-Shipping Calculator ===")


total_belanja = float(input("Masukkan Total Belanja (Rp): "))
status_member_input = input("Apakah Anda Member? (Ya/Tidak): ").strip().lower()
jarak_pengiriman = float(input("Masukkan Jarak Pengiriman (km): "))


is_member = (status_member_input == 'ya')

diskon_persen = 0.0

if is_member and total_belanja >= 500000:
    diskon_persen = 0.20  
elif is_member or total_belanja >= 300000:
    diskon_persen = 0.10 
else:
    diskon_persen = 0.0   

nominal_diskon = total_belanja * diskon_persen
total_setelah_diskon = total_belanja - nominal_diskon

ongkir = 0

if total_setelah_diskon >= 200000 and jarak_pengiriman <= 10:
    ongkir = 0 
else:
    ongkir = jarak_pengiriman * 3000  # Rp 3.000 / km

total_bayar = total_setelah_diskon + ongkir

print("\n--- Rincian Pembayaran ---")
print(f"Total Belanja Awal  : Rp {total_belanja:,.0f}")
print(f"Diskon Didapat      : {int(diskon_persen * 100)}% (Rp {nominal_diskon:,.0f})")
print(f"Total Setelah Diskon: Rp {total_setelah_diskon:,.0f}")
print(f"Biaya Pengiriman    : Rp {ongkir:,.0f}")
print(f"---------------------------------- +")
print(f"TOTAL YANG DIBAYAR  : Rp {total_bayar:,.0f}")