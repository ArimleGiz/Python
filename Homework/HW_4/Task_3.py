# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# Первый способ решения

if __name__ == '__main__':

    nums = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 8]

    nums[:] = list(set(nums))
    print(nums)

exit()

# Второй способ
if __name__ == '__main__':

    nums = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 8]

    visited = set()
    nums[:] = [x for x in nums if x not in visited and not visited.add(x)]

    print(nums)

# Третий способ

if __name__ == '__main__':

    nums = [1, 5, 2, 1, 4, 5]

    nums[:] = reduce(lambda l, x: l if x in l else l + [x], nums, [])
    print(nums)
# Четвертый способ решения с использованием словаря


if __name__ == '__main__':

    nums = [1, 5, 2, 1, 4, 5]

    nums[:] = list(OrderedDict.fromkeys(nums))
    print(nums)
# Пятый способ решения отсортировка уникальных элементов

if __name__ == '__main__':

    nums = [1, 5, 2, 1, 4, 5]

    nums[:] = np.unique(nums)
    print(nums)
