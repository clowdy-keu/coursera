'''Для быстрого вычисления наибольшего общего делителя двух чисел
используют алгоритм Евклида. Он построен на следующем соотношении:
НОД(a,b)=НОД(b,a % b).

Реализуйте рекурсивный алгоритм Евклида в виде функции gcd(a, b).

Формат ввода

Вводится два целых положительных числа.

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


a, b = (int(input()) for _ in range(2))
print(gcd(a, b))
