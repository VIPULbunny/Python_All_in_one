str1 = input("Enter a string: ")

# str1 = str1.swapcase()
# print(str1)

for i in str1:
    if i==i.upper():
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")