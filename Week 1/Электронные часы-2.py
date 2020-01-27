'''Электронные часы показывают время в формате h:mm:ss,
то есть сначала записывается количество часов (число от 0 до 23),
потом обязательно двузначное количество минут, затем обязательно
двузначное количество секунд. Количество минут и секунд
при необходимости дополняются до двузначного числа нулями.

С начала суток прошло N секунд. Выведите, что покажут часы.

Формат ввода

Вводится число N — целое, неотрицательное.

Формат вывода

Выведите показания часов, соблюдая формат.

Примечания

Вывести числа можно поциферно.
'''
secondFromDayBegin = int(input()) % 86400
hours = secondFromDayBegin // 3600
surplus = secondFromDayBegin - hours * 3600
tensOfMinutes = surplus // 600
surplus = surplus - tensOfMinutes * 600
onesOfMinutes = surplus // 60
surplus = surplus - onesOfMinutes * 60
tensOfSeconds = surplus // 10
surplus = surplus - tensOfSeconds * 10
onesOfSeconds = surplus
print('{}:{}{}:{}{}'.format(hours,
                            tensOfMinutes,
                            onesOfMinutes,
                            tensOfSeconds,
                            onesOfSeconds))
