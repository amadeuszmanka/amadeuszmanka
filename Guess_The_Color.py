print("Welcome to the color guess game...Good luck.")
print("I'm thinking about one of the rainbow colors.")

import random

colors = ["red", "orange", "yellow", "green", "blue", "navy blue", "purple"]

while True:
    random_color = colors[random.randint(0,len(colors)-1)]
    guess = input("Can you guess the color? ")

    while True:
        if random_color == guess.lower():
            break
        else:
            guess = input("Nope. Try again: ")

    print("You guessed the color. I was thinking about", random_color, ".")

    play_again = input("Want to play again? Click ENTER to play again. Type 'no' to quit. ")

    if play_again.lower() == "no":
        break

print("It was fun, thanks for playing!")
        
    
    
