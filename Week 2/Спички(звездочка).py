'''Вдоль прямой выложены три спички.
Необходимо переложить одну из них так,
чтобы при поджигании любой спички сгорали все три.
Для того чтобы огонь переходил с одной спички на другую,
 необходимо чтобы эти спички соприкасались (хотя бы концами).

Требуется написать программу, определяющую,
какую из трех спичек необходимо переместить.

Формат ввода

Вводятся шесть целых чисел :
 l₁, r₁, l₂, r₂, l₃, r₃ – координаты первой,
 второй и третьей спичек соответственно (0 ≤ lᵢ < rᵢ ≤ 100).
 Каждая спичка описывается координатами
 левого и правого концов по горизонтальной оси OX.

Формат вывода

Выведите номер искомой спички.
Если возможных ответов несколько,
то выведите наименьший из них (наименьший по номеру спички).
В случае, когда нет необходимости перемещать какую-либо спичку,
выведите 0. Если же требуемого результата
достигнуть невозможно, то выведите -1.
'''
# left1, right1, left2, right2, left3, right3 = (int(input()) for _ in range(6))
#
#
#
# matches = [left1, right1, left2, right2, left3, right3]
setMatches = [[0, 2, 4, 5, 3, 6], [1, 2, 9, 10, 12, 20], [1, 5, 0, 1, 4, 8]]
for matches in setMatches:
    firstTouchSecond = matches[1] > matches[2]
    firstTouchThird = matches[1] > matches[4]
    secondTouchFirst = matches[3] > matches[0]
    secondTouchThird = matches[3] > matches[4]
    thirdTouchFirst = matches[5] > matches[0]
    thirdTouchSecond = matches[5] > matches[2]
    print(firstTouchSecond, firstTouchThird, secondTouchFirst, secondTouchThird, thirdTouchFirst, thirdTouchSecond)












# if matches[0] > matches[2]:
#     matches[0], matches[2], matches[1], matches[3] = matches[2], matches[0], matches[3], matches[1]
# if matches[2] > matches[4]:
#     matches[2], matches[4], matches[3], matches[5] = matches[4], matches[2], matches[5], matches[3]
# if matches[0] > matches[2]:
#     matches[0], matches[2], matches[1], matches[3] = matches[2], matches[0], matches[3], matches[1]
#
# length = [right - left for right, left in zip(matches[1::2], matches[0::2])]
#
# if matches[2] <= matches[1] and matches[4] <= matches[3]:
#     print('0')
# elif matches[2] <= matches[1]:
#     print('3')
# elif matches[4] <= matches[3]:
#     print('1')