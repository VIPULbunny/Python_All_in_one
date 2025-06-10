class complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def complexNum(self):
        print(self.real,"i + ",self.imag,"j")
    
    # def AddNum(self,num2):
    #     NewReal = self.real + num2.real 
    #     NewImg = self.imag + num2.imag
    #     return complex(NewReal, NewImg)

    def __add__(self,num2):
        NewReal = self.real + num2.real 
        NewImg = self.imag + num2.imag
        return complex(NewReal, NewImg)
    
    def __sub__(self,num2):
        NewReal = self.real - num2.real 
        NewImg = self.imag - num2.imag
        return complex(NewReal, NewImg)


num1 = complex(3,5)
num1.complexNum()

num2 = complex(6,8)
num2.complexNum()

# num3 = num1.AddNum(num2)
# num3.complexNum()

num3 = num1 + num2
num3.complexNum()

num3 = num1- num2
num3.complexNum()