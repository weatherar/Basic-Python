## Tutorial membaca file eksternal

print(3*"=","membaca file txt",3*"=")
file = open("64.reading_ekternal_file/data.txt",mode="r")

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")

#baca seluruh file
# print(file.read())

print(file.readline(),end ="") #baca baris pertama
print(file.readline(),end ="") #baca baris kedua

#baca semua baris dengan list
# print(file.readlines()) 
file.close()
print(f"apakah file sudah di close : {file.closed}")


## salah satu tehnik membuka file di python
print(3*"=","membaca file txt dengan with",3*"=")
with open("64.reading_ekternal_file/data.txt", mode="r")as file:
    content=file.readline()
    print(content,end="")
    print(f"apakah file sudah di close : {file.closed}")
    