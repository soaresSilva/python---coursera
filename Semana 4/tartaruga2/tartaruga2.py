import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")         # define a cor de fundo da janela

tess = turtle.Turtle()
tess.color("blue")               # tess fica azul
tess.pensize(3)                  # define a espessura da caneta

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()