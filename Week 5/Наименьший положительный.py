'''Выведите значение наименьшего из всех положительных элементов в списке.
 Известно, что в списке есть хотя бы один положительный элемент,
 а значения всех элементов списка по модулю не превосходят 1000.

Формат ввода

Вводится список чисел. Все числа списка находятся на одной строке.

Формат вывода

Выведите ответ на задачу.
'''
maxList = list(map(int, input().split()))
currentMinimum = 1001
for index in range(len(maxList)):
    if maxList[index] < currentMinimum and maxList[index] > 0:
        currentMinimum = maxList[index]
print(currentMinimum)
