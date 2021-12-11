def maximo (n,m):
    if n > m:
        maior = n
    else:
        maior = m
    return maior

n = int(input("escreva um número : "))
m = int(input("escreva outro número : "))

y = maximo(n,m)

print(y)

