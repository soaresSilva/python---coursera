def maior_primo (w):
    x=1
    controle = 0
    maior = 0
    while x <= w:
        i=1
        res=0
        while i <= x:
            if x%i==0:
                res=res+1        
            i=i+1
        if res==2 or res==1:
            controle = x
        if maior < controle:
            maior = controle
        x = x+1
    return maior
    
w = int(input("Escreva um numero: "))
y = maior_primo(w)
print(y)



