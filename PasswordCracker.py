from random import *
actualpwd = input("Enter your password")
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z',0,1,2,3,4,5,6,7,8,9,'!','@','#','$','%','&','*','-','_','=','+','/','A','B','C','D','E','F','G','H','I'
            ,'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
myguess = ""
while (myguess != actualpwd):
    myguess = ""
    for i in range(len(actualpwd)):
        guessletter = password[randint(0, 73)]
        myguess = str(guessletter) + str(myguess)
    print(myguess)
print("Your password is : ",myguess)