import turtle
wn = turtle.Screen()             # Cria uma janela e define seus atributos
wn.bgcolor("green")


tess = turtle.Turtle()           # cria tess e define seus atributos
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()           # cria alex

tess.forward(80)                 # tess desenha um tri�ngulo equil�tero
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                   # complete o tri�ngulo

tess.right(180)                  # tess muda de dire��o
tess.forward(80)                 # tess se move para longe da origem

alex.forward(50)                 # alex desenha um quadrado
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()