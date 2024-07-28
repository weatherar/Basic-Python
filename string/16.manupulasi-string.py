# operasi dan manupulasi string

#1. menymabung string (concatenate)
namaPertama =  "Ucup"
namaTengah = "D"
namaAkhir = "fame"

nama_lengkap= namaPertama+ " " + namaTengah  + "'" + namaAkhir
print(namaPertama) 

#2. menghitung (lenght)
panjang = len(nama_lengkap)
print('panjang dari' + nama_lengkap+ ' =' + str(panjang))

#3. operator untuk string(in)
#mengecek apakah ada komponen char atau string dalam string
d = 'd'
status = d in nama_lengkap
print(d + " ada di" + nama_lengkap + " = " + str(status))

D = 'D'
status = D in nama_lengkap
print(D + " ada di" + nama_lengkap + " = " + str(status))
# not in
d = 'd'
status = d not in nama_lengkap
print(d + " ada di" + nama_lengkap + " = " + str(status))

#mengulang string
print('wk'*10)
print(3*'wk')

#indexing
print('index ke - 0 :' + nama_lengkap[0])
print('index ke - 0 :' + nama_lengkap[2])
print('index ke - (-1) :' + nama_lengkap[-1])
print('indez ke [0,3] :' + nama_lengkap[0:4])
print('indez ke [0,2,4,6,8,10] :' + nama_lengkap[0:11:2])

#item paling kecil
print('paling kecil :' + min(nama_lengkap))
#item paling besar
print('paling besar :' + max(nama_lengkap))

ascii_code = ord(" ")
print('ASCII code untuk spasi adalah' + str(ascii_code))
data = 177
print("char untuk ASCII 117 adalah"+ chr(data))

#4. operator dalam method
data = "otong surotong pararotong"
jumlah = data.count("o")
print( 'jumlah "o" pada data = ' + data + 'adalah ' + str(jumlah ))