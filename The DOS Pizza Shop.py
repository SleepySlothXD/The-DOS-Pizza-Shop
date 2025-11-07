print("Hello there welcome to the DOS Pizza imporium! Can i get your name for the order?\n")

name = input()
menu = str("Cheese, Sausage, Pepperroni")
print("Nice to meet you " + name + " Here is a menu just let me know what you would like when your ready\n" + menu )


PizzaType = input()

if PizzaType == "cheese" or "sausage" or "pepperroni":
    PizzaSize = input("Okay what size do you want? We have Small, Medium, or Large\n")
else: PizzaType = input("sorry but we don't have that we only have" + menu )
    
if PizzaSize == "small" or "medium" or "large":
    print("Ok")
else: PizzaSize = input("Sorry we don't have that we only have Small, Medium, or Large\n")

if PizzaType == "cheese":
    pricetype = 5
elif PizzaType == "sausage":
    pricetype = 10
elif PizzaType == "pepperroni":
    pricetype = 12

if PizzaSize == "small":
    price = pricetype + 5
elif PizzaSize == "medium":
    price = pricetype + 10
elif PizzaSize == "large":
    price = pricetype + 12 

payment = input("Okay for the " + PizzaSize + " " + PizzaType + " pizza, Your total is: $" + str(price) + "\nJust say Pay to confirm your order\n")

if payment == "pay":
    print("ok your order will bet out in a moment")
    print("2 minutes later\n" + PizzaSize + " " + PizzaType + " pizza for " + name + "!!!")