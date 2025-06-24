# hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# prices = [30, 25, 40, 20, 20, 35, 50, 35]

# last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# # Sum all prices of haircuts
# total_price = 0

# # Loop through pice list add to total_price
# for price in prices:
#   total_price += price
# print(total_price)

# # Create average_price variable
# average_haircut_price = total_price / len(prices)
# print(f"Average Haircut Price: ${average_haircut_price}")

# # Use list comprehension to make a new list "new_prices"
# new_prices = [price - 5 for price in prices]
# print(new_prices)

# # Find total revenue for last week
# total_revenue = 0

# # Create a for loop 
# for index in range(len(hairstyles)):
#   # Find Total Revenue
#   # Find the Average Daily Revenue
#   total_revenue += prices[index] * last_week[index]
#   average_daily_revenue = total_revenue / 7
# print(f"Total Revenue: ${total_revenue}")
# print(f"Average Daily Revenue: ${average_daily_revenue}")

# # Create new list cuts_under_30 
# cuts_under_30 = [hairstyles[index] for index in range(len(new_prices)) if new_prices[index] < 30]
# print(cuts_under_30)

# Refined Code implmenting functions to make script more concise, readable, and reduce errors



from typing import List, Tuple

# Global Data
# These lists define the core data for hairstyles, their prices, adn last week's sales.
hairstyles = ["boufant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25 , 40, 20 , 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2] # Represents quantity sold for each haristyle

# Functions for Analysis
def calculate_price_summary(haircut_prices: List[int]) -> Tuple[int, float]:
    """
    Calculates the total and average price of a list of haircuts/

    Args:
        haircut_prices(List[int]): A list of prices for the haircuts

    Returns:
        Tuple[int, float]: A tuple containing:
                          - The total sum of all haricut prices (int).
                          - The average haircut price (float).
    
    """
    total_price = sum(haircut_prices) # Python's built-in sum() is highly efficient. Avoids manual loop, making it more concise and readable

    # Check to prevent division by zero if the list of prices is empty
    if not haircut_prices:
        return 0, 0.0 # Return 0 for total and average if no prices
    
    average_price = total_price / len(haircut_prices)
    return total_price, average_price

def apply_discount(original_prices: List[int], discount_amount: int) -> List[int]:
  """
  Applies a fixed discount to each price in a list, creating a new list of discounted prices.
  
  Args:
    original_prices (List[int]): A list of original prices
    discount_amount (int): The amount to subtract from each price.
    
  Returns:
    List[int]:A new list containing the discount prices.
              Prices will not go below zero.
  """

  # Using list comprehension for concise and Pythonic creation of the new list.
  # max(0, ...) ensures prices fon't become negarive after discount.
  return [max(0, price - discount_amount) for price in original_prices]

def calculate_revenue_summary(
    haircut_prices: List[int],
    sales_quantities: List[int],
    num_days_in_period: int
  ) -> Tuple[int, float]:
  """
      Calculates the total revenue and average daily revenue for a period.

      Args:
          haircut_prices (List[int]): A list of prices for each haircut.
          sales_quantities (List[int]): A list of quantities sold for each haircut.
                                      (Assumed to correspond to haircut_prices by index)
          num_days_in_a_period (int): The number of days over which the sales occured.
        
      
      Returns:
          Tuple[int, float]: A tuple containing:
                              - The total revenue for the period (int)
                              - The average daily revenie (float)
  """
  total_revenue = 0

    # Iterate using zip() for clean, parallel iteration over two lines.
    # Thisautomatically handles matching elements by index.
  for price, quantity in zip(haircut_prices, sales_quantities):
      total_revenue += price * quantity
    
    # Check to prevent division by zerp if num_daus_in_a_period is zero,
  if num_days_in_period == 0:
      return total_revenue, 0.0 # Can't calculate daily average if no days

  average_daily_revenue = total_revenue / num_days_in_period
  return total_revenue, average_daily_revenue


def get_cuts_under_price(
    haircut_names: List[str],
    haircut_prices: List[int],
    max_price_threshold: int
) -> List[str]:
      """
      Filters a list of haircuts to find those whose prices are below a specified threshold. 

      Args:
          haircut_names (List[str]): A list of hairstyle names.
          haircut_prices (List[int]): A list of corresponding prices for the hairstyles.
          max_price_threshold (int): The maximum price to include a haircut.

      Returns:
          List[str]: A new list contianing the names of hairstyles priced below threshold.
      """
      cuts_found = []
      # Again zip() is used for parallel iteration, ensuring names and prices are aligned.
      for name, price in zip(haircut_names, haircut_prices):
        if price < max_price_threshold:
          cuts_found.append(name)
      return cuts_found

# Main Execution Block
# This block runs when the script is executed directly
if __name__ == "__main__":
  print("--- Haircut Price Analysis ---")

  # Calculate and print total average haircut prices
  current_total_price, current_average_price = calculate_price_summary(prices)
  print(f"Total Haircut Price: ${current_total_price}")
  print(f"Average Haircut Price: ${current_average_price:.2f}") # Format to 2 decimal places

  print("\n--- Discount Prices ---")
  # Apply a $5 discount to prices
  discount_amount = 5
  new_prices = apply_discount(prices, discount_amount)
  print(f"New Prices (after ${discount_amount} discount): {new_prices}")

  print("\n--- Revenue Analysis ---")
  # Calculate a dn print total and average daily revenue
  num_days = 7 # Last week has 7 days
  total_revenue_last_week, average_daily_revenue_last_week = calculate_revenue_summary(prices, last_week, num_days)
  print(f"Total Revenue Last Week: ${total_revenue_last_week}")
  print(f"Average Daily Revenue Last Week: ${average_daily_revenue_last_week:.2f}") # Format to decimal places


  print("\n--- Affordable Haircuts (after Discount) ---")
  # Find haircuts under $30 after discount
  price_threshold = 30
  cuts_under_threshold = get_cuts_under_price(hairstyles, new_prices, price_threshold)
  print(f"Cuts under ${price_threshold} (after discoung): {cuts_under_threshold}")

  print("\n--- Origninal Haircuts (under original price) ---")
  # Example: Find haircuts under $30 at orginial price
  original_cuts_under_threshold = get_cuts_under_price(hairstyles, prices, price_threshold)
  print(f"Cuts under ${price_threshold} (orginal prices): {original_cuts_under_threshold}")