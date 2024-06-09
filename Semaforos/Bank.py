#Gestión de Tickets en un Banco

import threading as thr
import time
import random

services=["depósito","retiro","consulta","transferencia","otro proceso"]#nombres

class client:#Clase cliente
    def __init__(self,id,serv):
        self.id=id
        if serv==-1:#aleatorio
            self.serv=random.randint(0,4)
        else:#manual
            self.serv=serv

class vent:
    def __init__(self,serv,nt):
        self.serv=serv
        self.sem=thr.Semaphore(nt)#valor del semaforo

#5 ventanillas con 1 o 2 espacios
vens=[vent(i,random.randint(1,2)) for i in range(5)]
class control:
    def assign(cli):
        with vens[cli.serv].sem:#Semaforo de la ventanilla
            print("Cliente",cli.id,"pasa a ventanilla",cli.serv+1)
            time.sleep(2)
            print("Cliente",cli.id,"se va")

ctrl=control
def visit(cli):
    print("Cliente",cli.id,"viene a hacer",services[cli.serv])
    ctrl.assign(cli)#Asignar a ventanilla

#20 clientes vienen por servicios aleatorios
clis=[client(i+1,-1) for i in range(20)]

thrs=[]
for c in clis:
    thread=thr.Thread(target=visit,args=(c,))
    thrs.append(thread)
    thread.start()

for t in thrs:
    t.join()

print("Terminado")