print("=" * 40)
print("=== SMART E-COMMERCE CHECKOUT & FAST-SHIPPING ===")
print("=" * 40)

total_belanja = int(input("Total Belanja : "))
member = input("Status Member : ")
jarak = int(input("Jarak Pengiriman : "))

if member == "Ya" and total_belanja >= 500000:
    diskon = total_belanja * 0.2
elif member == "Ya" or total_belanja >= 300000:
    diskon = total_belanja * 0.1
else:
    diskon = 0

after_diskon = total_belanja - diskon

if after_diskon >= 200000 and jarak <= 10:
    ongkir = 0
else:
    ongkir = 3000 * jarak

print("=" * 40)
print(f"Diskon : Rp{diskon}")
print(f"Ongkir : Rp{ongkir}")
print(f"Total  : Rp{after_diskon + ongkir}")
print("Terimakasih sudah berbelanja!")
