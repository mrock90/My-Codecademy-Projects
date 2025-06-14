import random

name = "Matthew"
question = "Is this real life?"
answer = ""

# task 14: What if the question string is empty?
if question == "":
  print("The Magic 8-ball cannot provide a fortune without a question!")
else:
  random_number = random.randint(1, 12)
# print(random_number)

  if random_number == 1:
    answer= "Yes - definitely"
  elif random_number == 2:
    answer = "It is decidely so"
  elif random_number == 3:
    answer = "Without a doubt"
  elif random_number == 4:
    answer = "Reply hazy, try again"
  elif random_number == 5:
    answer = "Ask again later"
  elif random_number == 6:
    answer = "Better not tell you now"
  elif random_number == 7:
    answer = "My sources say no"
  elif random_number == 8:
    answer = "Outlook not so good"
  elif random_number == 9:
    answer = "Very Doubtful"
  elif random_number == 10:
    answer = "Better luck next time"
  elif randon_number == 11:
    answer = "Maybe, maybe not"
  elif random_number == 12:
    answer = "Welcome to the Multiverse"
  else:
    answer = "Error"

# Task 13: What if the asker does not provide a name?

if name == "":
  print(f"Question: {question}")
else:
  print(f"{name} asks: {question}")
# This will always print if question is provided
print(f"Magic 8-ball's answer: {answer}")