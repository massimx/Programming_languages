"""
1. Вычислить сумму и число положит. эл-тов матрицы находящимися над главной диагональю.
2. Найти в каждой строке матрицы max,min эл-ты и поменять их с первым и последним эл-тами строки соответсвенно.

!!! Организовать файловый i/o: Ввод данных (матриц), вывод результатов.
"""

def scanMatrix():
    with open('pr9_i_november.txt') as file:
        matrix = [list(map(int, row.split())) for row in file.readlines()]
    file.close()
    return matrix

def saveMatrix(matrix):
    with open('pr9_o_november.txt', 'w') as file:
        file.write('\n'.join([' '.join(map(str, row)) for row in matrix]))

def calcMatrix_A(matrix):
    summ = 0
    count = 0

    for row in range(len(matrix)):
        for col in range(row + 1, len(matrix)):
            if matrix[row][col] > 0:
                summ += matrix[row][col]
                count += 1

    return summ, count

def solve_1(A):
    summ_positive_A, count_positive_A = calcMatrix_A(A)
    print(f"\nСумма положительных элементов выше главной диагонали: {summ_positive_A}\n"
          f"Количество положительных элементов выше главной диагонали: {count_positive_A}")
    saveMatrix(A)


def solve_2(B):
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

    saveMatrix(B)

if __name__ == '__main__':
    # N = int(input("Введите N: "))
    # M = int(input("Введите M: "))

    # Решение задачи 1
    # A = scanMatrix()
    # solve_1(A)

    # Решение задачи 2
    B = scanMatrix()
    solve_2(B)
