print("Enter A")
a = int(input())
print("Enter B")
b = int(input())

while True:
    if a > b:
        print("Error! A must be less than or equal to B")
        print("Re-enter A")
        a = int(input())
    else:
        break

for i in range(a, b + 1):
    print(i)
