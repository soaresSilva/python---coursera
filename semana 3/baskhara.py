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
    print("O valor de x1 é:",x1, "e o valor de x2 é:",x2)
else:
    if delta == 0:
        x1=(-b + delta**(1/2))/(2*a)
        print("A raiz é",x1,"portanto só há uma respota.")
    else:
        print("O delta é",delta,"Essa equação não tem raízes reais.")



print("-------------------------------------------------")
print("-------------------------------------------------")
print("-------------------------------------------------")
