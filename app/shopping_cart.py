# shopping_cart.py
from functions import to_USD, human_friendly_timestamp, find_product
import datetime

#######################
#Initialize Constants #
#######################

DC_TAX_RATE = .06

#######################
#Initialize Variables #
#######################

dashes =  "--------------------------------------------------------------------------------"
doneBool = True #our Boolean switch
running_total = 0.0 #running total of price
idSelection = ""
cartList = []
t = datetime.datetime.now()
stdTime = human_friendly_timestamp(t)

############################
#Code to handle user input #
############################

while doneBool == True: #loop for grocery cart items
    try:
        idSelection = input("Please input a product identifer, or 'DONE', if there are no more items: ")
        
        id
        if idSelection == "DONE":   #if DONE
             doneBool = False
       
        elif int(idSelection) > 0 and int(idSelection) <21:

            matching_products  = find_product(idSelection)
            
            if len(matching_products) == 1:   #If only one item under this ID
                product = matching_products[0]
                cartList.append(product) #Adds item to cart
                price = product["price"]  #lookup price
                running_total += price
            else:
                for p in matching_products: #If multiple items match
                    cartList.append(p) #Adds item to cart
                    price = p["price"] # lookup price 
                    running_total += price         
        else: #Checks for invalid input
            print("\nPlease enter a valid input between 1 - 20.\n")

    except ValueError: #Checks for invalid data type that isn't "DONE"
            print("\nERROR: value error, Please enter 'DONE' if done\n")


###########################
#### Now print receipt ####
###########################

#Name
print(dashes)
print("\t\tMILLS and Co. Groceries, Goods, & More")
print(dashes)

#Store info and time
print("Web: https://github.com/colin-mills/Shopping-cart-project")
print("Phone: 1.202.687.0100")
print("Checkout Time: " + stdTime)
print(dashes)

#Prints items from cartList
print("Shopping Cart Items: ")

if len(cartList) == 0:
    print("No items purchased today")
else:
    print("")
    for items in cartList:
        itemPrice_USD = to_USD(items["price"])
        name = items["name"]
        print("+ " + name.ljust(70) + itemPrice_USD.rjust(8))

#Calculations for pricing
taxPortion = running_total * DC_TAX_RATE #sales tax
totalFinal = running_total + taxPortion

#Format totals
#price_USD = " (${0:.2f})".format(p["price"])
running_total_USD = to_USD(running_total)
taxPortion_USD = to_USD(taxPortion)
totalFinal_USD = to_USD(totalFinal)

#ALL pricing info
print(dashes)
print("Subtotal: ".ljust(70) + running_total_USD.rjust(10))
print("Plus Washington D.C. Sales Tax (6%): ".ljust(70) + taxPortion_USD.rjust(10))
print("Total: ".ljust(70) + totalFinal_USD.rjust(10))
print(dashes)

#outro
print("Thank you, please come again!\n\n")