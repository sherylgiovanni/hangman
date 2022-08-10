# CODE CHALLENGE - Hangman
# by Sheryl Tania
import random

def main():
  print(" __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __. ")
  print("|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  | ")
  print("|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  | ")
  print("|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  | ")
  print("|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   | ")
  print("|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__| ")
  print("Welcome to Hangman! We hope you enjoy playing.")
  play = True
  attempts = 10
  correctGuess = 0
  incorrectGuess = 0
  guesses = ""
  incorrectGuesses = []
  words = ["daffodil", "rose", "fuchsia", "amaranth", "lily", "daisy", "sunflower", "tulip", "carnation", "lavender"]
  randomWord = random.choice(words)
  wordLength = len(randomWord)
  print("Now, make a guess. Your word has " + str(wordLength) + " characters and you have 10 attempts.")

  while attempts > 0 and play:
    question = ""
    for letter in randomWord:
        if letter in guesses:
            question = question + letter
        else:
            question = question + "_" + " "
    if question == randomWord:
        print(question)
        print("Congratulations! You won with " + str(10 - attempts) + " attempts!")
        break
    print("\nWord: ", question)
    guess = input("Type in your guess: ")
    if guess not in randomWord:
        print("The letter '" + guess + "' is not in the word.")
        incorrectGuesses.append(guess)
        print("So far these are the letters not in the word: " + ' '.join(incorrectGuesses))
        incorrectGuess += 1
    else:
      correctGuess += 1
      guesses += guess
    drawHangman(incorrectGuess)
    attempts -= 1
    print("Attempts left: " + str(attempts))
    print("Correct guesses: " + str(correctGuess))
    print("Incorrect guesses: " + str(incorrectGuess))

  if attempts == 0:
    print("You lost!")
  
  playAgain = input('Play again? (Y/N) ')
  if playAgain == 'Y' or playAgain == 'y':
    play = True
    main()
  else:
    print("Thanks for playing, goodbye!")
    play = False

def drawHangman(incorrect):
  if incorrect == 0:
    print("|```````````|")
    print("|           |")
    print("|           |")
    print("|           |")
    print("|           |")
    print("|___________|")

  if incorrect == 1:
    print("|```````````|")
    print("|           |")
    print("|     0     |")
    print("|           |")
    print("|           |")
    print("|___________|")

  if incorrect == 2:
    print("|```````````|")
    print("|           |")
    print("|     0     |")
    print("|     |     |")
    print("|           |")
    print("|___________|")

  if incorrect == 3:
    print("|```````````|")
    print("|           |")
    print("|     0     |")
    print("|     |     |")
    print("|    /      |")
    print("|___________|")

  if incorrect == 4:
    print("|```````````|")
    print("|           |")
    print("|     0     |")
    print("|     |     |")
    print("|    / \    |")
    print("|___________|")

  if incorrect == 5:
    print("|```````````|")
    print("|           |")
    print("|   \ 0     |")
    print("|     |     |")
    print("|    / \    |")
    print("|___________|")

  if incorrect == 6:
    print("|```````````|")
    print("|           |")
    print("|   \ 0 /   |")
    print("|     |     |")
    print("|    / \    |")
    print("|___________|")

  if incorrect == 7:
    print("|`````|`````|")
    print("|           |")
    print("|   \ 0 /   |")
    print("|     |     |")
    print("|    / \    |")
    print("|___________|")

  if incorrect == 8:
    print("|`````|`````|")
    print("|     |     |")
    print("|   \ 0 /   |")
    print("|     |     |")
    print("|    / \    |")
    print("|___________|")

  if incorrect == 9:
    print("|`````|`````|")
    print("|     |     |")
    print("|     0     |")
    print("|    /|\    |")
    print("|    | |    |")
    print("|___________|")
  
  if incorrect == 10:
    print("|`````|`````|")
    print("|     |     |")
    print("|     X     |")
    print("|    /|\    |")
    print("|    | |    |")
    print("|___________|")


main()