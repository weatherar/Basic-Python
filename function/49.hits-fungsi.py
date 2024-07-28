#hit fungsi
# Type hints untuk fungsi 

# bentuk standar yang sudah di pelajari
'''

studi kasuus

def fungsi(parameter):
    hasil = parameter**2
    print(hasil)
    
fungsi(1)
fungsi("ucup")

'''

import string
# penggunaan  type hints
def sepuluh_pangkat(argument:int)-> int:
    output = 10**argument
    return output

HASIL = sepuluh_pangkat(4)
print(HASIL)

def display(argument:string):
    print(argument)

display("ucup")

import os
