def soma_hipotenusas(n):
    a=1
    b=1
    c=1
    hipo=0
    ver=0
    soma=0
    while a<=n:
        b=1
        while b<=n:
            c=1
            while c <= n:
                hipo = (b**2+c**2)**(1/2)
                if hipo==a:
                    if hipo!=ver:
                        soma+=a
                        print(a)
                    ver=hipo  
                c+=1
            b+=1
        a+=1
        
    return soma


n=float(input("Escreva um numero: "))
print("A soma é",soma_hipotenusas(n))
