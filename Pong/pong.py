import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#paddle1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.penup()
paddle1.goto(-350,0)

#paddle2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.penup()
paddle2.setposition(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.setposition(0,0)
ball.xspeed = .5
ball.yspeed = .5

#second ball
ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("square")
ball1.color("white")
ball1.penup()
ball1.setposition(0,0)
ball1.xspeed = -.5
ball1.yspeed = -.5

#score
score = turtle.Turtle()
score.hideturtle()
score.speed(0)
score.color("white")
score.penup()
score.setposition(-150, 150)
score.write("0", align = "center", font = ("Courier,",150, "normal"))

#score
score1 = turtle.Turtle()
score1.hideturtle()
score1.speed(0)
score1.color("white")
score1.penup()
score1.setposition(150, 150)
score1.write("0", align = "center", font = ("Courier,",150, "normal"))

#tracking score
player1_score = 0
player2_score = 0

#move paddle
def moveup_paddle1():
    y = paddle1.ycor()
    y += 50
    if(y>250):
        y=250
    paddle1.sety(y)
def movedown_paddle1():
    y = paddle1.ycor()
    y -= 50
    if(y<-250):
        y=-250
    paddle1.sety(y)
def moveup_paddle2():
    y = paddle2.ycor()
    y += 100
    if(y>250):
        y=250
    paddle2.sety(y)
def movedown_paddle2():
    y = paddle2.ycor()
    y -= 100
    if(y<-250):
        y=-250
    paddle2.sety(y)

#binding
window.listen()
window.onkeypress(moveup_paddle1,"w")
window.onkeypress(movedown_paddle1,"s")
window.onkeypress(moveup_paddle2,"Up")
window.onkeypress(movedown_paddle2,"Down")

#loop
while True:
    window.update()

    #ball movement
    ball.setx(ball.xcor()+ball.xspeed)
    ball.sety(ball.ycor() + ball.yspeed)

    ball1.setx(ball1.xcor() + ball1.xspeed)
    ball1.sety(ball1.ycor() + ball1.yspeed)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.yspeed *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.yspeed *= -1

    if ball1.ycor() > 290:
        ball1.sety(290)
        ball1.yspeed *= -1

    if ball1.ycor() < -290:
        ball1.sety(-290)
        ball1.yspeed *= -1

    if ball.xcor()>390:
        ball.setposition(0,0)
        ball.xspeed *= -1
        player2_score+=1
        score.clear()
        score.write(player2_score, align="center", font=("Courier,", 150, "normal"))

    if ball.xcor()<-390:
        ball.setposition(0,0)
        ball.xspeed *= -1
        player1_score+=1
        score1.clear()
        score1.write(player1_score, align="center", font=("Courier,", 150, "normal"))

    if ball1.xcor() > 390:
        ball1.setposition(0, 0)
        ball1.xspeed *= -1
        player2_score += 1
        score.clear()
        score.write(player2_score, align="center", font=("Courier,", 150, "normal"))

    if ball1.xcor() < -390:
        ball1.setposition(0, 0)
        ball1.xspeed *= -1
        player1_score += 1
        score1.clear()
        score1.write(player1_score, align="center", font=("Courier,", 150, "normal"))


    #collision
    if (ball.xcor()> 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor()>paddle2.ycor() - 50):
        ball.setx(340)
        ball.xspeed *= -1

    if (ball.xcor()< -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor()>paddle1.ycor() - 50):
        ball.setx(-340)
        ball.xspeed *= -1

    if (ball1.xcor() > 340 and ball1.xcor() < 350) and (ball1.ycor() < paddle2.ycor() + 50 and ball1.ycor() > paddle2.ycor() - 50):
        ball1.setx(340)
        ball1.xspeed *= -1

    if (ball1.xcor() < -340 and ball1.xcor() > -350) and (ball1.ycor() < paddle1.ycor() + 50 and ball1.ycor() > paddle1.ycor() - 50):
        ball1.setx(-340)
        ball1.xspeed *= -1
    
    #Ai
    if(player2_score == 10 or player1_score == 10):
        window.bye()
        break
    if ball.xcor()>ball1.xcor():
        if paddle2.ycor() < ball.ycor() and abs(paddle2.ycor() - ball.ycor()) > 50:
            moveup_paddle2()
        elif paddle2.ycor() > ball.ycor() and abs(paddle2.ycor() - ball.ycor()) > 50:
            movedown_paddle2()
    else:
        if paddle2.ycor() < ball1.ycor() and abs(paddle2.ycor() - ball1.ycor()) > 50:
            moveup_paddle2()
        elif paddle2.ycor() > ball1.ycor() and abs(paddle2.ycor() - ball1.ycor()) > 50:
            movedown_paddle2()

if(player2_score == 10):
    print("Player 2 wins")

if(player1_score == 10):
    print("You lose you")
