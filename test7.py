import random
ran=random.randint(1,50)
print('first ran is', ran)
i=int(input('choose a number: 1 for ran>num 2 for ran<num 0 for num=ran'))
while i==1:
    print(' ran is',ran,' and ran is bigger')
    ran=random.randint(1,ran)
    print('nw ran',ran)
    i=int(input('choose a number: 1 for ran>num 2 for ran<num 0 for num=ran'))
while i==2:
    print(' ran is',ran,' and ran is smaller')
    ran=random.randint(ran,50)
    print('nw ran',ran)
    i=int(input('choose a number: 1 for ran>num, 2 for ran<num, 0 for num=ran'))
else :
        print('nw ran',ran)
        print('you did it')
