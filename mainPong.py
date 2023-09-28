import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by ArvindKumar")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
#Score

score_a = 0
score_b = 0
#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


#Ball

pong_ball = turtle.Turtle()
pong_ball.speed(0)
pong_ball.shape("square")
pong_ball.color("white")
pong_ball.penup()
pong_ball.goto(0,0)
pong_ball.dx=0.08
pong_ball.dy=-0.08

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0  Player B:0",align="center",font=("courier",24,"normal"))


#functions
def paddle_a_up():
    y=paddle_a.ycor()
    y +=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y -=20
    paddle_a.sety(y)


def paddle_b_up():
    y=paddle_b.ycor()
    y +=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y -=20
    paddle_b.sety(y)


#KeyBoard Binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")



#Main game loop
while True:
        wn.update()

        #Move the ball
        pong_ball.setx(pong_ball.xcor() + pong_ball.dx)
        pong_ball.sety(pong_ball.ycor() + pong_ball.dy)

        #border check
        if pong_ball.ycor() > 290:
           pong_ball.sety(290)
           pong_ball.dy *= -1
           winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

        if pong_ball.ycor() < -290:
           pong_ball.sety(-290)
           pong_ball.dy *= -1
           winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

        if pong_ball.xcor() > 390:
            pong_ball.goto(0,0)
            pong_ball.dx *=-1
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("courier", 24, "normal"))

        if pong_ball.xcor() < -390:
           pong_ball.goto(0,0)
           pong_ball.dx *= -1
           score_b += 1
           pen.clear()
           pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",font=("courier", 24, "normal"))

        #paddle_and_ball_collision

        if (pong_ball.xcor() > 340 and pong_ball.xcor() < 350) and (pong_ball.ycor() < paddle_b.ycor() + 40 and pong_ball.ycor() > paddle_b.ycor() - 40):
            pong_ball.setx(340)
            pong_ball.dx *= -1
            winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

        if (pong_ball.xcor() < -340 and pong_ball.xcor() > -350) and (pong_ball.ycor() < paddle_a.ycor() + 45 and pong_ball.ycor() > paddle_a.ycor() - 45):
            pong_ball.setx(-340)
            pong_ball.dx *= -1
            winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)




