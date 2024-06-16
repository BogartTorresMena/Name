class dis:
    def __init__(self):
        self.leds=[(),(),(),(),()]

    def draw(self):
        for r in self.leds:
            for l in r:
                if l:
                    print("#",end="")
                else:
                    print(" ",end="")
            print()

    def num(self,r):
        rl=[(0,0,1),(1,0,0),(1,0,1),(1,1,1)]
        for i in range(5):
            self.leds[i]+=rl[r[i]]
    
    def addn(self,n):
        if len(self.leds[0]):
            for i in range(5):
                self.leds[i]+=(0,)
        if n==0:
            self.num([3,2,2,2,3])
        elif n==1:
            self.num([0,0,0,0,0])
        elif n==2:
            self.num([3,0,3,1,3])
        elif n==3:
            self.num([3,0,3,0,3])
        elif n==4:
            self.num([2,2,3,0,0])
        elif n==5:
            self.num([3,1,3,0,3])
        elif n==6:
            self.num([3,1,3,2,3])
        elif n==7:
            self.num([3,0,0,0,0])
        elif n==8:
            self.num([3,2,3,2,3])
        else:
            self.num([3,2,3,0,3])

    def disp(self,n):
        for c in n:
            self.addn(int(c))
        self.draw()


n=input("Int positive number: ")
try:
    ni=int(n)
    if ni<0:
        ni=0
    n=str(ni)
except:
    n="0"
d=dis()
d.disp(n)