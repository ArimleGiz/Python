# Реализуйте алгоритм перемешивания списка.
import random as r
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    j = r.randint(0, i + 1)
    temp = numbers[j]
    numbers[j] = numbers[-i]
    numbers[-i] = temp
print(numbers)
