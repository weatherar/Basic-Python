#multi key dictionanry
import datetime

mahasiswa1 = {
    'nama':'ucup surucup',
    'nim':'387404',
    'sks_lulus': 30,
    'beasiswa':'false',
    'lahir':datetime.datetime(2001,4,10)
}
mahasiswa2 = {
    'nama':'otong',
    'nim':'387402',
    'sks_lulus': 303,
    'beasiswa':'true',
    'lahir':datetime.datetime(2002,4,3)
}
mahasiswa3 = {
    'nama':'asep',
    'nim':'387405',
    'sks_lulus': 304,
    'beasiswa':'false',
    'lahir':datetime.datetime(2000,2,29)
}

data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3
}
print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'beasiswa':<9}{'lahir':10}")
print("-"*50)
for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS= data_mahasiswa[KEY]['sks_lulus']
    BEASISWA= data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x") 
    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9}{LAHIR:10}")
    
    