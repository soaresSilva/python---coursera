print("Quero saber responder uma equeção de segundo grau")
print("-------------------------------------------------")
print("A formúla é ax²+bx+c=0")
print("-------------------------------------------------")
print("Para acharmos o valor de x precisamos fazer a fórmula de baskhara")
print("-------------------------------------------------")



a = float(input("qual o número para a ?"))
b = float(input("qual o número para b ?"))
c = float(input("qual o número para c ?"))

delta = b**2-4*a*c

if delta > 0:
    print("O delta é",delta,"Temos dois resultados")
    x1=(-b + delta**(1/2))/(2*a)
    x2=(-b - delta**(1/2))/(2*a)
    if x1 > x2:
        print("O valor de x1 é:",x1, "e o valor de x2 é:",x2)
        print("aqui")
    else:
        print("O valor de x1 é:",x2, "e o valor de x2 é:",x1)
        print("aqui nao")
else:
    if delta == 0:
        x1=(-b + delta**(1/2))/(2*a)
        print("a raiz desta equação é",x1)
    else:
        print("esta equação não possui raízes reais")



print("-------------------------------------------------")
print("-------------------------------------------------")
print("-------------------------------------------------")
