#latihan perulangan memb=uat segitiga

#1. menggunakan for
sisi = 10
#dumy variable
count =1
print("awal dari for")
for i in range(sisi):
    print("*"*count)
    count +=1
    
print("AKHIR dari for")
    
#2. Menggunakan while
print("awal dari WHILE")
count = 1
while True:
    print("*"*count)
    count+=1

    if count>sisi:
        break
print("AKHIR dari WHILE")

 #3. hanya ganjil saja
print("awal dari WHILE")
count = 1
while True:
    #akan kembali ke atas jika ganjil
    if count %2:
        print("*"*count)
        count+=1
    #akan print jika ganjil
    else:
        count +=1
        continue
    #akan berhenti jika count melebihi sisi
    if count>sisi:
        break
print("AKHIR dari WHILE")

tes = 11
testing = tes%2 
print(testing)

 #4. hanya ganjil saja
print("awal dari WHILE")
count = 1
spasi = int(sisi/2)
while True:
    #akan kembali ke atas jika ganjil
    if count %2:
        print(" "*spasi , "+" *count)
        spasi-=1
        count+=1
    #akan print jika ganjil
    else:
       
        count +=1
        continue
    #akan berhenti jika count melebihi sisi
    if count>sisi:
        break
    
count = 11
spasi = 0
while True:
    #akan kembali ke atas jika ganjil
    if count %2:
        print(" "*spasi , "+" *count)
        spasi+=1
        count-=1
    #akan print jika ganjil
    else:
       
        count -=1
        continue
    #akan berhenti jika count melebihi sisi
    if count<1:
        break
    




print("AKHIR dari WHILE")

tes = 1
testing = tes%1
print(testing)
