# Fungsi dengan argumenrt (input)
#def nama_fungsi (input):
    #badan-function

from copy import deepcopy
# """
# def nama_fungsi(argument):
#     badan fungsi
# """
def hello_wordl(nama):
    #fungsi hello word menerima input dengan variable nama
    print(f"selamat datang dunia wahai {nama}")
    
hello_wordl("Ucup")

#program tambah
def tambah(angka1, angka2):
    #fungsi tambah
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")
    
tambah(1,3)

def say_hi (list_peserta):
    list_peserta [1] = "ara"
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"yang terhormat {peserta}")

anggota_boyband = ["ucup","otongg"]
print(anggota_boyband)

say_hi(anggota_boyband)

print(anggota_boyband)
