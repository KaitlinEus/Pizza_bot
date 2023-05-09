# Pizza bot program

import random
from random import randint

# List of random names
names = ["Nicole", "Denzelle", "Andrea", "Kris", "Ryanne", "Phuong", "Bomee", "Rian", "Kaitlin", "Unica"]

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
    print("*** Welcome to Dream Pizza***")
    print("*** My name is",name, "***")
    print("*** I will be here to help you order your delicious Dream Pizza ***")

# Menu for pickup or delivered




# Pick up information - name and phone




# Delivery information - name, address and phone




# Choose total number of Pizzas - max 5




# Pizza menu




# Pizza ordering - from menu - print each pizza order with cost




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


main()