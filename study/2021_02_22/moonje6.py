a = int(input("년도 입력"))  # 년도
b = int(input("월 입력"))  # 월

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    month[1] = 29

yun = (a - 1) // 4 - (a - 1) // 100 + (a - 1) // 400
total = (a - 1) * 365 + yun

yo1 = total % 7
d = 0

print(f"          {a}년")
for k in range(12):
    if k + 1 == b:
        yo2 = (yo1 + d) + 1
        print(f"************{k + 1}월***********")
        print("일\t월\t화\t수\t목\t금\t토")
        print("\t" * (yo2 % 7), end="")

        for i in range(1, month[k] + 1):
            print(i, end="\t")
            yo2 += 1
            if yo2 % 7 == 0:
                print()
    d += month[k]
