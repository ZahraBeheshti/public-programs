from numpy import choose


def menu():
    print("1:append    ")
    print("2: delete   ")
    print("3: update   ")
    print("4:search student No   ")
    print("5:search name   ")
    print("6:report all   ")
    print("7: exit   ")
    return choose
    def findStNo(StNo):
        myfile=open("D:/GitHub/file/student.cvc",'+a')
        myfile.seek(0)
        lines=myfile.readlines()
        recNo=0
        for line in lines:
            curRecord=line.split(',')
            if (StNo==curRecord[0]):
                return recNo 
            recNo=recNo+1
        myfile.close()
        returen -1
    def findName(fname,lname):
        myfile=open("D:/GitHub/file/student.cvc",'+a')
        myfile.seek(0)
        lines=myfile.readlines()
        recNo=0
        for line in lines:
            curRecord=line.split(',')
            if (fname==curRecord[1] and lname==curRecord[2]):
                return recNo 
            recNo=reccNo+1
        myfile.close()
        return -1
    def insert():
        stNo=input("enter stno: ")
        recNo=findStNo(stNo)
        if recNo==-1:
            fname=input(" enter fisr name: ")
            laname= input( " enter last name: ")
            average=float(input("enter average: " ))
            line=stNo+ ','+fname+','+str(average)+"\n"
            myfile=open("D:/GitHub/file/student.cvc",'+a')
            myfile.write(line)
            myfile.close()
        else:
            myfile=open("D:/GitHub/file/student.cvc",'+a')
            lines=myfile.readlines()
            curRecord=lines[recNo].split(',')
            printiInfo(curRecord)
            myfile.close()
        return
    def printInfo(curRecord):
        print("_"*40)
        print("student number", curRecord[0])
        print("first name: ",curRecored[1])
        print("last name :",curRecord[2])
        print("average: ",curRecord[3])
        print("_"*40)
        return
    def delete():
        stNo= input("enter stno: ")
        recNo=findStNo(stNo)
        if recNo!=-1
        myfile=open("D:/GitHub/file/student.cvc",'+a')
        lines=myfile.readlines() 
        curRecord=lines[recNo].split(',')
        printInfo(curRecord)
        ans=input("are you sure to delete?")
        if ans=='y' or ans=='Y': del lines[recNo] 