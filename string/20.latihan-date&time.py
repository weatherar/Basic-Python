#date and time ( latihan)
import datetime as dt

print("silahkan masukan tanggal,\n bulan dan tahun lahir anda")
tanggal = int(input("tanggal \t\t:"))
bulan = int(input("bulan \t\t:"))
tahun = int(input("tahun\t\t:"))
tanggal_lahir =dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Harinya adalah  : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"hari ini tanggal : {hari_ini}")
umur_hari = hari_ini-tanggal_lahir
umur_tahun = umur_hari.days//365
umur_bulan_sisa= (umur_hari.days%365)//30

print(f"hari ini adalah : {tanggal_lahir:%A}")
print(f"umur anda adalah : {umur_tahun } tahun, {umur_bulan_sisa} bulan")

if umur_tahun >= 20:
    print(f" umur anda:  {umur_tahun}, hahaha mudaan saya wkwk")