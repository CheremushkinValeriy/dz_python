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


# import datetime
# def random_int(num):
#     rand = datetime.datetime.now().microsecond/10**6
#     return int(num*rand)

# a = [1,2,3,4,5,6]
# print(a)
# random_int(5)
# for i in range(len(a)-1,-1,-1):
#     j = random_int(i+1)
#     a[i],a[j] = a[j],a[i]
# print(a)
