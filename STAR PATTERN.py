print("Enter the nummber")
n = int(input())
print("enter the boolean charater")
b = int(input())
print(bool(b))

if bool(b)==True:
    for i in range(n+1):
        print("*"*i)

else:
    for i in range(n,0,-1):
        print("*"*i)
        #i=i-1        

num = int(input("enter the number of rows--:  "))

for i  in range(n,0,-1):
    for j in range(n+1):
        print(" "*(n-1),"*"*i)

            

