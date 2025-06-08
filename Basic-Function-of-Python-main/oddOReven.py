def number(n):
    if n%2 == 0:
        print(n, "is a even number")
    else:
        print(n, "is a odd number")

n = int(input("Enter a number to check: "))
number(n)