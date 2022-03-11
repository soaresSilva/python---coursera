def computador_escolhe_jogada(n,m):
    retira=0
    nm = n - m
    if nm <= 0:
        retira = m
    else:
        if nm >= m+1:
            retira = m
        else:
            retira=m
            while nm < m+1:
                retira = retira-1
                nm = n-retira
    return retira
        
def usuario_escolhe_jogada(n,m):
    r = False
    retira = int(input("quantas peças você vai retirar ?"))
    while r == False:
        if retira <= m:
            r = True
        else:
            print("Valor informado é inválido")
            retira = int(input("Informe um numero válido ?"))
    return retira


def partida():
    n = int(input("Quantas peças o jogo tem ? "))
    m = int(input("quantas peças possíveis pode retirar ?"))
    retira=0
    quem_ganhou = True
    
    def computador(n,m):
        retira = computador_escolhe_jogada(n,m)
        print("O computador tirou",retira,"peça.")
        return retira
        
    def usuário(n,m):
        retira = usuario_escolhe_jogada(n,m)
        print("Você tirou",retira,"peça.")
        return retira
    
    if n%(m+1)==0:
        print("Você começa!")
        while n > 0:
            if n<m:
                m = n
            retira = usuário(n,m)
            quem_ganhou = False
            n = n-retira
            print("Peças que faltam retirar:",n)
            if n > 0:
                if n<m:
                    m = n
                retira = computador(n,m)
                quem_ganhou = True
                n = n-retira
                print("Peças que faltam retirar:",n)
    else:
        print("Computador começa!")
        while n > 0:
            if n<m:
                m = n
            retira = computador(n,m)
            quem_ganhou = True
            n = n-retira
            print("Peças que faltam retirar:",n)
            if n > 0:
                if n<m:
                    m = n
                retira = usuário(n,m)
                quem_ganhou = False
                n = n-retira
                print("Peças que faltam retirar:",n)

    if quem_ganhou == True:
        print("O computador ganhou!")
        quem_ganhou = 1
    else:
        print("Você ganhou!")
        quem_ganhou = 2
    return quem_ganhou

def campeonato():
    i=0
    computador=0
    voce=0
    partida=0
    while i < 3:
        partida = partida()
        if partida == 1:
            computador=computador+1
        else:
            voce=voce+1
        print("Placar: Você",voce,"X",computador,"Computador")
        i=i+1

print("Bem-vindo ao jogo do NIM! Escolha: ")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")

jogo=int(input(""))
if jogo == 1:
    print("Você escolheu uma partida isolada!")
    partida()
else:
    print("Voce escolheu um campeonato!")
    campeonato()
