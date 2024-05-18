#!/usr/bin/env python3

class MilkShake:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def check_budget_if_valid(self, budget):
        if not isinstance(budget, (int, float)):
            print("Please enter a valid amount")
            exit()
        
        if budget < 0:
            print("Sorry, you don't have money")
            exit()

    def get_change(self, budget):
        return budget - self.price

    def sell(self, budget):
        self.check_budget_if_valid(budget)
        if budget > self.price:
            print(f"You can buy the {self.name} milkshake.")
            if budget == self.price:
                print("Transaction completed.")
            else:
                print(f"Here is your chanage {self.get_change(budget)}")
            exit("Thank you for purchasing")
