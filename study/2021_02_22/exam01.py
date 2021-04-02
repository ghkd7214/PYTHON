# 모듈
import turtle
import returnday

# 터틀 입력창으로 연도 입력 받기 및 터틀 설정
turtle.title("달력 만들기")
turtle.hideturtle()
turtle.tracer(100)
inputYear = int(turtle.numinput("달력 만들기", "표시할 달력의 연도를 입력하시오."))
print("%d" % (inputYear))
print()

# 터틀 창 테두리 꾸미기
turtle.penup()
turtle.pensize(3)
turtle.goto(-457, 387)
turtle.pendown()
turtle.forward(910)
turtle.penup()
turtle.right(90)
turtle.forward(95)
turtle.right(90)
turtle.pendown()
turtle.forward(910)
turtle.penup()

# 달력 연도 꾸미기
turtle.penup()
turtle.goto(440, 308)
turtle.pencolor("black")
turtle.write("Calendar %dy" % (inputYear), align="right", font=("Bahnschrift", 45, "normal"))

# 일 배열 입력
arrayDay = []

for i in range(12):
    arrayDay.append(list(returnday.month_range(inputYear, i + 1)))

print(arrayDay, end="\n\n")

# 월 영어
arrEngMonth = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]

eng_y = 440
indexArrEngMonth = 0

# 월 배열 출력
for i in range(12):
    eng_x = -340
    eng_y -= 220
    for u in range(4):
        if indexArrEngMonth == 12:
            break
        turtle.goto(eng_x, eng_y)
        turtle.pencolor("black")
        turtle.write("%s" % arrEngMonth[indexArrEngMonth], align="center", font=("Bahnschrift", 25, "normal"))
        indexArrEngMonth += 1
        eng_x += 225


# 월별 일 입력 및 출력
arrayCalendarDay = []
eng_weekOfTheDay = ["S", "M", "T", "W", "T", "F", "S"]
arrColor = ["#930000", "black", "black", "black", "black", "black", "#005A81"]

# 리스트 7 * 7 * 12
for mm in range(12):
    for i in range(7):
        arrayCalendarDay.append([None] * 7)

m = 0
nummm = 0
frist_1 = 1
frist_2 = 2
wod_x = -414
wod_y = 190
wod_x_1 = 0
day_y_1 = 165
y_2 = 0

# 달력 출력
for num in range(12):
    day = 1
    isMonth = arrayDay[num][0]  # 1일이 어느 요일에 있는지
    isDay = arrayDay[num][1]  # 그 달이 며칠까지 있는지

    # 4열 출력후 아래로 계속 출력
    if m == 4:
        wod_x = -414
        wod_y -= 218
        day_y_1 -= 218
        m = 0

    # 요일 출력
    for i in range(7):
        arrayCalendarDay[nummm][i] = eng_weekOfTheDay[i]
        turtle.goto(wod_x, wod_y)
        turtle.pencolor(arrColor[i])
        if i == 0:
            wod_x_1 = wod_x
            wod_y_1 = wod_y - 50
        turtle.write("%s" % arrayCalendarDay[nummm][i], align="right", font=("Bahnschrift", 10, "normal"))
        wod_x += 26

    # 월 첫 주 먼저 출력
    for i in range(frist_1, frist_1 + 1):
        # 일 당기기
        day_x_1 = wod_x_1 + isMonth * 26
        for u in range(isMonth, 7):
            arrayCalendarDay[i][u] = day
            turtle.goto(day_x_1, day_y_1)
            turtle.pencolor(arrColor[u])
            turtle.write("%d" % arrayCalendarDay[i][u], align="right", font=("Bahnschrift", 10, "normal"))
            day_x_1 += 26
            day += 1

    # 그다음 출력
    for i in range(frist_2, frist_2 + 5):
        day_x_2 = wod_x_1
        day_y_2 = wod_y_1

        # 일이 해당 일보다 초과하면 다음으로 넘어감
        for u in range(7):
            if day > isDay:
                break
            arrayCalendarDay[i][u] = day
            day += 1
            turtle.goto(day_x_2, day_y_2)
            turtle.pencolor(arrColor[u])
            turtle.write("%d" % arrayCalendarDay[i][u], align="right", font=("Bahnschrift", 10, "normal"))

            day_x_2 += 26
        wod_y_1 -= 25

    wod_x += 40
    nummm += 7
    frist_1 += 7
    frist_2 += 7
    m += 1

print(arrayCalendarDay)
turtle.done()

# #1년 1월 1일 부터 총일 수 구하기
# dayOfWeek = ['일', '월', '화', '수', '목', '금', '토']
# year = 2021
# monthDay = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# month = 2
# total = 0
# yun = 0
# for i in range(1, year):
#     if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0): #윤년
#         total += 366
#     else:
#         total += 365
#
# print(total)
#
# total = total + monthDay[month - 1]
# print(monthDay[month - 1])
# #total
# if month == 2 and ((month % 4 == 0 and month % 100 != 0) or (month % 400 == 0)):
#     total += 1
#
# print(total)
# print("시작요일 -", dayOfWeek[total % 7 + 1])

# import turtle
# t1 = turtle.Turtle()
# t1.penup()
#
# #  write(출력문자, 정렬, font=(글자 폰터, 크기, 스타일)
# cal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# x = 0
# y = 0
#
# for i in range(0, len(cal)):
#
#     if i % 7 == 0: #행과 열을 계산하기 위해서
#         x = 0 #7개 출력하고나면 다시 원위치 해야하므로 x 값 0으로 초기화
#         y = y + 1 #출력해야될 줄은 1줄 증가
#     else:
#         x = x + 1 #한 줄에 7개 출력이 다 되지 않을경우 한 칸씩 옮겨야 하므로 x값 증가
#     t1.goto(45 * x, -45 * y)
#     t1.write(cal[i],  align="right", font=("맑은 고딕", 20, "bold"))
# turtle.done()
