x = int(input("Mande um número:"))
y = int(input("Mande outro número:"))
z = int(input("Mande mais um número:"))


if x > y and y > z:
    print (x,y,z)
else:
    if x > y and z > y:
        print (x,z,y)
    else:
        if y > x and x> z:
            print (y,x,z)
        else:
            if y > x and z > y:
                print (y,z,x)
            else:
                if z > x and x > y:
                    print (z,x,y)
                else:
                    print (z,y,x)
            
