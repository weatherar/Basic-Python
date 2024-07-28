#default argument
# def fungsi (argumrnt):
# def fungsi (argument = nilai defaultnya):

# contoh 1
def say_hello(nama = "kAamu"):
    # fungsi dengan default argument
    print(f"Hallo {nama}")
    
say_hello("Ucup")
say_hello()

# contoh 2
def sapa_dia(nama, pesan="apa kabar?"):
    # funsgi dengan 1 input biasa dan defaul argument?
    print(f'Hai {nama}, {pesan}')
    
sapa_dia("dudung","hai ganteng")
sapa_dia("aira")

def hitung_pangkat(angka, pangkat=2):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat=3, angka=2)
print(hasil)

# contoh 4

def fungsi(input1 =1, input2 =2 , input3=3, input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=10))