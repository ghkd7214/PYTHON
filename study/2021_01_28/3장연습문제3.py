nu = 0
for i in range(3, 100, 3):
    if i % 2 != 0:
        print(i, end=" ")

        nu = nu + i
print()
print(nu)
