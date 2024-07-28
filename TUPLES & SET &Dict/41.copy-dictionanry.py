#copy dictionary
teman_teman = {
    'ucup':"ucup surucup",   
    'otong':"otong surotong",    
    'dung':"dudung surudung",
    'sep':"asep si kasep",
    'ucuy':"si icuuy"    
}

friends = teman_teman.copy()

print(f"teman : {teman_teman}")
print(f"friends: {friends}")

teman_teman["cup"]="si kewren"
print(f"teman : {teman_teman}")
print(f"friends: {friends}")

#pop dictionary (berdasarkan key)
dataAsep = friends.pop("sep")
print(f"data asep = {dataAsep}\n")
print(f"friends = {friends}\n")

#ppopitem dictionary (yang terakhir aja)
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")
