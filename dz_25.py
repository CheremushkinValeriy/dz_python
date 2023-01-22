# 46. Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)
from random import randint
import math 

# list = [randint(0,20) for i in range(randint(5, 10))]
# print(list)
# size = math.ceil(len(list)/2)
# print(size)
# list_2 = []
# for i in range(size):
#     list_2.append(list[i] * list[-i - 1])    
# print(f'=> {list_2}')


list = [randint(0,20) for i in range(randint(0, 10))]
print(list)
# size = math.ceil(len(list)/2)
list_2 = [list[i] * list[-i - 1] for i in range(math.ceil(len(list)/2))]  
print(f'=> {list_2}')


