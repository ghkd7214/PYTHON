# num = input("숫자입력 :")
# print("num type :", type(num))
# print("num =", num)
# print("num =", num * 2)
#
# num1 = int(input("숫자입력 :"))
# print("num1 =", num1 * 2)
#
# num2 = float(input("숫자입력 :"))
# rs = num1 + num2
# print("rs =", rs)

# print("value =", 10 + 20 + 30 + +40 + 50)
# print("010", "1234", "5678", sep="-")
# print("가나다", 20, end=", ")
# print("라마바", 10)

# print("원주율 =", format(3.14159, "8.3f"))
# print("금액 =", format(10000, "10d"))
# print("금액 =", format(125000, "3,d"))

# name = "홍길동"
# age = 35
# price = 123.456
# print("이름 : %s,나이 : %d,data : %.2f" % (name, age, price))
#
# print("이름 : {},나이 :{},data : {}".format(name, age, price))
# print("이름 : {1},나이 :{0},data : {2}".format(age, name, price))

# string = "python"
# print(string[0])
# print(string[5])
# print(string[-1])
# print(string[-6])
#
# print("python" + " program")
# # print("python" + 3.7 + ".exe")
# print("python-" + str(3.7) + ".exe")

oneline = "this is one line string"

print(oneline.replace("this", "that"))
sent = oneline.split(" ")
print("스플릿 =", sent)

sent2 = ",".join(sent)
print(sent2)
