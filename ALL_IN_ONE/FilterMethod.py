arr = [1,2,3,4,5,6,7,8,9]
# The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.
print(list(filter(lambda x: x%2==0,arr)))
