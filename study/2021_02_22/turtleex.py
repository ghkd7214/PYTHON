import turtle as t
import math

a = t.Turtle()

a.pensize(4)

a.penup()
a.setposition(-300, 200)
a.pendown()
a.circle(60)
a.penup()

a.setposition(-450, -100)
a.pendown()
a.forward(900)
a.penup()

a.setposition(-100, -80)
a.pendown()
a.setheading(90)
a.forward(150)
a.rt(90)
a.forward(100)
a.rt(90)
a.forward(150)
a.penup()

a.setposition(70, -80)
a.pendown()
a.setheading(90)
a.forward(300)
a.rt(90)
a.forward(100)
a.rt(90)
a.forward(300)

# for i in range(5):
#     a.forward(100)
#     a.rt(144)

t.mainloop()
