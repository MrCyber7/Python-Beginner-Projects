# 2d keypad

keypad = ((1, 2, 3),
          (4, 5, 6),
          (7, 8, 9),
          ("*", 0, "#"))

for collection in keypad:
  for num in collection:
    print(num, end=" ")
  print()