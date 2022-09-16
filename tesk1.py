# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


from decimal import Decimal, getcontext
from unicodedata import decimal
import math

d = input('Введите точность: ')
c=abs(Decimal(d.rstrip('0')).as_tuple().exponent)
p=math.pi
print(round(p,c))

