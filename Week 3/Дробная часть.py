'''Дано положительное действительное число X.
Выведите его дробную часть.

Формат ввода

Вводится положительное действительное число.

Формат вывода

Выведите ответ на задачу.
'''
x = float(input())
fractionPart = x - int(x)
print(fractionPart)
