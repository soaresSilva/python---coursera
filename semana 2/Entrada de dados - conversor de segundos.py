segundos = input ("Quantidade de segundos ? ")
totalsegundos = int(segundos)


dias = totalsegundos // 86400
restos_segundos = totalsegundos % 86400
horas = restos_segundos // 3600
segun_restan = totalsegundos % 3600
minutos = segun_restan // 60
segun_final = segun_restan % 60

print (dias ,"dias",horas, " horas", minutos, " minutos e", segun_final," segundos.")
