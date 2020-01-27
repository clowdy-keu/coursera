'''В доме несколько подъездов.
В каждом подъезде одинаковое количество квартир.
Квартиры нумеруются подряд, начиная с единицы.
Может ли в некотором подъезде первая квартира иметь номер x,
а последняя – номер y?

Формат ввода

Вводятся два натуральных числа x и y (x ≤ y).

Формат вывода

Выведите слово YES (заглавными латинскими буквами),
если такое возможно, и NO в противном случае.
'''
firstAppartments, lastAppartments = (int(input()) for _ in range(2))
numberAppartmentsInDoorway = lastAppartments - firstAppartments + 1
if (firstAppartments - 1) % numberAppartmentsInDoorway == 0:
    print('YES')
else:
    print('NO')
