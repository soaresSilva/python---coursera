
x = int(input("Escreva um numero: "))
i=1
res=0
while i <= x:
    if x%i==0:
        res=res+1        
    i=i+1
if res==2 or res==1:
    print("primo")
else:
    print("nao primo")





