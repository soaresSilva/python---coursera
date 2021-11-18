decrescente = True
anterior = int(input("escolha o primeiro número: "))
valor = 1
while valor !=0 and decrescente:
    valor = int(input("digite o próximo número: "))
    if valor > anterior:
        decrescente = False
    anterior = valor
        
if decrescente:
    print("A sequência está em ordem descrecente")
else:
    print("A sequência não está em ordem descrecente")
