'''За день машина проезжает N километров.
Сколько дней нужно, чтобы проехать маршрут длиной M километров?

Формат ввода

Программа получает на вход числа N и M (целые, положительные).

Формат вывода

Выведите ответ на задачу.
'''
kilometersPerDay, distance = int(input()), int(input())
print(distance // kilometersPerDay + int(bool(distance % kilometersPerDay)))
