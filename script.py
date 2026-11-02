# Week1
def print_hi(name):
  print(f'Hi, {name}!')

def tell_story():
  print("Today is a good day!")


# Week2
def ask_name():
  return input("What is your name: ")


# Week 3
def ask_age():
  return input("How old are you: ")

def calculate_birthday_year(age):
  return 2026 - int(age)

def print_age(year):
  return print(f'You were born in the year {year}')

# Extra
def do_you_like_programming():
  answer = input("Do you like programming (yes/no): ")
  if (answer == "yes"):
    print("Nice, me too!")
  elif (answer == "no"):
    print("No problem!")
  else:
    print("Only 'yes' and 'no' are valid anwsers!")


# Week 5: Types, arithmetic, and decisions
def snack_challenge():
  coins = 10
  snack_price = 3

  snacks_text = input("How many snacks do you want to buy? ")
  snacks = int(snacks_text)  # Convert the input text (str) to a number (int)

  total_cost = snacks * snack_price

  if total_cost <= coins:
    coins_left = coins - total_cost
    print(f"You bought {snacks} snacks and have {coins_left} coins left.")
  else:
    print(f"You need {total_cost} coins, but you only have {coins}.")


if __name__ == "__main__":
  # Week1
  name = "Ragnar"
  print_hi(name)
  tell_story()
  
  # Week2
  friendName  = ask_name()
  age = ask_age()
  
  # Week3 types of data&math intro
  name = "Alice"       # String (str)
  age = 25             # Integer (int)
  price = 19.99        # Float (float)
  is_active = True     # Boolean (bool)

  birth_year = calculate_birthday_year(age)
  print_age(birth_year)
  do_you_like_programming()

  # Week 5: Snack challenge
  snack_challenge()

