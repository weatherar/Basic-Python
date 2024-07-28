#perulangan (loop)
angka = [0,1,2,3]
print(angka)

for i in angka:
    print(f"i sekarang -> {i}")
print("ini adalah akhir program")

#ini dengan range

angka2_range = range(2,5)
for i in angka2_range:
    print(f"i sekarang -> {i}")
print("akhir program 2")

#menggunakan string
data_str = "saya ganteng abies"
for huruf in data_str:
    print(huruf)
