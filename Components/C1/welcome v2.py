import random
from random import randint

# List of random names
names = ["Nicole", "Denzelle", "Andrea", "Kris", "Ryanne", "Phuong", "Bomee", "Rian", "Kaitlin", "Unica"]

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

def main():
     
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: None
    Returns: None
    '''
     
    welcome()


main()