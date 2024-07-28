import datetime 

data_waktu = datetime.datetime.now()
print(f"date time now {data_waktu}")
print(f"tahun : {data_waktu.year}")
print(f"Hari : {data_waktu.strftime('%A')}")

from collections import Counter 
data = ["a","b","c","d","a"]

# count = 0
# for i  in data:
#     if i == "a":
#         count += 1
# print (count)

data_count = Counter(data)


print(f"data count = {data_count}")
print(f"jumlah a = {data_count['a']}")
print(f"jumlah b = {data_count['b']}")

import io 
file = io.open("introduction/studi kasus & library/file_text.txt","r")
print(file.read())

