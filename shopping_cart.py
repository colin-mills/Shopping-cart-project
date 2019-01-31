# shopping_cart.py

import datetime


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# TODO: write some Python code here to produce the desired functionality...

#######################
#Initialize Variables #
#######################

dashes =  "---------------------------------------------------------"
doneBool = True #our Boolean switch
running_total = 0.0 #running total of price
idSelection = ""
cartList = []
t= datetime.datetime.now()
stdTime = t.strftime("%Y-%m-%d  %H:%M:%S")

############################
#Code to handle user input #
############################

while doneBool == True: #loop for grocery cart items
    try:
        idSelection = input("Please input a product identifer, or 'DONE', if there are no more items: ")
        print("Your selection was: " + idSelection)
        
        if idSelection == "DONE":   #if DONE
             doneBool = False
       
        elif int(idSelection) > 0 and int(idSelection) <21:
            

            #cartList.append(idSelection) #Adds item to cart

            matching_products  = [p for p in products if p["id"] == int(idSelection)] #Finds all matching items
            
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
print("MILLS and Co.")
print(dashes)

#Store info and time
print("Web: https://github.com/colin-mills/Shopping-cart-project")
print("Phone: 1.202.687.0100")
print("Checkout Time: " + stdTime)
print(dashes)

#Prints items from cartList
print("Shopping Cart Items: ")

for items in cartList:
   print("+ " + str(items["name"]) + str(items["price"]))

#Calculations for pricing
taxPortion = running_total * .06 #sales tax
totalFinal = running_total + taxPortion

#ALL pricing info
print(dashes)
print("Subtotal: " + str(running_total))
print("Plus Washington D.C. Sales Tax (6%): " + str(taxPortion))
print("Total: " + str(totalFinal))
print(dashes)

#Closing
print("Thank you come again.")