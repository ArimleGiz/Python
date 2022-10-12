# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('RLE_1.txt', 'w') as file:
    file.write('mmmnnnnsssslllzzzzzc')
    file.close()

# считываем нашу строку из первого файла

with open('RLE_1.txt', 'r') as data:
    rle_1_string = data.read()

# модуль сжатия


def encode_the_string(param_1: str):
    new_string_encoding = ''
    previous_char = ''
    counter = 1
    if not param_1:
        return ''
    for current_char in param_1:
        if current_char != previous_char:
            if previous_char:
                new_string_encoding += str(counter) + previous_char
            counter = 1
            previous_char = current_char
        else:
            counter += 1
    else:
        new_string_encoding += str(counter) + previous_char
    return new_string_encoding


encoded_string = encode_the_string(rle_1_string)
print(f'Сжатые данные: {encoded_string}')

# записываем сжатые данные во второй файл

with open('RLE_2.txt', 'w') as file:
    file.write(encoded_string)
    file.close()


# считываем нашу строку из второго файла для декодинга

with open('RLE_2.txt', 'r') as data:
    rle_2_string = data.read()
    file.close()

# модуль восстановления


def decode_the_string(param_1: str):
    new_string_decoding = ''
    counter_string = ''
    for char in param_1:
        if char.isdigit():
            counter_string += char
        else:
            new_string_decoding += char * int(counter_string)
            counter_string = ''
    return new_string_decoding


decoded_string = decode_the_string(rle_2_string)
print(f'Восстановленные данные: {decoded_string}')
