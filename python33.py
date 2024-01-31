# mengenal tabel translasi untuk string mapping pada python

sumber = "aieo"
tujuan = "4130"
string_input = "kota cirebon"
tabel_translasi = str.maketrans(sumber, tujuan)
string_output = string_input.translate(tabel_translasi)

print(f"Hasil konversi: {string_output}")