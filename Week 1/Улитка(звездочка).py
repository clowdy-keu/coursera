'''Задача со звездочкой.
Улитка ползет по вертикальному шесту высотой H метров,
поднимаясь за день на A метров, а за ночь спускаясь на B метров.
На какой день улитка доползет до вершины шеста?

Формат ввода

Программа получает на вход целые H, A, B.
Гарантируется, что A > B ≥ 0.

Формат вывода

Программа должна вывести одно натуральное число.
'''
stickHeight, upMeters, downMeters = (int(input()) for _ in range(3))
metersPerDay = upMeters - downMeters
distanceBeforeLastLeap = stickHeight - upMeters
howMuchDaysToFinish = distanceBeforeLastLeap // metersPerDay + 1 \
                      + int(bool(distanceBeforeLastLeap % metersPerDay))
print(howMuchDaysToFinish)
