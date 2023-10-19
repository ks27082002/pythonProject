class CoffeeMachine:
    def __init__(self):
       self.MENU = {
           "espresso": {
               "ingredients": {
                   "water": 50,
                   "milk": 0,
                   "coffee": 18,
               },
               "cost": 1.5,
           },
           "latte": {
               "ingredients": {
                   "water": 200,
                   "milk": 150,
                   "coffee": 24,
               },
               "cost": 2.5,
           },
           "cappuccino": {
               "ingredients": {
                   "water": 250,
                   "milk": 100,
                   "coffee": 24,
               },
               "cost": 3.0,
           }
       }

       self.resources = {
           "water": 300,
           "milk": 200,
           "coffee": 100,
       }

    def report(self):
        print(f"water : {self.resources['water']}")
        print(f"milk : {self.resources['milk']}")
        print(f"coffee : {self.resources['coffee']}")

    def make_payment(self, recipe):
        cost = self.MENU[recipe]["cost"]
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        pennies = int(input("How many pennies? "))
        payment = 0.25*quarters + 0.01*pennies + 0.1*dimes

        if payment < cost:
            print("Not enough money. Money refunded")
            return False
        else:
            print(f"Here is your change ${round(payment - cost, 2)}")
            return True



    def make_coffee(self, recipe):
        if self.MENU[recipe]["ingredients"]["water"] > self.resources['water'] or self.MENU[recipe]["ingredients"]["milk"] > self.resources['milk'] or self.MENU[recipe]["ingredients"]["coffee"] > self.resources['coffee']:
            print("not enough resources")
            return
        if self.make_payment(recipe):
            self.resources['water'] -= self.MENU[recipe]["ingredients"]["water"]
            self.resources['milk'] -= self.MENU[recipe]["ingredients"]["milk"]
            self.resources['coffee'] -= self.MENU[recipe]["ingredients"]["coffee"]
            print("Here is your coffee. Enjoy☕️")

    def work(self):
        while True:
            recipe = input("What would u like? (espresso, latte, cappuccino)")
            if recipe == "report":
                self.report()
            elif recipe == "off":
                break
            else:
                self.make_coffee(recipe)

cm = CoffeeMachine()
cm.work()




