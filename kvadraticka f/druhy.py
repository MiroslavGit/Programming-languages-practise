import math

a = int(input("Zadaj a"))
b = int(input("Zadaj b"))
c = int(input("Zadaj c"))

print("Tvoja rovnica je :", a,"x*x+",b,"x+",c)

D = b*b - 4 *a *c

if(D < 0):
    print("Rovnica nemá riešenie")
elif(D == 0):
    print("Rovnica má jedno riešenie")
    x1 = -b/2*a
    print("X1 je:",round((x1),2))
else:
    odmocninaD = round( math.sqrt(D),2)
    print("Odmocnina s diskriminantu je:",odmocninaD)
    x1 = (-b-odmocninaD)/2*a
    x2 = (-b+odmocninaD)/2*a
    print("X1 je:",round((x1),2)," X2 je: ", round((x2),2))
