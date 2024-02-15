import random
import turtle
import time


#Criar a tela de jogo
screen = turtle.Screen()
screen.title("Jogo da Cobra") 
screen.setup(width=700, height=700)
screen.tracer(0)  
screen.bgcolor("#1d1d1d")


#Criando as bordas do jogo
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

#Definir a pontuação
Score = 0;
delay = 0.1

#Cobra
snake = turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

#Comida
fruta = turtle.Turtle()
fruta.speed(0)
fruta.shape("square")
fruta.color("white")
fruta.penup()
fruta.goto(30, 30)

old_fruit = []

#Resultado
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("White")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Pontuação: ", align="center", font=("Courier", 24, "bold"))

#Movimentação da cobrinha
def snake_monv_up():
    if snake.direction != "down":
        snake.direction = "up"


def snake_monv_down():
    if snake.direction != "up":
        snake.direction = "down"


def snake_monv_left():
    if snake.direction != "right":
        snake.direction = "left"


def snake_monv_right():
    if snake.direction != "left":
        snake.direction = "right"


def mov():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


#Movimentação teclado
screen.listen()
screen.onkeypress(snake_monv_up, "Up")
screen.onkeypress(snake_monv_down, "Down")
screen.onkeypress(snake_monv_left, "Left")
screen.onkeypress(snake_monv_right, "Right")

#Loop menu 
while True:
    screen.update()

    #Cobrinha e Comida 
    if snake.distance(fruta) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruta.goto(x, y)
        scoring.clear()
        Score += 1
        scoring.write("Pontuação: {}".format(Score), align="center", font=("Courier", 24, "bold"))
        delay -= 0.001


        #Novas comidas no mapa
        nova_fruta = turtle.Turtle()
        nova_fruta.speed(0)
        nova_fruta.shape("square")
        nova_fruta.color("red")
        nova_fruta.penup()
        old_fruit.append(nova_fruta)


    #Adicionar uma parte da cobre
    for index in range(len(old_fruit) -1, 0, -1):
        a = old_fruit[index -1].xcor()
        b = old_fruit[index -1].ycor()

        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)
    mov()


    #Colisão com a parede 
    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0, 0)
        scoring.write("      Game Over \n Sua pontuação foi:   {}".format(Score), align="center", font=("Courier", 24, "bold"))


    #Colisão com o corpo
    for comida in old_fruit:
        if comida.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write("      Game Over \n Sua pontuação foi:   {}".format(Score), align="center", font=("Courier", 24, "bold"))


    time.sleep(delay)

turtle.Terminator()
