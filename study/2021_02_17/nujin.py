sa = int(input("이번 달의 전기사용량을 입력하세요 :"))

gibon = 0
sy = []


def e1(sa):
    sy.append(sa * 52)


def e2(sa):  # 100초과
    sy.append((sa - 100) * 88.5)
    e1(100)


def e3(sa):  # 200초과
    sy.append((sa - 200) * 127.8)
    e2(200)


def e4(sa):  # 300초과
    sy.append((sa - 300) * 184.3)
    e3(300)


def e5(sa):  # 400초과
    sy.append((sa - 400) * 274.3)
    e4(400)


def e6(sa):  # 500초과
    sy.append((sa - 500) * 494.0)
    e5(500)


if sa >= 0:

    if sa > 500:
        gibon = 9330
        e6(sa)

    elif sa > 400:
        gibon = 5130
        e5(sa)

    elif sa > 300:
        gibon = 2710
        e4(sa)

    elif sa > 200:
        gibon = 1130
        e3(sa)

    elif sa > 100:
        gibon = 660
        e2(sa)

    elif sa <= 100:
        gibon = 330
        e1(sa)

sss = sum(sy)  # 전기 사용 요금

se = (gibon + sss) * 0.09

print(gibon)
print(sss)
print(gibon + sss + se)
