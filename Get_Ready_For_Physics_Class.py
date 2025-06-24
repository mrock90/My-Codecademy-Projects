# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below:

# Create a function called f_to_c to convert Fahrenheit to Celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

# Define a variable f100_in_celsius
f100_in_celsius = f_to_c(100)
# print(f100_in_celcius)

# Creae a function called c_to_f to conver Celsius to Fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

# Define a variable c0_in_fahrenheit
c0_in_fahrenheit = c_to_f(0)
# print(c0_in_fahrenheit)

# Create a function called get_force
def get_force(mass, acceleration):
  return mass * acceleration

# Test get_force
get_force(train_mass, train_acceleration)
train_force = get_force(train_mass, train_acceleration)
print(train_force)

# Print String 
print(f"The GE train supplies {train_force} Newtons of force.")

# Create function called get_energy
def get_energy(mass, c=3*10**8):
  return mass * c ** 2

# Test get_energy
bomb_energy = get_energy(bomb_mass)
print(bomb_energy)

# Print string
print(f"A 1kg bomb supplies {bomb_energy} Joules.")
# Create final function get_work
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

# Test get_work
get_work(train_mass, train_acceleration, train_distance)
train_work = get_work(train_mass, train_acceleration, train_distance)

# Print String
print(f"The GE Train does {train_work} Joules of work over {train_distance} meters.")