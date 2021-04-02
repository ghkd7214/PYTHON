# x = [100, 30, 25.2, "num", 14, 51]
# for i in x:
#     print(i)
#     try:
#         y = i ** 2
#         print("y =", y)
#     except:
#         print("숫자아님", i)


try:
    div = 1000 / 2.53
    print("div =%5.2f" % (div))
    div = 1000 / 0
    f = open("c:/test.txt")
    num = int(input("숫자입력 :"))

    print("num =", num)

except ZeroDivisionError as er:
    print("오류정보 :", er)
except FileNotFoundError as er:
    print("오류정보 :", er)
except Exception as er:
    print("오류정보 :", er)
finally:
    print("finally 항상 실행됨")
