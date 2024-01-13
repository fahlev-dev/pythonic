# fungsi zip untuk menyatukan sekumpulan list di python

nim = ['001', '002', '003']
nama = ['bejo', 'karti', 'tejo']
ipk = [3.25, 2.33, 1.88]
siswa = list(zip(nim, nama, ipk))
    
print(f'siswa: {siswa}')