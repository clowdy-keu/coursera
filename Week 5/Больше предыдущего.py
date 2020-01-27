'''Дан список чисел. Выведите все элементы списка,
которые больше предыдущего элемента.

Формат ввода

Вводится список чисел. Все числа списка находятся на одной строке.

Формат вывода

Выведите ответ на задачу.
'''
biggerThenLastList = list(map(int, input().split()))
for index in range(len(biggerThenLastList) - 1):
    if biggerThenLastList[index] < biggerThenLastList[index + 1]:
        print(biggerThenLastList[index + 1], end=' ')
