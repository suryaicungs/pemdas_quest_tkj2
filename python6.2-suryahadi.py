print("1. persegi/n")

sisi = int(input("masukan nilai sisi: "))
luas_p = sisi * sisi
print("luas persegi adalah", luas_p)

print("2. persegi panjang")

panjang = int(input("masukan nilai panjang: "))
lebar = int(input("masukan nilai lebar"))
luas_pp = panjang * lebar
print("luas persegi panjang adalah:", luas_pp)

print("3. segitiga")

alas = int(input("masukan nilai alas: "))
tinggi = int(input("masukan nilai tinggi: "))
luas_s = alas * tinggi / 2
print("luas segitiga adalah:", luas_s)

print("4. jajar genjang")

alas = int(input("masukan nilai alas: "))
tinggi = int(input("masukan nilai tinggi: "))
luas_jg = alas * tinggi
print("luas jajar genjang adalah:", luas_jg)

print("5. lingkaran")

Phi = 3.14
r = int(input("masukan nilai panjang jari-jari lingkaran: "))
luas_l = Phi * r * r
print("luas lingkaran adalah:", luas_l)


