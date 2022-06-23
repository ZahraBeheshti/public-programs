def filterfile(oldfile,newfile,charfilter):
    myfile1=open(oldfile,'rt')
    myfile2=open(newfile,'wt')
    while True: 
        char=myfile1.read(1)
        if char=="": break
        if char==charfilter: continue
    myfile2.write(char)
    myfile1.close()
    myfile2.close()
def showfile(filename):
    print("------filename :", filename,"--------")  
    myfile=open(filename)
    lines=myfile.read()
    print(lines)
    myfile.colse()
oldfile=input("enter oldfilename:  ")
newfile=input("enter newfilwname:  ")
charfilter=input("filter char:  ")
showfile(oldfile)
filterfile(oldfile,newfile,charfilter)
showfile(newfile)






