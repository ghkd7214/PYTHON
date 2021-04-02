# x = int(input("height :"))
# y = 0
#
# for i in range(1, x + 1):
#     print("*" * i)
#     y += i
#
# print("별개수 :", y)


x = int(input("height :"))

for i in range(1, x + 1):
    for j in range(i):
        print("*", end="")
    print()
