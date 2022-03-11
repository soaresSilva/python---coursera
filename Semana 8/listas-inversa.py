inverso = []
i=1
while i > 0:
    i = int(input("Digite um numero: "))
    if i !=0:
        inverso.append(i)
    
j=len(inverso)
j-=1
while j >= 0:
    print(inverso[j])
    j-=1
