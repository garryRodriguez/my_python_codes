#!/usr/bin/env python3

class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)



    def check_budget(self, budget):
        # check if the budget is valid
        if not isinstance(budget, (int, float)):
            print('Enter int or float')
            exit()
        if budget < 0:
            print('Sorry you don\'t have money.')
            exit()



    def get_change(self, budget):
        return budget - self.price



    def sell(self, budget):
        self.check_budget(budget)
        if budget >= self.price:
            print(f"You can buy the {self.name} coffee")
            if budget == self.price:
                print('It\'s complete')
            else:
                print(f"Here is your change {self.get_change(budget)}$")
            exit('Thanks for your transaction')

small = Coffee('small', 2)
regular = Coffee('regular', 5)
big = Coffee('Big', 6)

try:
    user_budget = float(input('What is your budget? '))
except ValueError:
    exit('Please enter a number')

for coffee in [big, small, regular]:
    coffee.sell(user_budget)




