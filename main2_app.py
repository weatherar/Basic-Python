import package_sains
from package_sains.matematika import scientific

hasil_tambah = package_sains.matematika.basic.tambah(2,3,4)
print(f"hasil tambah = {hasil_tambah}")

hasil_fisika = package_sains.fisika.gaya(29,3)
print(f"hasil tambah = {hasil_fisika}")

hasil_kali = package_sains.matematika.kali(2,3,3,3,4)
print(f"hasil kali = {hasil_kali}")

pangkat_3 = scientific.pangkat(3)
print(f"hasil kali = {pangkat_3(5)}")

# from package_sains import*

# hasil_tambah = matematika.basic.tambah(2,3,4)
# print(f"hasil tambah = {hasil_tambah}")

# hasil_fisika = fisika.gaya(29,3)
# print(f"hasil tambah = {hasil_fisika}")

# hasil_kali = matematika.basic.kali(2,3,3,3,4)
# print(f"hasil kali = {hasil_kali}")