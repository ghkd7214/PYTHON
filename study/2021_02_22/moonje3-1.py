#더러움 해소
from collections import Counter

t = int(input())
san = []

for i1 in range(t):
    x = int(input())
    y = int(input())
    z = int(input())

    a = int(max(x, y, z))
    li = [x, y, z]
    b = Counter(li)
    c = sorted(b, key=b.get, reverse=True)
    print(c)
    d = c[0]

    if len(b) == 1:
        san.append(10000 + (a * 1000))
    elif len(b) == 2:
        san.append(1000 + (d * 100))
    elif len(b) == 3:
        san.append(a * 100)

print(san)
print(max(san))
