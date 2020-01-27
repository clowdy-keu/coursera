'''Задача со звездочкой.
Решить в целых числах уравнение: (ax+b) / (cx+d) =0

Формат ввода

Вводятся 4 числа: a,b,c,d; c и d не равны нулю одновременно.

Формат вывода

Необходимо вывести все решения, если их число конечно,
“NO” (без кавычек), если решений нет,
и “INF” (без кавычек), если решений бесконечно много.
'''
a, b, c, d = (int(input()) for _ in range(4))
if a == 0 and b != 0:
    print('NO')
else:
    if a == 0 and b == 0:
        if c == 0:
            print('NO')
        else:
            if d % c == 0:
                print('INF')
            else:
                print('NO')
    else:
        if b % a == 0:
            x = int(-b / a)
            if c * x + d == 0:
                print('NO')
            else:
                print(x)
        else:
            print('NO')
