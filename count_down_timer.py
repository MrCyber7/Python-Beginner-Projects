# Count down timer
import time

timer = int(input("Enter the time in seconds: "))

for i in range(timer, 0, -1):
  seconds = i % 60
  minute = int(i / 60) % 60
  hour = int(i / 3600)
  print(f"{hour:02}:{minute:02}:{seconds:02}")
  time.sleep(1)

print("Time's Up!")