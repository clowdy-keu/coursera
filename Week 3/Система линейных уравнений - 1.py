'''Даны вещественные числа a, b, c, d, e, f.
Известно, что система линейных уравнений:

ax + by = e

cx + dy = f

имеет ровно одно решение.
Выведите два числа x и y, являющиеся решением этой системы.

Формат ввода

Вводятся шесть чисел a, b, c, d, e, f

- коэффициенты уравнений системы.

Формат вывода

Выведите ответ на задачу.
'''
a, b, c, d, e, f = (float(input()) for _ in range(6))
if a == 0:
    y = round(e / b, 6)
    x = round((f - round(d * y, 6)) / c, 6)
else:
    y = round((round(f * a, 6) - round(c * e, 6)) /
              (round(d * a, 6) - round(b * c, 6)), 6)
    x = round((round(-b * y, 6) + e), 6) / a
print(x, y)


