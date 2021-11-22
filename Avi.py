import turtle

sr = turtle.Screen()
sr.title("Pong Game by Avi")
sr.bgcolor('black')
sr.setup(width = 800 , height = 600)
sr.tracer()

wins_1 = False
wins_2 = False

#paddle_1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape('square')
paddle_1.color('white')
paddle_1.shapesize(stretch_wid = 5 , stretch_len = 1)
paddle_1.penup()
paddle_1.goto(-370,0)

#paddle_2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape('square')
paddle_2.color('white')
paddle_2.shapesize(stretch_wid = 5 , stretch_len = 1)
paddle_2.penup()
paddle_2.goto(370,0)

#ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape('square')
ball.color('white')
ball.penup()
ball.dx = -3
ball.dy = 3

#score
score_1 = 0
score_2 = 0
score_lim = 5

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(-0,260)
pen.write("Player 1: {} Player 2: {}".format(score_1,score_2),align="center" ,font=("Courier",24,"normal"))

#function
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)
    
def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)
    
def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)
    
#keyboard binding
sr.listen()
sr.onkeypress(paddle_1_up,"w")
sr.onkeypress(paddle_1_down,"s")
sr.onkeypress(paddle_2_down,"Down")
sr.onkeypress(paddle_2_up,"Up")

#main game loop
while True:
    sr.update()
    
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #border Cheking
    if ball.ycor() > 285:
        ball.sety(285)
        ball.dy *= -1
        
    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1
        
    if ball.xcor() > 400:
        ball.goto(0,0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1,score_2),align="center" ,font=("Courier",24,"normal"))
        
    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1,score_2),align="center" ,font=("Courier",24,"normal"))
        
    #paddle ball Collision
    if (ball.xcor() > 350 and ball.xcor() <360) and (ball.ycor() < paddle_2.ycor() + 70 and ball.ycor() > paddle_2.ycor() - 70):
        ball.setx(350)
        ball.dx *= -1
        
    if (ball.xcor() < -350 and ball.xcor() >-360) and (ball.ycor() < paddle_1.ycor() + 70 and ball.ycor() > paddle_1.ycor()-70):
        ball.setx(-350)
        ball.dx *= -1
        
    if score_1 == score_lim:
        wins_1 = True
        break
        
    if score_2 == score_lim:
        wins_2 = True
        break
        
while True:
    if wins_1:
        sr.bgcolor('black')
        pen.goto(0,0)
        pen.write("Player 1 is WINNER!!!!",align='center',font=('Courier',30,"normal"))
    else:
        sr.bgcolor('black')
        pen.goto(0,0)
        pen.write("Player 2 is WINNER!!!!",align='center',font=('Courier',30,"normal"))
turtle.done()