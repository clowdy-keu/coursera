'''Даны действительные коэффициенты a, b, c,
при этом a != 0.
Решите квадратное уравнение ax²+bx+c=0 и выведите все его корни.

Формат ввода

Вводятся три действительных числа.

Формат вывода

Если уравнение имеет два корня,
выведите два корня в порядке возрастания,
если один корень — выведите одно число,
если нет корней — не выводите ничего.
'''
from math import sqrt
a, b, c = (float(input()) for _ in range(3))
discriminant = b ** 2 - 4 * a * c
if discriminant < 0:
    print('')
elif discriminant == 0:
    print(-b / (2 * a))
else:
    x1 = (-b + sqrt(discriminant)) / (2 * a)
    x2 = (-b - sqrt(discriminant)) / (2 * a)
    if x1 < x2:
        print(x1, x2)
    else:
        print(x2, x1)
