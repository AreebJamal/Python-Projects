#----------FIBONACCHI SERIES------------

print(".....FIBONACCHI SERIES.....")
var1 = 0
var2 = 1
sum = 1
for i in range(15):
    if i==0:
        print(i , end=" ")

    elif i==1:
        print(i , end=" ")

    else:
        sum = var1+var2
        print(sum , end=" ")
        var1 = var2   
        var2 = sum 
print("........")


