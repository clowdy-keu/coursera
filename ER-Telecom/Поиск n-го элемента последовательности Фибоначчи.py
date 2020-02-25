'''Задается натуральное число n - позиция
искомого элемента последовательности.
Выводится элемент последовательности.
'''


def FibPositionRec(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return FibPositionRec(n - 1) + FibPositionRec(n - 2)


exceptText = "Позиция элемента должна быть натуральным числом"
while True:
    n = input("Пожалуйста, введите позицию элемента: ")
    try:
        n = int(n)
        if n < 0:
            raise Exception
        break
    except:
        print(exceptText)
try:
    print("На позиции {} находится число {}".format(n, FibPositionRec(n)))
except:
    print("Большое значение позиции, выберите поменьше")


