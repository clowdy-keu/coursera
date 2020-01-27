'''Даны пять действительных чисел: x, y, xc, yc, r.

Проверьте, принадлежит ли точка (x,y) кругу с центром (xc, yc) и радиусом r.

Если точка принадлежит кругу, выведите слово YES, иначе выведите слово NO.

Решение должно содержать функцию IsPointInCircle(x, y, xc, yc, r),
возвращающую True, если точка принадлежит кругу и False, если не принадлежит.

Основная программа должна считать координаты точки,
вызвать функцию IsPointInCircle и в зависимости от возвращенного значения
вывести на экран необходимое сообщение.
Функция IsPointInCircle не должна содержать инструкцию if.

Формат ввода

Вводится пять действительных чисел.

Формат вывода

Выведите ответ на задачу.
'''


def distance(x1, y1, x2, y2):
    from math import sqrt
    distance = sqrt(round((x2 - x1) ** 2, 6) + round((y2 - y1) ** 2, 6))
    return distance


def IsPointInCircle(x, y, xc, yc, r):
    return distance(xc, yc, x, y) <= r

x, y, xc, yc, r = (float(input()) for _ in range(5))
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
