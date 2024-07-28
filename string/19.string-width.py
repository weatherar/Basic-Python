#widht and multiline
#data
data_nama = "ucup surucup"
data_umur = 17
data_tinggi = 180
data_nomer_sepatu =44

#string standart
data_string = f"nama {data_nama},umur = {data_umur}, tinggi = {data_tinggi}, nomer sepatu = {data_nomer_sepatu}"
print(5*'='+"Data string"+5*'=')
print(data_string)

#string mengatur lebar
data_string = f"""
nama {data_nama :>5}
umur = {data_umur:>5}
tinggi = {data_tinggi:>5}
nomer sepatu = {data_nomer_sepatu:<5}"""
print(data_string)


