# Operasi logika
#not, and, or, xor

print('===NOT===')
a = True
c = not a
print('data a =', a)
print('-----------NOT')
print('data c', c)

#OR adalah GROW MINDSED\

print('===OR===')
a = True
b = False
c = a or b
print(a, " OR",b, '=', c)
a = True
b = True
c = a or b
print(a, " OR",b, '=', c)
a = False
b = True
c = a or b
print(a, "OR",b, '=', c)
a = False
b = False
c = a or b
print(a, "OR",b, '=', c)

#AND adalah FIX MINDSED\

print('===and===')
a = True
b = False
c = a and b
print(a, " and",b, '=', c)
a = True
b = True
c = a and b
print(a, " and",b, '=', c)
a = False
b = True
c = a and b
print(a, "and",b, '=', c)
a = False
b = False
c = a and b
print(a, "and",b, '=', c)

#XOR akan true jika salah satu truem sisanya false (FIXED MINSED)

print('===XOR===')
a = True
b = False
c = a ^ b
print(a, " XOR",b, '=', c)
a = True
b = True
c = a ^ b
print(a, " XOR",b, '=', c)
a = False
b = True
c = a ^ b
print(a, "XOR",b, '=', c)
a = False
b = False
c = a ^ b
print(a, "XOR",b, '=', c)