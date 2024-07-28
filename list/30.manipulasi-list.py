#manipulasi list
#operasi
#index 0           1       2(-1)
data = ["otong","ucup","dudung"]

#mengambil data dari llist
data_0 = data[0]
print(f"data pertama indexc nol = {data_0}")

data_terakhir= data[-1]
print(f"data pertama indexc terakhir = {data_0}")

data_uccup = data [-3]
print(f"daat ucup = {data_uccup}")

#mengambui info jumlah (len)
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

#manipulasi data list
#menambahkan item dalam list sesuai posisi
print(f"data sebelumdi tambah\n{data}")
data.insert(1,"Asep")
print(f"data sesudah di tambah\n{data}")
 #menambah diakhir
data.append("jajang")
print(f"data di tambaha lagi\n {data}")

#menambah lsit
data_baru = ["ujang", "usep","dadang"]
data.extend(data_baru)
print(f"data gabungan \n {data}")

#merubah data
# data ke 3 ganti jadi michael
data[2]="Michel"
print(f"data rubah {data}")

#meremove\
data.remove("ujang")
print(f"daat revome \n {data}")


#remove data paling belakang
data.pop()
print(f"data akhir = \n {data}")