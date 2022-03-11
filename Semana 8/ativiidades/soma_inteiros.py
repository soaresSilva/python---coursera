def soma_elementos(lista):
    j=0
    for i in lista:
        j+=i
    return j

lista = [2,5,4,7,8,9,5,4]

soma = soma_elementos(lista)

print("A soma dos inteiros é: ",soma)
