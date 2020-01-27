'''Заданы две клетки шахматной доски.
Если они покрашены в один цвет, то выведите слово YES,
а если в разные цвета – то NO.

Формат ввода

Вводятся 4 числа - координаты клеток.

Формат вывода

Выведите ответ на задачу.
'''
firstCol, firstRow, secondCol, secondRow = (int(input()) for _ in range(4))
firstCell = abs(firstRow - firstCol) % 2 == 0
secondCell = abs(secondRow - secondCol) % 2 == 0
if firstCell == secondCell:
    print('YES')
else:
    print('NO')
