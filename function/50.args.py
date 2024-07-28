# args pada function 

# memasukan data/argument 
def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    
fungsi("ucup",23,43)

def fungsi (data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data [1]
    berat = data [2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    
fungsi(["otong",110,20])

# kenalan dengan args

def fungsi(*args): 
    nama =  args[0]
    tinggi =  args [1]
    berat =   args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    
fungsi("dudung", 120,34)

def tambah(*data):
    # daaat tipenya adalha tuple dan bisa di iterasi 
    output = 0
    for angka in data:
        output+= angka
    return output

hasil = tambah(1,2,3,4,5,6,6,7)
print(f"hasil = {hasil}")

hasil = tambah(1,2)
print(f"hasil = {hasil}")
    