numbers =(1, 4 ,9 ,16 ,25 ,36 ,49 ,64 ,81 ,100)
x = int(input("Enter a number to search: "))
i=0
for val in numbers:
    if(val == x):
        print("Number found at",i)
        break
    i+=1