'''Даны два натуральных числа n и m.

Сократите дробь (n / m), то есть выведите два других числа
p и q таких, что (n / m) = (p / q) и дробь (p / q) — несократимая.

Решение оформите в виде функции ReduceFraction(n, m),
получающая значения n и m и возвращающей кортеж из двух чисел:
return p, q.

Тогда вывод можно будет оформить как print(*ReduceFraction(n, m)).

Формат ввода

Вводятся два натуральных числа.

Формат вывода

Выведите ответ на задачу.
'''


def gcd(a, b):
    if a == 1 or b == 1:
        return 1
    if a == 0:
        return b
    if b == 0:
        return a
    if b == a:
        return a
    elif a > b:
        return gcd(b, a % b)
    else:
        return gcd(a, b % a)


def ReduceFraction(n, m):
    devider = gcd(n, m)
    return int(n / devider), int(m / devider)


n, m = (int(input()) for _ in range(2))
a, b = ReduceFraction(n, m)
print(a, b)
