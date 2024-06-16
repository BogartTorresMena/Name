def read_int(prompt, min, max):
    v=input(prompt)
    try:
        v=int(v)
        if v<min or max<v:
            print("Error: el valor no está dentro del rango permitido("+str(min)+".."+str(max)+")")
        else:
            return v
    except:
        print("Error: entrada incorrecta")

v=None
while v==None:
    v=read_int("Ingresa un numero entre -10 a 10: ", -10, 10)

print("El número es:", v)