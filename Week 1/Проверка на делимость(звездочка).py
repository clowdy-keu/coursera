'''Задача со звездочкой.
В этой задаче необходимо проверить,
делится ли число A на число B нацело.
Использовать можно только арифметические операции,
использование любых видов ветвлений, функций и т.п. запрещено.

Формат ввода

Вводятся два натуральных числа A и B.

Формат вывода

Выведите "YES", если A кратно B и "NO" в противном случае.
'''
a, b = (int(input()) for _ in range(2))
print("YES" * int(not(bool(a % b))))
print("NO" * int(bool(a % b)))
