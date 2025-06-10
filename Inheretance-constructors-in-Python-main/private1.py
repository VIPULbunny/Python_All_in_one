class person:
    __name= "anomynious"

    def __hello(self):
        print("Hello vipul")

    def welcome(self):
        self.__hello()

p1 = person()

print(p1.welcome())