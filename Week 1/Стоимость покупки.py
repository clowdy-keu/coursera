'''Пирожок в столовой стоит A рублей и B копеек.
Определите, сколько рублей и копеек нужно заплатить за N пирожков.

Формат ввода

Программа получает на вход три числа:
A, B, N — целые, неотрицательные, не превышают 10000.

Формат вывода

Программа должна вывести два числа: стоимость покупки в рублях и копейках.
'''
priceRubles, pricePennies, numberOfPies = (int(input()) for _ in range(3))
priceOfPieInPennies = pricePennies + priceRubles * 100
totalPrice = priceOfPieInPennies * numberOfPies
totalPricePennies = totalPrice % 100
totalPriceRubles = totalPrice // 100
print(totalPriceRubles, totalPricePennies)
