print("enter 1st no.")
n1 = int(input())
print("enter 2nd no.")
n2 = int(input())
print("choose operator\n1 for '+' , 2 for '-' , 3 for '*' , 4 for '/'")
oper = int(input())

if n1==45 and n2==4:
    print(60)

elif n1==36 and n2==6:
    print(8)

elif n1==41 and n2==35:
    print(4) 

else:       
    if oper==1:
        print(n1+n2)

    elif oper==2:
        print(n1-n2)

    elif oper==3:
        print(n1*n2) 

    elif oper==4:
        print(float(n1/n2))           

    else:
        print("not valid")    


