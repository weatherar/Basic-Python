# latihan fungsi

# import os

# # program menghitung luas dan kelilinh persedi panjang

# # header program

# os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILLING PERSIGU PANJANG':^40}")
# print(f"{'-'*40 :^40}")

# # mengambil input
# LEBAR = int (input('Masukan lebar : '))
# PANJANG = int (input('Masukan panjang :  '))

# # program menghitung PANJANG
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# # tampilkan hasilnya
# print(f"hasil perhitunga LUAS = {LUAS}")
# print(f"hasil perhitungan KELILING = {KELILING}")


def header():
    # fungsi header
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILLING PERSIGU PANJANG':^40}")
    print(f"{'-'*40 :^40}")
    
# fungsi input
def input_user():
    lebar = int (input('Masukan lebar : '))
    panjang = int (input('Masukan panjang :  '))
    
    return lebar,panjang

def hitung_luas(lebar, panjang):
    # fungsi luas
    return lebar*panjang

def hitung_keliling(lebar, panjang):
    # fungsi keliling \
    return 2*(lebar+panjang)

def display(message, value):
    # fungsi display 
    print(f"hasil perhitungan {message} = {value}")
# progam utama    
    
while True:
    header() 
    opsi = input("pilih 1 untuk luas, 2 untuk keliling, 3 untuk keduanya")
    if opsi == "1":
        LEBAR,PANJANG = input_user()
        LUAS = hitung_luas(LEBAR,PANJANG)
        display("luas", LUAS)
    elif opsi == "2":
        LEBAR,PANJANG = input_user()
        KELILING = hitung_keliling(LEBAR, PANJANG)
        display("keliling", KELILING)
    elif opsi == "3":
        LEBAR,PANJANG = input_user()
        LUAS = hitung_luas(LEBAR,PANJANG)
        KELILING = hitung_keliling(LEBAR, PANJANG)
        display("luas", LUAS)
        display("keliling", KELILING)
    
    isContinue = input("Apakah lanjut (y/n)")
    if isContinue == "n":
        break
    
print("program selsesai")