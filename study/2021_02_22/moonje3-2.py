# 한줄로 입력받기
from collections import Counter

t = int(input())
san = []

for i1 in range(t):
    x, y, z = input().split(" ")

    a = int(max(x, y, z))

    li = [x, y, z]
    b = Counter(li)
    c = sorted(b, key=b.get, reverse=True)
    d = c[0]

    if len(b) == 1:
        san.append(10000 + (a * 1000))
    elif len(b) == 2:
        san.append(1000 + (int(d) * 100))
    elif len(b) == 3:
        san.append(a * 100)

print(san)
print(max(san))
