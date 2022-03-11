def remove_repetidos(lista):
    res = []
    for element in lista:
        if element not in res:
            res.append(element)
    i = 0
    res.sort()       
    return res


lista = [2,5,4,2,5,2]

res = remove_repetidos(lista)

print (res)



