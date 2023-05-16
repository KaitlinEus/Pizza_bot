# list of pizza names and prices
pizza_names = ['Margherita', 'Pepperoni', 'Hawaiian', 'Cheese', 'Italian', 'Veggie', 'Vegan', 
               'Chicken Deluxe', 'Mega Meat Lovers', 'Seafood Deluxe', 'Apricot Chicken Deluxe', 'BBQ Chicken Deluxe']
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

#list to store ordered pizzas
order_list = []

#list to store pizzas prices
order_cost = []

#list to store order cost

def menu():
        num_pizzas = 12

        for count in range (num_pizzas):
            print("{} {} ${:.2f}".format(count+1, pizza_names[count], pizza_prices[count]))

menu()

# ask for total number of pizzas for order

num_pizzas = 0

num_pizzas = int(input("How many pizzas do you want to order? "))

print(num_pizzas)


# choose from menu
print("Please choose your pizzas by entering the number from the menu")
for item in range(num_pizzas):
      while num_pizzas > 0:
            pizza_ordered = int(input())
            order_list.append(pizza_names[pizza_ordered])
            order_cost.append(pizza_prices[pizza_ordered])
            num_pizzas = num_pizzas -1

print(order_list)
print(order_cost)


#Countdown until all pizzas are ordered


# print order