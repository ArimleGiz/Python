# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def get_fibonacci_numbers(parameter: int):
    fibinacci_list = []
    fib_num_1 = 1
    fib_num_2 = 1
    for i in range(parameter):
        fibinacci_list.append(fib_num_1)
        fib_num_1, fib_num_2 = fib_num_2, fib_num_1 + fib_num_2

    fib_num_1 = 0
    fib_num_2 = 1
    for i in range(parameter + 1):
        fibinacci_list.insert(0, fib_num_1)
        fib_num_1, fib_num_2 = fib_num_2, fib_num_1 - fib_num_2

    return fibinacci_list


number = int(input('Введите число: '))
final_list = get_fibonacci_numbers(number)
print(f'Cписок чисел Фибоначчи: {final_list}')
