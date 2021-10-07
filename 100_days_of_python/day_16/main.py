from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
turn_off = False
while turn_off == False:
    order = input(f"What would you like? ({menu.get_items()})")
    drink = menu.find_drink(order)
    if order == 'off':
        turn_off = True
    elif order == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        money_machine.make_payment(drink.cost)
        coffee_maker.is_resource_sufficient(drink)
        coffee_maker.make_coffee(drink)
