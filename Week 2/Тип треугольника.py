'''Даны три стороны треугольника a,b,c.
Определите тип треугольника с заданными сторонами.
Выведите одно из четырех слов:
rectangular для прямоугольного треугольника,
acute для остроугольного треугольника,
obtuse для тупоугольного треугольника или
impossible, если треугольника с такими сторонами не существует
(считаем, что вырожденный треугольник тоже невозможен).

Формат ввода

Вводятся три целых числа.

Формат вывода

Выведите ответ на задачу.
'''
from math import acos, degrees
a, b, c = (int(input()) for _ in range(3))
if (-1 < (b ** 2 + c ** 2 - a ** 2) / (2 * b * c) > 1) \
        or (-1 < (a ** 2 + c ** 2 - b ** 2) / (2 * a * c) > 1) \
        or (-1 < (b ** 2 + a ** 2 - c ** 2) / (2 * a * b) > 1):
    print('impossible')
else:
    cornerA = round(degrees(acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))), 3)
    cornerB = round(degrees(acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))), 3)
    cornerC = round(degrees(acos((b ** 2 + a ** 2 - c ** 2) / (2 * a * b))), 3)
    cornerSummary = cornerA + cornerB + cornerC
    if cornerA == 0.0 or cornerB == 0.0 or cornerC == 0.0:
        print('impossible')
    else:
        if cornerA == 90.0 or cornerB == 90.0 or cornerC == 90.0:
            print('rectangular')
        elif cornerA > 90.0 or cornerB > 90.0 or cornerC > 90.0:
            print('obtuse')
        else:
            print('acute')
