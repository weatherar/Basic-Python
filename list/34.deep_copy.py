#Deep Copy Nested list
data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0,data_1,3]
data_2D_copy = data_2D.copy()
print(f"data = {data_2D}")

#mengambil
data = data_2D[0][1]
print(f"data {data}")

#adreess semuanya
print(f"data 2d = {hex(id(data_2D[0]))}")
print(f"data 2d = {hex(id(data_2D_copy[0]))}")

data_2D [1][0] = 5
data_2D [2] = 9
print(f"data = {data_2D}")
print(f"data = {data_2D_copy}")

#kita gunakan deepcopy
from copy import deepcopy

data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"address asli = {hex(id(data_2D))}")
print(f"address deepcopy = {hex(id(data_2D_deepcopy))}")

print("adrees dari member ke -1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address deepcopy = {hex(id(data_2D_deepcopy[0]))}")

data_2D[1][0] = 30
print(f"data = {data_2D}")
print(f"data = {data_2D_copy}")
print(f"data = {data_2D_deepcopy}")
