def custom_write(file_name, strings):
    strings_position = {}
    count = 0
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        count += 1
        strings_position[(count, file.tell())] = i
        file.write(f'{i}\n')
    file.close()
    return strings_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('text.txt', info)
for elem in result.items():
    print(elem)
