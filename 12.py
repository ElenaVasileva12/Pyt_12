# Программа загадывает число от 0 до 1000. 
# Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

LOWER_LIMIT=0
UPPER_LIMIT=1000

from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
#print(num)

k=9
while True:
    a=int(input('Введите предполагаемое число: '))
    if a==num:
        print(f'верно!!!, загаданное число {num}')
        break
    elif a>num:
        print(f'меньше, осталось попыток {k}')
        k-=1
    elif a<num:
        print(f'больше, осталось попыток {k}')
        k-=1
    if k<0:
        print('Все попытки исчерпаны!!!')
        break



