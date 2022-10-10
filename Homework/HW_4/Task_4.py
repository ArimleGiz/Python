# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
degree_of_polynomial = int(input('Введите натуральную степень k:'))


def get_polynomial(param_1: int):
    polynomial = ""
    while param_1 >= 0:
        coefficient = random.randint(0, 101)
        if coefficient != 0:
            match param_1:
                case 1: polynomial += (str(coefficient) + "*x" + " + ")
                case 0: polynomial += (str(coefficient) + " = 0")
                case _: polynomial += (str(coefficient) + "*x^" + str(param_1) + " + ")
        param_1 -= 1
    return polynomial


polynomial_1 = get_polynomial(degree_of_polynomial)
print(f'Многочлен степени {degree_of_polynomial}: {polynomial_1}')

# записываем в файл первый многочлен

with open('file_task_4.txt', 'w') as data:
    data.write(polynomial_1)

# записываем в файл второй многочлен для 5 задачи

degree_of_polynomial_2 = int(input('Введите натуральную степень k:'))
polynomial_2 = get_polynomial(degree_of_polynomial)
print(f'Многочлен второй степени {degree_of_polynomial_2}: {polynomial_2}')

with open('file_task_4_2.txt', 'w') as data:
    data.write(polynomial_2)
