def pow_(x, n):
    if n == 1 and n > 0:
        return x
    else:
        return (x * pow_(x, n - 1))

def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

def max2_(a, n):
    if n == 1:
        return a[0]
    x = max2_(a[n//2:], n - n//2)
    return x if x > a[0] else a[0]

def max_(a):
    return max2_(a, len(a))

def task_1(x, n):
    return pow_(x, n)/factorial(n)

def task_2(a):
    return max_(a)

if __name__ == '__main__':
    a = [3, 2, 20, 0]
    print(f"Ответ на задачу 1: {task_1(2, 3)}")
    print(f"Ответ на задачу 2: {task_2(a)}")
