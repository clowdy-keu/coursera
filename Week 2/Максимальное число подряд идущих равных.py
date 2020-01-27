'''Дана последовательность натуральных чисел, завершающаяся числом 0.
Определите, какое наибольшее число подряд идущих
элементов этой последовательности равны друг другу.

Формат ввода

Вводится последовательность натуральных чисел,
оканчивающаяся числом 0 (само число 0 в последовательность не
входит, а служит как признак ее окончания).

Формат вывода

Выведите ответ на задачу.
'''
number = -1
maximumOneByOne = 0
countOneByOne = 1
while number != 0:
    previousNumber = number
    number = int(input())
    if previousNumber == number:
        countOneByOne += 1
    else:
        if countOneByOne > maximumOneByOne:
            maximumOneByOne = countOneByOne
        countOneByOne = 1
print(maximumOneByOne)
