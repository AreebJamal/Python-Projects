import re
import os

my_str = """ hello my name is john banega don
kya kehte ho areebjamal1003@gmail.com 
this is my another id --  jamalareeb1003@gmail.com
hdks8@gmail.com 83737tsgx xjb ggaag3453@gmail.com
the happy ending """

# patt = re.compile(r'(\w+@gmail.com)')
patt = re.compile(r'[a-zA-Z0-9._+%]+@[a-zA-Z0-9._+%]+[.][a-zA-Z.0-9]+')

email = []
matches = patt.finditer(my_str)
for match in matches:
    print(match)
    list = match.span()
    email.append(my_str[list[0]:list[1]])
print(email)

#storing in a file 
os.chdir("E:\VISUAL_STUDIO_CODE\PYTHON_FOR_BEGINNERS\EXPRESSIONS")
with open("regex.txt" , "a") as f:
    for i in range(1 , len(email)+1):
        f.write(f"Email {i} -- {email[i-1]}\n") 