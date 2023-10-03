from turtle import *


def redlight_on():
    #red
    color("red")
    penup()
    goto(0, 100)
    pendown()
    begin_fill()
    circle(35)
    end_fill()

    #yellow
    color("yellow")
    penup()
    goto(0, 0)
    pendown()
    circle(35)

    #green
    color("green")
    penup()
    goto(0, -100)
    pendown()
    circle(35)


def yellowlight_on():
    #red
    color("red")
    penup()
    goto(0, 100)
    pendown()
    circle(35)

    #yellow
    color("yellow")
    penup()
    goto(0, 0)
    pendown()
    begin_fill()
    circle(35)
    end_fill()

    #green
    color("green")
    penup()
    goto(0, -100)
    pendown()
    circle(35)


def greenlight_on():
    #red
    color("red")
    penup()
    goto(0, 100)
    pendown()
    circle(35)

    #yellow
    color("yellow")
    penup()
    goto(0, 0)
    pendown()
    circle(35)

    #green
    color("green")
    penup()
    goto(0, -100)
    pendown()
    begin_fill()
    circle(35)
    end_fill()



speed(20)
question = input("What traffic light is on now red/yellow/green?")
if question == "red":
    redlight_on()
if question == "yellow":
    yellowlight_on()
elif question == "green":
    greenlight_on()


hideturtle()
exitonclick()