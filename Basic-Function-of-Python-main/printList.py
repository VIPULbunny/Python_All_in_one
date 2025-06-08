def printLIST(list,i=0):
    if i == len(fruits):
        return
    print(fruits[i])
    printLIST(list,i+1)

    # for i in range(0,len(fruits)):
    #     print(fruits[i])
    #     i += 1


fruits = ["mango","banana","ananas","kiwi","cherry","chiku"]
printLIST(fruits)