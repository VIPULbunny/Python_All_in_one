class circle():
    def __init__(self,radius):
        self.radius = radius
        print("Radius = ", self.radius)
    
    def area(self):
        print("Area of circle =",3.14*(self.radius **2))
    
    def para(self):
        print(2* 3.14* self.radius)

rad = circle(5)
rad.area()
rad.para()