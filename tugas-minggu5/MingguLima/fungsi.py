def hitung_diskon(total_belanja, persen_diskon = 0.1):
    nominal_diskon = total_belanja * persen_diskon
    return nominal_diskon

diskon1 = hitung_diskon(100000)
diskon2 = hitung_diskon(200000, 0.2)

print(f"Diskon 1 : Rp {diskon1:,.0f}")
print(f"Diskon 2 : Rp {diskon2:,.0f}")