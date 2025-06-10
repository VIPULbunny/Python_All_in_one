class student:
    def __init__(self,phy,che,maths):
        self.phy = phy
        self.che = che
        self.maths = maths
   

    @property
    def Percentage(self):
        return str((self.phy + self.che + self.maths) / 3 ) + "%"


p1 = student(90,91,89)
print(p1.Percentage)

p1.phy = 100
print(p1.Percentage)
