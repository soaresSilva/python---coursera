i = 0
x=0
y=0
while i < 5:
    x = int(input("Me fala um número: "))
    x = x + y
    y = x
    i+=1
print("o total é",x)
