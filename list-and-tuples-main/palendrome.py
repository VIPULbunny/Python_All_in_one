list1 = list(input("enter a pelendrome :"))
print(list1)
list3 = list1.copy()
list3.reverse()
print(list3)
if(list1 == list3):
    print("Entered List is a pelendrome")
else:
    print("it is not an palendrome.")