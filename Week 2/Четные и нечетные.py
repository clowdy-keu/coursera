'''Даны три целых числа A, B, C.
Определить, есть ли среди них хотя бы одно четное и хотя бы одно нечетное.

Формат ввода

Числа A, B, C, не превышающие по модулю 10000.

Формат вывода

Одна строка – "YES" или "NO".
'''
a, b, c = (int(input()) for _ in range(3))
haveOdd, haveEven = False, False
if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    haveEven = True
if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
    haveOdd = True
if haveEven and haveOdd:
    print('YES')
else:
    print('NO')
