dic1 = {"python":"language\nfor more information click on this\nhttps://www.python.org" ,
        "c++":"programming" , "java":"script" ,
        "note":"pad" , "adobe":"photoshope"}

print("Enter your word")
word = input()

if word in dic1:
    print("meaning is :" , dic1[word])
    

else:
    print("not found")    
