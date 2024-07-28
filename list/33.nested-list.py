#nested list
data_0 = [1,2]
data_1 = [3,4]

dara_list_biasa = [2,3,4]
list2D = [data_0,data_1,3,4]
print(f"list 2D = {list2D}")

#contoh penggunaan
peserta_0 = ["umur", 24, "laki2"]
peserta_1 = ["umur", 25, "perempuan"]
peserta_2 = ["umur", 23, "laki2"]

list_peserta = [peserta_0,peserta_1,peserta_2]
for peserta in list_peserta:
    print(f"nama \t :{peserta[0]}")
    print(f"umur \t :{peserta[1]}")
    print(f"gender \t :{peserta[2]}")
    
#permasalahn denga reference
list_copy = list_peserta.copy();
print(f"peserta = {list_copy}")
peserta_0[0]= "michel"

print(list_copy)
print(list_peserta)