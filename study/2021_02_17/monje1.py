a = int(input())
b = int(input())
t = 0
if a > b:
    a, b = b, a

for i in range(a, b + 1):
    t += i
print(t)