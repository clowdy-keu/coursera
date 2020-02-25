'''Задается действительное число, десятичный логарифм которого
необходимо посчитать, и точность вычислений.
Выводится десятичный логарифм действительного числа.
'''


def DecLog(number, accuracy):
    nextDig, normNum = Normalize(number)
    result = str(nextDig) + '.'
    for step in range(accuracy):
        normNum **= 10
        nextDig, normNum = Normalize(normNum)
        result += str(nextDig)
    return float(result)


def Normalize(number):
    devCount = 0
    while number >= 10:
        number /= 10
        devCount += 1
    return devCount, number


exceptTextNum = "Некорректно введенно число"
exceptTextAcc = "Некорректно введена точность"
while True:
    data = input("Пожалуйста, введите число и точность вычисления: ").split()
    try:
        number = float(data[0])
        if number <= 0:
            raise Exception
    except:
        print(exceptTextNum)
        continue
    try:
        accuracy = int(data[1])
        if accuracy < 0:
            raise Exception
        break
    except:
        print(exceptTextAcc)
countForBelowOne = 0
while number < 1:
    number *= 10
    countForBelowOne += 1
print(DecLog(number, accuracy) - countForBelowOne)
