# menukar nilai antar variabel

a, b = 10, 20
print('sebelum pertukaran')
print(f'a={a}, b={b}')

a, b = b, a
print('setelah pertukaran')
print(f'a={a}, b={b}')

print('====================')

a, b, c, d, e = 10, 20, 30, 40, 50

print('sebelum pertukaran')
print(f'a={a}, b={b}, c={c}, d={d}, e={e}')

a, b, c, d, e = c, e, d, a, b

print('setelah pertukaran')
print(f'a={a}, b={b}, c={c}, d={d}, e={e}')