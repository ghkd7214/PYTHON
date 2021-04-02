import random

print(">>숫자 맞추기 게임<<")
com = random.randint(1, 10)

while True:
    my = int(input("예상숫자를 입력하세요. :"))

    if my < com:
        print("그것보다 큽니다.")
    elif my > com:
        print("그것보다 작습니다.")
    else:
        print("정답입니다!")
        break
