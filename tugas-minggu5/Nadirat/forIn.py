keranjang = [
    {"nama": "Buku tulis", "harga": 5000},
    {"nama": "Pensil", "harga": 2000}
]

total_bayar = 0

for item in keranjang:
    print(f"- {item['nama']}: Rp {item['harga']}")
    total_bayar += item['harga']

print(f"Total bayar: Rp {total_bayar}")