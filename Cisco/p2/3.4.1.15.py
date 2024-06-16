import math

class Point:
    def __init__(self,x=0.0,y=0.0):
        self.x=x
        self.y=y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def distance_from_xy(self,x,y):
        return math.sqrt(math.pow(self.x-x,2)+math.pow(self.y-y,2))

    def distance_from_point(self,point):
        return self.distance_from_xy(point.getx(),point.gety())

class Triangle:
    def __init__(self,vertice1,vertice2,vertice3):
        self.v=[vertice1,vertice2,vertice3]

    def perimeter(self):
        p=0
        for i in range(3):
            p+=self.v[i].distance_from_point(self.v[i-1])
        return p

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
