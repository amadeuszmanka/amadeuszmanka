rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random
choices = [rock, paper, scissors]

print("Welcome to the Rock, Paper, Scissors Game!")
print("------------------------------------------")

while True:
    player_choice = input("Rock, paper or scissors? ").lower()
    print("------------------------------------------")
    if player_choice == "rock":
        print(f"Your choice:\n{choices[0]}")
    elif player_choice == "paper":
        print(f"Your choice:\n{choices[1]}")
    else:
        print(f"Your choice:\n{choices[2]}")

    computer_choice = random.choice(choices)
    print(f"Computer's choice:\n{computer_choice}")

    if player_choice == "rock":
        if computer_choice == scissors:
            print("You win!")
        elif computer_choice == paper:
            print("You lose...")
        else:
            print("It's a tie!")

    if player_choice == "paper":
        if computer_choice == rock:
            print("You win!")
        elif computer_choice == scissors:
            print("You lose...")
        else:
            print("It's a tie!")

    if player_choice == "scissors":
        if computer_choice == paper:
            print("You win!")
        elif computer_choice == rock:
            print("You lose...")
        else:
            print("It's a tie!")


    print("------------------------------------------")


    play_again = input("Want to play again? Type 'no' to quit. ")

    if play_again.lower() == 'no':
        break

print("Thanks for playing. See you next time ;)")






