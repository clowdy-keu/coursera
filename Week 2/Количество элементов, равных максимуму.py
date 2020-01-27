'''Последовательность состоит из натуральных чисел
и завершается числом 0. Определите количество элементов
этой последовательности, которые равны ее наибольшему элементу.

Формат ввода

Вводится последовательность целых чисел,
оканчивающаяся числом 0 (само число 0 в последовательность
не входит, а служит как признак ее окончания).

Формат вывода

Выведите ответ на задачу.
'''
maximumNumber = 0
number = 1
while number != 0:
    number = int(input())
    if number > maximumNumber:
        maximumNumber = number
print(maximumNumber)
