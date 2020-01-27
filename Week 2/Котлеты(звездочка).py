'''Задача со звездочкой.
На сковородку одновременно можно положить k котлет.
Каждую котлету нужно с каждой стороны обжаривать m минут непрерывно.
За какое наименьшее время удастся поджарить с обеих сторон n котлет?

Формат ввода

Программа получает на вход три числа: k,m,n.

Формат вывода

Программа должна вывести одно число: наименьшее количество минут.
'''
panCapacity, minutes, numberCutlet = (int(input()) for _ in range(3))
numberOperations = numberCutlet * 2 // panCapacity + \
                   int(bool(numberCutlet * 2 % panCapacity))
if numberCutlet * 2 <= panCapacity:
    numberOperations *= 2
print(numberOperations * minutes)
