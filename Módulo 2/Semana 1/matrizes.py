def criaMatriz(numLinhas, numColunas, valor):
    matriz = []
    for i in range(numLinhas):
        linha = []
        for j in range(numColunas):
            linha.append(valor)

        matriz.append(linha)

    return matriz
