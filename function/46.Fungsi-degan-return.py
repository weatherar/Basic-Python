#fungsi dengan kemballian

# template fungsi dengan kembalina
#def nama_fungso (argument):
#   BADAN FUNGSI
#   return output

#fyngsi kuadrad

def kuadrad(input_angka):
    output_kuadrad = input_angka**2
    return output_kuadrad
    
y = kuadrad(5)
print(y)

print(kuadrad(55))

z = 10 + kuadrad(7)
print(z)

#fungsi fungsi_tambah
def fungsi_tambah(angka1, angka2):
    return angka1 + angka2

a = fungsi_tambah(3,4)
print(a)

#fungsi dengan return banyak

def operasi_matematika(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 = angka2
    kali = angka1*angka2
    bagi = angka1/angka2
    
    return tambah, kurang, kali, bagi

k,l,m,n = operasi_matematika(9,5)
print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")