'''За многие годы заточения узник замка Иф
проделал в стене прямоугольное отверстие размером D×E.
Замок Иф сложен из кирпичей, размером A×B×C.
Определите, сможет ли узник выбрасывать кирпичи в море через это отверстие
(очевидно, стороны кирпича должны быть параллельны сторонам отверстия).

Формат ввода

Программа получает на вход числа A, B, C, D, E.

Формат вывода

Программа должна вывести слово YES или NO.
'''


def sortBricksUp(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return (a, b, c)


brickA, brickB, brickC = (int(input()) for _ in range(3))
brickA, brickB, brickC = sortBricksUp(brickA, brickB, brickC)
wallA, wallB = (int(input()) for _ in range(2))
if wallA > wallB:
    wallA, wallB = wallB, wallA
if brickA <= wallA and brickB <= wallB:
    print('YES')
else:
    print('NO')
