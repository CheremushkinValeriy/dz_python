# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 



k = int(input('Число элементов: '))
 
def p_fib(n):
    if n in [1, 2]:
        return 1
    else:
        return p_fib(n - 1) + p_fib(n - 2)
 
p_list = []
for i in range(1, k + 1):                                                                                                                   
    p_list.append(p_fib(i))
print(p_list)
 
def n_fib(n):
    if n in [0, 1]:
        return 1
    else:
        return n_fib(n - 2) - n_fib(n - 1)

n_list = []
for i in range(2, k + 3):                                                                                                                   
    n_list.append(n_fib(i))

print(n_list)

print(n_list[::-1] + p_list)
