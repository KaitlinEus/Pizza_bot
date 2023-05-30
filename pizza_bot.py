# Pizza bot program

#12/5/2023
# Bugs - Name input allows numbers 
#      - Phone number input allowes letters

import random
from random import randint

# List of random names
names = ["Nicole", "Denzelle", "Andrea", "Kris", "Ryanne", "Phuong", "Bomee", "Rian", "Kaitlin", "Rafael"]


# list of pizza names and prices
pizza_names = ['Margherita', 'Pepperoni', 'Hawaiian', 'Cheese', 'Italian', 'Veggie', 'Vegan', 
               'Chicken Deluxe', 'Mega Meat Lovers', 'Seafood Deluxe', 'Apricot Chicken Deluxe', 'BBQ Chicken Deluxe']
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

#list to store odered pizzas
order_list =[]
#list to store pizzas prices
order_cost =[]

# customer detailes dictionary
customer_details = {}

# Validates inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid: 
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("Sorry this cannot be blank")


# Welcome message with random name

def welcome():

    '''
    Purpose: To run all functions
    Parameters: None
    Returns: None
    '''

    num = randint(0,9)
    name = (names[num])

    # Welcome message
    print("*** Welcome to Dream Pizza ***")
    print("*** My name is",name, "***")
    print("*** I will be here to help you order your delicious Dream Pizza ***")

# Menu for pickup or delivered

def order_type():

    print("Is your order for pickup or delivery?")

    print("For deliver please enter 1")
    print("For pickup please enter 2")

    while True: 
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:

                if delivery == 1:
                    print("Delivery")
                    delivery_info()
                    break

                elif delivery == 2:
                    print("Pickup")
                    pickup_info()
                    break
                    
            else: 
                print("Number must be 1 or 2")

        except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 2")

# Pick up information - name and phone
def pickup_info():

    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)

    #print(customer_details["name"])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)


    print(customer_details)



# Delivery information - name, address and phone
def delivery_info():

    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)

    print(customer_details["name"])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)

    print(customer_details["phone"])

    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question)

    print(customer_details['house'])

    question = ("Please enter your street name ")
    customer_details['street'] = not_blank(question)

    print(customer_details['street'])

    question = ("Please enter your suburb ")
    customer_details['suburb'] = not_blank(question)

    print(customer_details['suburb'])



# Pizza menu
def menu():
        num_pizzas = 12

        for count in range (num_pizzas):
            print("{} {} ${:.2f}".format(count+1, pizza_names[count], pizza_prices[count]))






# Choose total number of Pizzas - max 5
# Pizza ordering - from menu - print each pizza order with cost
def order_pizzas():
    #ask for total number of pizzas for order
    num_pizzas = 0

    while True:
        try:
            num_pizzas = int(input("How many pizzas do you want to order? "))
            if num_pizzas >= 1 and num_pizzas <= 5:
                break
            else:
                print("Your order must be between 1 and 5")
        except ValueError:
            print("That is not a valid number")
            print("Please enter a number between 1 and 5")


    #choose pizza from menu

    for item in range(num_pizzas):
        while num_pizzas > 0:
                while True:
                    try:
                        pizza_ordered = int(input("Please choose your pizzas by entering the number from the menu "))
                        if pizza_ordered >= 1 and pizza_ordered <= 12:
                            break
                        else:
                            print("You order must be between 1 and 12")
                    except ValueError:
                        print("That is not a valid number")
                        print("Please enter a number from the menu")
        
                    
                pizza_ordered = pizza_ordered -1
                order_list.append(pizza_names[pizza_ordered])
                order_cost.append(pizza_prices[pizza_ordered])
                num_pizzas = num_pizzas-1
                print("{} ${:.2f}" .format(pizza_names[pizza_ordered],pizza_prices[pizza_ordered]))



#  Print order out - including if order is delivery or pick up and names and price of each pizza - total cost including any delivery charge




# Ability to cancel or proceed with order




# Option fornew order or to exit




# Main Funcion

def main():
     
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: None
    Returns: None
    '''
     
    welcome()
    order_type()
    menu()
    order_pizzas()


main()