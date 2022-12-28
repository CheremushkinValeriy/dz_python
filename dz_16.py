# Вычислить число c заданной точностью d
 
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
 
# import math
# n = int(input('округлить до: '))
# print(round((math.pi), n))
 
import math
n = float(input('введите точность: '))
if n <= 10**(-1) and n >= 10**(-10):
    pi = math.pi
    str = str(n)
    a= int(len(str)-2)
    print(round(pi, a))
else:
    print('некорректный ввод')