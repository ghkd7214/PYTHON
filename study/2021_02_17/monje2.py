arr = [4, 4, 4, 3, 3]
d = []

for i in arr:

    if d[-1:] != [i]:
        d.append(i)

print(d)
