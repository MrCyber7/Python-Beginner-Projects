# rock paper scissors game
import random

player = 0
computer = 0
play = True
options = ("rock", "paper", "scissors")

while play:
 choice = input("Player: ").lower()

 if choice not in options:
  print("Invalid Choice!")
 else:
   option = random.choice(options)
   print(f"Computer : {option}")

   if option == choice:
     print("Draw!")
   elif option == "rock" and choice == "scissors":
     print("Computer Wins!")
     computer += 1
   elif option == "paper" and choice == "rock":
     print("Computer Wins!")
     computer += 1
   elif option == "scissors" and choice == "paper":
     print("Computer Wins!")
     computer += 1
   else:
     print("Player Wins!")
     player += 1
   print(f"Player: {player}\nComputer: {computer}")

 if computer == 5:
    play = False
    print("==== RESULT ====")
    print("You Lost!""\n""Computer Wins!")
 elif player == 5:
    print("==== RESULT ====")
    play = False
    print("Congratulations!""\n""You Won!")
