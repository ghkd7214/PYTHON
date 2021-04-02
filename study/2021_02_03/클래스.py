# def calc_func(a, b):
#     x = a
#     y = b
#
#     def plus():
#         p = x + y
#         return p
#
#     def minus():
#         m = x - y
#         return m
#
#     return plus, minus
#
#
# p, m = calc_func(10, 20)
# print("plus :", p())
# print("minus :", m())
#
#
# class calc_class:
#     x = y = 0
#
#     def __init__(self, a, b):
#         self.x = a
#         self.y = b
#
#     def plus(self):
#         p = self.x + self.y
#         return p
#
#     def minus(self):
#         m = self.x - self.y
#         return m
#
#
# obj = calc_class(10, 20)
#
# print("plus =", obj.plus())
# print("minus =", obj.minus())


# class Account:
#     __balance = 0
#     __accName = None
#     __accNo = None
#
#     def __init__(self, bal, name, no):
#         self.__balance = bal
#         self.__accName = name
#         self.__accNo = no
#
#     def getBalance(self):
#         return self.__balance, self.__accName, self.__accNo
#
#     def deposit(self, money):
#         if money < 0:
#             print("금액확인")
#             return
#         self.__balance += money
#
#     def withdraw(self, money):
#         if self.__balance < money:
#             print("잔액부족")
#             return
#         self.__balance -= money
#
#
# acc = Account(100, "홍길동", "125-152-4125-41")
#
# # acc.__balance
# bal = acc.getBalance()
# print("계좌정보 :", bal)
#
# acc.deposit(10000)
# bal = acc.getBalance()
# print("계좌정보 :", bal)


# class Super:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print("name :", self.name, ", age :", self.age)
#
#
# sup = Super("부모", 55)
# sup.display()
#
#
# class Sub(Super):       #상속받는 법
#     gender = None
#
#     def __init__(self, name, age, gender):
#         # self.name = name
#         # self.age = age
#         super().__init__(name, age)     # super 함수를 통해서 부모의 생성자를 호출할 수 있음
#         self.gender = gender
#
#     def display(self):
#         print("name :", self.name, ", age :", self.age, ", gender :", self.gender)
#
#
# sub = Sub("자식", 25, "여자")
# sub.display()


class Employee:
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name

    def pay_calc(self):
        pass


class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, base, bonus):
        self.pay = base + bonus
        print("총수령액 :", format(self.pay, "3,d"), "원")


class Temporary(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, tpay, time):
        self.pay = tpay * time
        print("총수령액 :", format(self.pay, "3,d"), "원")


p = Permanent("이순신")
p.pay_calc(3000000, 200000)

t = Temporary("홍길동")
t.pay_calc(15000, 80)


