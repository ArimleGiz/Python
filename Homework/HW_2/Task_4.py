# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
path = 'file.txt'
with open(path, 'r') as f:
    opened_file = f.readlines()
last_line = opened_file[-1]
first_line = opened_file[0]
print(first_line)
print(last_line)
print(int(last_line) * int(first_line))
