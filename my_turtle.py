import turtle
a=turtle.Turtle()
a.screen.bgcolor("black")
a.hideturtle()
def f():
    a.pencolor("blue")
    a.setheading(90)
    a.forward(30)
def f1():
    a.pencolor("lightgreen")
    a.setheading(360)
    a.forward(30)
def f2():
    a.pencolor("purple")
    a.setheading(180)
    a.forward(30)
    a.screen.onkeypress(f,"RM")
def f3():
    a.pencolor("white")
    a.setheading(270)
    a.forward(30)
a.screen.onkeypress(f,"Up")
a.screen.onkeypress(f3,"Down")
a.screen.onkeypress(f2,"Left")
a.screen.onkeypress(f1,"Right")
a.hideturtle()

a.screen.listen()
#make pen up by click of mouse button and do more stuff
