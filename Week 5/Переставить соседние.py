'''Переставьте соседние элементы списка
(A[0] c A[1],A[2] c A[3] и т.д.).
Если элементов нечетное число, то последний элемент остается на своем месте.

Формат ввода

Вводится список чисел. Все числа списка находятся на одной строке.

Формат вывода

Выведите ответ на задачу.
'''
arrangeEvenElementsList = list(map(int, input().split()))
for i in range(len(arrangeEvenElementsList)):
    if i % 2 == 1:
        arrangeEvenElementsList[i], arrangeEvenElementsList[i - 1] \
            = arrangeEvenElementsList[i - 1], arrangeEvenElementsList[i]
print(*arrangeEvenElementsList)
