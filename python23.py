# membuat fungsi dengan sekumpulan nilai kembalian (multiple return values) di python

def fungsiku():
    nim = '007'
    nama = 'Asep'
    ipk = 1.25
    return nim, nama, ipk

a, b, c = fungsiku()
print(f'a: {a}')
print(f'b: {b}')
print(f'c: {c}')