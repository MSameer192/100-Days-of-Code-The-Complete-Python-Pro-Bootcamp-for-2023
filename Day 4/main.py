import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
---.__()
'''

game_images = [rock, paper, scissors]

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

# Check if user input is valid
if user_choice not in ['0', '1', '2']:
    print("Invalid input. Please choose 0 for Rock, 1 for Paper, or 2 for Scissors.")
else:
    user_choice = int(user_choice)
    
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose")
