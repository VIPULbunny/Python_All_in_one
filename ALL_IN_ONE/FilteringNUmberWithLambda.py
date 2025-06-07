list = [1,2,3,4,5,6,7,8,9,10]
print((lambda list : [x for x in list if x%2==0])(list))