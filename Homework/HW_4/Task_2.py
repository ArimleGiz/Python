# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import math

number = int(input('Введите число: '))
list_n = []
n = 2
while number > 1:
    if number % n == 0:
        list_n.append(n)
        number = number / n
    else:
        n += 1
print(list_n)
