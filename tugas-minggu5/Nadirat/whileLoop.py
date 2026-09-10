running = True

while running:
    print("\n--- MENU APLIKASI ---")
    print("1. Jalankan fitur")
    print("2. Keluar")

    pilihan = input("Pilih (1/2): ")
    if pilihan == "1":
        print("Fitur lagi dijalanin")
    elif pilihan == "2":
        print("Terima kasih")
        running = False #Menghentikan loop