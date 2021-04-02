print("사격형의 넓이와 둘레를 계산합니다.")
w = int(input("사각형의 가로 입력 : "))
h = int(input("사각형의 세로 입력 : "))


class Rectangle:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_calc(self):
        area = self.width * self.height
        print("사각형의 넓이 :", area)

    def circum_calc(self):
        cir = (self.width + self.height) * 2
        print("사각형의 둘레 :", cir)


r = Rectangle(w, h)
print("-" * 30)
r.area_calc()
r.circum_calc()
print("-" * 30)
