#episode latihan loguja dan komparasi
#membuat gabungan area rentang dari angka
#+++3-----10++++
inputUser = float(input('masukan nilai yang bernilai \n kurang dari 3\n lebihdari 10 : '))

# ++++3====
#Memerisa angka kurang dari 3
isKurangDari = (inputUser<3)
print("kurang dari 3 = ", isKurangDari)
#Memerisa angka lebih dari 10
isLebihDari = (inputUser>10)
print("lebih dari 10 = ", isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan : ", isCorrect)

#----3+++10----
#kasus irisan
inputUser = float(input('masukan nilai yang bernilai \n kurang dari 3\n kurang dari 10 : '))
#--3++
#lebih dari 3
isLebihDari = (inputUser>3)
print("lebih dari 10 = ", isLebihDari)

#kurang dari
isKurangDari = (inputUser<10)
print("lebih dari 10 = ", isKurangDari)

isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukan : ", isCorrect)
