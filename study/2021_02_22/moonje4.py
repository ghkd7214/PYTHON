# n = int(input())

n = 100
num = set(range(2, n + 1))
print(num)
for i in range(2, n + 1):
    # print(i)
    if i in num:
        print(i)
        x = list(range(2 * i, n + 1, i))
        print(x)
        num -= set(range(2 * i, n + 1, i))

# print(num)
# print(len(num))
