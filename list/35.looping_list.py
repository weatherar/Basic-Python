#looping dari list

#for loop
print("ini adalah for loop")
kumpulan_angka = [2,3,4,3,2,1]
for angka in kumpulan_angka:
    print(f"angka = {angka}")
    
peserta = ["ucupl","nana","dadang"]
for nama in peserta:
    print(f"nama = {nama}")

#for loop and range
print("ini adalah for loop  and range")
kumpulan_angka = [1,2,3,4,5,6,3]
panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"kumpulan angka = {kumpulan_angka[i]}")
    
#while
print("\nini adalah while")
kumpulan_angka = [1,2,3,4,5,6,3]
panjang = len(kumpulan_angka)

i = 0
while i < panjang:
    print(f"ini while = {kumpulan_angka[i]}")
    i+= 1
    
#list comprehension
data = ["ucup",1,"otong"]
[print(f"data = {i}") for i in data]

#membuat list kuadrad
angka = [34,54,34,54]
angka_kuadrad = [i**2 for i in angka]
print(angka_kuadrad)
# enumerate

print("\n enumerate")
data_list = ["ucup",1,"otong"]
for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")
