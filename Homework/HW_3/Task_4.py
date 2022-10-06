# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def binary(number):
    result = ''
    while number > 0:
        result = str(number % 2) + result
        number //= 2
    return int(result)


number = 45
print(f'{number} -> {binary(number)}')
