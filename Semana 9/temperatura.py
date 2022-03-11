def MinMax(temperaturas):
    print("A menor temperatura do mês foi: ",min(temperaturas),"C")
    print("A menor temperatura do mês foi: ",max(temperaturas),"C")

def minima(temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i+=1
    return min

def maxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i+=1
    return max

def teste_pontual_minima(temp,valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para array", temp)
        print("valor_esperado",valor_esperado,". Valor calculado: ",valor_calculado)

def teste_pontual_maxima(temp,valor_esperado):
    valor_calculado = maxima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para array", temp)
        print("valor_esperado",valor_esperado,". Valor calculado: ",valor_calculado)

def testa_minima():
    print("Iniciando os testes da temperatura mínima")

    teste_pontual_minima([0],0)

    teste_pontual_minima([0,0,0,0,0,0],0)

    teste_pontual_minima([0,1,2,3,4,5,6,7,8,9,10],0)

    teste_pontual_minima([15,19,20,25,26,29,27],15)

    teste_pontual_minima([-15,-12,-2,0,30],-15)
    
    print("Finalizando os testes da temperatura mínima")

def testa_maxima():
    print("Iniciando os testes da temperatura maxima")

    teste_pontual_maxima([0],0)

    teste_pontual_maxima([0,0,0,0,0,0],0)

    teste_pontual_maxima([0,1,2,3,4,5,6,7,8,9,10],10)

    teste_pontual_maxima([15,19,20,25,26,29,27],29)

    teste_pontual_maxima([-15,-12,-2,0,30],30)
    
    print("Finalizando os testes da temperatura maxima")
