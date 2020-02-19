'''Дан список из N (N≤2*10⁵) элементов,
которые принимают целые значения от 0 до 100 (100 включая).

Отсортируйте этот список в порядке неубывания элементов.
Выведите полученный список.

Решение оформите в виде функции CountSort(A),
которая модифицирует передаваемый ей список.
Использовать встроенные функции сортировки нельзя.
'''


def CountSort(A):
    i = 0
    countList = [0] * 101
    for now in A:
        countList[now] += 1
    for mean in range(101):
        while countList[mean]:
            A[i] = mean
            countList[mean] -= 1
            i += 1
    return A


listForSort = list(map(int, input().split()))
print(*CountSort(listForSort))
