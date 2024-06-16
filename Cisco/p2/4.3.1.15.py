f=open("samplefile.txt","w")
f.write("ezsxdrcfvfycvhgjyrdhfgrsxuedsjgvedcsg")
f.close
f=open("samplefile.txt","r")
c=f.read(1)
d={}
while c!="":
    if c in d.keys():
        d[c]+=1
    else:
        d[c]=1
    c=f.read(1)
for a,b in d.items():
    print(a,"->",b)