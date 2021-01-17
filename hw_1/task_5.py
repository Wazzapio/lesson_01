proceed = input('Введите значение выручки компании: ')
cost = input('Введите значение издержек компании: ')

if float(proceed) > float(cost):
    print('Значение прибыли БОЛЬШЕ чем издержек.')
    profit = float(proceed) - float(cost) # вычисляем прибыль
    rent = float(proceed) / float(profit) # вычисляем соотношение
    print(f'Соотношение прибыли к выручке составляет: {round(rent, 2)}')
    num_of_staff = input('Какое кол-во сотрудников работает в компании?: ')
    profit_for_staff = float(profit) / float(num_of_staff)
    print(f'Прибыль фирмы в расчете на одного сотрудника составляет: {round(profit_for_staff, 2)}')

elif float(cost) > float(proceed):
    print('Значение издержек БОЛЬШЕ чем прибыли.')

elif float(proceed) == float(cost):
    print('Значения прибыли и издержек РАВНЫ.')
