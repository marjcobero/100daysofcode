from data import MENU, resources


print("Hi, Welcome to Marj's Coffee Shop!")


profit = 0

def coffee(order_ingredients):
    """Returns True when the order can be made, False if the ingredients are low."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def purchase():
    """Returns the total calculated from the coin inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def transaction(payment, price):
    """Returns True when the payment proccessed, or False if its declined."""
    if payment >= price:
        change = round(payment - price, 2)
        print(f"Here is your ${change} in change.")
        global profit
        profit += price
        return True
    else:
        print("Sorry the payment is declined.")    
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources.."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Thank you for the support! Here is your {drink_name}! ☕️. Enjoy!")


is_on = True
while is_on:
    ask_guess = input("What would you like? (espresso/latte/cappuccino): ")
    if ask_guess == "off":
        is_on = False
    elif ask_guess == "report":
        print(f"{resources['water']}ml")
        print(f"{resources['milk']}ml")
        print(f"{resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[ask_guess]
        if coffee(drink['ingredients']):
            payment = purchase()
            if  transaction(payment, drink['cost']):
                make_coffee(ask_guess, drink['ingredients'])