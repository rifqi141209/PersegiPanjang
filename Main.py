#meminta input panjang dan panjang dari penguna
panjang = float(input("masukan panjang persegi panjang : "))
lebar = float(input("masukan lebar persgi panjang: "))

#menghitung luas 
luas = panjang * lebar

#mengitung keliling 
keliling = 2 * (panjang + lebar)

#menampulkan hasil luas dan keliling 
print (f"luas persegi panjang adalah: {luas} satuan persegi")
print (f"keliling persegi panjang dalah: {keliling} satuan")