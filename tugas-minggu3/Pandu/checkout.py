print("=== SMART E_COMMERCE CALCULATOR ===")
total_belanja = int(input("Total Belanja : "))
member = input("Apakah kamu seorang member? : ")
jarak = int(input("Jarak Rumah Kamu (Km) : "))

if member == "Ya" and total_belanja >= 500000 :
    diskon = total_belanja * 0.2
elif member == "Ya" or total_belanja >= 300000 :
    diskon = total_belanja * 0.1
else :
    diskon = 0

after_diskon = total_belanja - diskon

if after_diskon >= 200000 and jarak <= 10 :
    ongkir = 0
else :
    ongkir = 3000 * jarak

print(f"Harga Awal : {total_belanja}")
print(f"Diskon : {int(diskon)}")
print(f"Harga Setelah Diskon : {int(after_diskon)}")
print(f"Ongkir : {ongkir}")
print("Terimakasih sudah berbelanja!")
