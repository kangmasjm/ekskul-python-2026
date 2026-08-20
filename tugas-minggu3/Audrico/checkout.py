totalbelanja = int(input("Masukan total belanja kamuuuu : "))
status = str(input("Apakah kamu seorang member (Ya/Tidak) : "))
jarak = int(input("Jarak rumah kamuuu (KM) : "))
diskon = 0
total = 0
harga = jarak * 3000

if status == "Ya" and totalbelanja >= 500000:
    diskon = totalbelanja * 0.2
    total = totalbelanja - diskon
    print(f"Total belanja kamu adalah = {int(total)}")
elif status == "Ya" or totalbelanja >= 300000:
    diskon = totalbelanja * 0.1
    total = totalbelanja - diskon
    print(f"Total belanja kamu adalah = {int(total)}")
else:
    print(f"Total belanja kamu adalah = {int(total)}")

if total >= 200000 and jarak <= 10:
    print("Harga ongkir = GRATISSS")
else:
    print(f" ongkir kamu = {int(harga)}")
    
