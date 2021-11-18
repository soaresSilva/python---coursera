
meuCartao = int(input("Escreva o número do cartão: "))
cartaoLido = 1
acheiCartao = False
while cartaoLido !=0 and not acheiCartao:
    cartaoLido = int(input("Escreva o próximo número de crtão de crédito: "))
    if meuCartao == cartaoLido:
        acheiCartao = True
        
if acheiCartao:
    print("Achei o meu cartão")
else:
    print("Não achei o cartão")
