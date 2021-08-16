class CoffeeMaker:
    """Models the machine that makes the coffee."""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
    
    
    def report(self):
        """Prints a report of all resources."""
        print(f"Water:{self.resources['water']}ml")
        print(f"Milk:{self.resources['milk']}ml")
        print(f"Coffee:{self.resources['coffee']}g")
    
    
    def enough_resources(self, drink):
        """Returns True when the order can be made, False if there is not enough ingredients."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry {item} has sold out!")
                can_make = False
        return True
    
    
    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Thank you for the support! Here is your {order.name}. Enjoy!")