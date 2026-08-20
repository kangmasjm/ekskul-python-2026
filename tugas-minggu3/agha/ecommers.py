bayar = int(input("Masukkan Jumlah Total Bayar : "))
status = input("Member Atau Bukan (Ya/Tidak) : ").upper()
jarak = int(input("Masukkan Jarak Tempuh KM : "))

if bayar >= 500000 and status == "YA":
    diskon = 0.2 * bayar
    bayar_setelah_diskon = bayar - diskon
    print(f"diskon didapat : {diskon}")
    print(f"Total Bayar Setelah Diskon : {bayar_setelah_diskon}")

elif bayar >= 300000 or status == "YA":
    diskon = 0.1 * bayar
    bayar_setelah_diskon= bayar - diskon
    print(f"diskon didapat : {diskon}")
    print(f"Total Bayar Setelah Diskon : {bayar_setelah_diskon}")

else:
    print(f"Total Bayar : {bayar} Tidak Dapat Diskon")

if jarak >= 10 and bayar_setelah_diskon >= 200000:
    ongkir = 0000
    print(f"Ongkir : {ongkir} !Gratis")
    total_bayar = bayar_setelah_diskon + ongkir
    print(f"Total Bayar : {total_bayar}")
    
else:
    ongkir = 3000
    print(f"Ongkir {ongkir}")
    total_bayar = bayar_setelah_diskon + ongkir
    print(f"Total Bayar : {total_bayar}")

    


