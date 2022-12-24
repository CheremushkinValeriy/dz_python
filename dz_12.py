# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint
import math 

list = [randint(0,20) for i in range(randint(5, 10))]
print(list)
size = math.ceil(len(list)/2)
# print(size)
list_2 = []
for i in range(size):
    list_2.append(list[i] * list[-i - 1])    
print('=>', list_2)

# list = [2, 3, 4, 34, 6, 8]
# print(list)
# import math 
# size = math.ceil(len(list)/2)
# # print(size)
# list_2 = []
# for i in range(size):
#     list_2.append(list[i] * list[-i - 1])    
# print('=>', list_2)

