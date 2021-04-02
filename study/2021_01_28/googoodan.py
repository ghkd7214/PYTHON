print("구구단\n")

for i in range(2, 10):
    print("  ", i, "단    ")
    for j in range(2, 10):
        print("%d * %d = %d" % (i, j, i * j))
