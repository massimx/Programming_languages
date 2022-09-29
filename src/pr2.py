from math import cos, sin


def task_1(x, y, z):
    return (2 * cos(x - 2 / 3) / (1 / 2 + pow(sin(y), 2))) * (1 + (pow(z, 2) / 3 - (pow(z, 2) / 5)))


x = 14.26
y = -1.22
z = 3.5 * pow(10, -2)

s = task_1(x, y, z)

print("s = {0:.2f}".format(s))

