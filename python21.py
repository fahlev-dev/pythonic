# mengabaikan nilai dengan underscore

# for _ in range(3):
#     print('Pemrograman dasar')

listku = [10, 20, 30, 40, 50]
a, b, *_ = listku

print(f'listku: {listku}')
print(f'a:{a} dan b:{b}')