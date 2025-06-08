x = int(input("Enter a number to search in tuple : "))
numbers =(1, 4 ,9 ,16 ,25 ,36 ,49 ,64 ,81 ,100)
i=1
while numbers[i] != x:
    i+=1
print(x,"is at ",i,"th index")