import turtle

t = turtle.Turtle()
t2 = turtle.Turtle()
t2.hideturtle()
screen = t.getscreen()
c = 0
color = ["red", "#00FF00", "blue"]

t.color("#FF0000")
t.shape("turtle")
t.speed(0)
# t.ondrag(t.goto)

t2.penup()
t2.goto(-400, -370)
t2.write("c : color change  o : draw circle  z : undo  q : quit  t : clear", font=20)
t2.goto(-400, -390)
t2.color("red")
t2.write("red", font=20)


def left():
    t.left(30)


def right():
    t.right(30)


def up():
    t.forward(30)


def down():
    t.backward(30)


def circle():
    t.circle(30)


def undo():
    t.undo()


def space():
    if t.isdown():
        t.penup()
    else:
        t.pendown()


def change():
    global c
    c += 1

    if c % 3 == 0:
        t.color(color[0])
        printcolor()
    elif c % 3 == 1:
        t.color(color[1])
        printcolor()
    else:
        t.color(color[2])
        printcolor()


def end():
    screen.bye()


def dragging(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)


def printcolor():
    if c % 3 == 0:
        t2.color("#FFFFFF")
        t2.write(color[2], font=20)
        t2.color(color[0])
        t2.write(color[0], font=20)

    elif c % 3 == 1:
        t2.color("#FFFFFF")
        t2.write(color[0], font=20)
        t2.color(color[1])
        t2.write("green", font=20)
    else:
        t2.color("#FFFFFF")
        t2.write("green", font=20)
        t2.color(color[2])
        t2.write(color[2], font=20)


def sclear():
    t.clear()

screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(circle, "o")
screen.onkeypress(undo, "z")
screen.onkeypress(space, "space")
screen.onkeypress(end, "q")
screen.onkeypress(change, "c")
screen.onkeypress(sclear, "t")
screen.listen()
t.ondrag(dragging)
screen.mainloop()
