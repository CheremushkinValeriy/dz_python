# **44. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние 
# между ними в 2D пространстве.

# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
import math

x_1 = int(input('x_1 ='))
x_2 = int(input('x_2 ='))
y_1 = int(input('y_1 ='))
y_2 = int(input('y_2 ='))
print('Len =', round(math.sqrt(((x_2 - x_1)**2)+((y_2 - y_1)**2)),1))

# a = [int(input(f'Введи {i} координату точки a: ')) for i in 'xy']
# b = [int(input(f'Введи {i} координату точки b: ')) for i in 'xy']

# res = round(sum ([(element[1] - element[0])**2 for element in zip(a,b)])**0.5,2)
# print(res)
