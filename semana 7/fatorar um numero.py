def primo (p):
    i=1
    primo=0
    while i <= p:
        ver= p % i
        if ver == 0:
            primo = primo + 1
        
        i+=1
    if primo == 2 or p == 1:
        print("Primo")
    else:
        print("Não primo")

n = int(input("Digite um numero inteiro maior que 1: "))

fator = 2
multiplicidade = 0
primo(n)

while n > 1:
    while n%fator==0:
        multiplicidade = multiplicidade + 1
        n = n / fator
    if multiplicidade > 0:
        print ("O fator",fator,"multiplicidade",multiplicidade)
    fator = fator + 1
    multiplicidade = 0
