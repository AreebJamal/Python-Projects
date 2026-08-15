# num = int(input("Enter the number--  "))

# if num==0:
#     a = 1
#     print(a)

# elif num==1:
#     a = 1
#     print(a)

# else :
#     a=num
#     for i in range(1,(num-1)):
#         a = a*(num-i)
#         # num = num-1
#         i = i+1
#     print(a)   


def fac(n):
    if n==0:
       return 1

    elif n==1:
        return 1

    else :
        return n*fac(n-1)
 
    
# num = int(input("Enter the number---   "))
print("enter the no.")
num = int(input())
print(fac(num))