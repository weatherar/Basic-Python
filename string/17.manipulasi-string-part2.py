#operator dalam bentuk methods
## merubah case dari string

# merubah semua ke UPPERCASE
salam = ' bro'
print('normal = ' + salam   )
salam = salam.upper()
print('normal = ' + salam   )

# merubah semua ke Lower
alay = " aKu KeCe Abiess"
print('normal :' + alay)
alay = alay.lower()
print('normal :' + alay)

#pecekan dengan isX method
# contoh untuk pengecekan lower case
salam = "sisi"
apakah_lower = salam.islower() #hasilnya bool
print(salam + 'islower = '+ str(apakah_lower))
apakah_upper= salam.isupper()
print(salam + 'isupper = '+ str(apakah_upper))

#isalpha() untuk mengecek semuanya huruf
#isalnum() untuk huruf dan angka
#isdecimal() angka saja
#isspace () spasi, tab, newline \n
#istitle(l semua kata dimulai dengan huruf besar)

judul = "It's Okay Not To Be Orkay"
cek_judul = judul.istitle() #boolean
print(judul + 'is title = '+ str(cek_judul))

