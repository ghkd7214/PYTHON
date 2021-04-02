import random

i = []
j = []
rs = 0

while True:
    h = (random.randint(1, 45))

    if h in i:
        continue

    else:
        i.append(h)

    if len(i) == 6:
        break

i.sort()

print(i)

for a in range(6):
    k = int(input("로또 번호를 입력하세요 1 ~ 45\n"))

    j.append(k)

j.sort()
print("로또번호", i)
print("입력번호", j)

for a in range(6):
    if j[a] in i:
        rs += 1
print(rs)

if rs == 6:
    print("1등당첨입니다")
elif rs == 5:
    print("2등당첨입니다")
elif rs == 4:
    print("3등당첨입니다")
elif rs == 3:
    print("4등당첨입니다")
else:
    print("꽝입니다")
