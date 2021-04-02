class Employee:
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name


class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.base = base
        self.bonus = bonus

    def pay_calc(self, base, bonus):
        print("=" * 20)
        self.pay = base + bonus
        print("고용형태 : 정규직")
        print("이름 :", self.name)
        print("급여 :", format(self.pay, "3,d"))


class Temporary(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.tpay = tpay
        self.time = time

    def pay_calc(self, tpay, time):
        print("=" * 20)
        self.pay = tpay * time
        print("고용형태 : 임시직")
        print("이름 :", self.name)
        print("급여 :", format(self.pay, "3,d"))


empType = input("고용형태 선택(정규직<P>,임시직<T>) : ")

if empType == "p" or empType == "P":
    name = input("이름 :>?")
    base = int(input("기본급 :>?"))
    bonus = int(input("상여금 :>?"))
    e = Permanent(name)
    e.pay_calc(base, bonus)


elif empType == "t" or empType == "T":
    name = input("이름 :>?")
    time = int(input("작업시간 :>?"))
    tpay = int(input("시급 :>?"))
    e = Temporary(name)
    e.pay_calc(tpay, time)

else:
    print("=" * 30)
    print("입력오류")
