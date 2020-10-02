import turtle
from random import randint, choice
import math
from tkinter import *


position =[]
s = "l "
m = "l "
keep = False
first= turtle.Turtle(shape="square")
first.penup()
first.ht()
first.speed("fastest")
first.shapesize(stretch_len=5)
first.setheading(90)
first.setpos(-360, 0)
first.st()

# setting up the second object/ paddle
second = first.clone()
second.ht()
second.setpos(360, 0)
second.st()


# making the ball
#ball = turtle.Turtle(shape="circle")
ball = turtle.register_shape("ball.gif")
#ball.setpos(-340, 0)
#ball.penup()
#ball.speed("slowest")


# the start button


def up():
    first.fd(40)
    first_collide(first)

def down():
    first.bk(40)
    first_collide(first)

def ball_rect(pong):
    global s
    angle = randint(0, 40)
    angle2 = randint(320, 360)
    position.append(angle)
    position.append(angle2)
    global ang
    ang = 0
    if ang >= 300:
        new = 360 - ang
        ball_algorithmn(new)
#        ball.setheading(new)

    else:
        ball_algorithmn(ang)
    #    ball.setheading(ang)
    if pong == first:
        pass
        #ball.fd(distance+420)
    else:
        pass
        #ball.fd(distance+420)
    second.fd(numb)
    checkscore()
    position.clear()
    bill.clear()
    billord.clear()
    score()
    gameover()

def first_collide(pong):
    if pong.ycor() > 0:
        ynum = pong.ycor() - ball.ycor()
    else:
        ynum = ball.ycor() - pong.ycor()
    print(ynum)

    for i in range(-10, 50):
        if int(ynum) == i:
            reaction()
            break


def score():
    global bill
    global billord
    billord= turtle.Turtle()
    bill = turtle.Turtle()
    bill.ht()
    billord.ht()
    billord.penup()
    bill.penup()
    billord.setpos(-350,300 )
    bill.setpos(350, 300)
    global m
    billord.write(m, align="center" ,font=(5,15))
    global s
    bill.write(s , align="center",font=(5,15))


def ball_algorithmn(pos):
    global distance
    global numb
    if pos >= 300:
        pos = 360 - ang
        ball.setheading(31)
    value = 180-(pos + 90)
    distance = 340/math.sin(math.radians(value))
    numb = math.sin(math.radians(pos)) * (distance+340)
    dis = (numb+55)
    print(pos)
    print(distance)

def reaction():
    if first.ycor() < 0:
        pos= angle2 = randint(0, 40)
        ball.setheading(pos)
        ball_algorithmn(pos)
        ball.fd(distance)
        second_pong()
    else:
        pos= angle2 = randint(300, 360)
        ball.setheading(pos)
        ball_algorithmn(pos)
        ball.fd(distance)
        second_pong()
    print(ball.pos())

def second_pong():
    for i in range(0, 100):
        if ball.xcor() > 0:
            second.fd(0.5)
            first_collide(second)
            ball_rect(second)


def checkscore():
    global m
    global s
#    if ball.xcor() in range(390, 800):
#        m = m + "l "
#        reset()
#    elif ball.xcor() == -400:
#        s = s + "l "
#        reset

def reset():
    ball.ht()
    first.ht()
    second.ht()
    ball.setpos(0,0)
    first.sety(0)
    second.sety(0)
    ball.st()
    first.st()
    second.st()

def gameover():
    global s
    root = Tk()
    global m
    print(len(s))
    print(len(m))
    if len(m) == 4:#6:
        Label(root, text= "you won").pack()
    elif len(s) == 4:#6:
        Label(root, text="you lose").pack()
    root.mainloop()

score()
first.screen.onkeyrelease(up, "w")
first.screen.onkeyrelease(down, "s")
first.screen.listen()
ball_rect(first)
score()
turtle.done()
