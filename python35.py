# pengurutan data dengan custom key

def custom_key(nama):
    return nama.split()[-1]

siswa = ["karti susanti", "tejo purnawan", "bejo rahmadi"]

print(f"Sebelum Pengurutan : {siswa}")
terurut = sorted(siswa, key=custom_key)
print(f"Sesudah Terurut Sesuai Nama Belakang : {terurut}")