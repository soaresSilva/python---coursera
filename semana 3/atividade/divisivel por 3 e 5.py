x = int(input("Mande um número:"))


y = x % 3
z = x % 5
if y == 0 and z==0:
    print ("FizzBuzz.")
else:
    print (x)
