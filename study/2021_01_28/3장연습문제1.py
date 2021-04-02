print("짐의 무게는 얼마입니까?")
j = int(int(input()) / 10)
print(j)

if j == 0:
    print("수수료는 없습니다.")
else:
    print("수수료는 %d원입니다." % (j * 10000))
