#operasi list
data_angka = [2,4,5,56,3,2]
print(f"data angka {data_angka}")
#cout data angka

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 {jumlah_data_4}")
print(f"jumlah angka 3 {jumlah_data_3}")

#ambil posisi data
data = ["ucup","Otong","Dudung","Ujang"]
idex_dudung = data.index("Dudung")
print(f"index dudung {idex_dudung}")
#mengurutkan data
print(f"data angka sebelum di sort {data_angka}")
data_angka.sort()
print(data_angka)
data.sort()
print(f"data sort = {data}")

#balik list
data_angka.reverse()
data.reverse()
print(f"data-reverse {data_angka}")
print(f"data-reverse {data}")
