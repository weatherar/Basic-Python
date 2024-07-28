#operasi bitwise / binary
a=9
b=5

#bitwise OP (|)
c = a | b
print('\n =======OR======')
print('nilai :', a, ',binary', format(a,'08b'))
print('nilai :', b, ',binary', format(b,'08b'))
print('-------------------------------(|)')
print('nilai :', c, ',binary', format(c,'08b'))

#bitwise and (&)
c = a & b
print('\n =======AND======')
print('nilai :', a, ',binary', format(a,'08b'))
print('nilai :', b, ',binary', format(b,'08b'))
print('-------------------------------(&)')
print('nilai :', c, ',binary', format(c,'08b'))

#bitwise XOR (^)
c = a ^ b
print('\n =======AND======')
print('nilai :', a, ',binary', format(a,'08b'))
print('nilai :', b, ',binary', format(b,'08b'))
print('-------------------------------(^)')
print('nilai :', c, ',binary', format(c,'08b'))

#bitwise NOt (~)
c = ~a
print('\n =======NOT======')
print('nilai :', a, ',binary', format(a,'08b'))
print('-------------------------------(~)')
print('nilai :', c, ',binary', format(c,'08b'))
#flip
print('--------------------------------(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :', e^d, ', binary :', format(e^d, '08b'))

#shifting
#shifting right
c = a >>1
print('\n=========>>========')
print('nilai : ',a,', binar:', format(a,'08b'))
print('-------------------------------(>>)')
print('nilai : ',c,', binar:', format(c,'08b'))

#shifting left
c = a >>1
print('\n=========<<========')
print('nilai : ',a,', binar:', format(a,'08b'))
print('-------------------------------(<<)')
print('nilai : ',c,', binar:', format(c,'08b'))

