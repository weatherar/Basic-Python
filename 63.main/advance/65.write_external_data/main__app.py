## 1. mode write data external = dia akan membuat file baru
## akan menimpa atau overite isinya
with open("65.write_external_data/data_1.txt",'w',encoding ="utf-8") as file:
    file.write("ucucp surucup")
    
## 2. mode append data external = dia akan menambahkan data ke file yang sudah ada
with open("65.write_external_data/data_2.txt",'w',encoding ="utf-8") as file:
    file.write("ucucp surucup\n")
    
with open("65.write_external_data/data_2.txt",'a',encoding ="utf-8") as file:
    file.write("otong surotong\n")

with open("65.write_external_data/data_2.txt",'a',encoding ="utf-8") as file:
    file.write("ini akan tambah lagi")

#mode r+

with open("65.write_external_data/data_3.txt",'w',encoding="utf-8") as file:
    file.write("data ke 3\n")
with open("65.write_external_data/data_3.txt",'r+',encoding = "utf-8") as file:

    file.write("baris-1\n")
    file.write("baris-2\n")
    file.write("baris-3\n")
    
with open("65.write_external_data/data_3.txt",'r+',encoding = "utf-8") as file:
    data =file.read()
    print(data)
with open("65.write_external_data/data_3.txt",'r+',encoding = "utf-8") as file:
    file.write("overite\n")# menimpa isi  text sesuai dengan panjang data