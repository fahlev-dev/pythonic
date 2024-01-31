# pengurutan data dengan method sort

siswa = ["karti susanti", "tejo purnawan", "bejo rahmadi"]
print(f"Sebelum {siswa}")
# siswa.sort() # method sort dapat di gunakan dengan tipe data yang mutable, kalo yang imuttable tidak bisa
terurut = sorted(siswa) # menggunakan method sorted() dengan menghasilkan objek baru, bisa di gunakan pada semua tipe data di manapun
print(f"Sesudah {terurut}")

