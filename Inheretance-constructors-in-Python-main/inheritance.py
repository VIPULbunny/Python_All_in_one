class car():
    
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started..!!")

    @staticmethod
    def stop():
        print("Car stopped...!!")

class toyataCar(car):
     def __init__(self, name,type):
        self.name = name
        super().__init__(type)
        super().start()

# class Supra(toyataCar):
#     def __init__(self, name):
#         self.name = name

s1 = toyataCar("supra","petrol")
print(s1.type)
print(s1.name)