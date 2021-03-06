'''Даны два момента времени в пределах одних и тех же суток.
Для каждого момента указан час, минута и секунда.
Известно, что второй момент времени наступил не раньше первого.

Определите сколько секунд прошло между двумя моментами времени.

Формат ввода

Программа на вход получает шесть целых чисел через перевод строки.
Первые три целых числа соответствуют часам, минутам и секундам
первого момента, следующие три числа соответствуют второму моменту.

Часы задаются числом от 0 до 23 включительно.
Минуты и секунды — от 0 до 59.

Формат вывода

Выведите число секунд между этими моментами времени.
'''
hour1, minute1, second1 = (int(input()) for _ in range(3))
hour2, minute2, second2 = (int(input()) for _ in range(3))
firstMomentInSeconds = hour1 * 3600 + minute1 * 60 + second1
secondMomentInSeconds = hour2 * 3600 + minute2 * 60 + second2
print(abs(secondMomentInSeconds - firstMomentInSeconds))
