#operasi yang dapat dilakikan dengan peyingkatan
#operasi di tambah dengan assigment

a = 5
print('nilai a=',a)

a += 1
print('nilai a +=1, nilai a menjadi',a)

a -=2
print('nilai a -=1, nilai a menjadi',a)

a *=2
print('nilai a *=1, nilai a menjadi',a)

a /=2
print('nilai a /=1, nilai a menjadi',a)

# modulus dan floor division
b = 10
b %= 3
print('nilai b %=1, nilai b menjadi',b)

b = 10
b //= 3
print('nilai b %=1, nilai b menjadi',b)
a = 5 
print('nilai a=',a)
b **= 3
print('nilai a **=1, nilai a menjadi',a)

#operasi bitwise
#OR
c = True
print('\n nilai c =',c)
c |= False
print('nilai c |= false, nilai c menjadi', c)
c = False
print('\n nilai c =',c)
c |= False
print('nilai c |= false, nilai c menjadi', c)

#AND
print('-------and------')
c = True
print('\n nilai c =',c)
c &= False
print('nilai c &= false, nilai c menjadi', c)
c = False
print('\n nilai c =',c)
c &= True
print('nilai c &= false, nilai c menjadi', c)

#XOR
print('-------XOR------')
c = True
print('\n nilai c =',c)
c ^= False
print('nilai c ^= false, nilai c menjadi', c)
c = False
print('\n nilai c =',c)
c ^= True
print('nilai c ^= false, nilai c menjadi', c)

#geser geser
d = 0b0100
print('\n nilai  d =,', format(d,'04b'))
d >>= 2
print('nilai d >>=2, nilai d  menjadi',format(d, '04b'))
d <<= 1
print('nilai d <<=2, nilai d  menjadi',format(d, '04b'))