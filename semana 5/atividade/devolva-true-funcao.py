def vogal (x):
    if x == "A" or x == "a" or x == "E" or x == "e" or x == "I" or x == "i" or x == "O" or x == "o" or x == "U" or x == "u":
        y = 1
    else:
        y=0
    return y

x = input("Escreva : ")
y = vogal(x)
if y == 1:
    print("True")
else:
    print("False")
