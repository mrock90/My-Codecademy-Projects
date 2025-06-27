# time_travelers_toolkit.py: Main script to simulate time travel experience

import datetime as dt
from decimal import Decimal
from random import randint, choice
from custom_module import generate_time_travel_message

# Retrieve current date and time
current_date = dt.date.today()
current_time = dt.datetime.now().time()

print(f"Current date: {current_date}")
print(f"Current time: {current_time}")

# Create a target year
current_year = current_date.year
# print(current_year)

target_year = randint(current_year + 50, current_year +  200)
# print(target_year)

# Possbile Destination/Selected Destination
possible_destinations = ["Futuristic Neo-Bangkok", "Space Colony Alpha", "Megalithic Era", "New Ice Age", f"Cyber Punk {target_year}"]
# print(possible_destinations)
try:
  selected_destination = choice(possible_destinations)
# print(selected_destination)
except IndexError:
  selected_destination = "Unknown Destination"

# Cost calculation
base_cost = Decimal("1000.00")
year_difference = target_year - current_year
cost_multiplier = year_difference / 10.0
final_cost = base_cost * Decimal(str(cost_multiplier))
formatted_final_cost = f"{final_cost:.2f}"

# print(year_difference)
# print(cost_multiplier)
# print(final_cost)
# print(formatted_final_cost)

print(generate_time_travel_message(target_year, selected_destination, formatted_final_cost))