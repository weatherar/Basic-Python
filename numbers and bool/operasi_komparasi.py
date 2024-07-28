# opeerasi komparasi
#setiap komperasi hasolnya adalam boolean

#>,<, <=, >=, ==, !=, is , is not

a=4
b=4
#sama dengan ==
print("=======hasil dari sama dengan ==")
hasil = a==4
print(a, "==", hasil)

print("=======hasil dari sama dengan !=")
hasil = a!=4
print(a, "==", hasil)

# is dan is not
print('=== ini is ===')
x = 5
y = 5
print('nilai x = ', x, ',id =', hex(id(x)))
print('nilai x = ', y, ',id =', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)

print('=== ini is not ===')
x = 5
y = 6
print('nilai x = ', x, ',id =', hex(id(x)))
print('nilai x = ', y, ',id =', hex(id(y)))
hasil = x is not y
print('x is y = ', hasil)