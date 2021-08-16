from menu import Menu, MenuItem 
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

print("Hi, Welcome to Marj's Virtual Coffee Shop!")
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        enough_resources = coffee_maker.enough_resources(drink)
        payment_successful = money_machine.transaction(drink.cost)
        if enough_resources and payment_successful:
            coffee_maker.make_coffee(drink)