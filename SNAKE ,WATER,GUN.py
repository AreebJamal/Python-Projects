import random

list = ["snake" , "water" , "gun"]
comp = random.choice(list)

print("    --SNAKE WATER GUN--")
print("you get 5 times to choose and your points will be estimated at every time")

a = 0
b = 0
i=5
while(i>=1):
    print("choose from the list-- " , list,end="---- ")
    me = input()
    print("I choose-- " ,comp)


    if me=="snake" and comp=="water":
        print("You lose\n")
        print("MY points is" , (a+1),"\n")
        print("Your points is" , b,"\n")
        a=a+1
        i=i-1
        if i==0:
            print("TIMES UP")
        else:
            print("you have", (i),"time more")

    elif me=="water" and comp=="snake":
        print("you win\n")
        print("My points is", a,"\n")
        print("Your points is" , (b+1),"\n")
        b=b+1
        i=i-1
        if i==0:
            print("TIMES UP")
        else:
            print("you have", (i),"time more")

    elif me=="water" and comp=="gun":
        print("You lose\n")
        print("MY points is" , (a+1),"\n")
        print("Your points is" , b,"\n") 
        a=a+1
        i=i-1
        if i==0:
            print("TIMES UP")
        else:
            print("you have", (i),"time more")

    elif me=="gun" and comp=="water":
        print("you win\n")
        print("My points is", a,"\n")
        print("Your points is" , (b+1),"\n")
        b=b+1
        i=i-1
        if i==0:
            print("TIMES UP")
        else:
            print("you have", (i),"time more")

    elif me=="snake" and comp=="gun":
        print("You lose\n")
        print("MY points is" , (a+1),"\n")
        print("Your points is" , b,"\n") 
        a=a+1
        i=i-1
        if i==0:
            print("TIMES UP")
        else:
            print("you have", (i),"time more")

    elif me=="gun" and comp=="snake":
        print("you win\n")
        print("My points is", a,"\n")
        print("Your points is" , (b+1),"\n")
        b=b+1
        i=i-1
        if i==0:
            print("TIMES UP")
        else:
            print("you have", (i),"time more")

    elif me==comp:
        print("Its draw\n")
        print("We both don't get any points\n") 
        i=i-1
        if i==0:
            print("TIMES UP")
        else:
            print("you have", (i),"time more")         
    
    else:
        print("INVALID input\n")
        i=i-1
        if i==0:
            print("TIMES UP")
        else:
            print("you have", (i),"time more")

       

print("Your total points are-- " , b)    
print("My total points are-- " , a) 

if a>b :
    print("You lose")  

elif b>a:
    print("Congrates you win")

else:
    print("DRAW")