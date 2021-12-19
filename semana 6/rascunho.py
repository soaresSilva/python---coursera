def computador_escolhe_jogada(n,m):
    if n % (m+1)==0:
        retira=m
    else:
        retira=1
    return retira

n = int(input("Quantas peças o jogo tem ? "))
m = int(input("quantas peças possíveis pode retirar ?"))
retira = computador_escolhe_jogada(n,m)
print(retira)
