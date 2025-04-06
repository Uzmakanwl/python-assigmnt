import random

number=random.randint(1,10)
print("Would u like to guess which number i pick")
while True:
  guess = random.randint(1,10)
  print(f"Computer guess:{guess}")

  if guess== number:
    print("Computer got it")
    break
  elif guess < number:
    print("too low!")
  else :
    print("too high!")