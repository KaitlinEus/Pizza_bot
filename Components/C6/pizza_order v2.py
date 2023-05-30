# list of pizza names and prices
pizza_names = ['Margherita', 'Pepperoni', 'Hawaiian', 'Cheese', 'Italian', 'Veggie', 'Vegan', 
               'Chicken Deluxe', 'Mega Meat Lovers', 'Seafood Deluxe', 'Apricot Chicken Deluxe', 'BBQ Chicken Deluxe']
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

#list to store odered pizzas
order_list =[]
#list to store pizzas prices
order_cost =[]

#list to store order cost


def menu():
        num_pizzas = 12

        for count in range (num_pizzas):
            print("{} {} ${:.2f}".format(count+1, pizza_names[count], pizza_prices[count]))

menu()

########

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
         print("That is not a valid error")
         print("Please enter a number between 1 and 5")


print(num_pizzas)

#choose pizza from menu

print("Please choose your pizzas by entering the number from the menu")

for item in range(num_pizzas):
      while num_pizzas > 0:
            pizza_ordered = int(input())
            order_list.append(pizza_names[pizza_ordered])
            order_cost.append(pizza_prices[pizza_ordered])
            num_pizzas = num_pizzas-1

print(order_list)
print(order_cost)

#countdown until all pizzas are ordered


#print order