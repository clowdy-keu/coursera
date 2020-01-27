'''В кафе мороженое продают по три шарика и по пять шариков.
Можно ли купить ровно k шариков мороженого?

Формат ввода

Вводится число k (целое,положительное)

Формат вывода

Программа должна вывести слово YES,
если при таких условиях можно набрать ровно k шариков (не больше и не меньше)
, в противном случае - вывести NO.
'''
nic = numberIceCream = int(input())
if (nic % 3 == 0) or \
        (nic % 5 == 0) or\
        (nic % 3 == 2 and (nic - 5) % 3 == 0 and (nic - 5) >= 0) or \
        (nic % 3 == 1 and (nic - 10) % 3 == 0 and (nic - 10) >= 0):
    print('YES')
else:
    print('NO')
