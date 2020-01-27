'''Напишите программу, которая по данному числу N от 1 до 9 выводит на экран N пингвинов.
Изображение одного пингвина имеет размер 5×9 символов, между двумя соседними пингвинами
также имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после
последнего пингвина. Для упрощения рисования скопируйте пингвина из примера в среду разработки.
   _~_
  (o o)
 /  V  \
/(  _  )\
  ^^ ^^

Формат ввода

Вводится натуральное число.

Формат вывода

Выведите ответ на задачу.
'''
penguinsCount = int(input())
print('   _~_    ' * penguinsCount)
print('  (o o)   ' * penguinsCount)
print(' /  V  \  ' * penguinsCount)
print('/(  _  )\ ' * penguinsCount)
print('  ^^ ^^   ' * penguinsCount)
