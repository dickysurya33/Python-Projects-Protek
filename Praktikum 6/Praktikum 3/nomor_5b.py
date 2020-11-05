# operasi (4+7)*(6-9)
from operation import *

empat = 4
tujuh = 7
enam = 6
sembilan = 9

print('(', empat, '+', tujuh, ')', '*', '(', enam, '-', sembilan, ')',
      ':', kali(jumlah(empat, tujuh), kurang(enam, sembilan)))
