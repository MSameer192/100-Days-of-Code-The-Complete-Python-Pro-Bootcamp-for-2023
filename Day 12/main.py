from random import randint
from art import logo

def display_welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

def generate_random_number():
    return randint(1, 100)

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return 10
    elif level == "hard":
        return 5
    else:
        print("Invalid input. Please choose 'easy' or 'hard.")
        return set_difficulty()

def play_game():
    print(logo)
    display_welcome_message()
    answer = generate_random_number()
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    for _ in range(turns):
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == answer:
            print(f"You got it! The answer was {answer}.")
            return
        elif guess < answer:
            print("Too low.")
        else:
            print("Too high.")

        turns -= 1

    print("You've run out of guesses, you lose.")


if __name__ == "__main__":
    play_game()
