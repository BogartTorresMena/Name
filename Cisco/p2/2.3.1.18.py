def mysplit(st):
    st=str(st)+" "
    vs=[]
    tm=""
    for c in st:
        if c==" " or c=="\n" or c=="\t":
            if tm!="":
                vs.append(tm)
                tm=""
        else:
            tm+=c
    return vs

print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
