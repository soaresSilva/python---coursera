x = int(input("Mande um número de y:"))
y = int(input("Mande um número de x:"))
x2 = int(input("Mande um número de y2:"))
y2 = int(input("Mande um número de x2:"))

d = ((x - x2)**2 + (y - y2)**2)**(1/2)
print(d)
if d >= 10:
    print ("longe")
else:
    print ("perto")
            
