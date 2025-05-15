'''
    Create a class called Order which stores item & its price
    Use Dunder Function __gt__() to convey that
        order1 > order2 if price of order1 > price of order 2
'''

class Order: 
    def  __init__(self, name, price):
        self.name = name
        self.price = price

    def __gt__(self, odr2):
        if(self.price > odr2.price):
            return "order1 > order2"
        else:
            return "order1 < order2"

odr1 = Order("Chips", 20)
odr2 = Order("Tea", 15)

result = odr1 > odr2
print(result)