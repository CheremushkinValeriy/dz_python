# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
 
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
list_num = [randint(0,50) for i in range(randint(5, 10))]
print(list_num)
sum_num = 0
for i in range(1, len(list_num), 2):
    sum_num += list_num[i]
print(f"Cумма элементов на нечётных позициях: {sum_num}")



# number = int(input('Введите кол-во эле-в списка: '))
# list = []
# summ = 0
# for i in range(1, number+1):
#     list.append(i)
# print(list)
# for i in range(1, len(list), 2):
#         summ += list[i]       
#         print(list[i])
# print(f"Сумма элементов на нечётных позициях: {summ}")

