#continue
#past
#past >> berfungsi sebagai dumy tidak akan di eksekusi
# angka = 0 
# while angka < 5:
#     angka += 1
#     if angka ==3:
#         pass #tidak akan di eksekusi
#     print(angka)

#continue
angka = 0
print(f"angka sekaran - > {angka}")

while angka <5:
    angka +=1
    
    print(f"angka sekarang - > {angka}")
    if angka == 3:
        print("nice!")
        continue #membuat loop meloncat ke aksi setelahnya
    print("Watsupp")#dilewat sekali
print("finish")