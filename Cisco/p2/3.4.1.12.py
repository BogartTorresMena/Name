import time

class Timer:
    def __init__(self,h,m,s):
        self.t=[h,m,s]

    def __str__(self):
        so=""
        for i in range(3):
            ns=str(self.t[i])
            if len(ns)==1:
                ns="0"+ns
            so+=ns
            if i!=2:
                so+=":"
        return so

    def next_second(self):
        m=[24,60,60]
        for i in range(2,-1,-1):
            self.t[i]=(self.t[i]+1)%m[i]
            if self.t[i]!=0:
                break

    def prev_second(self):
        m=[24,60,60]
        for i in range(2,-1,-1):
            b=self.t[i]!=0
            self.t[i]=(self.t[i]-1)%m[i]
            if b:
                break

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
while True:
    time.sleep(1)
    timer.next_second()
    print(timer)