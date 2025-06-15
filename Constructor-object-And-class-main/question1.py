class student:
    def __init__(self,name,marks ):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Average marks of",s1.name,"=",(sum)/3)


s1 = student("Vipul",[10,20,30])
s1.avg()