class order():
    def __init__(self,Item,price) -> None:
        self.item = Item
        self.price = price

    def __gt__(self,order2):
        return self.price > order2.price

order1 = ("Soap", 10)
order2 = ("Shampoo", 20)
print(order1 > order2)