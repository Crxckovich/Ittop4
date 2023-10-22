dict = {}

while True:
    name = input('Введите (или \' выход \' для остановки): ')
    if name.lower() == 'выход':
        break
    age = int(input('Введите age человека: '))

    dict[name] = age

    max_age_man = max(dict, key=dict.get)
    print('Человек max age:', max_age_man)

print('конец')