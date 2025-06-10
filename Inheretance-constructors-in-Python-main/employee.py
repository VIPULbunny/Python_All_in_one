class emp():
    def __init__(self,role,dept,scale) -> None:
        self.role = role
        self.dept = dept
        self.scale = scale
    
    def showDetails(self):
        print("Role = ",self.role,
              "\ndept = ",self.dept,
              "\nScelery = ",self.scale)

class enginerr(emp):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        super().__init__("Engineer","AI","90,000")

    def enggDetails(self):
        print("Name = ",self.name,
              "\nage = ",self.age,)

engg1 = enginerr("Vipul",21)
engg1.showDetails()
engg1.enggDetails()