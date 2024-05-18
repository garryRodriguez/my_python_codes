#!/usr/bin/env python3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return f" My name is {self.name} and I am ({self.age}) years old."
    
    def my_func(self):
        print("Hello my name is " + self.name)


p1 = Person("garry", 22)
p1.age = 32
print(p1.age)