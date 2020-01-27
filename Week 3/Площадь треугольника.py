'''Даны длины сторон треугольника. Вычислите площадь треугольника.

Формат ввода

Вводятся три положительных действительных числа.

Формат вывода

Выведите ответ на задачу.
'''
from math import sqrt
a, b, c = (float(input()) for _ in range(3))
halfPerimeter = (a + b + c) / 2
square = sqrt(halfPerimeter *
              (halfPerimeter - a) *
              (halfPerimeter - b) *
              (halfPerimeter - c))
print(square)
