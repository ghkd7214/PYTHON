i = tot = 0
while i < 5:
    i += 1
    tot += i
    print(i, tot)

cnt = tot = 0
data = []
while cnt < 100:
    cnt += 1
    if cnt % 3 == 0:
        tot += cnt
        data.append(cnt)

print("1~100사이의 3배수의 합 = %d" % tot)
print("data =", data)
