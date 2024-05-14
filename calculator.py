#Declaracion de variables globales
import time

n1=0
n2=0
o=-1

n1=float(input("Ingresa el primer numero: "))
n2=float(input("Ingresa el segundo numero: "))

def sum():
    return n1+n2

def subst():
    return n1-n2

def divid():
    return n1/n2

def multi():
    return n1*n2

while(o!=0):
    o=int(input("\n1.- Sumar\n2.- Restar\n3.- Dividir\n4.- Multiplicar\n0.- Salir\nSelecciona:"))
    print("\n")
    if o==1:
        print("La suma es: ",sum())
    elif o==2:
        print("La resta es: ",subst())
    elif o==3:
        print("La division es: ",divid())
    elif o==4:
        print("La multiplicacion es: ",multi())
    if o!=0:
        o=-1
        time.sleep(2)