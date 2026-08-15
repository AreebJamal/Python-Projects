print("            WELCOME TO THE GUESS THE NUMBER GAME")
print("you have only  5 guess")
print("   game start")

i=1
while(i<=5):

    num = int(input("enter the number\n"))

    if num==30:
        print("congratulation")
        print("you guess the no. in", i ,"guess")
        break

    elif num<=10:
        print("very small ----Try greater")
        print("you have left" , 5-i , "guess")
        if i==5:
            print("game over")
            break
        else:
            i=i+1

    elif 10<num<=20:
        print("you are going to the right path----please go far more")
        print("you have left" , 5-i , "guess")
        if i==5:
            print("game over")
            break
        else:
            i=i+1

    elif 20<num<30:
        print("try bit more")
        print("you have left" , 5-i , "guess")
        if i==5:
            print("game over")
            break
        else:
            i=i+1

    elif num>30:
        print("you are going to far")
        print("you have left" , 5-i , "guess") 
        if i==5:
            print("game over")
            break
        else:
            i=i+1              