def criaMatriz(numLinhas, numColunas):
    matriz = []
    for i in range(numLinhas):
        linha = []
        for j in range(numColunas):
            valor = int(input("Digite o elemento [" + str(i) + "] [" + str(j) + "]"))
            linha.append(valor)

        matriz.append(linha)

    return matriz

def leMatriz():
    linhas = int(input("Digite o número de linhas da matriz: "))
    colunas = int(input("Digite o número de colunas da matriz: "))
    return criaMatriz(linhas,colunas)
