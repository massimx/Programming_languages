import random

"""
1. Дан одномерный массив, состоящий из N целых элементов.
Ввести массив с клавиатуры. Найти максимальный элемент.
Вывести массив на экран в обратном порядке
"""""


def Filling_array(size):
    arr = []
    for _ in range(size):
        arr.append(int(input()))
    return arr


if __name__ == '__main__':
    print('Введите размер массива:')
    size = int(input())

    print('Введите вариант решения (1 или 2) который нужно запустить:')
    solution = int(input())

    print("Введите элементы массива через enter:")
    array_var1 = Filling_array(size)

    print("Исходный массив: ", array_var1)
    print(f"Максимальный элемент массива: {max(array_var1)}")
    print(f"Перевёрнутый массив: {array_var1[::-1]}")
