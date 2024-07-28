#looping dictionary
teman_teman = {
    "cup":"ucup surucup",    
    "tong":"otong surotong",    
    "sep":"asep si kasep",    
    "kuy": "kuyus si  kyui"
   }


#looping first try (yang keluar adalah keynya)
for teman in teman_teman:
    print(teman)
    
#operator untuk mengambil item
keys = teman_teman.keys()
print(keys)

for keys in teman_teman.keys():
    print(keys)
values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)
    
items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(item)
    
for key,value in teman_teman.items():
    print(f"KEy = {key}, Values = {value}")