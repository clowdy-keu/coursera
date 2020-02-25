'''Задается натуральное число n, факториал которого
труебется посчитать.
Выводится факториал числа.
'''


def FactorialRec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * FactorialRec(n - 1)


exceptText = "Программа считает факториал натуральных чисел"
while True:
    n = input("Пожалуйста, введите натуральное число: ")
    try:
        n = int(n)
        if n < 0:
            raise Exception
        break
    except:
        print(exceptText)
try:
    print("Факторил {} равен {}".format(n, FactorialRec(n)))
except:
    print("Большое значение, выберите поменьше")
