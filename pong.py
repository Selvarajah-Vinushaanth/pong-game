import turtle

win=turtle.Screen()
win.setup(800,600)
win.bgcolor("black")
win.title("pong game")
win.tracer(0)
left_paddle=turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("yellow")
left_paddle.shapesize(stretch_wid=5,stretch_len=1)
left_paddle.speed(0)
left_paddle.penup()
left_paddle.goto(-390,0)

right_paddle=turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("yellow")
right_paddle.shapesize(stretch_wid=5,stretch_len=1)
right_paddle.speed(0)
right_paddle.penup()

right_paddle.goto(390,0)
ball=turtle.Turtle()
ball.shape("circle")
ball.color("yellow")
ball.speed(0)
ball.dx=0.071
ball.dy=0.071
ball.penup()

def left_paddle_up():
    left_paddle.sety(left_paddle.ycor()+20)
def left_paddle_down():
    left_paddle.sety(left_paddle.ycor()-20)
def right_paddle_up():
    right_paddle.sety(right_paddle.ycor()+20)
def right_paddle_down():
    right_paddle.sety(right_paddle.ycor()-20)


win.listen()
win.onkeypress(left_paddle_up,"w")
win.onkeypress(left_paddle_down,"s")
win.onkeypress(right_paddle_up,"Up")
win.onkeypress(right_paddle_down,"Down")

score_a=0
score_b=0
pen=turtle.Turtle()
pen.color("red")
pen.penup()
pen.speed(0)
pen.goto(0,260)
pen.write("player A: 0  player B: 0",align="center",font=("Ariel",24,"normal"))
pen.hideturtle()



def change():
    win_new = turtle.Screen()
    win_new.setup(800, 600)
    win_new.bgcolor("black")
    win_new.title("Game Finished")
    pen_new=turtle.Turtle()
    pen_new.speed(0)
    pen_new.penup()
    pen_new.hideturtle()
    pen_new.color("red")
    pen_new.write("Game Over",align="center",font=("Ariel",40,"normal"))

    return win_new









while True:
    win.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor()<-285:
        ball.sety(-285)
        ball.dy *= -1
    if ball.xcor()>385:
        ball.setx(385)
        ball.dx *=-1
        score_a+=1
        pen.clear()
        pen.write(f"player A: {score_a}  player B: {score_b}", align="center", font=("Ariel", 24, "normal"))
    if ball.xcor()<-385:
        ball.setx(-385)
        ball.dx *= -1
        score_b+=1
        pen.clear()
        pen.write(f"player A: {score_a}  player B: {score_b}", align="center", font=("Ariel", 24, "normal"))
    if ball.xcor()>370 and (right_paddle.ycor()-50)<ball.ycor()<(right_paddle.ycor()+50):
        ball.setx(370)
        ball.dx*=-1
    if ball.xcor() <- 370 and (left_paddle.ycor() - 50) < ball.ycor() < (left_paddle.ycor() + 50):
        ball.setx(-370)
        ball.dx*=-1
    if score_a==3 or score_b==3:
        win.clear()

        win=change()
        win.mainloop()