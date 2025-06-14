# Test cases

weight = 4.8
# Recalculeate costs and print results

# weight = 41.5
# Recalculate costs and print results

cost_ground_premium = 125.00

# Ground Shipping
def calculate_ground_shipping(weight):
  if weight <= 2:
    return weight * 1.5 + 20
  if weight <= 6:
    return weight * 3 + 20
  if weight <= 10:
    return weight * 4 + 20
  else: 
    return weight * 4.75 + 20

cost_ground = calculate_ground_shipping(weight)

print("Ground Shipping $", cost_ground)
print("Ground Shipping Premium $", cost_ground_premium)

# Drone Shipping
def calculate_drone_shipping(weight):
  if weight <= 2:
    return weight * 4.50
  if weight <= 6:
    return weight * 9
  if weight <= 10:
    return weight * 12
  else: 
    return weight * 14.25

cost_drone = calculate_drone_shipping(weight)

print("Drone Shipping $", cost_drone)

# Determine the cheapest shipping method 
if cost_ground < cost_ground_premium and cost_ground < cost_drone:
  print("The cheapest option is Ground Shipping at $", cost_ground)
elif cost_ground_premium < cost_ground and cost_ground_premium < cost_drone:
  print("The cheapest option is Ground Shipping Premium at $", cost_ground_premium)
else:
  print("The cheapest option is Drone Shipping at $", cost_drone)