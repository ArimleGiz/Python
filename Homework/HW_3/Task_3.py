# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# Первый способ решения
list = [1.1, 1.2, 3.1, 5, 10.01]


def diff_number(list: list):
    i = 0
    while i < len(list):
        list[i] = list[i] % 1
        i += 1
    return list


print(f'{list} =>{max(diff_number(list))-min(diff_number(list))}')

# Второй способ решения
#list = [1.1, 1.2, 3.1, 5, 10.01]
#min_num = 0
#max_num = 0
# for i in list:
#    if (i - int(i)) <= min_num:
#        min_num = i - int(i)
#    if (i - int(i)) >= max_num:
#        max_num = i - int(i)
#result = max_num - min_num
#print(f'{list} => {result}')
