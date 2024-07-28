#operator dictionaty
data_dict = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"surudung"  
}

#panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionay : {LENDICT}")

#mengecek key exit atau tidak
KEY = "cup"
CHECKEY = KEY in data_dict
print(f"apakah {KEY} ada di data dict : {CHECKEY}")

#Mengakses value(read)dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak di temukan")) #ini adlah check key dengan mesage tidak ditemukan

#mengapdate data
data_dict["cup"] ="ucup si gantteng"
print(data_dict)

data_dict["sep"] = "asep si kasep"
print(data_dict)

data_dict.update({"cup":"ucup surucup"})
print(data_dict)

data_dict.update({"faqih":"si keren"}) #kalau ga ada di add aja
print(data_dict)

# mendelete data pada dictionary
del data_dict["faqih"]
print(data_dict)