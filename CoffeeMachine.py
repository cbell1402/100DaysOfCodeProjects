def make_coffee():
    """Prompts user for input and makes their coffee."""
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "espresso":
        compare("espresso")
    elif choice == "latte":
        compare("latte")
    elif choice == "cappuccino":
        compare("cappuccino")
    elif choice == "report":
        report()
    elif choice == "off":
        quit()
    else:
        print("I did not recognize that input, please try again.")
    make_coffee()


def report():
    """Gives a report on the resources in the machine."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def compare(coffee):
    """Compares the requested beverage against the resources."""
    if MENU[coffee]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
    elif MENU[coffee]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
    elif MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
    else:
        coinage(coffee)


def coinage(coffee):
    drink_cost = MENU[coffee]["cost"]
    print(f"A {coffee} is ${drink_cost:.2f}, please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
    if drink_cost > total:
        print("Sorry, that's not enough money. Money refunded.")
        return
    elif drink_cost <= total:
        change = total - drink_cost
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        brew_drink(coffee)


def brew_drink(coffee):
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    resources["money"] += MENU[coffee]["cost"]
    print(f"Here is your {coffee}☕, enjoy!")


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

make_coffee()