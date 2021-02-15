from turtle import *
import os
import math

window = Screen()
window.bgcolor("black")
window.title("Space Invader")
window.tracer(0)

#border setup
border_pen = Turtle()
border_pen.speed(0)
border_pen.penup()
border_pen.setposition(-310,-310)
border_pen.pensize(3)
border_pen.pendown()
border_pen.color("white")

#register shape
register_shape("invader.gif")
register_shape("player.gif")

#draws border
for i in range(4):
    border_pen.forward(620)
    border_pen.left(90)
border_pen.hideturtle()

#score
score = 0
score_pen = Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.hideturtle()
score_pen.penup()
score_pen.setposition(-300,290)
score_string = "Score: {}".format(score)
score_pen.write(score_string,False, align = "left", font = ("Ariel", 14, "normal"))


#player turtle
player = Turtle()
player.color("green")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
player.speed = 0


#multiple enemies
number_opp = 30
opps = []
for i in range(number_opp):
    opps.append(Turtle())

opp_x = -200
opp_y = 225
num1 = 0

# opposition
for opp in opps:
    opp.color("red")
    opp.penup()
    opp.speed(0)
    opp.shape("invader.gif")
    x = opp_x + (50*num1)
    y = opp_y
    opp.setposition(x, y)
    num1 += 1
    if num1 == 10:
        opp_y-=50
        num1 = 0

opp_speed = 0.1

#player attack
att = Turtle()
att.color("yellow")
att.shape("triangle")
att.penup()
att.speed(0)
att.setheading(90)
att.shapesize(.5,.5)
att.hideturtle()
att_speed = 20
att_state = "ready"

def left():
    player.speed = -2
def right():
    player.speed = 2
def move():
    x = player.xcor()
    x+=player.speed
    if x<-300:
        x=-300
    if x>300:
        x=300
    player.setx(x)

#attack function
def attack():
    global att_state
    if att_state == "ready":
        os.system("afplay /Users/emiljiang/Downloads/shoot1.wav&")
        att_state = "not ready"
        x = player.xcor()
        y = player.ycor()
        att.setposition(x,y+10)
        att.showturtle()

#collision function
def isCollision(a,b):
    d = math.sqrt(math.pow(a.xcor()-b.xcor(),2)+math.pow(a.ycor()-b.ycor(),2))
    if d<15:
        return True
    else:
        return False

#keys
onkey(left, "Left")
onkey(right, "Right")
onkey(attack,"space")
listen()

#main
while True:
    move()
    window.update()
    for opp in opps:
        x = opp.xcor()+opp_speed
        opp.setx(x)
        if opp.xcor()>300:
            for i in opps:
                y = i.ycor()-40
                i.sety(y)
            opp_speed /= -1
        if opp.xcor()<-300:
            for i in opps:
                y = i.ycor() - 40
                i.sety(y)
            opp_speed /= -1
        if isCollision(att, opp) == True:
            os.system("afplay /Users/emiljiang/Downloads/expl1.wav&")
            att.hideturtle()
            att_state = "ready"
            opp.setposition(0,100000)
            score+=10
            score_pen.clear()
            score_string = "Score: {}".format(score)
            score_pen.write(score_string, False, align="left", font=("Ariel", 14, "normal"))

        if isCollision(player, opp):
            player.hideturtle()
            opp.hideturtle()
            att.hideturtle()
            print("Game Over")
            break;
    if att_state == "not ready":
        y = att.ycor()+att_speed
        att.sety(y)
    if att.ycor()>300:
        att.hideturtle()
        att_state = "ready"
    if score ==300:
        window.bye()
        print("You Win")
        break;

