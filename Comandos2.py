import subprocess

o=-1
p=0
c=0
lastF=""
lastD=""

def pytouch(name):
    subprocess.run('touch '+name,shell=True)
    return name

def pymkdir(name):
    subprocess.run('mkdir '+name,shell=True)
    return name

def pymv(name,folder):
    subprocess.run('mv '+name+' '+folder,shell=True)

def pycp(name,folder):
    subprocess.run('cp -r '+name+' '+folder,shell=True)

def rename(name,newName):
    subprocess.run('mv '+name+' '+newName,shell=True)

def insert(name,text):
    subprocess.run('echo '+text+' >> '+name,shell=True)
    subprocess.run('cat '+name,shell=True)

def pytree(name):
    if(name==""):
        name="."
    subprocess.run(['tree '+name],shell=True)

def runFile(name):
    subprocess.run(['python3 '+name],shell=True)

while(o!=0):
    print("\n1. Create file\n2. Create folder\n3. Move\n4. Copy")
    print("5. Rename\n6. Insert to file\n7. Tree\n8. Calculator\n0. Exit")
    o=int(input("Select: "))
    if(o==1):
        lastF=pytouch(input("File name: "))
    elif(o==2):
        lastD=pymkdir(input("Folder name: "))
    elif(o==3 or o==4):
        if(o==3):
            ot="Move"
        else:
            ot="Copy"
        while(p<1 or 3<p):
            print("\n1. "+ot+" last made file\n2. "+ot+" last made folder\n3. "+ot+" other")
            p=int(input("Select: "))
        if(p==1):
            if(lastF!=""):
                if(lastD==""):
                    c=2
                while(c<1 or 2<c):
                    print("\n1. "+ot+" to last made folder\n2. "+ot+" to other folder")
                    c=int(input("Select: "))
                if(c==1):
                    if(o==3):
                        pymv(lastF,lastD)
                    else:
                        pycp(lastF,lastD)
                elif(c==2):
                    if(o==3):
                        pymv(lastF,input("Destination: "))
                    else:
                        pycp(lastF,input("Destination: "))
                c=0
            else:
                print("\nThere's no last file")
        elif(p==2):
            if(lastD!=""):
                if(o==3):
                    pymv(lastD,input("Destination: "))
                else:
                    pycp(lastD,input("Destination: "))
            else:
                print("\nThere's no last folder")
        elif(p==3):
            if(o==3):
                pymv(input("File/folder to "+ot+": "),input("Destination: "))
            else:
                pycp(input("File/folder to "+ot+": "),input("Destination: "))
        p=0
    elif(o==5):
        pymv(input("File/folder to rename: "),input("New name: "))
    elif(o==6):
        insert(input("File to insert to: "),input("Text line: "))
    elif(o==7):
        pytree(input("Folder to show: "))
    elif(o==8):#Carpeta original del programa de calculadora
        runFile("~/Documents/VisualStudio/Python/calculator.py")
    if(o!=0):
        o=-1