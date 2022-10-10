# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# создание двух файлов

import re
import itertools


# Получение данных из файла

def get_polynomial_out_of_file(param_1):
    with open(param_1, 'r') as data:
        polynomial = data.read()
    return polynomial

# Получение списка кортежей каждого (<коэффициент>, <степень>)


def convert_pol(pol):
    pol = pol.replace('= 0', '')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x':
            i.insert(0, 1)
        if i[-1] == 'x':
            i.append(1)
        if len(i) == 1:
            i.append(0)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol

# Получение списка кортежей суммы (<коэф1 + коэф2>, <степень>)


def fold_pols(pol1, pol2):
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    for i in pol1 + pol2:
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key=lambda r: r[1], reverse=True)
    return res

# Составление итогового многочлена


def get_sum_pol(pol):
    var = ['*x^'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_pol = [[str(a), str(b), str(c)]
               for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0':
            del (x[0])
        if x[-1] == '0':
            del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^':
            del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1':
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))


def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)


file1 = 'file_task_4.txt'
file2 = 'file_task_4_2.txt'
file_sum = 'sum_polynomials.txt'

polynomial_1 = get_polynomial_out_of_file(file1)
polynomial_2 = get_polynomial_out_of_file(file2)
polynom_1 = convert_pol(polynomial_1)
polynom_2 = convert_pol(polynomial_2)

pol_sum = get_sum_pol(fold_pols(polynom_1, polynom_2))
write_to_file(file_sum, pol_sum)

print(polynomial_1)
print(polynomial_2)
print(pol_sum)
