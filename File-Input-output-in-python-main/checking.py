def findword():
    with open("D:\Python- Apna College\python codes\lecture 7\practice1","r") as f:
        para = f.read()
        if (para.find("learning")):
            print("Found")
        else:
            print("NOT FOUND")

findword()

def findline():
    word ="learning"
    data = True
    line_no = 1
    with open("D:\Python- Apna College\python codes\lecture 7\practice1","r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
                return
            line_no +=1
        return print("-1")
findline()