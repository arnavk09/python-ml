from os import name
import string


class Item:
    def __init__(self, name, price, qty) -> None:
        print(f"initiated object : {name} price : {price} and qty : {qty}")
        self.name = (input("Name: "))
        self.price = int(input("Price: "))
        self.qty = int(input("Qty: "))

    def totalPrice(self):
        return self.price*self.qty


item1 = Item('Phone', 3, 1000)
item2 = Item('Laptop', 5, 2000)

print(item1.totalPrice())
print(item2.totalPrice())