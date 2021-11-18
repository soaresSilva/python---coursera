m = int(input("Me mande um número com 6 dígitos : "))
ver = int(input("Digite o numero que deseja verificar: "))
soma=0
n=m
if n > 0:
    if 0 <= ver <= 9:
        cem_mil= n // 100000
        n=n%100000
        if cem_mil==ver:
            soma=soma+1
        dez_mil= n // 10000
        n=n%10000
        if dez_mil==ver:
            soma=soma+1
        mil= n // 1000
        n=n%1000
        if mil==ver:
            soma=soma+1
        centena= n // 100
        n=n%100
        if centena==ver:
            soma=soma+1
        dezena= n // 10
        n=n%10
        if dezena==ver:
            soma=soma+1
        unidade= n // 1
        n=n%1
        if unidade==ver:
            soma=soma+1
print("O número",ver,"aparece",soma,"vezes no número",m)
    
        
