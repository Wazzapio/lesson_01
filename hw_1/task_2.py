sec = input('Введите кол-во ковертируемых секунд: ')
hour = int(sec) / 3600
min = (int(sec) % 3600) / 60
sec = (int(sec) % 3600) % 60

print(int(hour) ,str('ч'),int(min), str('м'),int(sec),str('с'))