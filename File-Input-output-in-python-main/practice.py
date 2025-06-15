with open("practice1","r") as f:
    data = f.read()
    new_data= data.replace("python","java")
    print(new_data)

with open("practice1","w") as f:
    data = f.write(new_data)