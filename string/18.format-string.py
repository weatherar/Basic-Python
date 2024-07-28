#format string#
#contoh generic
nama = "marline"
format_Str = f"Hello{nama}"
print(format_Str)

#angka
angka = 2002.3
format_Str=f"angka = {angka}"
print(format_Str)

#boolean
boolean = True
format_Str = f"boolean = {boolean}"
print(format_Str)

#bilangan bulat
angka = 1500
format_Str= f"bilangan bulat = {angka:d}"
print(format_Str)

#bilangan eibuan
angaka = 2000
format_Str= f"jutaan = {angaka:,}"
print(format_Str)

#angka desimal
angka = 200.334
format_Str = f"desimal = {angka:01.2f}"
print(format_Str)

#menampilkan tanda - atau +
angka_minus = -20
angka_plus = 10
format_mines = f"ini mines = {angka_minus:d}"
format_plus = f"ini plus = {angka_plus:+2f}"

print(format_mines)
print(format_plus)

#format persen
persentase = 0.34
format_persen= f"format persen = {persentase:.0%}"
print(format_persen)

#melakukan aritmatika dengan placeholder
harga = 225
jumlah = 2
format_Str = f"harga total ={harga*jumlah}"
print(format_Str)

#format angka lain
angka = 332
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)