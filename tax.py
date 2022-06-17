class Employee:
    def _init_(self,code,fname,lname,salary):
        self.code=code
        self.fname=fname
        self.lname=lname
        self.saalary=salary
    def _del_(self):
        print("object is deleted")
    def caltax(self):
        if self.salary < 2000: return 0 
        else: return(self.salary- 2000)*10/100
    def calinsurance(self):
        return self.salary*7/100
    def pay(self):
        return self.salary-self.caltax()-self.calinsurance()
    def _str_(self):
        s="code:   "+self.code
        s+=" firat name "+self.fname
        s+=" last name "+self.lname
        s+=" salary is :"+str(self.salary)
        s+=" insurance is : "+str(self.calinsurance())
        s+=" tax is: "+str(self.caltax())
        s+= "pay is : "+str(self.pay())
        return S
code= input("enter a code : ")
fname=input("enter name : ")
lname=input("inter last name: ")
salary=int(input("enter salary : "))
e= Employee()
print(str(e))
del e        
