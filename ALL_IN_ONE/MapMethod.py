listt = [1,2,3,4,5,6,7,8,9,10]
# The map () function returns a map object(which is an iterator) of the results after applying 
# the given function to each item of a given iterable (list, tuple, etc.).
a =list(map(lambda x: x+x,listt))
print(a)