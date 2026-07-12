# Vowel counter

vowels = "aeiouAEIOU"
counter = 0
word = input("Enter a Word: ")

for letters in word:
  for vowel in vowels:
    if letters == vowel:
      counter += 1
    else:
      continue
print(counter)