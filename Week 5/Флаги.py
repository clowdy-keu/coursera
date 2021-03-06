'''Напишите программу, которая по данному числу n
от 1 до 9 выводит на экран n флагов.
Изображение одного флага имеет размер 4×4 символов,
между двумя соседними флагами также имеется пустой (из пробелов) столбец.
Разрешается вывести пустой столбец после последнего флага.
Внутри каждого флага должен быть записан его номер — число от 1 до n.

Формат ввода

Вводится натуральное число.

Формат вывода

Выведите ответ на задачу.
'''
flagsCount = int(input())
print("+___ " * flagsCount)
for currentFlag in range(flagsCount):
    flagString = "|" + str(currentFlag + 1) + " / "
    print(flagString, end='')
print()
print("|__\\ " * flagsCount)
print("|    " * flagsCount)
