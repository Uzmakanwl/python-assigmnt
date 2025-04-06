import random
print("Welcome to the Simple Number Guessing Game")

secret_number = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10:"))

chances_left = 3

while chances_left > 0:
  guess = int(input(f"You have {chances_left} chances left. Guess again"))

  if guess == secret_number:
    print("Congratulations! you guessed the right  number!")
    break
  else:
    if guess < secret_number:
      print("Too low!")
    else:
      print("Too high")
    chances_left -= 1
if chances_left == 0:
  print(f"Game over! The number was {secret_number}")

