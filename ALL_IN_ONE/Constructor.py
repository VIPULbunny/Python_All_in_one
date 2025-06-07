class Animal:
    def __init__(self,Name,activity) -> None:
        self.name = Name
        self.activity = activity

    def speaks(self):
        print("The",self.name," makes the sound", self.activity)

a1 = Animal("Dog","Barking")
a1.speaks()