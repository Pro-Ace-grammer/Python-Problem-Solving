class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    
    def __gt__(self,other):
        return self.price>other.price
    
ord1 = Order('Toothpaste',20)
ord2 = Order('Soap',39)
print(ord2>ord1)