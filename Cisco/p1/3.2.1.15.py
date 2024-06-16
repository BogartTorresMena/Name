c0=abs(int(input("Number: ")))

if c0==0:c0=1
p=0

while c0!=1:
    if c0%2:
        c0=3*c0+1
    else:
        c0/=2
    print(int(c0))
    p+=1
print("Pasos =",p)