# print("Setup Python Berhasil!")

# #A. Cetak Teks (print)
# #Fungsi print() digunakan untuk menampilkan keluaran ke layar.
# print("Selamat Datang di Ekstrakulikuler Python!")


#B. Menerima Input (input) & Variabel
#Variabel digunakan untuk menyimpan data. 
#Fungsi input() mengambil masukan dalam bentuk string.
nama = input("Masukkan nama kamu: ")
jurusan = input("Masukkan jurusan kamu: ")
print("Selamat datang di Ekstrakulikuler Python, " + nama + " dari jurusan " + jurusan + "!")

#C. F-String (Formatted String Literals)
#Cara modern, rapi, dan standar industri untuk menggabungkan variabel ke dalam teks.
print(f"Selamat datang di Ekstrakulikuler Python, {nama} dari jurusan {jurusan}!")