# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

number = int(input('Введите кол-во эле-в списка: '))
list = []
summ = 0
for i in range(number):
    list.append(round((uniform(0, 10)),2))
print(list)
x_max = round((max(list) % 1), 2)
x_min = round((min(list) % 1), 2)
print(x_max)
print(x_min)
difference = x_max - x_min
print('=>', round(difference,2))


