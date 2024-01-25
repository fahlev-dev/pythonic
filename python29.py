# menyatukan dictionary

data1 = {'nim':'001', 'nama':'bejo'}
data2 = {'ipk':3.25, 'semester':4}
data3 = {'kota': 'Bandung', 'hobi': 'membaca'}
siswa = {**data1, **data2, **data3}


print(f"data siswa {siswa}")