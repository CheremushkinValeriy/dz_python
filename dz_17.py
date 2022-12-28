# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
 
N = int(input('N = '))
list = []
 
while N % 2 == 0 :
    N = N/2
    list.append(2)
while N % 3 == 0 :
    N = N/3
    list.append(3)
while N % 5 == 0 :
    N = N/5
    list.append(5)
while N % 7 == 0 :
    N = N/7
    list.append(7)
# list.append(int(N))
print(list)



# def Factor(n):
#     Ans = []
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             Ans.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         Ans.append(n)
#     return Ans