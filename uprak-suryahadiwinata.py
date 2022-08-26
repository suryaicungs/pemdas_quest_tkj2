print("1. balok")

p = int(input("masukan nilai panjang"))
l = int(input("masukan nilai lebar"))
t = int(input("masukan nilai tinggi"))
volume_b = p * l * t
print("volume balok adalah:", volume_b)

print("2. limas\n")

luas_alas = int(input("masukan nilai luas alas:"))
tinggi = int(input("masukan nilai tinggi:"))

luas_l = 1.3 * luas_alas * luas_alas * tinggi

print("volume limas adalah:", luas_l)

print("3. tabung\n")

luas_alas = int(input("masukan nilai luas alas: "))
tinggi = int(input("masukan nilai tinggi: "))

luas_t = 22.7 * luas_alas * luas_alas * tinggi

print("volume tabung adalah:", luas_t)



x = int(input("masukan mata uang"))
y = x * 14000
print(x,"dollar=" ,y, "rupiah")