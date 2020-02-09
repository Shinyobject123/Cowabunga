# Hangman game
import random

done = False
# PSEUDOCODE
# setup your game by doing the following
# make a word list for your game
# grab a random word from your list and store it as a variable

# in a loop, do the following
# display the hangman using the gallows
# display the used letters so the user knows what has been selected
# display the length of the word to the user using blank spaces and used letters
# prompt the user to guess a letter
# don't allow the user to select the same letter twice
# if the guess is incorrect increment incorrect_guesses by 1
# if the incorrect_guesses is greater than 8, tell the user they lost and exit the program
# if the user gets all the correct letters, tell the user they won

# ask if they want to play again
word_list = ["BLE", "TABLE", "CHAIR", "BRIDGE", "PROGRAM", "LIST", "EIGHT", "WIN"]
word = word_list[random.randrange(8)]
word_progress = ["_" for x in range(len(word))]
correct = 0
gallows = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
]
man = 0
guesses = ["_"]

print(gallows[man])
for x in range(len(word_progress)):
    print(word_progress[x], end=" ")
while not done:
    guess = input("\nGuess a letter: ").upper()
    for x in range(len(guesses)):
        if guess == guesses[x]:
            print("Aready guessed.")
            found = True
        else:
            guesses.append(guess)
            found = False
            for x in range(len(word_progress)):
                if guess == word[x]:
                    word_progress[x] = word[x]
                    found = True


    if found == False:
        man += 1
    else:
        correct += 1
    print(gallows[man])
    for x in range(len(word_progress)):
        print(word_progress[x], end=" ")
    if man == 6:
        print("\nYou Lose")
        done = True
    if correct >= len(word_progress):
        print("\nYou Win!")
        done = True
