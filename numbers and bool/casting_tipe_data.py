#belajar casting tipe data
#merubah tupe data ke tipe lain
data_int = 9;
print("data =", data_int, type(data_int) )

#merubah INT ke float
data_float = float(data_int)
print("data =", data_float, type(data_float) )
data_str = str(data_int)
print("data =", data_str, type(data_str) )
data_bool = bool(data_int) #akan false jjika nilai int= 0
print("data =", data_bool, type(data_bool) )

#float akan di bulatkan ke bawah misal 9.9 jadi = 9


#merubah Boolean
data_bool = False
print("data =", data_bool, type(data_bool) )

data_str = str(data_bool)
print("data =", data_str, type(data_str) )

data_int = int(data_bool) #akan false jjika nilai int= 0
print("data =", data_int, type(data_int) )

# merubah string
#string harus angka
#string menjadi false jika stringnya kosong
