from employee import *
from customer import *
import os

choice = input("Are you an Employee or a Customer at ArChar's Bakery?(e/c): ").lower()

while choice != "none":
    if(choice != "e" and choice != "c"):
        print("Please choose between e (employee) and c (customer)!")
        choice = input("Are you an Employee or a Customer at ArChar's Bakery?(e/c) ").lower()
        continue
    
    if choice == 'e':
        e1 = Employee()
        e1.choice()
    
    elif choice == 'c':
        c1 = Customer()
        c1.orderFromMenu()
        break