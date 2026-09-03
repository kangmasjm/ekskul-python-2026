print("=================================")
print("=== SMART E-COMMERCE CHECKOUT ===")
print("=================================")

totalBelanja = int(input("total belanja (Rp) : "))
statusMember = input("status member (ya/tidak) :").strip().lower()
jarakPengiriman = int(input("jarak pengiriman (km) :"))

if statusMember == "ya" and totalBelanja >= 500000:
    diskon = 20
elif statusMember == "ya" or totalBelanja >= 300000:
    diskon = 10
else:
    diskon = 0

nominal_diskon = totalBelanja * (diskon / 100)
belanjaSetelahDiskon = totalBelanja - nominal_diskon

if belanjaSetelahDiskon >= 200000 and jarakPengiriman <= 10:
    ongkir = 0
else:
    ongkir = jarakPengiriman * 3000

semuaTotal = belanjaSetelahDiskon + ongkir

print("\n=== Rincian Belanja ===")
print(f"total belanja : Rp {totalBelanja}")
print(f"diskon : {diskon}%")
print(f"ongkir : Rp {ongkir}")
print(f"total bayar : Rp {semuaTotal}")