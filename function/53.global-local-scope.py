# global and local scope 
nama_global = "otong" # <- variabel global

# akses variabel global dalam fungsi 
def fungsi1():
    print(f"fungsi menampilkan {nama_global}")
    
fungsi1()
# akses variabel global dalam loop
for i in range (0,5):
    print(f"loop {i} - {nama_global}")
    
# percabangan 
if True:
    print(f"if menampilkan {nama_global}")

## variabel local scope
def fungsi2():
    nama_local = "ucup" #ini adalah var local scope
fungsi2()
# print(nama_local) #tidak bisa di lakukan

# contoh : 1 akses vaiabel
def say_otong():
    print(f"hello {nama}")
    
nama = "otong"
say_otong()

# contoh :2 merubah variabel global 
angka = 0
name = "ucup"
def ubah (nilai_baru, nama_baru):
    global angka #fungsi ini mendapat akses var angka
    global name
    angka = nilai_baru
    name = nama_baru

print(f"sebelum {angka, name}")
ubah(10,"ucupz")
print(f"sesudah {angka, name}")

# contoh : 3 
angka = 0
for i in range (0,5):
    angka += i
    angka_dumy = 0
print(angka)
print(angka_dumy)
    
if True :
    angka = 10
    angka_dumy = 10
print(angka)
print(angka_dumy)