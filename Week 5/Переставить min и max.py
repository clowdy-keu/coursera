'''В списке все элементы попарно различны.
Поменяйте местами минимальный и максимальный элемент этого списка.

Формат ввода

Вводится список целых чисел.
Все числа списка находятся на одной строке.

Формат вывода

Выведите ответ на задачу.
'''
minMaxList = list(map(int, input().split()))
sortedList = sorted(minMaxList)
iMin = minMaxList.index(sortedList[0])
iMax = minMaxList.index(sortedList[len(minMaxList) - 1])
minMaxList[iMin], minMaxList[iMax] = minMaxList[iMax],  minMaxList[iMin]
print(*minMaxList)
