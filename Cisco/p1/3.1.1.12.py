year = int(input("Introduce un año:"))

if(1582<=year):
    if(year%4!=0):
        print("Año Común")
    elif(year%100!=0):
        print("Año Bisiesto")
    elif(year%400!=0):
        print("Año Común")
    else:
        print("Año Bisiesto")
else:
    print("No esta dentro del período del calendario Gregoriano")