str1 = input("Enter a string: ").lower()

# var1 = reversed(str1)
var1 = str1[::-1]

if list(str1) == list(var1):
    print("Palindrome")
else:
    print("Not Palindrome")