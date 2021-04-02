# def Func1(name, *names):
#     print(name)
#     print(names)
#
#
# Func1("홍길동", "이순신", "유관순")
#
# from statistics import mean, variance, stdev
#
#
# def statics(func, *data):  # *하나는 튜플
#     if func == "avg":
#         return mean(data)
#     elif func == "var":
#         return variance(data)
#     elif func == "std":
#         return stdev(data)
#     else:
#         return "TypeError"
#
#
# print("avg=", statics("avg", 1, 2, 3, 4, 5))
# print("var=", statics("var", 1, 2, 3, 4, 5))
# print("std=", statics("std", 1, 2, 3, 4, 5))
# print("asd=", statics("asd", 1, 2, 3, 4, 5))
#
#
# def emp_func(name, age, **other):  # **는 딕트
#     print(name)
#     print(age)
#     print(other)
#
#
# emp_func("홍길동", 35, addr="서울시", height=175, weight=65)


# x = 50
#
#
# def local_func(x):
#     x += 50
#
#
# local_func(x)
# print("x=", x)
#
#
# def global_func():
#     global x
#     x += 50
#
#
# global_func()
# print("x=", x)


# def a():
#     print("a함수")
#
#     def b():
#         print("b함수")
#
#     return b
#
#
# b = a()
# b()


# data = list(range(1, 101))
#
# def outer_func(data):
#     dataSet = data  # 일부러 이래둠 #디버그시 용이
#
#     def tot():
#         tot_val = sum(dataSet)
#         return tot_val
#
#     def avg(tot_val):
#         avg_val = tot_val / len(dataSet)
#         return avg_val
#
#     return tot, avg
#
#
# tot, avg = outer_func(data)  # 내부함수를 인트턴스화함
# print(tot)
#
# tot_val = tot()
# print("tot= ", tot_val)
#
# avg_val = avg(tot_val)
# print("avg= ", avg_val)


# from statistics import mean
# from math import sqrt
#
# data = [4, 5, 3.5, 2.5, 6.3, 5.5]
#
#
# def scattering_func(data):
#     dataset = data
#
#     def avg_func():
#         avg_val = mean(dataset)
#         return avg_val
#
#     def var_func(avg):
#         diff = [(data - avg) ** 2 for data in dataset]
#         # print(sum(diff))
#         var_val = sum(diff) / (len(dataset) - 1)
#         return var_val
#
#     def std_func(var):
#         std_val = sqrt(var)
#         return std_val
#
#     return avg_func, var_func, std_func
#
#
# avg, var, std = scattering_func(data)
#
# print("평균 :", avg())
# print("분산 :", var(avg()))
# print("표준편차 :", std(var(avg())))


def wrap(func):
    def decorated():
        print("반가워요")
        func()
        print("잘가요")

    return decorated


@wrap
def hello():
    print("hi ", "홍길동")


hello()
