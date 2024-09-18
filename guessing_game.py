import time
import random

# Function to start the game with a given number of chances
def start_game(chances):
    number_to_guess = random.randint(1, 100)
    print(f"You have {chances} chances to guess the number.")
    
    while chances > 0:
        try:
            guess = int(input("Enter your guess: "))
            
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print("Congratulations! You guessed the number!")
                continue_game()
                return True
            
            chances -= 1
            if chances > 0:
                print(f"You have {chances} chances left.")
            else:
                print(f"Sorry, you're out of chances. The number was {number_to_guess}.")
                return False
        
        except ValueError:
            print("Please enter a valid integer.")

# Function to handle retrying the game
def retry_game_fail():
    while True:
        retry = input("Would you like to try again? (y/n): ").strip().lower()
        if retry == 'y':
            main()
            break
        elif retry == 'n':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

            # Function to handle retrying the game
def continue_game():
    while True:
        retry = input("Would you like to continue playing? (y/n): ").strip().lower()
        if retry == 'y' :
            main()
            break
        elif retry == 'n' :
            print("Thankyou for playing")
            break



# Main function to control the flow of the game
def main():
    print("Welcome to the Guessing Game!")
    time.sleep(1)
    print("I'm thinking of a number between 1 and 100.")
    time.sleep(1)
    print("You have a number of chances to guess the number based on the difficulty you choose.")

    # Difficulty levels
    difficulty = input("Choose difficulty level (easy, medium, hard): ").strip().lower()

    if difficulty == "easy":
        chances = 10
    elif difficulty == "medium":
        chances = 8
    elif difficulty == "hard":
        chances = 5
    else:
        print("Invalid choice. Defaulting to medium difficulty.")
        chances = 8

    game_result = start_game(chances)
    if not game_result:
        retry_game_fail()


# Start the game
main()
