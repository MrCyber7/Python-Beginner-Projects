# Number Guessing game with For loop
import random

# Starting screen
print("==== Python Number Guesser ====")
print("==== Guess Between 1-100 ====")
print("==== Guess Within 10 Tries ====")

guess = int(input("Enter the Guess: "))
secret_num = random.randint(1, 100)
guesses = 1
total_guess = 10

for x in range(1,10):
  if guess > 100 or guess < 1:
    print("Invalid Number!")
    guess = int(input("Enter the Guess: "))
  elif guess == secret_num:
    continue
  elif guess > secret_num:
    guesses += 1
    print("Try Lower!")
    guess = int(input("Enter the Guess: "))
  else:
    guesses +=1
    print("Try Higher!")
    guess = int(input("Enter the Guess: "))

print("Congragulations!")
print(f"Your Guess: {guess}")
print(f"The Secret Number: {secret_num}")
print(f"The Guess Counter: {guesses}")
