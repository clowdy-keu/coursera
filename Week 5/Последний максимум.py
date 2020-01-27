'''Найдите наибольшее значение в списке и индекс последнего элемента,
который имеет данное значение за один проход по списку,
не модифицируя этот список и не используя дополнительного списка.

Выведите два значения.
'''
maxList = list(map(int, input().split()))
currentMaximum = maxList[0]
indexMaximum = 0
for index in range(len(maxList)):
    if maxList[index] >= currentMaximum:
        currentMaximum = maxList[index]
        indexMaximum = index
print(currentMaximum, indexMaximum)
