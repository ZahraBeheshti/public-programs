from math import pi
class point(object):
    def _init_(self,x,y):
        self.x=x
        self.y=y
    def _del_(self):
        print("object point is deleted")
    def _str_(self):
        s="x: "+str(self.x)
        s+="  y :"+str(self.y)
        return s
class circle(point):
    def _init_ (self,x,y,r):
        point._init_(self,x,y)
        self.r=r
    def _del_(self):
        print("object circle is deleted")
    def area(self):
        return self.pi*self.r**2
    def perim(self):
        return 2*pi*self.r
    def _str_(self):
    s=point. _str_(self)
    s+=" r:  "+str(self.r)
    s+="  area :  "+str(self.area())
    s+="  perim : "+str(self.perim())
    return s 
class cylinder(circle):
    def _init_ (self,x,y,r,h):
        circle._init_(self,x,y,r)
        self.h=h
    def _del_(self):
        print("object cylinder is deleted")
    def area(self):
        return circle.area(self)*2+circle.perim(self)*self.h
    def _str_(self):
        s=point._str_(self)
        s+=" r : "+str(self.r)
        s=" h: "+str(self.h)
        s=" area: "+str(self.area())

x=int(input("enter x: "))
y=int(input(" enter y: "))
p=point(x,y)
print(str(p))
del p
print("="*50)
r=int(input("enter r : "))
c= circle (x,y,r)
print(str(c))
del c
print("="*50)
h= int(input(" enter h: "))
cy=cylinder( x,y,r,h)
print(str(cy))
del cy