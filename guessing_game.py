import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 tries to guess the number.")
    print("After each guess, I'll give a hint!")

    # Generate a random number between 1 and 20
    secret_number = random.randint(1, 20)

    player_attempts = 0 
    player_guesses = []
    while player_attempts < 5:
        player_attempts += 1
        print(f"Guess #{player_attempts}")
        player_guess = int(input("Enter your guess: "))
        player_guesses.append(player_guess)

        if player_guess == secret_number:
            print("You guessed it! You win!")
            break
        elif abs(player_guess  - secret_number) <= 3:
            print("Hot! So close!")
        elif abs(player_guess - secret_number) <= 5:
            print("Warm! Getting there!")
        else:
            print("Cold! Way off!")
    
    with open("log.txt", "a") as f:
        f.write(f"Player guessed {player_guesses}")
        