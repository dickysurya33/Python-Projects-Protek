                                                                                                                                                                                                                                                     # (10 + 2) / (7 + 5) / (12 - 34)
from operation import *

a = 10
b = 2
c = 7
d = 5
e = 12
f = 34

print('(', a, '+', b, ')', '/', '(', c, "+", d, ')', '/',
      '(', e, '-', f, ')', ':', bagi(jumlah(a, b), jumlah(c, d))/kurang(e, f))
