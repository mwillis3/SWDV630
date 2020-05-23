#-------------------------------------------------------------------------------
# author: Marcelious Willis
# sem   : Summer 2020
# class : SWDV-630 Object-oriented programming
# @file : Pizza.py
#-------------------------------------------------------------------------------
class Pizza:
    # Constructor for the Pizza superclass
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity
        self.price = 0
        self.total = 0
        self.base_price = 0

    # Method to get the price of the pizza based on size.
    def get_price(self):
        if self.size == "S":
            self.price = 3.99
        elif self.size == "M":
            self.price = 5.99
        elif self.size == "L":
            self.price = 7.99
        elif self.size == "XL":
            self.price = 9.99
        else:
            print("Unrecognized size selected. Accepted sizes are S, M, L, XL.")
            return
        print("The price of size " + self.size + " is: " + str(self.price))
        return
    
    # Method to get the total price based on number of pizzas ordered.
    def get_total_price(self):
        self.total = self.quantity * self.price + self.base_price
        print("Your Total Price is: " + str(self.total))
        return
            

class Cheese(Pizza):
    # Constructor for the Cheese subclass
    def __init__(self, *args, **kwargs):
        self._toppings = ["Sauce", "Cheese"]
        super(Cheese, self).__init__(*args, **kwargs)

    # Method to get toppings of the pizza
    def get_toppings(self):
        print(self._toppings)
        return

    # Method to base price of the pizza type based on toppings
    def get_base_price(self):
        self.base_price = 0.1 * len(self._toppings)
        print("The price of your toppings is: " + str(self.base_price))
        return

class Pepperoni(Pizza):
    # Constructor for the Pepperoni subclass
    def __init__(self, *args, **kwargs):
        self._toppings = ["Sauce", "Pepperoni", "Cheese"]
        super(Pepperoni, self).__init__(*args, **kwargs)

    # Method to get toppings of the pizza
    def get_toppings(self):
        print(self._toppings)
        return

    # Method to base price of the pizza type based on toppings
    def get_base_price(self):
        self.base_price = 0.1 * len(self._toppings)
        print("The price of your toppings is: " + str(self.base_price))
        return

class Veggie(Pizza):
    # Constructor for the Veggie subclass
    def __init__(self, *args, **kwargs):
        self._toppings = ["Sauce", "Cheese", "Onions", "Peppers", "Olives"]
        super(Veggie, self).__init__(*args, **kwargs)

    # Method to get toppings of the pizza
    def get_toppings(self):
        print(self._toppings)
        return

    # Method to base price of the pizza type based on toppings
    def get_base_price(self):
        self.base_price = 0.1 * len(self._toppings)
        print("The price of your toppings is: " + str(self.base_price))
        return

#-------------------------------------------------------------------------------
# Driver Code
cheese_order = Cheese("S", 2)
cheese_order.get_toppings()
cheese_order.get_price()
cheese_order.get_base_price()
cheese_order.get_total_price()
print("\n")
veggie_order = Veggie("L", 3)
veggie_order.get_toppings()
veggie_order.get_price()
veggie_order.get_base_price()
veggie_order.get_total_price()
print("\n")
pepperoni_order = Pepperoni("XL", 1)
pepperoni_order.get_toppings()
pepperoni_order.get_price()
pepperoni_order.get_base_price()
pepperoni_order.get_total_price()