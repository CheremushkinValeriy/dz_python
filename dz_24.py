# 45. Найти сумму чисел списка стоящих на нечетной позиции
import random
a = [random.randint(0, 100) for i in range(6)]
print(a)

def summ(a):
    summ = 0
    for i, val in enumerate(a):
        if i % 2 != 0:
            summ = summ + val
            print(f'-> {val}')
    print(f'Sum = {summ}')

summ(list(a))

# res = sum([value for index, value in enumerate(a) if index % 2 == 1])
# print(res)
 