n = int(input("Enter a number: "))
fact = 1
num = "1"
for i in range(1, n+1):
    fact = fact * i
    num +=str(i)
print(fact)
print(num)