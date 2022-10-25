import random
from math import pi, pow, sqrt, sin

"""
3(1). Вычисление площади разных геом.фигур

3(2). Даны 3 различных массива целых чисел (размер <= 15). В каждом найти сумму элементов и мат.ожидание
"""""


def square_area():
    print("Введите сторону квадрата (a) и его диагональ (d) через enter:")
    a = int(input("a = "))
    d = int(input("d = "))

    first = pow(a, 2)
    second = pow(d, 2) / 2

    print(f"Площадь квадрата по формуле S = a^2: {first}"
          f"\nПлощадь квадрата по формуле S = 1/2 * d^2: {second}")


def rhombus_area():
    print(
        "\nВведите длину стороны ромба (a), высоты (h), значение угла между сторонами (alpha), и две диагононали (d1, d2) через enter:")
    a = int(input('a = '))
    h = int(input('h = '))
    alpha = int(input('alpha = '))
    d1 = int(input('d1 = '))
    d2 = int(input('d2 = '))

    first = a * h
    second = pow(a, 2) * sin(alpha)
    third = (d1 * d2) / 2

    print(f'\nПлощадь ромба по формуле S = a * h: {first}'
          f'\nПлощадь ромба по формуле S = a^2 * sin(alpha): {second}'
          f'\nПлощадь ромба по формуле S = 1/2 * d1 * d2: {third}')


def trapezoidal_area():
    print("\nВведите длину оснований трапеции (a, b), высоту (h) и длину боковых сторон (c, d) через enter:")
    a = int(input('a = '))
    b = int(input('b = '))
    h = int(input('h = '))
    c = int(input('c = '))
    d = int(input('d = '))
    p = (a + b + c + d) / 2
    first = ((a + b) / abs(a - b)) * sqrt((p - a) * (p - b) * (p - a - c) * (p - a - d))
    second = 0.5 * (a + b) * h

    print(f'\nПлощадь трапеции по формуле Герона: {first}'
          f'\nПлощадь ромба по формуле S = 1/2*(a+b)*h: {second}')


def circle_area():
    print("\nВведите радиус (r) и диаметр (d) круга через enter:")
    r = int(input('r = '))
    d = int(input('d = '))

    first = pi * pow(r, 2)
    second = (pi * pow(d, 2)) / 4

    print(f'\nПлощадь круга по формуле pi*r^2: {first}'
          f'\nПлощадь круга S = 1/4*pi*d^2: {second}')


def sum_and_mean_arr(arr):
    return sum(arr), sum(arr) / len(arr)


if __name__ == '__main__':
    print('Введите номер задачи (1 или 2) которое нужно запустить:')
    task = int(input())

    if task == 1:
        square_area()
        print(f"\n{'':.^40}")
        rhombus_area()
        print(f"\n{'':.^40}")
        trapezoidal_area()
        print(f"\n{'':.^40}")
        circle_area()

    elif task == 2:
        size_1 = random.randint(1, 15)
        size_3 = random.randint(1, 15)
        size_2 = random.randint(1, 15)

        arr_1 = [random.randint(1, 1000) for el in range(size_1)]
        arr_2 = [random.randint(1, 1000) for el in range(size_2)]
        arr_3 = [random.randint(1, 1000) for el in range(size_3)]

        sum_1, mean_1 = sum_and_mean_arr(arr_1)
        sum_2, mean_2 = sum_and_mean_arr(arr_2)
        sum_3, mean_3 = sum_and_mean_arr(arr_2)

        print(f"Сумма и мат.ожидание первого массива: {sum_1} и {mean_1} соответственно")
        print(f"Сумма и мат.ожидание первого массива: {sum_2} и {mean_2} соответственно")
        print(f"Сумма и мат.ожидание первого массива: {sum_3} и {mean_3} соответственно")
    else:
        print('Такой задачи нет')
