n = int(input("Me mande um número com 6 dígitos : "))
par=0
impar=0
if n > 0:
    cem_mil= n // 100000
    cem_mil=cem_mil%2
    print(cem_mil)
    if cem_mil==0:
        par=par+1
    else:
        impar=impar+1
    dez_mil= n // 10000
    dez_mil=dez_mil%2
    print(dez_mil)
    if dez_mil==0:
        par=par+1
    else:
        impar=impar+1
    mil= n // 1000
    mil=mil%2
    print(mil)
    if mil==0:
        par=par+1
    else:
        impar=impar+1
    centena= n // 100
    centena=centena%2
    print(centena)
    if centena==0:
        par=par+1
    else:
        impar=impar+1
    dezena= n // 10
    dezena=dezena%2
    print(dezena)
    if dezena==0:
        par=par+1
    else:
        impar=impar+1
    unidade= n // 1
    unidade=unidade%2
    print(unidade)
    if unidade==0:
        par=par+1
    else:
        impar=impar+1
print("Par",par)
print("Impar",impar)
    
        
