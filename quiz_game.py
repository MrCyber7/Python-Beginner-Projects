# Quiz game 

questions = ("Q1: Which app became the most downloaded social media platform worldwide during the COVID-19 period?",
             "Q2: Which country was the first to officially ban single-use plastic bags nationwide?",
             "Q3: What device feature allows a smartphone screen to recognize your fingerprint?",
             "Q4: What does the blue tick on social media accounts usually indicate?",
             "Q5: Which company was the first to reach a market value of 1 trillion US dollars?",)

options = (("A.Youtube", "B.Tiktok", "C.Facebook", "D.Instagram"),
           ("A.Thailand", "B.Bangladesh", "C.Myammar", "D.India"),
           ("A.Retina Scanner", "B.Fingerprint Sensor", "C.Face unlock", "D.Touch ID Camera"),
           ("A.User has reached 1 million users", "B.Inactive account", "C.Premium Account", "D.Verified Account"),
           ("A.Samsung", "B.Tesla", "C.Apple", "D.SpaceX"))

answers = ("B", "B", "B", "D", "C")
guesses = []
q_num = 0
score = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[q_num]:
      print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[q_num]:
      score += 1
      print("Correct!")
    else:
      print("Incorrect!")
      print(f"{answers[q_num]} is correct!")
    q_num += 1

print("==== RESULT ====")
print("Answers: ", end="")
for ans in guesses:
  print(ans, end=" ")
print()
print("        -----------")
print("Correct: ", end="")
for answer in answers:
  print(answer, end=" ")
print()
score = float(score / len(questions) * 100)
print(f"Score = {score: .2f}%")