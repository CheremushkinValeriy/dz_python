# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
 
number_quater = int(input('Введите номер четверти: '))
if number_quater >=1 and number_quater <=4:
  if number_quater == 1:
    print('100 <= x >= 0')
    print('100 <= y >= 0')
  if number_quater == 2:
    print('0 <= x >= -100')
    print('100 <= y >= 0')
  if number_quater == 3:
    print('0 <= x >= -100')
    print('0 <= y >= -100')
  if number_quater == 4:
    print('100 <= x >= 0')
    print('0 <= y >= -100')
else:
  print('Неверный номер четверти') 