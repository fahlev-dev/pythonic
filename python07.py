# fungsi zip pada perulangan for loop

nim = ['001', '002', '003']
nama = ['bejo', 'karti', 'tejo']
hobi = ['makan', 'nyanyi', 'tidur']

for data_nim, data_nama, data_hobi in zip(nim, nama, hobi):
    print(f'{data_nim}--{data_nama}--{data_hobi}')