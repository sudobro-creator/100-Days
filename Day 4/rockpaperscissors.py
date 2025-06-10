#from random import choice
import random

print("Welcome to the official Rock, Paper, and Scissors Game.")
print("Game Rules: Type 0 for Rock, 1 for Paper, 2 for Scissors")
print("--------------------------------------------------------")
print('''
rock beats scissors
paper beats rock
scissors beat paper
''')

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

game_images = [rock, paper, scissors]

rock = 0
paper = 1
scissor = 2

while True:
    computer = [0, 1, 2]
    computer_choice = random.choice(computer)
    user_choice = int(input("Select one number between 0 to 2 to select your option: "))
    if user_choice >= 0 and user_choice <= 2:
        print(game_images[user_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win. You picked rock and you broke computer scissors.")
    elif user_choice == 1 and computer_choice == 0:
        print("You win. You picked paper and wrapped computer rock.")
    elif user_choice == 2 and computer_choice == 1:
        print("You win. You picked Scissors and you ripped computer paper.")
    elif user_choice == computer_choice:
        print("It is a draw.")
    elif user_choice != 0 or 1 or 2:
        print("You typed an invalid number. You lose.")
    else:
        print("You lose. Computer pick:")
        print(game_images[computer_choice])

    restart = input("Do you want to play again? Type 'yes' to continue or 'no' to exit: ").lower()
    if restart != 'yes':
        print("Thank you for playing. Goodbye!")
        break

print(user_choice)