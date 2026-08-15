#                  CHECK THE PALINDROME
print("------------CHECKING PALINDROME-----------")
str1 = input("Enter string--:  ")

original = str1[0:]
reverse = str1[::-1]

if original==reverse:
    print("YES it is palindrome")

else:
    print("NO it is not palindrome")


