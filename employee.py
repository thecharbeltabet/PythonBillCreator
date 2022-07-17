import os
import sys
import re

menu = open("menu.txt", "r")

writeToMenu = open("menu.txt", "a")

trimmedList = [line.rstrip() for line in menu] #remove \n
menuList = []

for item in trimmedList:
    menuList.extend(item.split()) #seperate white spaces:


class Employee:
    def __init__(self, name = "Mark"):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + ", I am an Employee at ArChar's Bakery!"

    #Check if item is in the menu:
    def checkItem(self, item):
        for word in menuList:
            if word == item:
                return True
        return False

    def choice(self):
        name = input("\nPlease enter your name: ").title()

        while name != -1:
            if name.isnumeric():
                print("Your name cannot be a number, please enter your real name!")
                name = input("Please enter your name: ")
                continue
            else:
                print("\nWelcome " + name + " you have successfully logged into the system.")
                print("You now have the freedom to add or remove items from the menu!")

            choice = input("\nWould you like to add or remove items form the menu? (a/r): ")
            while True:
                if choice != 'a' and choice != 'r':
                    print("Please choose either a or r.")
                    choice = input("Would you like to add or removed form the menu? (a/r): ")
                    continue
                if choice == 'a':
                    self.addItem()
                    break
                elif choice == 'r':
                    self.removeItem()
                    break
            sys.exit()

    #Add item to the menu with its price:
    def addItem(self):
        self = Employee() #create an instance for employee to use the .Item() function
        item = input("Item to be added: ").title()

        while item.lower() != "done":
            #fix the number string format to remove every entry if the a number was detected
            if item.isnumeric(): #check if the value of item is a number
                print("An item cannot be a number, please try again!")
                item = input("\nItem to be added (type done when you're done): ").title()
                continue
            
            #exception handling
            if re.search(r'[1, 2, 3, 4, 5, 6, 7, 8, 9, \s]', item): #check if the value of item is a number
                print("An item cannot have a number nor spaces in it, please try again!")
                item = input("\nItem to be added (type done when you're done): ").title()
                continue

            else:
                if self.checkItem(item):
                    print(item + " already exists in the menu!")
                    item = input("\nItem to be added (type done when you're done): ").title()
                    continue
                else:
                    menuList.append(item)
                    writeToMenu.write(item)

                    price = input("Please add the price for " + item + " in LBP: ")
                    #check if the value of price is a string
                    while price != '0':
                        if price.isnumeric():
                            menuList.append(price)
                            writeToMenu.write(" " + price + "\n")
                            break
                        else:
                            print("An item's price cannot be of type string, please try again!")
                            price = input("Please add the price for " + item + " in LBP: ")
                            continue

                    print(item + " was added successfully!")
                    item = input("\nItem to be added (type done when you're done): ").title()
        print("\n")
        print(menuList)
        # os.startfile("menu.txt")
        self.seeBill()

    def removeItem(self):
        if len(menuList) != 0:
            print(menuList)
            item = input("Item to be removed: ").title()

            while item.lower() != "done":
                if item.isnumeric() == True:
                    print("Cannot use numbers here, please try again!")
                    item = input("\nItem to be removed (type done when you're done): ").title()
                    continue

                if self.checkItem(item):
                    index = menuList.index(item) #know where the index is
                    del menuList[index] #remove item
                    del menuList[index] #remove item's price
                    print(item + " was succesfully removed from the menu!")
                    print("\n")
                    print(menuList)
                    
                    #emptying the file and adding the items
                    writeNewMenu = open("menu.txt", "w")
                    for i in range(0, len(menuList), 2):
                        if i == len(menuList):
                            writeNewMenu.write(menuList[i] + " " + menuList[len(menuList) - 1] + "\n") #to fix error: index out of range
                            menuList.clear()
                        else:
                            writeNewMenu.write(menuList[i] + " " + menuList[i + 1] + "\n")
                    if len(menuList) != 0:
                        item = input("\nItem to be removed (type done when you're done): ").title()
                        continue
                    else:
                       self.checkLength()
                elif self.checkItem(item) == False:
                    print("This item was not found on the menu!")
                    item = input("\nItem to be removed (type done when you're done): ").title()
                    continue
                print("menu.txt")
        else:
            self.checkLength()
        self.seeBill()

    def checkLength(self):
        print("The menu has no more items to remove from!")
        choice = input("Would you like to add items or see customers bill? (a/s): ")
        while choice != "done":
            if choice != 'a' and choice != 's':
                print("You must choose between a (add) or e (exit)!")
                choice = input("Would you like to add items or see customers bill? (a/s): ")
                continue
            if choice == 'a':
                self.addItem()
                break
            elif choice == 's':
                self.seeBill()
                break

    def searchName(self, name):
        customers = open("customers.txt", "r")
        customersList = [name.rstrip() for name in customers]
        #check for customer's name in txt file:
        for names in customersList:
            if names == name:
                return True
        return False

    def seeBill(self):

        choice = input("Would you like to see what a specific customer has previously ordered? (y/n): ").lower()

        while True:
            if choice != 'y' and choice != 'n':
                print("Your choice must be either y (yes) or n (no).")
                choice = input("Would you like to see what a specific customer has previously ordered? (y/n): ").lower()
                continue
            break

        if choice == 'y':
            customer = input("Please enter customer's name: ").title()

            while customer != "Done":
                if customer.isnumeric():
                    print("A customer's name cannot be a number")
                    customer = input("Please enter customer's name: ").title()
                    continue

                if self.searchName(customer):
                    os.startfile(customer.title() + "'sbill.txt")
                    break
                else:
                    print("Bill not found!")
                    customer = input("Please enter customer's name: ").title()
                    continue
        elif choice == 'n':
            os.startfile("menu.txt")

menu.close()