import turtle as t

# a = int(input("년도 입력"))  # 년도
# b = int(input("월 입력"))  # 월


z = t.Turtle()
# t.tracer(1000)
z.pensize(2)
z.hideturtle()

a = 2021
b = 2

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    month[1] = 29

yun = (a - 1) // 4 - (a - 1) // 100 + (a - 1) // 400
total = (a - 1) * 365 + yun

yo1 = total % 7
d = 0
z.penup()
z.goto(-200, 100)

x = -200
y = 80
y_he = 20

z.write(f"{a}년")
z.goto(x, y)
for k in range(12):
    if k + 1 == b:
        yo2 = (yo1 + d) + 1
        z.write(f"\t\t\t{k + 1}월")
        z.goto(x, y - (1 * y_he))
        z.write("일\t월\t화\t수\t목\t금\t토")
        z.goto(x, y - (2 * y_he))
        y -= y_he * 3

        for i in range(1, month[k] + 1):
            z.goto(x + (yo2 % 7) * 48, y)
            z.color("black")
            if yo2 % 7 == 0:
                z.color("red")
            z.write(i)
            yo2 += 1
            if yo2 % 7 == 0:
                y -= 20
                z.goto(x, y)

    d += month[k]

t.mainloop()
