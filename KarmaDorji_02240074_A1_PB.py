import random

def guess_number_game():
    print("Let's play Guessing Number Game!")
    print(" Choose a number between 1 and 50.")
    secret_number = random.randint(1, 50)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1-50): "))
            attempts += 1

            if guess < 1 or guess > 50:
                print("Enter a number between 1 and 50.")
                continue

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Well done ! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input.  Enter a valid number.")

def rock_paper_scissors_game():
    print("Welcome to Rock Paper Scissors!")
    choices = ['rock', 'paper', 'scissors']

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or 'exit' to quit: ").lower()

        if user_choice == 'exit':
            print("Thanks for playing!")
            break

        if user_choice not in choices:
            print("Invalid choice. Choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("You lose!")

def main():
    while True:
        print("\nSelect a game to play:")
        print("1. Guess the Number")
        print("2. Rock Paper Scissors")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                guess_number_game()
            elif choice == 2:
                rock_paper_scissors_game()
            elif choice == 3:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
