def even(num):
    arr=[]
    for i in num:
        if i % 2==0:
            arr.append(i)
        else:
            pass
    return arr

num = (1,2,3,4,5,6,7,8,9,10)
print(even(num))