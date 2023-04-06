import random


def rps():
    print("Welcome to Rock, Paper, Scissors!")
    mode = input(
        "Do you want to play against the computer or another player? (C or P): ")
    while mode.upper() != "C" and mode.upper() != "P":
        print("Invalid input. Please enter C or P.")
        mode = input(
            "Do you want to play against the computer or another player? (C or P): ")

    play = 'Y'
    player_1_score = 0
    player_2_score = 0
    player_draws = 0
    while (play.upper() == "Y"):
        # Player 1 input
        player_1 = input("Player 1: Enter R, P, or S: ")
        if player_1.upper() != "R" and player_1.upper() != "P" and player_1.upper() != "S":
            print("Invalid input. Please enter R, P, or S.")
            exit()
        with open("log.txt", "a") as f:
            f.write(f"Player 1 choose '{player_1}'\n")

        # Player 2 input
        if mode.upper() == "C":
            player_2 = random.choice(["R", "P", "S"])
            print(f"Player 2: {player_2}")
        else:
            player_2 = input("Player 2: Enter R, P, or S: ")
            if player_2.upper() != "R" and player_2.upper() != "P" and player_2.upper() != "S":
                print("Invalid input. Please enter R, P, or S.")
                exit()
        with open("log.txt", "a") as f:
            f.write(f"Player 2 choose '{player_2}'\n")

        # Get RPS result
        if player_1.upper() == player_2.upper():
            print("Tie!")
            player_draws += 1
        elif player_1.upper() == "R" and player_2.upper() == "S":
            print("Player 1 wins!")
            player_1_score += 1
        elif player_1.upper() == "R" and player_2.upper() == "P":
            print("Player 2 wins!")
            player_2_score += 1
        elif player_1.upper() == "P" and player_2.upper() == "R":
            print("Player 1 wins!")
            player_1_score += 1
        elif player_1.upper() == "P" and player_2.upper() == "S":
            print("Player 2 wins!")
            player_2_score += 1
        elif player_1.upper() == "S" and player_2.upper() == "P":
            print("Player 1 wins!")
            player_1_score += 1
        elif player_1.upper() == "S" and player_2.upper() == "R":
            print("Player 2 wins!")
            player_2_score += 1
        else:
            print("This shouldnt happen.")

        print(
            f"Current Wins: Player 1: {player_1_score}, Player 2: {player_2_score}, Draws: {player_draws}")
        with open("log.txt", "a") as f:
            f.write(
                f"Current Wins: Player 1: {player_1_score}, Player 2: {player_2_score}, Draws: {player_draws}\n")

        play = input("Do you want to play again? (Y or N): ")
