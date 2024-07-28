#latihan operator logika
#---0+++5--- 8+++11---
#9,10
#+++0---5+++8---11+++

#range nol - 11, lenih dari 5, . (6,7) tidak termasuk. lebih dari 8, kuranga dari 11
#lebih dari nol. lebih dari 5, kurang dari 8, lebih dari 11
# 6,7,12,13,14..
nilai = float(input("Masukan nilai : "))
isNilai1 =(nilai>0)
isNilai2 = (nilai<5)
isNilai3 = (nilai>8)
isNilai4 = (nilai<11)


isCorrect = isNilai1 and isNilai2 or isNilai3 and isNilai4
print(isCorrect)