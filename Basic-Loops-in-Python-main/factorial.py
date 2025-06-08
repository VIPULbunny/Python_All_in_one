#Factorial of n numbers
n = int(input("Enter a nummber to get factorial: "))
fact = 1
i=1

for val in range(1,n+1):
    fact= val * fact
print(fact)