# memadukan list comprehension dan fungsi zip pada bahasa python

nama = ['bejo', 'karti', 'tejo']
usia = [23, 31, 26]
listku = [[data_nama, data_usia] for data_nama, data_usia in zip(nama, usia)]

print(f'listku:{listku}')