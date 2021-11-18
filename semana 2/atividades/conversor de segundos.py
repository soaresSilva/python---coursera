segundostotal=int(input("Por favor, entre com o número de segundos que deseja converter:"))

dias = segundostotal // 86400
sobra1 = segundostotal % 86400
horas = sobra1 // 3600
sobra2 = sobra1 % 3600
minutos = sobra2 // 60
segundos = sobra2 % 60

print(dias,"dias",horas,"horas",minutos,"minutos e",segundos,"segundos.")
