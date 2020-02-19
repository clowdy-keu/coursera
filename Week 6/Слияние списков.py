'''Даны два целочисленных списка A и B, упорядоченных по неубыванию.
Объедините их в один упорядоченный список С
(то есть он должен содержать len(A)+len(B) элементов).
Решение оформите в виде функции merge(A, B), возвращающей новый список.
Алгоритм должен иметь сложность O(len(A)+len(B)).
Модифицировать исходные списки запрещается.
Использовать функцию sorted и метод sort запрещается.

Формат ввода

Программа получает на вход два неубывающих списка, каждый в отдельной строке.

Формат вывода

Программа должна вывести последовательность неубывающих чисел,
полученных объединением двух данных списков.
'''


def merge(A, B):
    C = []
    indexA = 0
    indexB = 0
    for i in range(len(A + B)):
        if A[indexA] < B[indexB]:
            C.append(A[indexA])
            indexA += 1
            if indexA == len(A):
                for j in range(indexB, len(B)):
                    C.append(B[j])
                break
        else:
            C.append(B[indexB])
            indexB += 1
            if indexB == len(B):
                for j in range(indexA, len(A)):
                    C.append(A[j])
                break
    print(*C)


A = list(map(int, input().split()))
B = list(map(int, input().split()))
merge(A, B)
