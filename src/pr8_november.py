"""
1. Вычислить сумму и число положит. эл-тов матрицы находящимися над главной диагональю.
2. Найти в каждой строке матрицы max,min эл-ты и поменять их с первым и последним эл-тами строки соответсвенно.
"""
import random
from random import randint

def printMatrix(matrix):
    for row in matrix:
        for el in row:
            print(el, end=' ')
        print()

def calcMatrix_A(matrix, N):
    summ = 0
    count = 0

    for row in range(N):
        for col in range(row + 1, N):
            if matrix[row][col] > 0:
                summ += matrix[row][col]
                count += 1

    return summ, count

def solve_1(N, A):
    summ_positive_A, count_positive_A = calcMatrix_A(A, N)

    printMatrix(A)
    print(f"\nСумма положительных элементов выше главной диагонали: {summ_positive_A}\n"
          f"Количество положительных элементов выше главной диагонали: {count_positive_A}")

def solve_2(B):
    printMatrix(B)
    # поиск индексов max и min эл-та
    for i, row in enumerate(B):
        max_ = min_ = 0
        for j, elem in enumerate(row):
            if elem > row[max_]:
                max_ = j
            if elem < row[min_]:
                min_ = j


        # swap элементы
        row[max_], row[0] = row[0], row[max_]
        row[min_], row[-1] = row[-1], row[min_]

    print()
    printMatrix(B)

if __name__ == '__main__':
    # N = int(input("Введите N: "))
    # M = int(input("Введите M: "))
    N = 3
    M = 5

    A = [[randint(-20, 20) for _ in range(N)] for _ in range(N)]
    B = [[random.randrange(10) for i in range(M)] for j in range(N)]
    # Решение задачи 1
    print("Задача 1\n")
    solve_1(N, A)

    # Решение задачи 2
    print("Задача 2\n")
    solve_2(B)
