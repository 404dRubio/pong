import turtle
import winsound

window = turtle.Screen()
window.title("Pong By Geass Gaming")
window.bgcolor("black")
window.setup(width=800, height=600) #screen size
window.tracer(0) #tracer stops the window from updating things would run slower without

#Score
score1 = 0
score2 = 0

#Paddle A
paddle_a = turtle.Turtle()  # lower t is the module - capital T is the class name
paddle_a.speed(0)  #speed of animation, not how fast it moves on the screen
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # changes the size of the pixel , original size 20 by 20
paddle_a.penup()
paddle_a.goto(-350, 0) #coordinates for the paddle 


#Paddle B
paddle_b = turtle.Turtle()  # lower t is the module - capital T is the class name
paddle_b.speed(0)  #speed of animation, not how fast it moves on the screen
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # changes the size of the pixel , original size 20 by 20
paddle_b.penup()
paddle_b.goto(+350, 0) #coordinates for the paddle 


#Ball
ball = turtle.Turtle()  # lower t is the module - capital T is the class name
ball.speed(0)  #speed of animation, not how fast it moves on the screen
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0  PLayer 2: 0", align="center", font=("courier", 24, "normal"))

#Function
def paddle_a_up():
    y = paddle_a.ycor() #ycor is a turtle function what grabs the y coordinate
    y += 25
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() 
    y -= 25
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() 
    y += 25
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() 
    y -= 25
    paddle_b.sety(y)


#Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

#Main Game loop
while True:
    window.update()

    #Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("Borderhit.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("Borderhit.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Player 1: {}  PLayer 2: {}".format(score1, score2), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("Player 1: {}  PLayer 2: {}".format(score1, score2), align="center", font=("courier", 24, "normal"))

    
    #Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("Borderhit.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1    
        winsound.PlaySound("Borderhit.wav", winsound.SND_ASYNC)

