import os
print(os.getcwd())
os.chdir("E:\OH soldier")
# print(os.getcwd())
# with open("") as f:
#     print(f.readlines())

# print(os.listdir())
# for i in os.listdir():
#     os.rename(i , i.lower())

for i in os.listdir():
    if i=='this.txt' and i=='that.txt':
        break
    else:
         os.rename(i  , i.capitalize())
print(os.listdir())

n=1
# for i in os.listdir():
#     if i.endswith('.png'):
#         os.rename(i , str(n)+'.png')
#         n= n+1

print(os.listdir())        