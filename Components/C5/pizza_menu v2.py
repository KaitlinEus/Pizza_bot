# list of pizza names and prices
pizza_names = ['Margherita', 'Pepperoni', 'Hawaiian', 'Cheese', 'Italian', 'Veggie', 'Vegan', 
               'Chicken Deluxe', 'Mega Meat Lovers', 'Seafood Deluxe', 'Apricot Chicken Deluxe', 'BBQ Chicken Deluxe']
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]



#print("How many pizzas would you like to order? ")
#num_pizza = int(input())

def menu():
        num_pizzas = 12

        for count in range (num_pizzas):
            print("{} {} ${:.2f}".format(count+1, pizza_names[count], pizza_prices[count]))

menu()

