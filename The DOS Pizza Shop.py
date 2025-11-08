print("Hello there welcome to the DOS Pizza imporium! Can i get your name for the order?\n")


name = input()
menu = str("Cheese Pizza, Starting at $5.75,\nSausage Pizza, Starting at $7.75,\nPepperroni Pizza, Starting at $10.75")
print("Nice to meet you " + name + " Here is a menu just let me know what you would like when your ready\n\n" + menu )

#Ordering
PizzaType = input()

if PizzaType == "cheese" or "sausage" or "pepperroni":
    PizzaSize = input("Okay what size do you want? We have Small, Medium, or Large\n")
else: PizzaType = input("sorry but we don't have that we only have" + menu )
    
if PizzaSize == "small" or "medium" or "large":
    print("Ok")
else: PizzaSize = input("Sorry we don't have that we only have Small, Medium, or Large\n")

#Payment
if PizzaType == "cheese":
    pricetype = 5
elif PizzaType == "sausage":
    pricetype = 7
elif PizzaType == "pepperroni":
    pricetype = 10

if PizzaSize == "small":
    price = pricetype + 0.75
elif PizzaSize == "medium":
    price = pricetype + 3.25
elif PizzaSize == "large":
    price = pricetype + 5.25 

payment = input("Okay for the " + PizzaSize + " " + PizzaType + " pizza, Your total is: $" + str(price) + "\n\nJust say Pay to confirm your order. If not order will be cancelled")

if payment == "pay":
    print("ok your order will bet out in a moment\n\n")
    print("2 minutes later\n\n" + PizzaSize + " " + PizzaType + " pizza for " + name + "!!!")