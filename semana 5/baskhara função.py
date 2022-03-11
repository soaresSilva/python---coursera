print("Quero saber responder uma equeção de segundo grau")
print("-------------------------------------------------")
print("A formúla é ax²+bx+c=0")
print("-------------------------------------------------")
print("Para acharmos o valor de x precisamos fazer a fórmula de baskhara")
print("-------------------------------------------------")

def delta (a,b,c):
    return b**2-4*a*c

def main ():
    a = float(input("qual o número para a ?"))
    b = float(input("qual o número para b ?"))
    c = float(input("qual o número para c ?"))
    imprime(a,b,c)

def imprime(a,b,c):
    calculo = delta(a,b,c)**(1/2)
    if calculo > 0:
        print("O delta é",delta(a,b,c),"Temos dois resultados")
        x1=(-b + calculo)/(2*a)
        x2=(-b - calculo)/(2*a)
        print("O valor de x1 é:",x1, "e o valor de x2 é:",x2)
    else:
        if delta == 0:
            x1=(-b + calculo)/(2*a)
            print("a raiz desta equação é",x1)
        else:
            print("esta equação não possui raízes reais")



print("-------------------------------------------------")
print("-------------------------------------------------")
print("-------------------------------------------------")
