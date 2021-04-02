class Person:
    name = None
    gender = None
    age = 0

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def display(self):
        if self.gender == "f":
            __g = "여자"
        else:
            __g = "남자"
        print("이름 :", self.name, ", 성별 :", __g)
        print("나이 :", self.age)


name = input("이름 : ")
age = int(input("나이 : "))
gender = input("성별(m/f) : ")

p = Person(name, gender, age)

p.display()
