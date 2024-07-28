# import 
# fungsinya adalah mengambil programn dari file extrnal py 

# 1. untuk import program 
import program_print
import program_siucup

# 2. import dengan data 
import variable

# data ada di namaspace variable 
print(variable.data)

# 3. import dengan fungsi 
import introduction.function.matematika as matematika

hasil = matematika.tambah(4,5)
print(hasil)