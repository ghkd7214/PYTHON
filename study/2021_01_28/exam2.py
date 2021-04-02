while True:
    print("연산할 두 숫자를 입력해주세요 :")
    a = int(input())
    b = int(input())

    print("수행할 연산을 선택해주세요")
    print("1:+, 2:-, 3:*, 4:/, (이외의 것을 입력하면 처음으로 돌아갑니다.)")

    c = int(input())

    if c == 1:
        print(a + b)
    elif c == 2:
        print(a - b)
    elif c == 3:
        print(a * b)
    elif c == 4:
        print(a / b)
    elif c == 0:
        print("프로그램 종료")
        break
    else:
        continue
