x = int(input())
y = input()
q, w = 0

for i in range(x):
    if y[i] == "A":  # if "A" in y:
        q += 1
    else:  # if "B" in y:
        w += 1

if q > w:
    print("A")
elif q == w:
    print("Tie")
else:
    print("B")
