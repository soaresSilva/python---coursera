import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

print(range(5,60,2))
tess.penup()                    # isso � novo
for size in range(5,60,2):      # come�ar com size = 5 e passo 2
    tess.stamp()                # deixar um carimbo no canvas
    tess.forward(size)          # tess, v� para frente
    tess.right(24)              # tess, vire 24 graus a direita

wn.exitonclick()
