lista = [1,9,1,5,9,1,5,9,1,5,9,1,5]

lista2 = [300,200,200,200,200,200]

lista2 = lista

lista2[0] = 100
print(lista)
print(lista2)

print("Não clonou")

lista2 = lista[:]

lista2[0] = 500

print(lista)
print(lista2)

print("Clonou")






