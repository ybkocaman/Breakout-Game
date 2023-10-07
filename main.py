import turtle
import random

colors = ["blue", "red", "pink", "yellow", "green", "gray", "white", "cyan"]

window = turtle.Screen()
window.title('Breakout Game')
window.bgcolor('black')
window.setup(width=600, height=600)
window.tracer(0)

paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_wid=1, stretch_len=4)
paddle.penup()
paddle.goto(0, -250)

ball = turtle.Turtle()
ball.speed(40)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

bricks = []

for i in range(6):
    for j in range(17):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape('square')
        brick.color(random.choice(colors))
        brick.penup()
        brick.goto(-225 + j * 25, 250 - i * 40)
        bricks.append(brick)

remaining_bricks = len(bricks)


def paddle_right():
    x = paddle.xcor()
    x += 20
    if x > 250:
        x = 250
    paddle.setx(x)


def paddle_left():
    x = paddle.xcor()
    x -= 20
    if x < -250:
        x = -250
    paddle.setx(x)


window.listen()
window.onkeypress(paddle_right, 'Right')
window.onkeypress(paddle_left, 'Left')


def check_collision(obj1, obj2):
    distance = ((obj1.xcor() - obj2.xcor())**2 + (obj1.ycor() - obj2.ycor())**2)**0.5
    if distance < 30:  # Adjust this value for accurate collisions
        return True
    else:
        return False


while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1

    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # if ball.ycor() < -290:
    #     ball.goto(0, 0)
    #     ball.dy *= -1

    if check_collision(ball, paddle):
        ball.sety(-240)
        ball.dy *= -1

    for brick in bricks:
        if check_collision(ball, brick):
            brick.goto(1000, 1000)
            ball.dy *= -1
            remaining_bricks -= 1

    if ball.ycor() < -290:
        break

    if remaining_bricks == 0:
        you_win = turtle.Turtle()
        you_win.color('green')
        you_win.penup()
        you_win.hideturtle()
        you_win.goto(0, 0)
        you_win.write('You Win!', align='center', font=('Courier', 24, 'normal'))
        break

game_over = turtle.Turtle()
game_over.color('red')
game_over.penup()
game_over.hideturtle()
game_over.goto(0, 0)
game_over.write('Game Over', align='center', font=('Courier', 24, 'normal'))

window.exitonclick()
