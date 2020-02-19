'''Штаб гражданской обороны Тридесятой области решил обновить
план спасения на случай ядерной атаки. Известно,
что все n селений Тридесятой области находятся вдоль одной прямой дороги.
Вдоль дороги также расположены m бомбоубежищ,
в которых жители селений могут укрыться на случай ядерной атаки.

Чтобы спасение в случае ядерной тревоги проходило как можно эффективнее,
необходимо для каждого селения определить ближайшее к нему бомбоубежище.

Формат ввода

В первой строке вводится число n - количество селений (1 <= n <= 100000).
Вторая строка содержит n различных целых чисел,
i-е из этих чисел задает расстояние от начала дороги до i-го селения.
В третьей строке входных данных задается число
m - количество бомбоубежищ (1 <= m <= 100000).
Четвертая строка содержит m различных целых чисел,
i-е из этих чисел задает расстояние
от начала дороги до i-го бомбоубежища.
Все расстояния положительны и не превышают 10⁹.
Селение и убежище могут располагаться в одной точке.

Формат вывода

Выведите n чисел - для каждого селения выведите
номер ближайшего к нему бомбоубежища.
Бомбоубежища пронумерованы от 1 до m в том порядке,
в котором они заданы во входных данных.

Указание

Создайте список кортежей из пар (позиция селения, его номер в исходном списке),
а также аналогичный список для бомбоубежищ. Отсортируйте эти списки.

Перебирайте селения в порядке возрастания.

Для селения ближайшими могут быть два соседних бомбоубежища,
среди них надо выбрать ближайшее.
При переходе к следующему селению не обязательно искать
ближайшее бомбоубежище с самого начала.
Его можно искать начиная с позиции, найденной для предыдущего города.
Аналогично, не нужно искать подходящее бомбоубежище
до конца списка бомбоубежищ: достаточно найти самое близкое.
Если Вы неэффективно реализуете эту часть, то решение тесты не пройдет.

Для хранения ответа используйте список, где индекс
будет номером селения, а по этому индексу будет
запоминаться номер бомбоубежища.
'''
citiesNumber = int(input())
citiesPlaceList = list(map(int, input().split()))
shelterNumber = int(input())
shelterPlaceList = list(map(int, input().split()))
cityList = []
shelterList = []
for indexCity in range(citiesNumber):
    cityList.append((citiesPlaceList[indexCity], indexCity))
for indexShelter in range(shelterNumber):
    shelterList.append((shelterPlaceList[indexShelter], indexShelter))
cityList.sort()
shelterList.sort()

resList = [0] * citiesNumber
prFoundedPos = 0
for city in cityList:
    cityPosition = city[0]
    previousShelter = shelterList[prFoundedPos][0]
    currentWay = abs(cityPosition - previousShelter)
    if prFoundedPos < shelterNumber - 1:
        for iShelter in range(prFoundedPos + 1, shelterNumber):
            if abs(cityPosition - shelterList[iShelter][0]) > currentWay:
                resList[city[1]] = shelterList[prFoundedPos][1] + 1
                break
            else:
                currentWay = abs(cityPosition - shelterList[iShelter][0])
                prFoundedPos = iShelter
                if prFoundedPos == shelterNumber - 1:
                    resList[city[1]] = shelterList[prFoundedPos][1] + 1
    else:
        resList[city[1]] = shelterList[prFoundedPos][1] + 1
print(*resList)
