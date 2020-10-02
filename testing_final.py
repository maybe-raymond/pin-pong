import turtle
from random import randint, choice
import math
from tkinter import *

p =0
position = []
t =[]
keep = True
play = True
go = True
count = 0
s = " l"
m = " l"

# The first pad
first= turtle.Turtle(shape="square")
first.penup()
first.ht()
first.speed("fastest")
first.shapesize(stretch_len=5)
first.setheading(90)
first.setpos(-360, 0)
first.st()
t.append(first)

#  The second pad
second = first.clone()
second.ht()
second.speed("fastest")
second.setpos(360, 0)
second.st()


# making the ball
ball = turtle.Turtle(shape="circle")
ball.fillcolor("red")
ball.shapesize(stretch_wid= 0.9)
ball.penup()
ball.speed(2)

# The moving functions
def up():
    first.fd(40)

def down():
    first.bk(40)


# This determines the direction of the the ball
def ball_rect():
    #print("ball rect start")
    global ang
    angle = randint(0, 20)
    angle2 = randint(340, 360)
    position.append(angle)
    position.append(angle2)
    ang = choice(position)
    ball.setheading(ang)
    #print("ball rect end")


# Function for edge detection
# the algorthimn takes the x and y postion of the pong and ball and subtracks them until the number is below 15 then it will move
def first_collide(pong):
    global p
    global keep
    global py
    global px
    global ypos
    x_cord=0.5
    y_cord=0.5
    if pong.pos() == ball.pos():
        pass
    if abs(pong.xcor()) > abs(ball.xcor()):
        num = abs(pong.xcor()) - abs(ball.xcor())
        x_cord = abs(num)
    elif abs(pong.xcor()) < abs(ball.xcor()):
        num = abs(ball.xcor()) - abs(pong.xcor())
        x_cord = abs(num)


    if abs(pong.ycor()) < abs(ball.ycor()):
        ynum = abs(ball.ycor()) - abs(pong.ycor())
        y_cord = abs(ynum)
    elif abs(pong.ycor()) > abs(ball.ycor()):
        ynum = abs(pong.xcor()) - abs(ball.xcor())
        y_cord = abs(ynum)
    check()

    if x_cord < 15 and y_cord < 15:
        keep = False # keep is used so that the second pong knows the ball is comming so it would move and allow for edge detection
        if p == 0 :
            p = 1
            px = ball.xcor()
            py = ball.ycor()
        else:
            p =0
    checkscore()



# The scorebord of the game
def score():
    global bill
    global billord
    billord= turtle.Turtle()
    bill = turtle.Turtle()
    bill.ht()
    billord.ht()
    billord.penup()
    bill.penup()
    billord.setpos(-250,300 )
    bill.setpos(250, 300)
    global m
    billord.write(m, align="center" ,font=(5,15))
    global s
    bill.write(s , align="center",font=(5,15))


# Ai for the second pong
def second_pong_algorithmn(pos):
    global numb
    global go
    global change
    global ypos
    aa = pos
    if pos >= 300:
        aa = 360 - ang
    value = 180-(aa + 90)
    distance = 680/math.sin(math.radians(value))
    numb = math.sin(math.radians(pos)) * distance
    new_num = aa * 7
    if ball.xcor() > 0:
        if go == True:
            if pos in range(340, 360):
                second.sety(ypos)
            else:
                second.sety(ypos)
            go = False


# Makes the ball move until colision
def ball_move():
    global p
    global go
    while keep:
        if p == 0:
            ball.bk(10)
            first_collide(first)
        else: # this is why keep is important it allows the ball to change direction and so the other functions can run
            ball.fd(10)
            first_collide(second)
            second_pong_algorithmn(ang)



def  main():
    global keep
    global p
    global go
    change = True
    while play:
        keep = True
        go = True
        score()
        ball_rect()
        ball_move()
        billord.clear()
        bill.clear()
        gameover()

# the algorithmn is y = mx + c which determines the position the second pong to go
def check():
    global ypos
    if ball.xcor() > 0:
        ppx = px - ball.xcor()
        ppy = py - ball.ycor()
        newp = ppy/ ppx
        yintercept = ball.ycor()
        ypos = newp *360 + yintercept
        return ypos


def checkscore():
    global m
    global s
    if ball.xcor() > 370:
        m = m + "l "
        reset()
    elif ball.xcor() == -370:
        s = s + "l "
        reset()
    elif ball.ycor() > 370:
        m = m + "l "
        reset()
    elif ball.ycor() < -370:
        s = s + "l "
        reset()

def reset():
    global keep
    ball.ht()
    first.ht()
    second.ht()
    ball.setpos(0,0)
    first.sety(0)
    second.sety(0)
    ball.st()
    first.st()
    second.st()
    keep = False


def gameover():
    global play
    global s
    global m
    print(len(s))
    print(len(m))
    if len(m) == 8:
        play = False
    elif len(s) == 8:
        play = False

first.screen.onkeyrelease(up, "w")
first.screen.onkeyrelease(down, "s")
first.screen.listen()
main()
turtle.done()
