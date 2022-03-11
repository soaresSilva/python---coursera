a=int(input("Escreva a altura: "))
l=int(input("Escreva a largura: "))
i=1
while i <= l:
    j=1
    while j <= a:
        if j == 1 or i == 1 or j==a or i==l:
            print ("#",end = "")
        else:
            print("", end=" ")
        j+=1
    print("")
    i+=1
        
        
