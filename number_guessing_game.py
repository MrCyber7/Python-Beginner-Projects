# Number Guessing game
import random

# starting screen
print("-----Python Guesser-----")
print("Guess number between 1 - 100")

guess = int(input("Enter your Guess: "))
secret_num = random.randint(1, 100)
attempts = 1

#loop
while not guess == secret_num:
  if guess > 100 or guess < 1:
     print("Guess should be within 1 - 100!")
     guess = int(input("Enter your Guess: "))
  elif guess < secret_num:
    print("Try Higher!")
    guess = int(input("Enter your Guess: "))
    attempts += 1
  else:
     print("Try Lower!")
     guess = int(input("Enter your Guess: "))
     attempts += 1

print("Congratulations!")
print(f"You guessed the number: {secret_num}")
print(f"Attempts: {attempts}")