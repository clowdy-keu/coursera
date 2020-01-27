'''Есть две коробки, первая размером A₁×B₁×C₁,
вторая размером A₂×B₂×C₂.
Определите, можно ли разместить одну из этих коробок
внутри другой, при условии, что поворачивать коробки можно
только на 90 градусов вокруг ребер.

Формат ввода

Программа получает на вход числа A₁,B₁,C₁,A₂,B₂,C₂.

Формат вывода

Программа должна вывести одну из следующих строчек:

Boxes are equal, если коробки одинаковые,

The first box is smaller than the second one,
если первая коробка может быть положена во вторую,

The first box is larger than the second one,
если вторая коробка может быть положена в первую,

Boxes are incomparable, во всех остальных случаях.
'''


def sortBoxesUp(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return (a, b, c)


box1a, box1b, box1c, box2a, box2b, box2c = (int(input()) for _ in range(6))
box1a, box1b, box1c = sortBoxesUp(box1a, box1b, box1c)
box2a, box2b, box2c = sortBoxesUp(box2a, box2b, box2c)
if box1a == box2a and box1b == box2b and box1c == box2c:
    print('Boxes are equal')
elif box1a <= box2a and box1b <= box2b and box1c <= box2c:
    print('The first box is smaller than the second one')
elif box1a >= box2a and box1b >= box2b and box1c >= box2c:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
