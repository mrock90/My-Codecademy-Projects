hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Sum all prices of haircuts
total_price = 0

# Loop through pice list add to total_price
for price in prices:
  total_price += price
print(total_price)

# Create average_price variable
average_haircut_price = total_price / len(prices)
print(f"Average Haircut Price: ${average_haircut_price}")

# Use list comprehension to make a new list "new_prices"
new_prices = [price - 5 for price in prices]
print(new_prices)

# Find total revenue for last week
total_revenue = 0

# Create a for loop 
for index in range(len(hairstyles)):
  # Find Total Revenue
  # Find the Average Daily Revenue
  total_revenue += prices[index] * last_week[index]
  average_daily_revenue = total_revenue / 7
print(f"Total Revenue: ${total_revenue}")
print(f"Average Daily Revenue: ${average_daily_revenue}")

# Create new list cuts_under_30 
cuts_under_30 = [hairstyles[index] for index in range(len(new_prices)) if new_prices[index] < 30]
print(cuts_under_30)