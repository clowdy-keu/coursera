'''Напишите программу, которая находит в массиве элемент,
самый близкий по величине к данному числу.

Формат ввода

В первой строке задается одно натуральное число N,
не превосходящее 1000 – размер массива.
Во второй строке содержатся N чисел – элементы массива
(целые числа, не превосходящие по модулю 1000).
В третьей строке вводится одно целое число x, не превосходящее по модулю 1000.

Формат вывода

Вывести значение элемента массива, ближайшее к x.
Если таких чисел несколько, выведите любое из них.
'''
numberListElements = int(input())
nearestNumberList = list(map(int, input().split()))
testingNumber = int(input())
bestAttempt = 10000
for number in nearestNumberList:
    if abs(testingNumber - number) < bestAttempt:
        bestAttempt = abs(testingNumber - number)
        bestNumber = number
print(bestNumber)
