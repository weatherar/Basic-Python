# kwargs
def fungsi (nama, tinggi, berat):
    # fungsi biasa 
    print(f"nama {nama}, tinggi {tinggi}, berat {berat}")
    
fungsi("ucup",233,45)

def fungsi (**kwargs):
    # fungsi kwargas
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"nama {nama}, tinggi {tinggi}, berat {berat}")
  
fungsi(nama= "ucup", tinggi = 183, berat=79)

# studi kasus
def math (*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else :
        print("tdak ada operasi")
    
    return output

hasil = math(1,2,3,6, option = "tambah")
print(f"hasil jumulah {hasil}")
hasil = math(1,2,3,4, option = "kali")
print(f"hasil kali {hasil}")