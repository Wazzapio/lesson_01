day = 1
km = int(input('Введите сколько "км" Вы преодолели в 1-ый день: '))
km_max = int(input('Введите сколько "км" в день Вы хотите преодолевать.\nА в ответ, Вы получите на какой день '
                   'Вам удастся достичь результата при увеличении нагрузки на 10% в день: '))

print(f'\n{day}-й день: {km} км')

while int(km) < int(km_max):
    day += 1
    km = (km * 0.1) + km
    print(f'{day}-й день: {round(km, 2)} км')

print(f'\nОтвет: на {day}-й Вы достигнете результата — не менее {round(km, 2)} км.')