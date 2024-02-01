# melakukan unpacking argument pada pemanggilan fungsi dalam bahasa pemrograman python

def jumlahkan(angka1, angka2):
    return angka1 + angka2

listku = [10, 20]
dictku = {'angka1': 100, 'angka2': 200}

hasil_list = jumlahkan(*listku)
print(f"hasil listku {listku[0]} + {listku[1]} = {hasil_list}")

hasil_dict = jumlahkan(**dictku)
print(f"hasil dictku {dictku['angka1']} + {dictku['angka2']} = {hasil_dict}")