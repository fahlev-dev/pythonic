# fungsi enumerate pada perulangan for loop

nim = ['001', '002', '003']
nama = ['bejo', 'karti', 'tejo']

for i, data_nim in enumerate(nim):
    print(f'{data_nim}--{nama[i]}')

