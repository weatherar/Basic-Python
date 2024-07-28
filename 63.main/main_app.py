#__main __ adalah top laevel code enviroment
#__name == "__maiin__" akan terjadi jika ada di program pertama
##__name__ pada file program eksternal
import  fungsi

## contoh penggunaaan __main__

#deklarasi
def fungsi_tambah (a:int,b:int)->int:
    return a+b
#fungsi utama

if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1,angka2)
    print(f"Hasil tambah = {hasil}")
    
##import package
import package
