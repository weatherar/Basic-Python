import sains.matematika
from sains import fisika
from sains.fisika import gaya as force
# import time


# t_start = time.time()
hasil_tambah = sains.matematika.tambah(1,23,4,3)
print(f"hasil tambah dari package {hasil_tambah}")

gaya = force(90,10)
print(f"gaya adalah = {gaya}")
# t_end = time.time()
# print(f"waktu eksekusi adalah = {t_end - t_start}")