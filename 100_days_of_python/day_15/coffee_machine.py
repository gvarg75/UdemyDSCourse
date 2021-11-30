from typing import Sequence
from data import MENU, resources


remaining_resources = resources
remaining_resources['money'] = 0
machine_power = True
drink_orders = ['espresso', 'latte', 'cappuccino']

def check_resources(order, remaining_resources):
    chosen_order = MENU[order]['ingredients']
    for ingredient in remaining_resources:
        if remaining_resources[ingredient] <= chosen_order[ingredient]:
            return print(f'Sorry, there is not enough {ingredient}')
        else:
            return True

def make_coffee(order,remaining_resources):
    chosen_order = MENU[order]
    ingredients_water = chosen_order["ingredients"]['water']
    ingredients_coffee = chosen_order["ingredients"]['coffee']
    ingredients_milk = chosen_order["ingredients"]['milk']
    ingredients_money = chosen_order['cost']
    remaining_resources['water'] -= ingredients_water
    remaining_resources['coffee'] -= ingredients_coffee
    remaining_resources['milk'] -= ingredients_milk
    remaining_resources['money'] += ingredients_money
    return remaining_resources

def pay(order, quarters, dimes, nickles, pennies):
    order_cost = MENU[order]['cost']
    sum_quarters = quarters * .25
    sum_dimes = dimes * .1
    sum_nickles = nickles * .05
    sum_pennies = pennies * .01
    subtotal = sum([sum_quarters, sum_dimes, sum_nickles, sum_pennies])
    change = round(subtotal - order_cost,2)
    return change
    




while machine_power == True:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    print('Please insert coins.')
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    change = pay(order, quarters, dimes, nickles, pennies)
    if change >= 0:
        print(f"Here is ${change} in change.")
        if order in drink_orders:
            if check_resources(order, remaining_resources):
                water, milk, coffee, money = make_coffee(order, remaining_resources).values()
                print()

        elif order == 'report':
            print(remaining_resources)
        else: 
            machine_power = False
    else:
        print("Sorry, not enough money")
    
    remaining_resources = {
        'water': water,
        'milk': milk,
        'coffee': coffee,
        'money': money}
    print(remaining_resources)

