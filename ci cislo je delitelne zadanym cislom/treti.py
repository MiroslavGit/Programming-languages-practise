import math

a = int(input("Zadaj cislo: "))
b = int(input("Zadaj cislo ktorým chceš deliť predchádzajúce číslo: "))

zvysok = a % b;

if(zvysok == 0):
    print("Číslo ", a, "je deliteľné číslom ", b)
else:
    print("Číslo ", a, "nie je deliteľné číslom ", b)
