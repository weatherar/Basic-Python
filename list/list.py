## ===LIST====
#kunpulan data nubers
data_angka = [1,2,3]
print(data_angka)
#kumpulan data string
data_string = ["ucup","otong","odah"]
print(data_string)

#kumpulan data bool
data_bool = [True, False]
print(data_bool)

#kumpulan data campuran
campuran = [True, "uxux",2]

#cara alternatif
data_range = range(0,10,2) #ra nge start-stop-step
print(data_range)
data_list = list(data_range)
print(data_list)

#membuar kist denga loop, list comprehension
list_pake_for = [i**3 for i in range(0,10)]
print(list_pake_for)

#membuata list pjke for pke if
list_pake_for_if = [i for i in range(0,10) if i !=5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 == 0]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 != 0]
print(list_pake_for_if)