def f_kuadrat (angka):
    return angka**2
print(f"hasil kuadrat {f_kuadrat(3)}")

# kita coba dengan lamda 
# output = lamda argument : expresion  

kuadrat = lambda angka: angka**2
print(f"hasil lamnda kuadrad  = {kuadrat(5)}")

pangkat = lambda num, pow : num*pow
print(f"hasil lamda pangkat - {pangkat(4,2)}")

# kegunaan 
# shorting untuk list biasa
data_list= ["otong", "ucup", 'asep']
data_list.sort()
print(f"sorted list = {data_list}")

# shorting untuk list pakai panjang
def panjang_nama (nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"sorted list by len = {data_list}")

# short pakai lambda 
data_list= ["otong", "ucup", 'asefp']
data_list.sort(key= lambda nama : len(nama))
print(f"sorted list by lambda = {data_list}")

# filter 
data_angka = [1,2,3,4,56,7,88]
def kurang_dari_lima(angka):
    return angka <5
data_angka_baru = list(filter(kurang_dari_lima,data_angka))
data_angka_baru = list(filter(lambda x:x<5, data_angka))
print(data_angka_baru)

# kasus genap 
data_genap = list(filter(lambda x:(x%2 == 0), data_angka))
print(data_genap)
# kasus ganjil
data_ganjil = list(filter(lambda x: (x%2 != 0), data_angka))
print(data_ganjil)
# kasus kelipatan 3\
data_3 = list(filter(lambda x: (x%3 == 0), data_angka))
print(data_3)

# anoniymous function 
# currying <- Haskell curry 

def pankat (angka , n):
    hasil = angka**n
    return hasil

data_hasil = pangkat (5,4)
print(data_hasil)

#  dengan currying 
def pangkat(n):
    return lambda angka : angka**n

pangkat2 = pangkat(2)
print(f"pamgkat2 = {pangkat2(5)}")

pangkat3 = pangkat (3)
print(f"pamgkat3 = {pangkat3(3)}")
print(f"pamgkat bebas = {pangkat(4)(2)}")
