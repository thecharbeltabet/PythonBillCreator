import os
from random import randint
from employee import *
import datetime
import time
import os

year = datetime.date.today().year

# randomNumber = random.sample(range(1000, 9999), 100)
randomNumber = randint(1000, 9999)

timeNow = datetime.datetime.now().strftime('%I:%M:%S')

menu = open("menu.txt", "r")

customers = open("customers.txt", "r")

trimmedList = [line.rstrip() for line in menu] #remove \n

itemsList = []
priceList = []

sortedMenu = []

customersList = [name.rstrip() for name in customers]

#seperate white spaces:
for item in sorted(trimmedList):
    sortedMenu.extend(item.split())

#seperate item from price:
for i in range(0, len(sortedMenu)):
    if i%2 == 0:
        itemsList.append(sortedMenu[i])
    else:
        priceList.append(sortedMenu[i])

class Customer:
    def __init__(self, name = ""):
        self.name = name
    
    def __str__(self):
        return "Welcome " + self.name + " to ArChar's Bakery!"
    
    def checkItem(self, item):
        for word in itemsList:
            if word == item:
                return True
        return False
    
    def searchName(self, name):
        customers = open("customers.txt", "a")
        #check for customer's name in txt file:
        for names in customersList:
            if names == name:
                # print("Customer's name exists: " + name)
                return True
        # print("Customer's name was not found")
        customers.write(name + "\n") 
        return False

    #print number below menuSorted to visualize better but has an issue when i have a lot of items on the menu it doesn't fit well
    # def printNumbers(self, list):
    #     for i in range(1, int(len(list) / 2) + 1):
    #         print("        " + str(i) + "      ", end="")
    #     print("\n")

    def orderFromMenu(self):
        totalItems = 0
        totalPrice = 0
        tipPrice = 0
        tipTotal = 0

        numPeople = []
        addedItems = []
        totalForCurrency = []

        print("\nHello and welcome to ArChar's Bakery!\n")

        self.name = str(input(("Please provide us with your name: ")))
        nameTitle = self.name.title()

        show = input("\nWould you like to see the items' price in lbp or usd?: ").lower()

        while True:
            if show != "lbp" and show != "usd":
                print("Please choose between lbp or usd.")
                show = input("\nWould you like to see the items' price in lbp or usd?: ").lower()
                continue
            else:
                break

        if show == "usd": #change the list items price from lbp to usd
            for i in range(0, len(sortedMenu)):
                if i%2 != 0: #to get the prices
                    sortedMenu[i] = float("%.2f" % ((float(sortedMenu[i]) / 1500)))

        time.sleep(1)
        print("\nThis is our menu for today " + nameTitle + " listed as [item price]:\n")
        print("Menu:")

        if show == "lbp":
            for i in range(0, len(itemsList)):
                print(str(i + 1) + ": " + str(itemsList[i]) + "  " + str(priceList[i]) + "LBP")
        elif show == "usd":
            for i in range(0, len(itemsList)):
                priceList[i] = float("%.2f" % ((float(priceList[i]) / 1500))) #change the list items price from lbp to usd
                print(str(i + 1) + ": " + str(itemsList[i]) + "  " + str(priceList[i]) + "USD")
        
        #revert back to normal
        if show == "usd":
            for i in range(0, len(itemsList)):
                    priceList[i] = float("%.2f" % ((float(priceList[i]) * 1500))) #change the list items price from lbp to usd


        type = input("\nWould you like to order the menu's items with their numbers or by their title? (n/t): ")

        while True:
            if type != 'n' and type != 't':
                print("\nPlease this question can be answered by either n (numbers) or t (title), thank you!\n")
                type = input("\nWould you like to order the menu's items with their numbers or by their title? (n/t): ")
                continue
            break

        print("\nWhat would you like to order " + nameTitle + "? Please select from the menu above.")
        #added a way to enter items using 1 2 3 4... from 1 to len(itemsList)

        if type == 'n':
            order = input("\nItem: ")
            while True:
                if order.lower() == "done":
                    if totalItems == 0:
                        print("\nYour order must contain at least 1 item from the menu!")
                        print("Menu:", sortedMenu)
                        # self.printNumbers(sortedMenu)
                        order = order = input("\nItem: ")
                        continue
                    else:
                        break
                
                if order.isnumeric() == False:
                    print("You chose to choose items by their numbers!")
                    order = input("\nItem: ")
                    continue
                
                if int(order) >= 1 and int(order) <= len(itemsList):
                    totalItems += 1
                    totalPrice += int(priceList[int(order) - 1])
                    #add items: 
                    addedItems.append(str(itemsList[int(order) - 1]) + " " + str(priceList[int(order) - 1]))
                    print("\n" + str(itemsList[int(order) - 1]) + " was added to your order!\n")
                    print("Menu:", sortedMenu)
                    # self.printNumbers(sortedMenu)
                    order = str(input("Item (type done when you're done ordering): ")).title()
                    continue
                
                else:
                    print("This number doesn't match any item from the menu!")
                    order = str(input("Item (type done when you're done ordering): ")).title()
                    continue

        elif type == 't':
            order = input("\nItem: ").title()
            while True:
                if order.lower() == "done":
                    if totalItems == 0:
                        print("\nYour order must contain at least 1 item from the menu!")
                        print("Menu:", sortedMenu)
                        # self.printNumbers(sortedMenu)
                        order = input("Item (type done when you're done ordering): ").title()
                        continue
                    else:
                        break

                if self.checkItem(order):
                    index = itemsList.index(order)
                    totalItems += 1
                    totalPrice += int(priceList[index])
                    #add items: 
                    addedItems.append(order + " " + str(priceList[index]))
                    print("\n" + order + " was added to your order!\n")
                    print("Menu:", sortedMenu)
                    # self.printNumbers(sortedMenu)
                    order = input("Item (type done when you're done ordering): ").title()
                    continue
                
                print("\nUnfortunately, the item you selected is not on the menu!")
                print("Please select another item.\n")
                print("Menu:", sortedMenu)
                # self.printNumbers(sortedMenu)
                order = input("Item (type done when you're done ordering): ").title()

        print("\nThank you for your order.")

        splitBill = input("\nWould you like to split the bill? (y/n): ").lower()

        while True:
            if splitBill != 'y' and splitBill != 'n':
                print("\nPlease this question can be answered by either y or n, thank you!\n")
                splitBill = input("Would you like to split the bill? (y/n): ")
                continue
            break
        
        currency = input("Would you like to pay in LBP or USD? (lbp/usd): ").lower()
        while True: #implement a try catch for the lbp and usd 
            if currency != "lbp" and currency != "usd":
                print("\nPlease this question can be answered by either lbp or usd, thank you!\n")
                currency = input("Would you like to pay in LBP or USD? (lbp/usd): ").lower()
                continue

            if currency == "lbp":
                if splitBill == 'y':
                    people = input("\nHow many people are you?: ")
                    while True:
                        if people.isnumeric() == False:
                            print("Number of people cannot be a string!")
                            people = input("\nHow many people are you?: ")
                            continue
                        if int(people) <= 0:
                            print("Number of people cannot be <= 0")
                            people = input("\nHow many people are you?: ")
                            continue
                        else:
                            numPeople.append(int(people))#add it to the list to use it after
                            print("\nYou order has: " + str(totalItems) + " items.")
                            print("\nYour total will be: " + str("{:,}".format(totalPrice)) + "LBP")
                            print("Each person has to pay: " + str("{:,}".format((totalPrice) / int(people))) + "LBP")
                            totalForCurrency.append(str("{:,}".format(totalPrice) + "LBP"))
                            totalForCurrency.append(str("{:,}".format((totalPrice) / int(people))) + "LBP")
                            break
                    break
                elif splitBill == 'n':
                    print("\nYou order has: " + str(totalItems) + " items.")
                    print("\nYour total will be: " + str("{:,}".format(totalPrice)) + "LBP")
                    totalForCurrency.append(str("{:,}".format(totalPrice) + "LBP" ))
                    break
            elif currency == "usd":
                if splitBill == 'y':
                    people = input("\nHow many people are you?: ")
                    while True:
                        if people.isnumeric() == False:
                            print("Number of people cannot be a string!")
                            people = input("\nHow many people are you?: ")
                            continue
                        if int(people) <= 0:
                            print("Number of people cannot be <= 0")
                            people = input("\nHow many people are you?: ")
                            continue
                        else:
                            numPeople.append(int(people))#add it to the list to use it after
                            print("\nYou order has: " + str(totalItems) + " items.")
                            print("\nYour total will be: " + str("%.2f" % (totalPrice / 1500)) + " USD")
                            print("Each person has to pay: " + str(float("%.2f" % ((totalPrice / int(people)) / 1500))) + " USD") #fake USD rate ;)
                            totalForCurrency.append(str(float("%.2f" % ((totalPrice / 1500)))) + " USD")
                            totalForCurrency.append(str(float("%.2f" % ((totalPrice / int(people)) / 1500))) + " USD") #adding the each person amount
                            break
                    break
                elif splitBill == 'n':
                    print("\nYou order has: " + str(totalItems) + " items.")
                    print("\nYour total will be: " + str(float("%.2f" % ((totalPrice / 1500)))) + " USD")
                    totalForCurrency.append(str(float("%.2f" % ((totalPrice /1500)))) + " USD")
                    break
        
        tip = input("\nWould you like to leave a tip? (y/n): ").lower()
        while True:
            if tip != 'y' and tip != 'n':
                print("Please this question can be answered by either y or n, thank you!")
                tip = input("\nWould you like to leave a tip? (y/n): ").lower()
                continue

            if tip == 'y':
                tipPercent = input("Please choose a % tip: ")

                while True:
                    if tipPercent.isnumeric() == False:
                        print("Please enter a numeric value for the tip!")
                        tipPercent = input("Please choose a % tip: ")
                        continue

                    if float(tipPercent) < 1 or float(tipPercent) > 100:
                        print("The tip percentage cannot be lower than 1% nor greater than 100%!")
                        tipPercent = input("Please choose a % tip: ")
                        continue
                    
                    if splitBill == 'y':
                        if currency == "lbp":
                            tipPrice = int((totalPrice * int(tipPercent) / 100)) # ex: 150000 * 0.1 (10%)
                            tipTotal = int(tipPrice + totalPrice)
                            print("\nThank you for keeping " + str("{:,}".format(tipPrice)) + "LBP as a tip!")
                            print("\nTotal with tip: " + str("{:,}".format(tipTotal)) + "LBP")
                            print("Each person has to pay: " + str("{:,}".format((tipTotal) / int(numPeople[0]))) + "LBP")
                            totalForCurrency.append(str("{:,}".format(tipTotal) + "LBP" ))
                            totalForCurrency.append(str("{:,}".format((tipTotal) / int(numPeople[0]))) + "LBP")
                            print("\nGenerating your order's receipt...")
                            time.sleep(1)
                            break
                        elif currency == "usd":
                            tipPrice = float(((totalPrice / 1500) * float(tipPercent) / 100)) # ex: 150000 * 0.1 (10%)
                            tipTotal = float(tipPrice + (totalPrice / 1500))
                            print("\nThank you for keeping " + str("%.2f" % tipPrice) + " USD as a tip!")
                            print("\nTotal with tip: " + str("%.2f" % tipTotal) + " USD")
                            print("Each person has to pay: " + str(float("%.2f" % ((tipTotal / int(numPeople[0]))))) + " USD")
                            totalForCurrency.append(str("%.2f" % tipTotal)+ " USD") #adding the total
                            totalForCurrency.append(str(float("%.2f" % ((tipTotal / int(numPeople[0]))))) + " USD") #adding how much each person has to pay
                            print("\nGenerating your order's receipt...")
                            time.sleep(1)
                            break
                    
                    elif splitBill == 'n':
                        if currency == "lbp":
                            tipPrice = int((totalPrice * int(tipPercent) / 100)) # ex: 150000 * 0.1 (10%)
                            tipTotal = int(tipPrice + totalPrice)
                            print("\nThank you for keeping " + str("{:,}".format(tipPrice)) + "LBP as a tip!")
                            print("\nTotal with tip: " + str("{:,}".format(tipTotal)) + "LBP")
                            totalForCurrency.append(str("{:,}".format(tipTotal) + "LBP" ))
                            print("\nGenerating your order's receipt...")
                            time.sleep(1)
                            break
                        elif currency == "usd":
                            tipPrice = float(((totalPrice / 1500) * float(tipPercent) / 100)) # ex: 150000 * 0.1 (10%)
                            tipTotal = float(tipPrice + (totalPrice / 1500))
                            print("\nThank you for keeping " + str("%.2f" % tipPrice) + " USD as a tip!")
                            print("\nTotal with tip: " + str("%.2f" % tipTotal) + " USD")
                            totalForCurrency.append(str("%.2f" % tipTotal)+ " USD") #adding the total
                            print("\nGenerating your order's receipt...")
                            time.sleep(1)
                            break
                break
            elif tip == 'n':
                print("\nGenerating your order's receipt...")
                time.sleep(1)
                break
        
        newAddedItems =[]

        #seperating item from price to use them later
        for item in addedItems:
            newAddedItems.extend(item.split())
        
        # print(newAddedItems)
        itemsList.clear()
        priceList.clear()

        #adding the chosen items to their place in where each item is in itemsList and each price in priceList
        for i in range(0, len(newAddedItems)):
            if i%2 == 0:
                itemsList.append(newAddedItems[i])
            else:
                priceList.append(newAddedItems[i])

        if show == "usd" or currency == "usd": #change prices to usd
            for i in range(0, len(priceList)):
                priceList[i] = float("%.2f" % ((float(priceList[i]) / 1500)))
        elif show == "lbp":
            for i in range(0, len(priceList)):
                priceList[i] = str("{:,}".format(int(priceList[i])))

        #Write to file:
        if self.searchName(nameTitle) == True: #same customer
            billFile = open(nameTitle + "'sbill.txt", "a")
            self.writeFile(billFile, show, tip, currency, totalItems, addedItems, itemsList, priceList, totalForCurrency, numPeople)

            os.remove("tempbill.txt")

            tempFile = open("tempbill.txt", "x")
            self.writeFile(tempFile, show, tip, currency, totalItems, addedItems, itemsList, priceList, totalForCurrency, numPeople)
            os.startfile("tempbill.txt")
        
        else: #new customer
            billFile = open(nameTitle + "'sbill.txt", "x")
            self.writeFile(billFile, show, tip, currency, totalItems, addedItems, itemsList, priceList, totalForCurrency, numPeople)
            os.startfile(nameTitle + "'sbill.txt")
        
    def writeFile(self, fileName, show, tip, Currency, totalitems, addeditems, itemslist, pricelist, totalforcurrency, numOfPeople ):
        randomNumb = randomNumber #in order not to generate a new rand num
        #generating order's receipt:
        fileName.write("\n\n\n\nOrder ID: " + str(year) + str(randomNumb) + " at " + str(timeNow) + ": \n\n" )
        fileName.write("Your order has " + str(totalitems) + " items:\n")
        if show == "lbp" and Currency == "lbp":
            # fileName.write(str('\n'.join(str(p) for p in addeditems) + "LBP"))
            for i in range(0, len(addeditems)):
                fileName.write("" + str(itemslist[i]) + "   " + str(pricelist[i]) + "LBP\n")
        elif show == "lbp" and Currency == "usd":
            # billFile.write(str('\n'.join(str(p) for p in addeditems) + "LBP"))
            for i in range(0, len(addeditems)):
                fileName.write("" +str(itemslist[i]) + "   " + str(pricelist[i]) + "USD\n")
        elif show == "usd" and Currency == "usd":
            for i in range(0, len(addeditems)):
                fileName.write("" +str(itemslist[i]) + "   " + str(pricelist[i]) + "USD\n")
        elif show == "usd" and Currency == "lbp":
            for i in range(0, len(addeditems)):
                fileName.write("" +str(itemslist[i]) + "   " + str(pricelist[i] * 1500) + "LBP\n")

        if len(numOfPeople) == 0: #just to add the each person has to pay phrase
            if tip == 'n':
                fileName.write("\n\nYour total is: " + str(totalforcurrency[0]))
            elif tip == 'y':
                fileName.write("\n\nYour total is: " + str(totalforcurrency[0]))
                fileName.write("\n\nYour total with the tip is: " + str(totalforcurrency[1]))
        else:
            if tip == 'n':
                fileName.write("\n\nYour total is: " + str(totalforcurrency[0]))
                fileName.write("\n\tEach Person has to pay: " + str(totalforcurrency[1]))
            elif tip == 'y':
                fileName.write("\n\nYour total is: " + str(totalforcurrency[0]))
                fileName.write("\n\nYour total with the tip is: " + str(totalforcurrency[2]))
                fileName.write("\nEach Person has to pay: " + str(totalforcurrency[3]))
    
menu.close()
