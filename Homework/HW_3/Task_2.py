# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# Первый способ решения
first_number = [2, 3, 4, 5, 6]
result = []
for i in range(0, (len(first_number) + 1)//2):
    result.append(first_number[i]*first_number[len(first_number)-1-i])
print(f'{first_number} => {result}')

# Второй способ решения
#first_number = [2, 3, 5, 6]
#result = []
#left = 0
# while left < len(first_number)/2:
#    right = (left + 1) * -1
#    result.append(first_number[left]*first_number[right])
#    left += 1
#print(f'{first_number} => {result}')
