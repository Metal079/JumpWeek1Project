from rps import rps
from guessing_game import guessing_game

def main():
    print("Available games:")
    print("1. Rock, Paper, Scissors")
    print("2. Number Guessing Game")
    print("3. Tic Tac Toe")
    print("4. Connect Four")

    game_choice = input("What game would you like to play? ")

    if game_choice == "1":
        rps()
    elif game_choice == "2":
        guessing_game()
    elif game_choice == "3":
        pass
    elif game_choice == "4":
        pass
    else:
        print("Invalid input. Please enter a number between 1 and 4.")
        main()

if __name__ == "__main__":
    main()