# Your code below:
# Create a list of toppings 
toppings = [
  "pepperoni",
  "pineapple",
  "cheese",
  "sausage",
  "olives",
  "anchovies",
  "mushrooms"
]
# Create price variable to track cost of pizza slice
prices = [
  2,
  6, 
  1, 
  3, 
  2,
  7,
  2
]
# Count number of "2" prices 
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Find len(toppings) list code to new variable
num_pizzas = len(toppings)

# Print the string (f"We sell {num_pizzas} diffent kinds of pizza") and code to new variable
print(f"We sell {num_pizzas} different kinds of pizza!")

# Create a two-dimensional list merging toppings and prices
pizza_and_prices = [
  [2, "pepperoni"], 
  [6, "pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "olives"],
  [7, "anchovies"],
  [2, "mushrooms"]
  ]
print(pizza_and_prices)

# Sort list so pizzas ascend in order of price
pizza_and_prices.sort()
print(pizza_and_prices)

# Store first element in new variable cheapest_pizza
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

# Get last item from pizza_and_prices list
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

# Remove "anchovies" from the list
pizza_and_prices = pizza_and_prices[:-1]
print(pizza_and_prices)

# Add new item to the list 
for i, pizza in enumerate(pizza_and_prices):
  if pizza[0] > 2.5:
    pizza_and_prices.insert(i, [2.5, "peppers"])
    break
print(pizza_and_prices)

# Slice pizza_and_prices and store 3 lowest cost pizzas in new list, three_cheapest
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)