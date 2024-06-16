be=[]
print("Paso 1:", be)

ne=["John Lennon","Paul McCartney","George Harrison"]
for na in ne:
    be.append(na)
print("Paso 2:", be)

for i in range(2):#1: Stu Sutcliffe 2: Pete Best
    be.append(input("New name("+str(i+1)+"/2): "))
print("Paso 3:", be)

del be[-2:]
print("Paso 4:", be)

be.insert(0,"Ringo Starr")
print("Paso 5:", be)


# probando la longitud de la lista
print("Los Fav", len(be))
