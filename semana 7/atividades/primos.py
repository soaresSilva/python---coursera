def n_primos(n):
    i=2
    n_primo=0
    while i<=n:
        j=1
        primo=0
        while j<=i:
            if i%j==0:
                primo+=1
            j+=1 
        if primo==2:
            n_primo+=1
        i+=1
    return n_primo

n = int(input("Escreva um numero :"))    
print(n_primos(n))
