import random

from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

print(logo)
print()

endGame = False
chosen_word = random.choice(word_list)
lives = 6

display = []
blank = '_'
for _ in range(len(chosen_word)):
    display.append(blank)
print(f"Try to guess a word: {' '.join(display)}\n")


guessed_letters = []
while not endGame:
    guess = input("Guess a letter: ").lower()
    print()

    if guess in display:
        print(f"You've already guessed {guess}")

    guessed_letters += guess

    for index, letter in enumerate(chosen_word):
        if guess == letter:
            display[index] = guess
            print("Good!\n")


    if guess not in chosen_word:
        print(f"Wrong guess. You lose a life.\n")
        lives -= 1
        if lives == 0:
            endGame = True
            print("You lost every life. Game over.")
            print(f"The word was: {chosen_word}\n")

    print(" ".join(display))
    print(stages[lives])
    print()
    print(f"Letters you've already guessed: {', '.join(guessed_letters)}\n")

    if '_' not in display:
        endGame = True
        print("You won!")


