from turtle import *

t = Turtle()
t.screen.setup(800, 800)
t.speed(30)
t.pensize(6)


# голова
t.circle(100)

# левое ухо
t.penup()
t.goto(-40, 200)
t.pendown()
t.right(-70)
t.fillcolor("white")
t.begin_fill()
t.circle(40, 180)
t.end_fill()

# правое ухо
t.penup()
t.goto(30, 200)
t.pendown()
t.left(60)
t.fillcolor("white")
t.begin_fill()
t.circle(40, -180)
t.end_fill()

# глаза
t.penup()
t.goto(-30, 130)
t.pendown()
t.color("pink")
t.begin_fill()
t.circle(15)
t.end_fill()

t.penup()
t.goto(50, 130)
t.pendown()
t.fillcolor("pink")
t.begin_fill()
t.circle(15)
t.end_fill()

# нос
t.penup()
t.goto(10, 90)
t.pendown()
t.fillcolor("pink")
t.begin_fill()
t.circle(10)
t.end_fill()

# рот
t.penup()
t.goto(30, 45)
t.pendown()
t.right(90)
t.circle(50, -100)

# Необходимо, чтобы окно не закрывалось само, а только по клику
t.screen.exitonclick()
t.screen.mainloop()
