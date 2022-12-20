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
