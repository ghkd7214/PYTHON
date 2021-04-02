t = int(input())

for i1 in range(t):
    a = int(input())
    b = int(input())

    for i in range(b, (a * b) + 1):
        if i % a == 0 and i % b == 0:
            print(i)
            break
