# belajar fungsi unzip di python

siswa = [
    ('001', 'bejo', 3.25),
    ('002', 'karti', 2.33),
    ('003', 'tejo', 1.88),
]

nim, nama, ipk = zip(*siswa)

print(f'nim: {nim}')
print(f'nama: {nama}')
print(f'ipk: {ipk}')
