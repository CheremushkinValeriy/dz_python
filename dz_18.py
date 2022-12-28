# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.


import random 

# list = [round(random.randint(0,7),2) for i in range(random.randint(10,20))]
# set = set(list)
# print(list)
# print(set)

list = [round(random.randint(0,7),2) for i in range(random.randint(10,20))]
list_2 = []
print(list)
for i in list:
   if list.count(i) == 1:
        list_2.append(i)
print(list_2)





