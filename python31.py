# mengenal else pada perulangan for loop

kecepatan = [60, 40, 80, 60, 90, 30, 110, 20]
ambang_batas = 100

for laju in kecepatan:
    if laju > ambang_batas:
        print("Kecepatan melampaui batas normal")
        break
else:
    print("Laju kendaraan normal")