import random
print("Welcome to hangman game")
print("guess form this:","pythonhangmancodeimuqadasplekin")
words = ["python","hangman","code","game" ,"muqadasuzma"]
word = random.choice(words)

guess = input(f"Guess the word({len(word)} letters): ") .lower()

if guess == word:
      print("congratulation! you guessed it right !")
else:
      print(f"Game over! The correct word was :{words}")