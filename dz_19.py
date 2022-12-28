# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random 
k = int(input('k = '))
list = [round(random.randint(0,100),2) for i in range(k + 1)]
print(list)
for i in list:
    if k != 0:
        if k == 1:
            print(f'{i}*x + ', end = ' ')
            k -=1
        else:
            print(f'{i}*x**{k} +', end = ' ')
            k -=1
    else:
        print(f'{i} = 0')

