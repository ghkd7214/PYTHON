n = 10

x = []

while True:

    if n % 3 == 1:
        print(1)
        x.append("1")
    elif n % 3 == 2:
        print(2)
        x.append("2")
    elif n % 3 == 0:
        print(4)
        x.append("4")
    print("n:", n)
    n = int(n / 3)

    if n < 3:
        break

print(x)