# Number Guessing Game improved
import random

lowest_number = input("Enter the Lowest Number: ")
highest_number = input("Enter the Highest Number: ")

while not lowest_number.isdigit() or not highest_number.isdigit() or not int(lowest_number) < int(highest_number):
  print("Error!")
  lowest_number = input("Enter the Lowest Number: ")
  highest_number = input("Enter the Highest Number: ")
  
lowest_number = int(lowest_number)
highest_number = int(highest_number)

secret_number = random.randint(lowest_number, highest_number)

print("==== Guess The Number ====")
print(f"  Guess between {lowest_number} and {highest_number}")

guesses = 0

guess = int(input("  Guess: "))

while guess != secret_number:
  if guess > highest_number or guess < lowest_number:
    print(f"  Guess between {lowest_number} and {highest_number}")
    guess = int(input("  Guess: "))
  elif guess > secret_number:
    print("  Try Lower!")
    guess = int(input("  Guess: "))
    guesses += 1
  else:
    print("  Try Higher!")
    guess = int(input("  Guess: "))
    guesses += 1

print("-----------------------")
print("Congratulations!")
print(f"You Guessed: {guess}")
print(f"The Number was: {secret_number}")
print(f"Number OF Guesses: {guesses + 1}")
