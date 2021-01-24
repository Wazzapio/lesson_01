user_num = input('Введите целое положительное число: ')
print(f'Ваше число: {int(user_num)}')

length = len(user_num)

a = 0
num_high = 0

while int(length) != 0:
    if int(user_num[a]) > num_high:
        length = int(length) - 1
        num_high = int(user_num[a])
        a += 1
    else:
        length = int(length) - 1
        a += 1

print(f'Самая большая цифра среди этого числа: {num_high}')