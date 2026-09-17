def hitung_rugi(harga):
    print (harga *  0.1)

def hitung_diskon(harga):
    return harga *0.1

def hitung_total_harga (harga_satuan, jumlah):
    total = harga_satuan *jumlah
    return total

tagihan_budi = hitung_total_harga(15000, 3)

ongkir = 10000

grand_total = tagihan_budi + ongkir


print(f"subtotal : Rp {tagihan_budi:,}")
print(f"Grand Total (+ongkir) : Rp {grand_total:,}")