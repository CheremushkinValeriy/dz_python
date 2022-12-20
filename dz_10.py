# Реализуйте алгоритм перемешивания списка.
 
N = int(input('Введите число N: '))
list = []
for i in range(-N, N + 1):
    new_element = i
    list.append(new_element)
print(list)
 
import random 
random.shuffle(list)
print(list)