#latihan kalkulator sederhana
print(10*"=")
print("Kalkulator sederhana")
print(10*"=" + "\n")

angka_1 = float(input("masukan angka 1"))
operator = input('operator +-/*')
angka_2= float(input("masukan angka 2"))

#[PERCABANGAN]
if operator == "+":
    hasil = angka_1+angka_2
    print(f"hasilnya adalah {hasil}")

elif operator == "-":
    hasil = angka_1-angka_2
    print(f"hasilnya = {hasil}")
     
elif operator == "/":
    hasil = angka_1/angka_2
    print(f"hasilnya = {hasil}") 
    
elif operator == "*" or "x":
    hasil = angka_1*angka_2
    print(f"hasilnya = {hasil}") 