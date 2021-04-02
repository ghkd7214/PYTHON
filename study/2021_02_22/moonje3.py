t = int(input())
san = []

for i1 in range(t):
    x = int(input())
    y = int(input())
    z = int(input())

    a = max(x, y, z)
    li = [x, y, z]

    if x == y == z:
        san.append(10000 + (a * 1000))
    elif x == y or x == z or y == z:
        if x == y:
            b = x
        elif x == z:
            b = x
        elif y == z:
            b = y
        san.append(1000 + (b * 100))
    else:
        san.append(a * 100)

print(san)
print(max(san))
