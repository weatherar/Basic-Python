#copy list
 #tehnik menduplikat list
data= ["ucup","otaong", "Dudung"]
print(f"a={data}")

b= data
print(f"b = {b}")

#kita akan merubah member
data[1]="Michel"
b.sort()
print(f"a={data}")
print(f"b = {b}")

#adrees je dua a dan b
print(f"adrees a = {hex(id(data))}")
print(f"adrees a = {hex(id(b))}")

#menduplikat denagn copy
print("membuat list c dengan a.copy")
c=data.copy()
print(f"adrees copy c {hex(id(c))}")
print(f"adrees  c {hex(id(data))}")
print(f"data = {data}")
print(f"data = {b}")
print(f"data = {c}")

c[0]="dadang"

print(f"data = {data}")
print(f"data = {b}")
print(f"data = {c}")