# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Первый способ решения
# lst_number = [2, 3, 5, 9, 3]
# print(lst_number)
# sum = 0
# for i in range(1, len(lst_number), 2):
#     sum = sum + lst_number[i]
# print('Сумма элементов списка на нечетных позициях равна:', sum)

# Второй способ решения

lst_number = [2, 3, 5, 9, 3]
print(lst_number)


def rec_sum(lst):
    Sum = 0
    count = 1
    for i in range(len(lst)):
        if i % 2 != 0:
            Sum += lst[i]
            count = count + 1
    return Sum


print('Сумма элементов списка на нечетных позициях равна:', rec_sum(lst_number))


