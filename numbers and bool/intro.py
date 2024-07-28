# name = input('masukan nama anda : ')
# print(name)

#mengkompile pyhton dengan yang namanya bytecode
#variable tempat menyimpan data
#Asiggment nilai

a=10
x=5
panjang = 100

print("nilai a = ", a)
print("nilai x = ", x)
print("nilai panjang = ", panjang)

#Tipe data => 1. integer
print("data", a, "bertipe", type(a))

#Tipe data => 2. Float
data_float = 1.4
print("type : ", type(data_float))

#Tipe data => 3. String
data_bool = True
print("type : ", type(data_bool))

#Tipe data => 4. Boolean
data_string = "aira"
print("type : ", type(data_string))

#type data complex
data_complex = complex(5,6)
print("data complex : ",data_complex, type(data_complex))

#type data dari bahasa C

from ctypes import c_double
data_c_double = c_double(10.5)
print("data c double : ",data_c_double, type(data_c_double))

