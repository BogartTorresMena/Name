class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.queue = []
    def put(self,elem):
        self.queue.insert(0,elem)
    def get(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            raise QueueError

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        self.l=0
    def put(self,v):
        self.l+=1
        Queue.put(self,v)
    def get(self):
        self.l-=1
        return Queue.get(self)
    def isempty(self):
        return self.l==0

que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")
