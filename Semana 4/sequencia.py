x = int(input("Numero: "))
anterior = None
soma = 0
saida = False
while (x != 0 and not saida):
    resto = x % 10
    x = (x - resto)//10
    if resto == anterior:
        saida = True
    anterior = resto
if saida:
    print("número adjacente igual é o", resto)
else:
    print("não há número adjacente igual")
