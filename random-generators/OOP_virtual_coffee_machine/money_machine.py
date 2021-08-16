class MoneyMachine:
    
    CURRENCY = "$"
    
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    
    def __init__(self):
        self.profit = 0
        self.payment = 0
    
    
    def report(self):
        """Prints the current profit."""
        print(f"Money: {self.CURRENCY}{self.profit}")
    
    
    def process_payment(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert your payment.")
        for coin in self.COIN_VALUES:
            self.payment += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.payment
    
    
    def transaction(self, cost):
        """Returns True when payment is accepted, or False if declined."""
        self.process_payment()
        if self.payment >= cost:
            change = round(self.payment - cost, 2)
            print(f"Here is your {self.CURRENCY}{change} change.")
            self.profit += cost
            self.payment = 0
            return True
        else: 
            print(f"Sorry the payment has declined.")
            return False