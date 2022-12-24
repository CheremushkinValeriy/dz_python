# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
 
N = int(input('Введите число N: '))
list = []
p = 1

for i in range(-N, N + 1):
    new_element = i
    list.append(new_element)
print(list)
 
path = 'text.txt'
data = open(path, 'r')
for line in data:
    print(line)
    p = p * list[int(line)]
print('Сумма: ', p)
data.close()

# import random
#
# n = int(input())
# list_num = [random.randint(-n,n) for i in range(n)]
# print(list_num)

# file = open("File.txt","r")
# multi = 1
# list_str = file.readlines()
# print(list_str)
# list_num = list(map(str.strip,list_str))
# print(list_num)
# list_num = list(map(int,list_num))
# print(list_num)
# for i in file:
#     multi*=list_num[int(i)]
# print(multi)
