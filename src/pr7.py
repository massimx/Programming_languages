import random

"""
2. В массиве действительных чисел все нулевые элементы заменить на мат.ожидание всех элементов массива
"""""


def mean_arr(arr):
    return sum(arr) / len(arr)


def array_change(arr, zero_number):
    mean = mean_arr(arr)
    # Заполнение массива нулями
    for idx in range(len(arr)):
        random_idx = random.randint(0, len(arr))
        if zero_number == 0:
            break
        arr.insert(random_idx, 0)
        zero_number -= 1
    print(f"\nModified array step 1:\n{arr}")

    print(f"\nExpected value of the array: {mean}\n")
    # Замена нулей на мат.ожидание
    for idx in range(len(arr)):
        if arr[idx] == 0:
            arr[idx] = mean
    print(f"Modified array step 2:\n{arr}")
    return arr


if __name__ == '__main__':
    print("Введите размер массива")
    size = int(input())
    array = [random.randint(1, 1000) for el in range(size)]

    print("Сколько нулей нужно добавить в массив?")
    zero_number = int(input())

    new_array = array_change(array, zero_number)
