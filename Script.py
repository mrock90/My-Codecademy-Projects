lovely_loveseat_description = 'Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'

lovely_loveseat_price = 254.00

stylish_settee_description = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'

stylish_settee_price = 180.50

luxurious_lamp_description = 'Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'

luxurious_lamp_price = 52.15

sales_tax = .088

customer_one_total = 0

customer_one_itemization = ""

# Add the price of the lovely loveseat to the total
customer_one_total += lovely_loveseat_price 

# Add the price of the luxurious lamp to the total
customer_one_total += luxurious_lamp_price

# Add the price of the Stylish Settee to the total
# customer_one_total += stylish_settee_price

# Example of error handling
#try:
  #customer_one_total += lovely_loveseat_price
# except TypeError:
  # print("Invalid price for Loveley Loveseat")

# Add the description of the lovely loveseat to the itemization
customer_one_itemization += lovely_loveseat_description 
# Add the description of the luxurious lamp to the itemization
customer_one_itemization += luxurious_lamp_description
# Add the descripton of the stylish settee to the itemization
# customer_one_itemization += stylish_settee_description

# Calculate the sales tax for the customers total
customer_one_tax = customer_one_total * sales_tax

# Calculate customers total price
#customer_one_total += customer_one_tax
def calculate_total_with_tax(total, tax_rate):
  return total + (total * tax_rate)

customer_one_total = calculate_total_with_tax(customer_one_total, sales_tax)

print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)