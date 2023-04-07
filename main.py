from rps import rps
from guessing_game import guessing_game
from tic_tac_toe import play_t3

def main():
    while True:
        print("Available games:")
        print("1. Rock, Paper, Scissors")
        print("2. Number Guessing Game")
        print("3. Tic Tac Toe")
        print("4. Exit")

        game_choice = input("What game would you like to play? ")

        if game_choice == "1":
            rps()
        elif game_choice == "2":
            guessing_game()
        elif game_choice == "3":
            play_t3()
        elif game_choice == "4":
            exit()
        else:
            print("Invalid input. Please enter a number between 1 and 4.")
            main()

if __name__ == "__main__":
    main()