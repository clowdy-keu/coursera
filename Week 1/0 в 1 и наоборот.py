'''Вводится число 0 или 1, необходимо вывести 1 или 0 соответственно.

Формат ввода

Число 0 или 1.

Формат вывода

Число 0 или 1.
'''
numberZeroOrOne = int(input())
print(int(not bool(numberZeroOrOne)))
