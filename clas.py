from math import pi
class circle:
        def _init_(self,r):
            self.r=r
        def _del_(self):
            print("object is deleted")
        def area(self):
            return self.pi*self.r**2
        def perim(self):
            return self.pi*self.r*2
        def _str_(self):
            s=" r : "+str(self.r)
            s+="  area:  "+str(self.area())
            s+="  perim:  "+str(self.perim())
            return s
r =int(input("enter r: "))
c=circle()
print(str(c))
del c

