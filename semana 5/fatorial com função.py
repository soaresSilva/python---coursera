def fatorial (x):
    i=1
    soma=x*i
    while i < x:
        soma = soma*i
        i=i+1
    if soma==0:
        soma=soma+1

    return soma

x=15
y=5
z=5

a = fatorial(x) / (fatorial(y) + fatorial(z))

print (a)
