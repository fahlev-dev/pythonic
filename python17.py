# pemanggilan fungsi berantai (chained function call) di python

def tambah(a, b): # fungsi tambah
    return a + b

def kali(a, b): #fungsi kali
    return a * b

x, y = 10, 20 # nilai untuk parameter
kondisi = False # kondisi untuk pengecekan

hasil = (tambah if kondisi else kali)(x, y) #masukan parameter untuk masukan datanya
    
print(f'hasil = {hasil}') # hasil yang akan di jalankan tergantung kondisi yang di cek di awal operasi