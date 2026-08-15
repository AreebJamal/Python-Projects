#--MENU DRIVEN PROGRAM OF ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION AND MODULES USING IF CONDITION------

print("------SIMPLE CALCULATOR------")


while(True):
    num1 = int(input("Enter the Ist number--:  "))
    num2 = int(input("Enter the Ind number--:  "))

    dict = {"ADDITION":' + ' , "SUBTRACTION":' - ' , "MULTIPLICATION":' * ' , "DIVISION":' / ' , "MODULO":" % "}
    i=0
    
    print("Which operator you want to use\nChoose from this---  " , dict)
    oper = input()

    if oper=='+':
        add = num1 + num2
        print("The addition of",num1 , "&" ,num2 , "is--:  " , add)

    elif oper=='-':
        sub = num1 - num2
        print("The subtraction of",num1 , "&" ,num2 , "is--:  " , sub)  

    elif oper=='*':
        mul = num1 * num2
        print("The multiplication of",num1 , "&" ,num2 , "is--:  " , mul)   

    elif oper=='/':
        div = num1 / num2
        print("The divion of",num1 , "by" ,num2 , "is--:  " , div)

    elif oper=='%':
        mod = num1 % num2
        print("The modulo of",num1 , "&" ,num2 , "is--:  " , mod)     

    else:
        print("INVALID SYNTAX\n")

    print("\n")   