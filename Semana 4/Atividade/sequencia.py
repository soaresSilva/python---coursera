x = int(input("Numero: "))
anterior = None
saida = False
while (x != 0 and not saida):
    resto = x % 10
    x = (x - resto)//10
    if resto == anterior:
        saida = True
    anterior = resto
if saida:
    print("sim")
else:
    print("nao")
