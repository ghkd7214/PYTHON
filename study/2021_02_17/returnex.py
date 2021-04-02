# def mul(num, n):
#     for i in range(n):
#         print(num * (i + 1), end=" ")
#
#
# mul(num, n)

def mul(num, n):
    t = []
    for i in range(1, n + 1):
        t.append(i * num)
    return t


r1, r2, r3, r4, r5 = mul(2, 5)
